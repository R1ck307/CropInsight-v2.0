import streamlit as st
from expert_system.diagnosis_engine import diagnose_crop

st.title("🧠 Crop Diagnosis Engine")

if "user" not in st.session_state:
    st.warning("Please login first")
    st.stop()

crop = st.selectbox("Select Crop", ["maize", "tomato", "beans"])

symptoms = st.text_area(
    "Enter Symptoms (comma separated)",
    placeholder="e.g. brown spots, yellow edges, leaf damage"
)

if st.button("Diagnose"):

    if symptoms.strip() == "":
        st.error("Please enter symptoms")
    else:
        result = diagnose_crop(crop, symptoms)

        st.subheader("📊 Diagnosis Result")
        st.write("Disease:", result["disease"])
        st.write("Confidence:", str(result["confidence"]) + "%")
        st.write("Severity:", result["severity"])
        st.success("Treatment: " + result["treatment"])
