from utils.auth import create_admin_if_not_exists

create_admin_if_not_exists()
import streamlit as st

st.set_page_config(
    page_title="CropInsight v2",
    page_icon="🌾",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

st.title("🌾 CropInsight v2")

if st.session_state["logged_in"]:
    user = st.session_state["user"]
    st.success(f"Logged in as {user['username']} ({user['role']})")
    st.write("Welcome to the system 🚀")
else:
    st.warning("Please login from the Login page to continue.")
