import streamlit as st
import re
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pymongo import MongoClient
import gridfs
from bson.objectid import ObjectId
from pymongo.server_api import ServerApi


uri = "mongodb+srv://GaneshKithana:iyES7TdrvmkuFxJ@justclick.ps3ayrm.mongodb.net/test?appName=JustClick"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['ATS']
jobs_collection = db['Job_desc']
job_role = db['jobs']
fs = gridfs.GridFS(db)


job_roles = jobs_collection.distinct('job_role')
jobs = job_role.distinct('title')


def extract_text_from_pdf(pdf_file):
    text = ""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text


common_skills = [
    "python", "java", "c++", "sql", "javascript", "html", "css", "machine learning",
    "deep learning", "data analysis", "project management", "communication", "problem-solving",
    "teamwork", "leadership", "time management", "agile", "scrum", "cloud computing", "aws", "azure"
]


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


st.title('ATS Score Calculator')


selected_job_role = st.selectbox('Select Job Role', [''] + jobs)

if selected_job_role:
    job_desc_doc = jobs_collection.find_one({'job_role': selected_job_role})
    job_desc = job_desc_doc['job_desc']

    st.subheader('Job Description')
    st.write(job_desc)

    job_title_collection_name = selected_job_role.replace(" ", "_")
    job_title_collection = db[job_title_collection_name]
    resumes = job_title_collection.find()

    scores = []
    for resume in resumes:
        resume_file = fs.get(ObjectId(resume['resume_id']))
        resume_text = extract_text_from_pdf(resume_file)
        ats_score, matched_skills, missing_skills, job_desc_skills, experience_match = calculate_ats_score(resume_text, job_desc)
        scores.append((resume['name'], ats_score))

    scores.sort(key=lambda x: x[1], reverse=True)

    st.subheader('Candidates and ATS Scores')
    for name, score in scores:
        st.write(f'{name}: {score:.2f}%')

    if not scores:
        st.write("No resumes found for this job role.")