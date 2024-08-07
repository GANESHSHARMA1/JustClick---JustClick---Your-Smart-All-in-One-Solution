import streamlit as st
import pymongo
from pymongo import MongoClient
import hashlib

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "User", "Admin"]

def get_mongo_client():
    uri = "mongodb+srv://GaneshKithana:iyES7TdrvmkuFxJ@justclick.ps3ayrm.mongodb.net/test?appName=JustClick"
    client = MongoClient(uri, server_api=pymongo.server_api.ServerApi('1'))
    return client

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    st.title("Register")

    email = st.text_input("Email")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register", key="register_button"):
        if password != confirm_password:
            st.error("Passwords do not match")
        else:
            client = get_mongo_client()
            db = client['user_database']
            users = db['users']

            if users.find_one({"username": username}):
                st.error("Username already exists")
            else:
                hashed_password = hash_password(password)
                new_user = {
                    "role": "User",
                    "email": email,
                    "username": username,
                    "password": hashed_password
                }
                users.insert_one(new_user)
                st.success("Registration successful! Please login.")
                st.experimental_set_query_params(page='login')
                st.experimental_rerun()

def login():
    st.header("Log in")
    role = st.selectbox("Choose your role (Login)", ROLES, key="login_role")

    if role:
        if role != "Admin":
            existing_or_new = st.radio("Are you an existing user?", ("Yes", "No"))

            if existing_or_new == "Yes":
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")

                if st.button("Login", key="login_button"):
                    client = get_mongo_client()
                    db = client['user_database']
                    users = db['users']

                    user = users.find_one({"username": username, "role": "User"})
                    if user and user["password"] == hash_password(password):
                        st.session_state.role = role
                        st.session_state.user_id = user["_id"]
                        st.success("Login successful!")
                        st.experimental_set_query_params(page='home')
                        st.experimental_rerun()
                    else:
                        st.error("Invalid username or password")
            else:
                register()
        else:
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            if st.button("Login", key="admin_login_button"):
                client = get_mongo_client()
                db = client['user_database']
                users = db['users']

                user = users.find_one({"username": username, "role": "Admin"})
                if user and user["password"] == hash_password(password):
                    st.session_state.role = role
                    st.session_state.user_id = user["_id"]
                    st.success("Login successful!")
                    st.experimental_set_query_params(page='admin')
                    st.experimental_rerun()
                else:
                    st.error("Invalid username or password")


def logout():
    st.session_state.role = None
    st.rerun()

role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
# settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
Home_page = st.Page(
    "my_pages/Homepage.py",
    title="Home Page",
    icon="👉",
    default=True,
)
About_us = st.Page(
    "my_pages/1_🔎_AboutUs.py",
    title="About Us",
    icon="🔎",
)
Check_ATS = st.Page(
    "my_pages/2_📄_CheckATS.py",
    title="Check ATS",
    icon="📝",
)
Job_portal = st.Page(
    "my_pages/3_🧾_jobPortal.py",
    title="Job Portal",
    icon="🧾",
)
Job_matcher = st.Page(
    "my_pages/4_📜_jobMatcher.py",
    title="Job Matcher",
    icon="📜",
)
Validator = st.Page(
    "my_pages/5_☑️_Validator.py",
    title="Resume Validator",
    icon="☑️",
)
admin_1 = st.Page(
    "company/admin.py",
    title="Applicant Scanner",
    icon=":material/person_add:",
)

# account_pages = [logout_page, settings]
account_pages = [logout_page]
user_pages = [Home_page, About_us, Check_ATS, Job_portal, Job_matcher, Validator]
admin_pages = [admin_1]

st.title(':blue[Welcome to CareerSync]')

page_dict = {}
if st.session_state.role in ["User", "Admin"]:
    page_dict["User"] = user_pages
if st.session_state.role == "Admin":
    page_dict["Admin"] = admin_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()
