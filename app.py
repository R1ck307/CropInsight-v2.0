import streamlit as st

from utils.theme import apply_theme
from utils.knowledge_base import load_crops
from expert_system.analytics_engine import (
    get_total_diagnoses,
    get_average_confidence
)

st.set_page_config(
    page_title="CropInsight AI",
    page_icon="🌾",
    layout="wide"
)

apply_theme()

# ---------------- HEADER ----------------

st.title("🌾 CropInsight AI")
st.caption("Smart Agricultural Decision Support System")

st.success("Welcome to CropInsight! Helping farmers make better decisions using intelligent crop diagnosis and recommendations.")

st.divider()

# ---------------- DASHBOARD CARDS ----------------

crop_count = 0
crops = load_crops()

if crops is not None:
    crop_count = len(crops)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🌱 Supported Crops", crop_count)

with col2:
    st.metric("🩺 Diagnoses", get_total_diagnoses())

with col3:
    st.metric("🎯 Avg Confidence", f"{get_average_confidence()}%")

with col4:
    st.metric("🟢 Status", "Online")

st.divider()

# ---------------- FEATURES ----------------

st.subheader("🚀 What CropInsight Can Do")

left, right = st.columns(2)

with left:
    st.markdown("""
- 🧠 Diagnose crop diseases
- 💊 Recommend treatments
- 🌿 Suggest fertilizers
- 📊 Track diagnosis history
""")

with right:
    st.markdown("""
- 🤖 AI Farming Assistant
- 📈 Farm analytics
- 📄 Generate reports
- 🌍 Designed for African agriculture
""")

st.divider()

# ---------------- GET STARTED ----------------

st.subheader("📍 Get Started")

st.info(
    """
1. Login using the Login page.
2. Create your farm profile.
3. Open the Diagnosis page.
4. Enter crop symptoms.
5. View recommendations and download your report.
    """
)

st.divider()

st.caption("CropInsight v2.0 • Nationals Edition • Developed by Richard Makwakwa")
