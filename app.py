from utils.report_generator import generate_pdf_report
import os
import streamlit as st
from expert_system.inference import CropExpertSystem

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="CropInsight V2 🌾",
    page_icon="🌱",
    layout="wide"
)

# ----------------------------
# DARK AI STYLE UI
# ----------------------------
st.markdown("""
<style>
.main {
    background-color: #0f172a;
}

h1 {
    color: #4ade80;
    font-weight: 800;
}

h2, h3 {
    color: #e2e8f0;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

div[data-testid="metric-container"] {
    background-color: #1f2937;
    border-radius: 12px;
    padding: 10px;
    color: white;
}

.stButton > button {
    background-color: #22c55e;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    background-color: #16a34a;
}

textarea {
    background-color: #1f2937 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# TITLE
# ----------------------------
st.title("🌾 CropInsight V2 - AI Crop Disease Expert System")
st.markdown("Smart farming assistant for African agriculture 🌍")

# ----------------------------
# LOAD SYSTEM
# ----------------------------
system = CropExpertSystem(
    "data/crops.csv",
    "data/diseases.csv",
    "data/treatments.csv"
)

# ----------------------------
# SIDEBAR NAV
# ----------------------------
st.sidebar.header("🧭 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Diagnose", "📊 Dashboard"])

# ----------------------------
# DIAGNOSIS PAGE
# ----------------------------
if page == "🏠 Diagnose":

    st.subheader("🧠 Crop Diagnosis Engine")

    col1, col2 = st.columns(2)

    with col1:
        crop = st.selectbox(
            "🌾 Select Crop",
            sorted(system.crops["name"].tolist())
        )

    with col2:
        symptoms = st.text_area(
            "✍️ Enter Symptoms",
            placeholder="e.g. yellow leaves, brown spots, wilting..."
        )

    if st.button("🔍 Run Diagnosis"):

        if not symptoms:
            st.warning("Please enter symptoms first.")
        else:
            result = system.run_diagnosis(crop, symptoms)

            if result["status"] == "no_match":
                st.error(result["message"])
            else:
                st.success("AI Diagnosis Complete ✔️")

                # ----------------------------
                # BEST MATCH CARD
                # ----------------------------
                best = result["best_match"]

                st.subheader("🎯 AI Diagnosis Result")

                st.markdown(f"""
                <div style="
                    background-color:#1f2937;
                    padding:20px;
                    border-radius:15px;
                    margin-bottom:15px;
                ">
                    <h3 style="color:#4ade80;">🦠 {best['disease']}</h3>
                    <p><b>🌾 Crop:</b> {crop}</p>
                    <p><b>📊 Confidence:</b> {best['confidence']}%</p>
                    <p><b>⚠️ Severity:</b> {best['severity']}</p>
                </div>
                """, unsafe_allow_html=True)

                # ----------------------------
                # ALL MATCHES
                # ----------------------------
                st.subheader("📊 Other Possible Matches")

                for m in result["matches"]:
                    st.write(f"🦠 {m['disease']} - {m['confidence']}%")

                # ----------------------------
                # TREATMENTS
                # ----------------------------
                st.subheader("💊 Recommended Treatments")

                for t in result["treatments"]:
                    st.markdown(f"""
                    <div style="
                        background-color:#0b1220;
                        padding:12px;
                        border-left:4px solid #22c55e;
                        margin-bottom:10px;
                        border-radius:10px;
                    ">
                        <b>{t['treatment_type']}</b><br>
                        {t['description']}
                    </div>
                    """, unsafe_allow_html=True)

# ----------------------------
# PDF REPORT GENERATION
# ----------------------------
st.subheader("📄 Download Report")

if st.button("⬇️ Generate PDF Report"):

    file_path = "crop_diagnosis_report.pdf"

    generate_pdf_report(file_path, crop, result)

    with open(file_path, "rb") as f:
        st.download_button(
            label="📥 Download PDF",
            data=f,
            file_name="CropInsight_Report.pdf",
            mime="application/pdf"
        )
# ----------------------------
# DASHBOARD PAGE
# ----------------------------
elif page == "📊 Dashboard":

    st.subheader("📊 System Overview")

    col1, col2, col3 = st.columns(3)

    col1.markdown(f"""
    <div style="background-color:#1f2937;padding:15px;border-radius:12px;">
    <h3 style="color:#4ade80;">🌾 Crops</h3>
    <h2>{len(system.crops)}</h2>
    </div>
    """, unsafe_allow_html=True)

    col2.markdown(f"""
    <div style="background-color:#1f2937;padding:15px;border-radius:12px;">
    <h3 style="color:#facc15;">🦠 Diseases</h3>
    <h2>{len(system.diseases)}</h2>
    </div>
    """, unsafe_allow_html=True)

    col3.markdown(f"""
    <div style="background-color:#1f2937;padding:15px;border-radius:12px;">
    <h3 style="color:#38bdf8;">💊 Treatments</h3>
    <h2>{len(system.treatments)}</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 🌾 Crops Database")
    st.dataframe(system.crops)

    st.markdown("### 🦠 Diseases Database")
    st.dataframe(system.diseases)
