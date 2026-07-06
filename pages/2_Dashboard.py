import streamlit as st

from utils.page_setup import setup_page

from utils.farm_manager import get_user_farms
from utils.database import Database


setup_page()


# ---------------- LOGIN CHECK ----------------

if "user" not in st.session_state:

    st.warning(
        "Please login first."
    )

    st.stop()


user = st.session_state["user"]



# ---------------- DATABASES ----------------

diagnosis_db = Database(
    "database/diagnoses.csv"
)



# ---------------- HEADER ----------------

st.title(
    "🌱 CropInsight Dashboard"
)


st.subheader(
    f"Welcome back, {user['username']} 👋"
)


st.write(
    "Your smart farming command centre."
)



st.divider()



# ---------------- FARM INFORMATION ----------------


farms = get_user_farms(
    user["id"]
)


total_farms = len(farms)



# ---------------- DIAGNOSIS INFORMATION ----------------


diagnoses = diagnosis_db.load()



if not diagnoses.empty:

    user_diagnoses = diagnoses[
        diagnoses["user_id"] == user["id"]
    ]

else:

    user_diagnoses = diagnoses



total_diagnoses = len(
    user_diagnoses
)



# ---------------- STAT CARDS ----------------


col1, col2, col3 = st.columns(3)



with col1:

    st.metric(
        "🌾 Total Farms",
        total_farms
    )



with col2:

    st.metric(
        "🔬 Diagnoses Completed",
        total_diagnoses
    )



with col3:

    st.metric(
        "🟢 System Status",
        "Online"
    )



st.divider()



# ---------------- FARM SUMMARY ----------------


st.header(
    "🌱 Farm Overview"
)



if farms.empty:

    st.info(
        "No farms registered yet. Add a farm in Farm Profile."
    )


else:


    for _, farm in farms.iterrows():

        with st.container():

            st.subheader(
                f"🌾 {farm['farm_name']}"
            )


            col1, col2 = st.columns(2)


            with col1:

                st.write(
                    f"📍 Location: {farm['location']}"
                )

                st.write(
                    f"📏 Size: {farm['size_hectares']} hectares"
                )


            with col2:

                st.write(
                    f"🌱 Main Crop: {farm['main_crop']}"
                )


st.divider()



# ---------------- RECENT DIAGNOSIS ----------------


st.header(
    "🧠 Recent Diagnosis Activity"
)



if user_diagnoses.empty:

    st.info(
        "No diagnosis history available."
    )


else:


    recent = user_diagnoses.tail(5)


    for _, item in recent.iterrows():


        st.success(
            f"""
🌱 Crop: {item.get('crop','Unknown')}

🦠 Disease:
{item.get('disease','Unknown')}

🎯 Confidence:
{item.get('confidence','N/A')}%
"""
        )



st.divider()



# ---------------- QUICK ACTIONS ----------------


st.header(
    "🚀 Quick Actions"
)



col1, col2, col3 = st.columns(3)



with col1:

    st.info(
        "🔬 Diagnose Crop\n\nUse AI disease diagnosis."
    )



with col2:

    st.info(
        "📸 Scan Image\n\nDetect crop problems from images."
    )



with col3:

    st.info(
        "🌦 Weather\n\nCheck crop risk."
    )



st.divider()



st.caption(
    "CropInsight v2.0 • Nationals Edition"
  )
