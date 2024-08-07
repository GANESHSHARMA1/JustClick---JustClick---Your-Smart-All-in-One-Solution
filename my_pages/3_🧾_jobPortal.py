import streamlit as st
from pymongo import MongoClient
import gridfs
from pymongo.server_api import ServerApi

# st.set_page_config(page_title="Job Openings", page_icon="📝")
st.title("Job Openings")

@st.cache_resource
def get_mongo_client():
    with st.spinner("Finding the open job roles..."):
        uri = "mongodb+srv://GaneshKithana:iyES7TdrvmkuFxJ@justclick.ps3ayrm.mongodb.net/test?appName=JustClick"
        client = MongoClient(uri, server_api=ServerApi('1'))
        return client

# Fetch job openings from MongoDB and cache the data
@st.cache_data
def get_job_openings():
    client = get_mongo_client()
    db = client['ATS']
    jobs_collection = db['jobs']
    return list(jobs_collection.find())

# Initialize MongoDB client and GridFS
client = get_mongo_client()
db = client['ATS']
fs = gridfs.GridFS(db)

with st.spinner("personalising best job roles for you..."):
    # Fetch job openings from the cache
    job_openings = get_job_openings()

if 'apply_status' not in st.session_state:
    st.session_state.apply_status = {}

for job in job_openings:
    job_id = str(job['_id'])
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.subheader(job['title'])
        st.write(job['description'])
    with col2:
        if st.button(f"Apply", key=f"apply_{job_id}"):
            st.session_state.apply_status[job_id] = True

    st.write(f"*Location:* {job['location']}")
    st.write(f"*Salary:* ${job['salary']}")
    

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
                st.session_state.apply_status[job_id] = False  # Reset the apply status
            else:
                st.error("Please provide your name and upload your resume.")

# Function to view applicants for each job (optional, for admin use)
@st.cache_data
def get_applicants(job_title):
    client = get_mongo_client()
    job_title_collection = client['ATS'][job_title.replace(" ", "_")]
    return list(job_title_collection.find())

def view_applicants():
    for job in job_openings:
        st.subheader(f"Applicants for {job['title']}")
        applicants = get_applicants(job['title'])
        
        for applicant in applicants:
            st.write(f"Applicant: {applicant['name']}, Resume: {applicant['resume_filename']}")
            if st.button(f"Download {applicant['resume_filename']}", key=f"download_{applicant['resume_id']}"):
                file_info = fs.get(applicant['resume_id'])
                st.download_button("Download", file_info.read(), applicant['resume_filename'])

# Uncomment the line below to view applicants (for admin use)
# view_applicants()
