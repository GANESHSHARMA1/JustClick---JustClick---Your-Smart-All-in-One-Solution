import streamlit as st
from utils import get_mongo_client, hash_password

st.set_page_config(page_title="Register", page_icon="📝")

client = get_mongo_client()
db = client['user_database']
users = db['users']

st.title("Register")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Register"):
    if users.find_one({"username": username}):
        st.error("Username already exists")
    else:
        users.insert_one({"username": username, "password": hash_password(password), "is_admin": False})
        st.success("Registration successful! Please login.")
        st.experimental_set_query_params(page='login')
        st.experimental_rerun()
