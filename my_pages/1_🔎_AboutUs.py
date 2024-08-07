import streamlit as st

# st.set_page_config(page_title="About Us - JustClick", page_icon="📝")

css = """
<style>
body {
    background-color: #f5f5f5;
    margin: 0;
    padding: 0;
}
h1, h2, h3, h4, h5, h6 {
    color: #2c3e50;
}
p {
    color: #34495e;
}
.section {
    background: #ffffff;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
ul {
    list-style-type: disc;
    margin-left: 20px;
}
</style>
"""
st.title("About Us")

st.markdown(css, unsafe_allow_html=True)


st.markdown("""
<div class="section">
    <h2>Welcome to CareerSync</h2>
    <p>Your one-stop solution for enhancing job application processes and bridging the gap between talented candidates and their dream jobs.</p>
</div>

<div class="section">
    <h3>Our Mission</h3>
    <p>At JustClick, we aim to streamline the recruitment process for both job seekers and companies. Our advanced AI-driven platform provides tools to improve resume quality, match skills with job descriptions, and optimize the entire hiring journey.</p>
</div>

<div class="section">
    <h3>What We Offer</h3>
    <h2>For Job Seekers</h2>
    <p>
    <strong>ATS Score Analysis:</strong> Our platform analyzes your resume against job descriptions, providing an ATS score to help you understand how well your resume matches the job requirements.</p>
    <p><strong>Skill Matching and Improvement Suggestions:</strong> Get detailed feedback on the skills you have, the skills you match with the job, and areas for improvement.</p>
    <p><strong>Experience Verification:</strong> Compare your experience with the job requirements to ensure you meet or exceed the necessary criteria.</p>
    <p><strong>Job Role Specific Analysis:</strong> Easily check how well your resume fits various job roles and get suggestions to align it better.</p>
</div>
<div class="section">
    <h3>For Companies</h3>
    <p>Job Posting:</strong> Post open job roles and attract qualified candidates.
        Candidate Screening: Utilize our platform to shortlist the best candidates based on their ATS scores and skill matches.
        Efficiency and Accuracy: Save time and resources by automating the initial screening process, ensuring you focus on the most promising applicants.</p>
</div>

<div class="section">
    <h3>How We Help</h3>
    <p>Whether you are a job seeker looking to enhance your resume or a company aiming to streamline your hiring process, JustClick is here to help. Join us today and take the first step towards a more efficient and effective job application process.</p>
</div>

<div class="section">
    <h3>Our Technology</h3>
    <p>We leverage state-of-the-art AI algorithms and machine learning models to provide accurate and insightful analysis of resumes and job descriptions. By integrating with various ATS systems and using advanced text analysis techniques, we ensure that our platform delivers reliable and actionable results.</p>
</div>

<div class="section">
    <h3>Get in Touch</h3>
    <p>Whether you are a job seeker or a company, CareerSync is here to assist. Contact us to learn more about how we can help you achieve your goals.</p>
    <p><strong>Contact Us:</strong> <a href="mailto:support@carrersync.com">support@careersync.com</a></p>
</div>
""", unsafe_allow_html=True)

