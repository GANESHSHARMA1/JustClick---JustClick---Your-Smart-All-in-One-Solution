import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import google.generativeai as genai
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import os
import time
import re
import PyPDF2 as pdf
from dotenv import load_dotenv

load_dotenv()

# st.set_page_config(
#     page_title="Check ATS Score Against JD",
#     page_icon="📝"
# )

st.title(':red[CareerSync] - Enhancing Your Efficiency, Every :blue[Click]')
st.sidebar.success("Check ATS Score against JD")
st.text("Test Your Resume ATS")

css = """
<style>
body {
    background-color: #f5f5f5;
    margin: 0;
    padding: 0;
}
h1 {
    color: white;
    text-align: justified;
}
.AI-Anyalyze{
    width: 100%;
    align-item: end;
}
.stButton {
    display: block;
    width: 100%;
    margin-bottom: 10px;
}
.job-description, .write-description {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 0 20px;
}
.job-desc{
    padding: 50px;
}
.textbox {
    height: 100%;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

common_skills = [
    "python", "java", "c++", "sql", "javascript", "html", "css", "machine learning",
    "deep learning", "data analysis", "project management", "communication", "problem-solving",
    "teamwork", "leadership", "time management", "agile", "scrum", "cloud computing", "aws", "azure"
]

def pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text


def extract_skills(text):
    skills = set()
    for skill in common_skills:
        if re.search(r'\b' + re.escape(skill) + r'\b', text, re.IGNORECASE):
            skills.add(skill.lower())
    return skills

def extract_experience(text):
    experience_pattern = r'(\d+)\+? years? of experience'
    experience_matches = re.findall(experience_pattern, text, re.IGNORECASE)
    experience = max(map(int, experience_matches), default=0)
    return experience



def calculate_ats_score(resume_text, job_desc):
    vectorizer = TfidfVectorizer()
    documents = [resume_text, job_desc]
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
    score = similarity_matrix[0][1] * 100

    resume_skills = extract_skills(resume_text)
    job_desc_skills = extract_skills(job_desc)
    matched_skills = list(resume_skills & job_desc_skills)
    missing_skills = list(job_desc_skills - resume_skills)

    resume_experience = extract_experience(resume_text)
    job_desc_experience = extract_experience(job_desc)

    experience_match = resume_experience >= job_desc_experience

    return score, matched_skills, missing_skills, job_desc_skills, experience_match




genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(prompt_input, pdf_tex, job_dec):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt_input, pdf_tex, job_dec])
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

input_prompt = """
Hey Act Like a skilled or very experienced ATS(Application Tracking System)
with a deep understanding of the tech field for the Job role given in the job description. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving the resumes. Assign the percentage matching based 
on JD and the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in a proper manner having the structure
"Job Description": "\n","","\n",
"JD Match":"%","\n",
"MissingKeywords:[]","\n",
"Profile Summary":""
"""


if 'job_desc' not in st.session_state:
    st.session_state.job_desc = ""

st.write("Click any button that satisfies your dream job role or enter job description in the textarea.")

@st.cache_resource
def initial_connection():
    # uri = os.getenv("MONGODB_URI")
    uri="mongodb+srv://GaneshKithana:iyES7TdrvmkuFxJ@justclick.ps3ayrm.mongodb.net/test?appName=JustClick"
    return MongoClient(uri, server_api=ServerApi('1'))

with st.spinner('Connecting to ATS server to personalize your result...'):
    try:
        client = initial_connection()
        st.success('Successfully connected to Server!')
    except Exception as e:
        st.error(f"Failed to connect to MongoDB: {e}")


st.cache_data(ttl=600)
def get_job_description(job_role):
    db = client['ATS']
    collection = db['Job_desc']
    # print(f"Looking for job role: {job_role}")
    # print(collection.find_one({'job_role': job_role}))
    document = collection.find_one({'job_role': job_role})
    if document:
        return document['job_desc']
    else:
        return "Enter Job Description manually."


col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="job-description job-desc">', unsafe_allow_html=True)
    if st.button("Software Developer/Engineer -->>"):
        st.session_state.job_desc = get_job_description("Software Developer")
    if st.button("Web Developer -->>"):
        st.session_state.job_desc = get_job_description("Web Developer")
    if st.button("Graphics Designer -->>"):
        st.session_state.job_desc = get_job_description("Graphics designer")
    if st.button("Systems Analyst -->>"):
        st.session_state.job_desc = get_job_description("Systems Analyst")
    if st.button("Product Manager -->>"):
        st.session_state.job_desc = get_job_description("Product Manager")
    if st.button("Data Scientist -->>"):
        st.session_state.job_desc = get_job_description("Data Scientist")
    if st.button("Data Analyst -->>"):
        st.session_state.job_desc = get_job_description("Data Analyst")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="write-description">', unsafe_allow_html=True)
    job_desc = st.text_area("Paste the Job Description", height=500, key="textbox", value=st.session_state.job_desc, help="Enter Job Description or click on buttons to get default job description")
    st.session_state.job_desc = job_desc
    st.markdown('</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")
 

btn1, btn2 = st.columns(2)

with btn1:
    st.markdown('<div class="AI-Anyalyze">', unsafe_allow_html=True)
    submit = st.button("Analyze ATS Score")
    st.markdown('</div>', unsafe_allow_html=True)

with btn2:
    st.markdown('<div class="AI-Anyalyze">', unsafe_allow_html=True)
    analyze = st.button("Analyze with AI")
    st.markdown('</div>', unsafe_allow_html=True)

if analyze:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt, text, job_desc)
        st.subheader(response)
    else:
        st.write("Please upload the resume")


def draw_pie_chart(ats_score):
    labels = 'Matched', 'Unmatched'
    sizes = [ats_score, 100 - ats_score]
    colors = ['#4CAF50', '#FF5722']
    explode = (0.1, 0)

    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
           shadow=False, startangle=140)
    ax.axis('equal')  
    fig.patch.set_facecolor('none') 
    ax.patch.set_facecolor('none')  

    st.pyplot(fig)


if submit:
    if uploaded_file is not None:
        with st.spinner('Analyzing resume...'):
            resume_text = input_pdf_text(uploaded_file)
            ats_score, matched_skills, missing_skills, job_desc_skills, experience_match = calculate_ats_score(resume_text, job_desc)

            st.subheader("Best ATS Score")
            st.write(f"Your resume matches {ats_score:.2f}% with the job description.")

    
            draw_pie_chart(ats_score)

            st.subheader("Skills Analysis")
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Required Skills**")
                st.write(list(job_desc_skills)[:20])
            with col2:
                st.write("**Matched Skills**")
                st.write(matched_skills[:20])

            st.subheader("Missing Skills")
            if missing_skills:
                st.write(missing_skills[:20])
            else:
                st.write("Your resume contains all the required skills.")

            st.subheader("Experience Match")
            if experience_match:
                st.write("Your experience meets or exceeds the job requirement.")
            else:
                st.write("Your experience does not meet the job requirement.")
    else:
        st.write("Please upload the resume")