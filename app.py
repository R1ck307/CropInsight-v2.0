import streamlit as st
from utils.knowledge_base import load_crops
from expert_system.analytics_engine import get_total_diagnoses

st.set_page_config(
    page_title="CropInsight AI",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 CropInsight AI Platform")

st.subheader("Smart Agricultural Decision Support System")

# ---------------- STATS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Supported Crops", len(load_crops()))

with col2:
    st.metric("Total Diagnoses", get_total_diagnoses())

with col3:
    st.metric("System Status", "Online 🟢")

st.markdown("---")

st.markdown("## 🚀 What CropInsight Does")

st.write("""
- 🧠 Detects crop diseases using AI-style reasoning
- 💊 Recommends treatments and fertilizers
- 🌾 Supports major African crops
- 📊 Tracks farm health over time
- 🤖 Provides AI farming assistance
""")

st.markdown("---")

st.markdown("## 👈 Use the sidebar to navigate")

st.info("Start with Diagnosis or Farm Profile to begin analyzing your crops.")
