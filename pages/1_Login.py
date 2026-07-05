import streamlit as st
from utils.auth import register_user, login_user

st.title("🔐 Login / Register - CropInsight v2")

menu = st.radio("Choose Action", ["Login", "Register"])

# ---------------- LOGIN ----------------
if menu == "Login":
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        success, result = login_user(username, password)

        if success:
            st.success(f"Welcome {result['username']}!")

            st.session_state["user"] = result
            st.session_state["logged_in"] = True
        else:
            st.error(result)

# ---------------- REGISTER ----------------
elif menu == "Register":
    username = st.text_input("New Username")
    password = st.text_input("New Password", type="password")

    if st.button("Create Account"):
        success, msg = register_user(username, password)

        if success:
            st.success(msg)
        else:
            st.error(msg)
