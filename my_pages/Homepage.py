import streamlit as st

# Set up the Streamlit page configuration
# st.set_page_config(
#     page_title="JustClick",
#     page_icon="👉"
# )

# st.title(':blue[Welcome to ATS Checker]')
st.sidebar.success(':blue[Welcome to CareerSync-Home Page]')


# CSS styling
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
.header {
    text-align: center;
    padding: 50px 20px;
    background: #3498db;
    color: white;
}
.features, .testimonials {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
}
.feature, .testimonial {
    background: #ffffff;
    padding: 20px;
    margin: 10px;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    flex: 1;
    min-width: 250px;
}
.feature h3, .testimonial h3 {
    color: #2c3e50;
}
.feature p, .testimonial p {
    color: #34495e;
}
.cta {
    text-align: center;
    padding: 40px;
    background: #2ecc71;
    color: white;
}
.cta a {
    color: #ffffff;
    text-decoration: none;
    font-weight: bold;
}
</style>
"""

# Apply the CSS styles
st.markdown(css, unsafe_allow_html=True)


# Header section
st.markdown("""
<div class="header">
    <h1>Transform Your Job Search Experience</h1>
    <p>Enhance your resume, match your skills, and land your dream job with our cutting-edge platform.</p>
</div>
""", unsafe_allow_html=True)

# What We Offer section
st.markdown("""
<div class="section">
    <h2>What We Offer</h2>
    <div class="features">
        <div class="feature">
            <h3>ATS Score Analysis</h3>
            <p>Get an in-depth analysis of how well your resume matches job descriptions with our ATS score feature.</p>
        </div>
        <div class="feature">
            <h3>Skill Matching</h3>
            <p>Identify and improve your skills to match the job requirements effectively.</p>
        </div>
        <div class="feature">
            <h3>Experience Verification</h3>
            <p>Ensure your experience aligns with job requirements and boost your application success.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Testimonials section
st.markdown("""
<div class="section">
    <h2>What Our Users Say</h2>
    <div class="testimonials">
        <div class="testimonial">
            <h3>Alfiya Zoya</h3>
            <p>"JustClick helped me refine my resume and secure a job I had been aiming for. The ATS analysis was incredibly useful!"</p>
        </div>
        <div class="testimonial">
            <h3>Harshita Seksaria</h3>
            <p>"The skill matching and improvement suggestions were spot on. I landed a job much faster than I expected."</p>
        </div>
        <div class="testimonial">
            <h3>Ganesh Sharma</h3>
            <p>"A fantastic tool for job seekers. The experience verification feature gave me the confidence I needed to apply."</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Call-to-Action section
# st.markdown("""
# <div class="cta">
#     <h2>Ready to Boost Your Job Search?</h2>
#     <p><a href="/register">Sign Up Now</a> to get started and take the first step towards your dream job!</p>
# </div>
# """, unsafe_allow_html=True)

