import streamlit as st

from expert_system.diagnosis_engine import diagnose_crop
from utils.knowledge_base import get_crop_names
from utils.diagnosis_manager import save_diagnosis
from utils.farm_manager import get_user_farms

st.title("🧠 Crop Diagnosis")

# ---------------- LOGIN CHECK ----------------

if "user" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

user = st.session_state["user"]

# ---------------- LOAD FARMS ----------------

farms = get_user_farms(user["id"])

if farms.empty:
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

# ---------------- LOAD CROPS ----------------

crop = st.selectbox(
    "Select Crop",
    get_crop_names()
)

# ---------------- SYMPTOMS ----------------

st.info(
    "Separate symptoms using semicolons (;)\n\n"
    "Example:\n"
    "yellow leaves; wilting; dark spots"
)

symptoms = st.text_area(
    "Symptoms"
)

# ---------------- DIAGNOSIS ----------------

if st.button("Diagnose"):

    if not symptoms.strip():
        st.error("Please enter symptoms.")
        st.stop()

    results = diagnose_crop(crop, symptoms)

    if len(results) == 0:
        st.error("No matching disease found.")
        st.stop()

    st.success("Diagnosis Complete")

    st.subheader("Top Matches")

    for i, result in enumerate(results, start=1):

    # SAFE FALLBACKS (prevents crashes)
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

        with st.expander(
            f"{i}. {result['disease']} ({result['confidence']}%)",
            expanded=(i == 1)
        ):

            st.write(f"**Disease Type:** {result['type']}")
            st.write(f"**Severity:** {result['severity']}")
            st.write(f"**Cause:** {result['cause']}")
            st.write(f"**Treatment:** {result['treatment']}")
            st.write(f"**Prevention:** {result['prevention']}")

    # Save only the highest-confidence diagnosis
    best = results[0]

    save_diagnosis(
        user_id=user["id"],
        farm_id=farm_id,
        crop=crop,
        symptoms=symptoms,
        result={
            "disease": best["disease"],
            "confidence": best["confidence"],
            "severity": best["severity"],
            "treatment": best["treatment"]
        }
    )

    st.success("Diagnosis saved successfully.")
