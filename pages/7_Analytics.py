import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.diagnosis_manager import get_user_diagnoses
from utils.farm_manager import get_user_farms

st.title("📊 Analytics Dashboard")

if "user" not in st.session_state:
    st.warning("Please login first")
    st.stop()

user = st.session_state["user"]

# LOAD DATA
diagnoses = get_user_diagnoses(user["id"])
farms = get_user_farms(user["id"])

if diagnoses.empty:
    st.info("No diagnosis data available yet.")
    st.stop()

# ---------------- SUMMARY ----------------
st.subheader("📌 Overview")

total_diagnoses = len(diagnoses)
unique_diseases = diagnoses["disease"].nunique()
avg_confidence = diagnoses["confidence"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Diagnoses", total_diagnoses)
col2.metric("Unique Diseases", unique_diseases)
col3.metric("Avg Confidence", f"{avg_confidence:.2f}%")

st.divider()

# ---------------- DISEASE DISTRIBUTION ----------------
st.subheader("🦠 Disease Distribution")

disease_counts = diagnoses["disease"].value_counts()

fig1, ax1 = plt.subplots()
disease_counts.plot(kind="bar", ax=ax1)
ax1.set_ylabel("Count")
ax1.set_xlabel("Disease")

st.pyplot(fig1)

st.divider()

# ---------------- CROP ANALYSIS ----------------
st.subheader("🌾 Crop Analysis")

crop_counts = diagnoses["crop"].value_counts()

fig2, ax2 = plt.subplots()
crop_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax2)

st.pyplot(fig2)

st.divider()

# ---------------- HISTORY TABLE ----------------
st.subheader("📜 Diagnosis History")

st.dataframe(diagnoses.sort_values("date", ascending=False))
