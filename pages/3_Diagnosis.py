import streamlit as st

from expert_system.diagnosis_engine import diagnose_crop
from utils.knowledge_base import get_crop_names
from utils.farm_manager import get_user_farms
from utils.diagnosis_manager import save_diagnosis


st.title("🧠 Crop Diagnosis System")

# ---------------- SESSION CHECK ----------------
if "user" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

user = st.session_state["user"]

# ---------------- LOAD FARMS ----------------
farms = get_user_farms(user["id"])

if farms is None or farms.empty:
    st.warning("No farms found. Please create a farm first.")
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

# ---------------- LOAD CROPS ----------------
crop_list = get_crop_names()

if not crop_list:
    st.error("No crops found in database.")
    st.stop()

crop = st.selectbox("Select Crop", crop_list)

# ---------------- SYMPTOMS INPUT ----------------
st.info("Separate symptoms using semicolons (;)\nExample: yellow leaves; wilting; dark spots")

symptoms = st.text_area("Enter Symptoms")

# ---------------- DIAGNOSIS BUTTON ----------------
if st.button("Run Diagnosis"):

    if not symptoms.strip():
        st.error("Please enter symptoms.")
        st.stop()

    results = diagnose_crop(crop, symptoms)

    if not results:
        st.error("No matching diseases found.")
        st.stop()

    st.success("Diagnosis Complete")

    st.subheader("Top 3 Possible Diseases")

    # ---------------- RESULTS DISPLAY ----------------
    for i, result in enumerate(results, start=1):

        disease = result.get("disease", "Unknown disease")
        confidence = result.get("confidence", 0)
        severity = result.get("severity", "Unknown")
        dtype = result.get("type", "Unknown")
        cause = result.get("cause", "Not available")
        treatment = result.get("treatment", "Not available")
        prevention = result.get("prevention", "Not available")

        with st.expander(
            f"{i}. {disease} ({confidence}%)",
            expanded=(i == 1)
        ):

            st.write(f"**Disease Type:** {dtype}")
            st.write(f"**Severity:** {severity}")
            st.write(f"**Cause:** {cause}")
            st.write(f"**Treatment:** {treatment}")
            st.write(f"**Prevention:** {prevention}")

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

    st.success("Saved to diagnosis history.")
