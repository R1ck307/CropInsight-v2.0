import streamlit as st
from utils.auth import register_user, login_user

st.title("🔐 Login - CropInsight v2")

menu = st.radio("Choose Option", ["Login", "Register"])

# SESSION INIT
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# LOGIN
if menu == "Login":

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        success, result = login_user(username, password)

        if success:
            st.session_state["logged_in"] = True
            st.session_state["user"] = result
            st.success(f"Welcome {result['username']}")
        else:
            st.error(result)

# REGISTER
if menu == "Register":

    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")

    if st.button("Create Account"):
        success, msg = register_user(new_username, new_password)

        if success:
            st.success(msg)
        else:
            st.error(msg)
