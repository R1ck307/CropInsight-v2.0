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
# SIDEBAR
# ----------------------------
st.sidebar.header("🧭 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Diagnose", "📊 Dashboard Info"])

# ----------------------------
# DIAGNOSIS PAGE
# ----------------------------
if page == "🏠 Diagnose":

    st.subheader("🧠 Crop Disease Diagnosis")

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

            if result["status"] == "no_match"]:
                st.error(result["message"])
            else:
                st.success("Diagnosis Complete ✔️")

                # ----------------------------
                # BEST MATCH
                # ----------------------------
                st.subheader("🎯 Best Match")

                best = result["best_match"]

                st.metric("Disease", best["disease"])
                st.metric("Confidence", f"{best['confidence']}%")
                st.metric("Severity", best["severity"])

                # ----------------------------
                # ALL MATCHES
                # ----------------------------
                st.subheader("📊 All Possible Matches")

                for m in result["matches"]:
                    st.write(f"🦠 {m['disease']} - {m['confidence']}% confidence")

                # ----------------------------
                # TREATMENTS
                # ----------------------------
                st.subheader("💊 Recommended Treatments")

                for t in result["treatments"]:
                    st.write(f"• {t['treatment_type']}: {t['description']}")

# ----------------------------
# DASHBOARD PAGE
# ----------------------------
elif page == "📊 Dashboard Info":

    st.subheader("📊 System Overview")

    st.write("🌾 Total Crops:", len(system.crops))
    st.write("🦠 Total Diseases:", len(system.diseases))
    st.write("💊 Total Treatments:", len(system.treatments))

    st.markdown("### 🌍 Crops Available")

    st.dataframe(system.crops)

    st.markdown("### 🦠 Disease Database")

    st.dataframe(system.diseases)
