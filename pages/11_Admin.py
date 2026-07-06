import streamlit as st
import pandas as pd

from utils.database import Database

st.title("🧑‍💼 Admin Dashboard")

if "user" not in st.session_state:
    st.warning("Please login first")
    st.stop()

user = st.session_state["user"]

# SIMPLE ROLE CHECK
if user.get("role") != "admin":
    st.error("Access denied. Admins only.")
    st.stop()

# LOAD DATABASES
users_db = Database("database/users.csv")
farms_db = Database("database/farms.csv")
diag_db = Database("database/diagnoses.csv")

users = users_db.load()
farms = farms_db.load()
diagnoses = diag_db.load()

# ---------------- OVERVIEW ----------------
st.subheader("📊 System Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Users", len(users))
col2.metric("Total Farms", len(farms))
col3.metric("Total Diagnoses", len(diagnoses))

st.divider()

# ---------------- USERS ----------------
st.subheader("👤 Users")
if users.empty:
    st.info("No users found")
else:
    st.dataframe(users)

st.divider()

# ---------------- FARMS ----------------
st.subheader("🌾 Farms")
if farms.empty:
    st.info("No farms found")
else:
    st.dataframe(farms)

st.divider()

# ---------------- DIAGNOSES ----------------
st.subheader("🧠 Diagnoses")
if diagnoses.empty:
    st.info("No diagnoses found")
else:
    st.dataframe(diagnoses)
