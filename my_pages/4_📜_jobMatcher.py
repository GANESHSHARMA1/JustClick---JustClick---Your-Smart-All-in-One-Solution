import streamlit as st
import re
import pandas as pd
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MultiLabelBinarizer
from pymongo import MongoClient
import gridfs
from pymongo.server_api import ServerApi


# st.set_page_config(page_title="Job Matcher", page_icon="📜")
# MongoDB connection details
@st.cache_resource
def get_mongo_client():
    uri = "mongodb+srv://<Username>:<Password>@justclick.ps3ayrm.mongodb.net/test?appName=JustClick"
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client

# Initialize MongoDB client and GridFS
client = get_mongo_client()
db = client['ATS']
jobs_collection = db['jobs']
fs = gridfs.GridFS(db)

# Sample job roles and required skills
job_roles = {
    'Data Scientist': ['Python', 'Machine Learning', 'Data Analysis', 'SQL', 'Statistics'],
    'Web Developer': ['HTML', 'CSS', 'JavaScript', 'React', 'Node.js'],
    'DevOps Engineer': ['Docker', 'Kubernetes', 'CI/CD', 'AWS', 'Linux'],
    'Data Analyst': ['Excel', 'SQL', 'Tableau', 'Python', 'Data Visualization']
}

# Convert job roles to a DataFrame
job_roles_df = pd.DataFrame(job_roles.items(), columns=['Job Role', 'Skills'])

# Create a dataset for training
data = [(role, ' '.join(skills)) for role, skills in job_roles.items()]
df = pd.DataFrame(data, columns=['Job Role', 'Skills'])

# Train the ML model
@st.cache_data
def train_model():
    mlb = MultiLabelBinarizer()
    X = df['Skills']
    y = mlb.fit_transform(df['Job Role'].apply(lambda x: [x]))
    model = make_pipeline(TfidfVectorizer(), OneVsRestClassifier(LinearSVC()))
    model.fit(X, y)
    return model, mlb

model, mlb = train_model()

# Function to extract skills from resume text
def extract_skills(resume_text, skill_set):
    extracted_skills = set()
    for skill in skill_set:
        if re.search(rf'\b{skill}\b', resume_text, re.IGNORECASE):
            extracted_skills.add(skill)
    return extracted_skills

# Function to match resume to job roles
@st.cache_data
def match_resume(resume_text):
    skill_set = {skill for skills in job_roles.values() for skill in skills}
    resume_skills = extract_skills(resume_text, skill_set)
    
    best_match = None
    max_matched_skills = 0
    missing_skills = {}
    
    for role, role_skills in job_roles.items():
        matched_skills = resume_skills.intersection(role_skills)
        if len(matched_skills) > max_matched_skills:
            max_matched_skills = len(matched_skills)
            best_match = role
            missing_skills[best_match] = set(role_skills) - resume_skills
    
    if best_match:
        missing_skills = {best_match: missing_skills[best_match]}
    
    return best_match, missing_skills

# Function to extract text from PDF
@st.cache_data
def extract_text_from_pdf(pdf_file):
    text = ""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text

# Streamlit app layout
st.title('Resume Job Role Matcher with ML')

st.header('Upload your resume')
uploaded_file = st.file_uploader('Choose a file', type=['pdf'])

if uploaded_file is not None:
    with st.spinner("Processing your resume and finding the best job roles..."):
        try:
            resume_text = extract_text_from_pdf(uploaded_file)
            predicted_role, missing_skills = match_resume(resume_text)
            
            st.subheader('Matched Job Role')
            if predicted_role:
                st.write(f'The best matching job role for you is: *{predicted_role}*')
            else:
                st.write('No matching job role found.')
            
            st.subheader('Skills to Learn')
            if predicted_role:
                st.write(f'For the role *{predicted_role}*, you need to learn: {", ".join(missing_skills[predicted_role])}' if missing_skills[predicted_role] else f'You have all the required skills for the role *{predicted_role}*.')
                
                matched_jobs = jobs_collection.find({"title": predicted_role})

                if 'apply_status' not in st.session_state:
                    st.session_state.apply_status = {}

                for job in matched_jobs:
                    job_id = str(job['_id'])
                    if st.button(f"Apply for {job['title']}", key=f"apply_{job_id}"):
                        st.session_state.apply_status[job_id] = True

                    if st.session_state.apply_status.get(job_id, False):
                        user_name = st.text_input("Enter your name", key=f"name_{job_id}")
                        uploaded_file = st.file_uploader("Upload your resume", type=['pdf', 'docx'], key=f"uploader_{job_id}")

                        if uploaded_file is not None:
                            st.write(f"File {uploaded_file.name} selected for upload.")

                        if st.button(f"Submit application for {job['title']}", key=f"submit_{job_id}"):
                            if user_name and uploaded_file is not None:
                                file_id = fs.put(uploaded_file.read(), filename=uploaded_file.name)

                                # Create or get the collection for the specific job title
                                job_title_collection = db[job['title'].replace(" ", "_")]

                                # Insert the applicant's information into the specific job title collection
                                job_title_collection.insert_one({
                                    "name": user_name,
                                    "resume_id": file_id,
                                    "resume_filename": uploaded_file.name
                                })
                                st.success(f"Resume uploaded for {job['title']}")
                                st.session_state.apply_status[job_id] = False
                            else:
                                st.error("Please provide your name and upload your resume.")
        except Exception as e:
            st.error(f"Error processing file: {e}")
