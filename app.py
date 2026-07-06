import streamlit as st

from utils.theme import apply_theme
from utils.branding import show_sidebar


st.set_page_config(
    page_title="CropInsight AI",
    page_icon="🌾",
    layout="wide"
)


# Global styling
apply_theme()


# Global branding
show_sidebar()


# ---------------- HOME PAGE ----------------

st.title("🌾 CropInsight AI")

st.subheader(
    "Smart Agricultural Decision Support System"
)


st.success(
    "Welcome to CropInsight — helping farmers diagnose crop problems, predict risks, and make better agricultural decisions."
)


st.divider()


# Dashboard summary

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "System",
        "Online 🟢"
    )


with col2:

    st.metric(
        "AI Modules",
        "Active"
    )


with col3:

    st.metric(
        "Version",
        "v2.0"
    )


st.divider()


st.header(
    "🚀 CropInsight Modules"
)


features = [
    "🧠 AI Disease Diagnosis",
    "📸 Crop Image Scanner",
    "💊 Treatment Recommendations",
    "🌦 Weather Intelligence",
    "🤖 AI Farming Assistant",
    "📊 Farm Analytics"
]


for feature in features:

    st.write(feature)


st.divider()


st.caption(
    "CropInsight v2.0 • Nationals Edition"
)
