import streamlit as st

from expert_system.diagnosis_engine import diagnose_crop
from expert_system.recommendation_engine import (
    get_treatment_advice,
    get_fertilizer_advice
)

from expert_system.report_engine import generate_report

from utils.knowledge_base import get_crop_names
from utils.farm_manager import get_user_farms
from utils.diagnosis_manager import save_diagnosis


st.title("🧠 CropInsight AI Diagnosis")


# LOGIN CHECK
if "user" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

user = st.session_state["user"]


# LOAD FARMS
farms = get_user_farms(user["id"])

if farms is None or farms.empty:
    st.warning("Please create a farm first.")
    st.stop()


farm_name = st.selectbox(
    "Select Farm",
    farms["farm_name"].tolist()
)


farm_id = int(
    farms.loc[
        farms["farm_name"] == farm_name,
        "farm_id"
    ].iloc[0]
)


# CROP SELECTION
crop = st.selectbox(
    "Select Crop",
    get_crop_names()
)


# SYMPTOMS
symptoms = st.text_area(
    "Enter symptoms separated by ;",
    placeholder="yellow leaves; spots; wilting"
)



if st.button("Run AI Diagnosis"):

    if not symptoms.strip():
        st.error("Enter symptoms first.")
        st.stop()


    results = diagnose_crop(
        crop,
        symptoms
    )


    if not results:
        st.error("No matching disease found.")
        st.stop()


    st.success("Diagnosis completed")


    st.subheader("Possible Diseases")


    for index, result in enumerate(results, start=1):

        if not isinstance(result, dict):
            continue


        disease = result.get(
            "disease",
            "Unknown"
        )

        confidence = result.get(
            "confidence",
            0
        )


        with st.expander(
            f"{index}. {disease} ({confidence}%)",
            expanded=(index == 1)
        ):

            st.write(
                "Severity:",
                result.get("severity")
            )

            st.write(
                "Cause:",
                result.get("cause")
            )

            st.write(
                "Treatment:",
                result.get("treatment")
            )

            st.write(
                "Prevention:",
                result.get("prevention")
            )


    best = results[0]


    # SAVE HISTORY
    save_diagnosis(
        user_id=user["id"],
        farm_id=farm_id,
        crop=crop,
        symptoms=symptoms,
        result=best
    )


    # REPORT DOWNLOAD
    report = generate_report(
        user=user,
        farm_name=farm_name,
        crop=crop,
        symptoms=symptoms,
        diagnosis=best
    )


    st.download_button(
        "📄 Download Diagnosis Report",
        report,
        file_name="cropinsight_report.txt"
    )


    st.success(
        "Diagnosis saved successfully."
    )
