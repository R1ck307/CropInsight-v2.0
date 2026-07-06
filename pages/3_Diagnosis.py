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

from utils.theme import apply_theme, page_header


# Apply theme
apply_theme()


page_header(
    "AI Crop Diagnosis",
    "Detect diseases and receive intelligent farming recommendations"
)


# ---------------- LOGIN CHECK ----------------

if "user" not in st.session_state:
    st.warning("Please login first.")
    st.stop()


user = st.session_state["user"]


# ---------------- FARM SELECTION ----------------

farms = get_user_farms(user["id"])


if farms is None or farms.empty:
    st.warning("Create a farm profile first.")
    st.stop()


farm_name = st.selectbox(
    "🌾 Select Farm",
    farms["farm_name"].tolist()
)


farm_id = int(
    farms.loc[
        farms["farm_name"] == farm_name,
        "farm_id"
    ].iloc[0]
)


# ---------------- CROP ----------------

crop = st.selectbox(
    "🌱 Select Crop",
    get_crop_names()
)


# ---------------- SYMPTOMS ----------------

symptoms = st.text_area(
    "🔍 Describe Symptoms",
    placeholder=
    "Example: yellow leaves; dark spots; wilting"
)


st.caption(
    "Separate symptoms using semicolons (;)"
)


# ---------------- DIAGNOSIS ----------------

if st.button("🧠 Run AI Diagnosis"):


    if not symptoms.strip():

        st.error(
            "Please enter symptoms first."
        )

        st.stop()



    results = diagnose_crop(
        crop,
        symptoms
    )


    if not results:

        st.error(
            "No matching disease found."
        )

        st.stop()



    st.success(
        "Analysis Complete"
    )


    st.subheader(
        "🔬 Diagnosis Results"
    )


    for index, result in enumerate(results, start=1):

        disease = result.get(
            "disease",
            "Unknown"
        )

        confidence = result.get(
            "confidence",
            0
        )

        severity = result.get(
            "severity",
            "Unknown"
        )


        with st.container():

            st.markdown("---")


            st.subheader(
                f"{index}. {disease}"
            )


            st.progress(
                min(
                    confidence / 100,
                    1.0
                )
            )


            st.write(
                f"🎯 Confidence: {confidence}%"
            )


            if severity.lower() == "high":

                st.error(
                    f"Severity: {severity}"
                )

            elif severity.lower() == "medium":

                st.warning(
                    f"Severity: {severity}"
                )

            else:

                st.success(
                    f"Severity: {severity}"
                )


            col1, col2 = st.columns(2)


            with col1:

                st.write(
                    "🦠 Disease Type"
                )

                st.write(
                    result.get(
                        "type",
                        "Unknown"
                    )
                )


                st.write(
                    "⚠ Cause"
                )

                st.write(
                    result.get(
                        "cause",
                        "Not available"
                    )
                )


            with col2:

                st.write(
                    "💊 Treatment"
                )

                st.write(
                    result.get(
                        "treatment",
                        "Not available"
                    )
                )


                st.write(
                    "🛡 Prevention"
                )

                st.write(
                    result.get(
                        "prevention",
                        "Not available"
                    )
                )


            st.markdown(
                "### 🌿 Smart Recommendations"
            )


            treatments = get_treatment_advice(
                disease
            )


            fertilizers = get_fertilizer_advice(
                crop
            )


            if treatments:

                for item in treatments:

                    st.write(
                        "💊",
                        item.get(
                            "treatment_name",
                            "Treatment"
                        )
                    )


            if fertilizers:

                for item in fertilizers:

                    st.write(
                        "🌱",
                        item.get(
                            "fertilizer_name",
                            "Fertilizer"
                        )
                    )



    # ---------------- SAVE + REPORT ----------------


    best = results[0]


    save_diagnosis(
        user_id=user["id"],
        farm_id=farm_id,
        crop=crop,
        symptoms=symptoms,
        result=best
    )


    report = generate_report(
        user=user,
        farm_name=farm_name,
        crop=crop,
        symptoms=symptoms,
        diagnosis=best
    )


    st.download_button(
        "📄 Download Farm Report",
        report,
        file_name="CropInsight_Report.txt"
    )


    st.success(
        "Diagnosis saved successfully."
            )
