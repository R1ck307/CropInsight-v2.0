import streamlit as st

from utils.page_setup import setup_page
from utils.system_check import run_system_check, system_ready


setup_page()


st.title("⚙️ System Administration")


st.subheader(
    "CropInsight System Health"
)


if system_ready():

    st.success(
        "✅ System Ready"
    )

else:

    st.error(
        "⚠️ Issues Detected"
    )


st.divider()


for item in run_system_check():


    if item["status"] == "OK":

        st.success(
            f"✅ {item['file']}"
        )

    else:

        st.error(
            f"❌ Missing: {item['file']}"
        )
