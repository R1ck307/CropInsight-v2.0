import streamlit as st

from utils.page_setup import setup_page


setup_page()


st.title(
    "⚙️ CropInsight Settings"
)


st.subheader(
    "Manage your account and application preferences"
)



# ---------------- USER CHECK ----------------


if "user" not in st.session_state:

    st.warning(
        "Please login first."
    )

    st.stop()



user = st.session_state["user"]



# ---------------- ACCOUNT ----------------


st.divider()


st.header(
    "👤 Account Information"
)


col1, col2 = st.columns(2)


with col1:

    st.info(
        f"Username:\n\n{user.get('username','Unknown')}"
    )


with col2:

    st.info(
        f"Role:\n\n{user.get('role','Farmer')}"
    )



st.divider()



# ---------------- PREFERENCES ----------------


st.header(
    "🌍 Preferences"
)


language = st.selectbox(
    "Application Language",
    [
        "English",
        "Siswati",
        "French",
        "Portuguese"
    ]
)


st.success(
    f"Selected language: {language}"
)



st.divider()



# ---------------- APPEARANCE ----------------


st.header(
    "🎨 Appearance"
)


st.write(
    "CropInsight uses the unified application theme."
)


st.info(
    "Theme management is controlled by the global theme system."
)



st.divider()



# ---------------- SECURITY ----------------


st.header(
    "🔐 Security"
)


st.write(
    "Password management and account security."
)


if st.button(
    "Change Password"
):

    st.info(
        "Password update feature can be connected to the authentication system."
    )



st.divider()



# ---------------- ABOUT ----------------


st.header(
    "ℹ️ About CropInsight"
)


st.write(
    """
CropInsight v2.0

Smart Agricultural Decision Support System.

Features:
• AI Disease Diagnosis
• Crop Image Scanner
• Weather Intelligence
• Risk Prediction
• Farming Assistant
• Agricultural Knowledge Base

Nationals Edition
"""
)



st.divider()


st.caption(
    "CropInsight v2.0 • Smart Farming Technology"
  )
