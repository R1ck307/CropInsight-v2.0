import streamlit as st

from utils.theme import apply_theme
from utils.knowledge_base import load_crops
from expert_system.analytics_engine import get_total_diagnoses


st.set_page_config(
    page_title="CropInsight AI",
    page_icon="🌾",
    layout="wide"
)


# Apply global theme
apply_theme()


# ---------------- HEADER ----------------

st.title("🌾 CropInsight AI Platform")

st.subheader(
    "Smart Agricultural Decision Support System"
)


# ---------------- STAT CARDS ----------------

col1, col2, col3 = st.columns(3)


with col1:
    crops = load_crops()

    if crops is not None:
        crop_count = len(crops)
    else:
        crop_count = 0

    st.metric(
        "Supported Crops",
        crop_count
    )


with col2:

    st.metric(
        "Total Diagnoses",
        get_total_diagnoses()
    )


with col3:

    st.metric(
        "System Status",
        "Online 🟢"
    )


st.divider()


# ---------------- FEATURES ----------------

st.header("🚀 CropInsight Features")


features = [
    "🧠 AI-powered crop disease diagnosis",
    "💊 Treatment and fertilizer recommendations",
    "🌱 African crop knowledge base",
    "📊 Farm health analytics",
    "🤖 AI farming assistant",
    "📄 Diagnosis report generation"
]


for feature in features:
    st.write(feature)


st.divider()


st.info(
    "Use the sidebar to navigate through CropInsight modules."
)
