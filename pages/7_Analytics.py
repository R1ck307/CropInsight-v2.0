import streamlit as st
from expert_system.analytics_engine import (
    get_most_common_diseases,
    get_most_affected_crops,
    get_average_confidence,
    get_total_diagnoses
)

st.title("📊 CropInsight Analytics Dashboard")

st.subheader("📈 System Overview")

st.metric("Total Diagnoses", get_total_diagnoses())
st.metric("Average Confidence", f"{get_average_confidence()}%")

st.markdown("---")

st.subheader("🦠 Most Common Diseases")

diseases = get_most_common_diseases()

if diseases:
    for k, v in diseases.items():
        st.write(f"- **{k}**: {v} cases")
else:
    st.write("No data yet.")

st.markdown("---")

st.subheader("🌾 Most Affected Crops")

crops = get_most_affected_crops()

if crops:
    for k, v in crops.items():
        st.write(f"- **{k}**: {v} cases")
else:
    st.write("No data yet.")
