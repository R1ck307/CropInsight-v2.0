from expert_system.report_engine import generate_report
import streamlit as st

from expert_system.diagnosis_engine import diagnose_crop
from expert_system.recommendation_engine import (
    get_treatment_advice,
    get_fertilizer_advice
)

from utils.knowledge_base import get_crop_names
from utils.farm_manager import get_user_farms
from utils.diagnosis_manager import save_diagnosis


st.title("🧠 CropInsight AI Diagnosis & Advisory")

# ---------------- LOGIN CHECK ----------------
if "user" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

user = st.session_state["user"]

# ---------------- FARMS ----------------
farms = get_user_farms(user["id"])

if farms is None or farms.empty:
    st.warning("No farms found. Please create a farm first.")
    st.stop()

farm_name = st.selectbox("Select Farm", farms["farm_name"].tolist())

farm_id = int(
    farms.loc[
        farms["farm_name"] == farm_name,
        "farm_id"
    ].iloc[0]
)

# ---------------- CROPS ----------------
crop = st.selectbox("Select Crop", get_crop_names())

# ---------------- SYMPTOMS ----------------
st.info("Use semicolon (;) to separate symptoms\nExample: yellow leaves; spots; wilting")

symptoms = st.text_area("Enter Symptoms")

# ---------------- RUN DIAGNOSIS ----------------
if st.button("Run AI Diagnosis"):

    if not symptoms.strip():
        st.error("Please enter symptoms.")
        st.stop()

    results = diagnose_crop(crop, symptoms)

    if not results:
        st.error("No matching disease found.")
        st.stop()

    st.success("Diagnosis Complete")

    st.subheader("🔍 Top 3 Possible Diagnoses")

    # ---------------- DIAGNOSIS RESULTS ----------------
    for i, result in enumerate(results, start=1):

        disease = result.get("disease", "Unknown")
        confidence = result.get("confidence", 0)
        severity = result.get("severity", "Unknown")
        dtype = result.get("type", "Unknown")
        cause = result.get("cause", "Not available")
        treatment = result.get("treatment", "Not available")
        prevention = result.get("prevention", "Not available")

        with st.expander(f"{i}. {disease} ({confidence}%)", expanded=(i == 1)):

            st.write(f"**Type:** {dtype}")
            st.write(f"**Severity:** {severity}")
            st.write(f"**Cause:** {cause}")
            st.write(f"**Treatment (from disease DB):** {treatment}")
            st.write(f"**Prevention:** {prevention}")

            # 🧠 NEW: SMART RECOMMENDATIONS
            st.markdown("---")
            st.subheader("💊 AI Recommendations")

            treatment_adv = get_treatment_advice(disease)
            fertilizer_adv = get_fertilizer_advice(crop)

            if treatment_adv:
                st.write("### Recommended Treatments")
                for t in treatment_adv:
                    st.write(f"- **{t['treatment_name']}**: {t['description']}")

            else:
                st.write("No specific treatment match found.")

            if fertilizer_adv:
                st.write("### Recommended Fertilizers")
                for f in fertilizer_adv:
                    st.write(f"- **{f['fertilizer_name']} ({f['npk_ratio']})**: {f['notes']}")

            else:
                st.write("No fertilizer recommendation found.")

    # ---------------- SAVE BEST RESULT ----------------
    best = results[0]

    save_diagnosis(
        user_id=user["id"],
        farm_id=farm_id,
        crop=crop,
        symptoms=symptoms,
        result={
            "disease": best.get("disease", "Unknown"),
            "confidence": best.get("confidence", 0),
            "severity": best.get("severity", "Unknown"),
            "treatment": best.get("treatment", "Not available")
        }
    )

    st.success("Saved to diagnosis history")
