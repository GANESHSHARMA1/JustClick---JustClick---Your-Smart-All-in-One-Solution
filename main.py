import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_repsonse(prompt_input, pdf_tex, job_dec):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt_input, pdf_tex, job_dec])
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text


# software engineering,data science ,data analyst
# and big data engineer

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field for the Job role given in job description. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in a proper manner having the structure
"Job Description": "\n","","\n",
"JD Match":"%","\n",
"MissingKeywords:[]","\n",
"Profile Summary":""
"""


st.title("JustClick - Enhancing Your Efficiency, Every Click")
st.text("Test Your Resume ATS")

job_desc=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt, text, job_desc)
        st.subheader(response)
    else:
        st.write("Please uplaod the resume")