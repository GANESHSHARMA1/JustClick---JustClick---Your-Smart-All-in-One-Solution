import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Check ATS Score Against JD",
    page_icon="📝"
)


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

st.title("JustClick - Enhancing Your Efficiency, Every Click")
st.sidebar.success("Check ATS Score against JD")
st.text("Test Your Resume ATS")

# uri = os.getenv("MONGODB_URI")
uri = "mongodb+srv://GaneshKithana:iyES7TdrvmkuFxJ@justclick.ps3ayrm.mongodb.net/test?appName=JustClick"
client = MongoClient(uri, server_api=ServerApi('1'))

db = client['Job_roles']
collection = db['Job_desc']

def get_job_description(job_role):
    document = collection.find_one({'job_role': job_role})
    if document:
        return document['job_desc']
    else:
        return "Enter Job Description manually."
    
if 'job_desc' not in st.session_state:
    st.session_state.job_desc = ""

st.write("Click any button that satisfies your dream job role or enter job description in the textarea.")
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="job-description job-desc">', unsafe_allow_html=True)
    if st.button("Software Developer/Engineer -->>"):
        st.session_state.job_desc = get_job_description("Software Developer")
    if st.button("Full Stack Web Developer -->>"):
        st.session_state.job_desc = get_job_description("Full Satck Web developer")
    if st.button("Graphics Designer -->>"):
        st.session_state.job_desc = get_job_description("Graphics designer")
    if st.button("Systems Analyst -->>"):
        st.session_state.job_desc = get_job_description("Systems Analyst")
    if st.button("Product Manager -->>"):
        st.session_state.job_desc = get_job_description("Product Manager")
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

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt, text, job_desc)
        st.subheader(response)
    else:
        st.write("Please upload the resume")
