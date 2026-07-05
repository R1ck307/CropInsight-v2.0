import streamlit as st
from expert_system.diagnosis_engine import diagnose_crop
from utils.diagnosis_manager import save_diagnosis
from utils.farm_manager import get_user_farms

st.title("🧠 Crop Diagnosis Engine")

if "user" not in st.session_state:
    st.warning("Please login first")
    st.stop()

user = st.session_state["user"]

# Get farms for dropdown
farms = get_user_farms(user["id"])

if farms.empty:
    st.warning("Please create a farm first")
    st.stop()

farm_options = farms["farm_name"].tolist()
selected_farm = st.selectbox("Select Farm", farm_options)

farm_id = int(farms[farms["farm_name"] == selected_farm]["farm_id"].values[0])

crop = st.selectbox("Select Crop", ["maize", "tomato", "beans", "rice", "sorghum"])

symptoms = st.text_area("Enter Symptoms (comma separated)")

if st.button("Diagnose"):

    if symptoms.strip() == "":
        st.error("Please enter symptoms")
    else:
        result = diagnose_crop(crop, symptoms)

        st.subheader("📊 Result")
        st.write(result)

        # SAVE RESULT
        save_diagnosis(
            user_id=user["id"],
            farm_id=farm_id,
            crop=crop,
            symptoms=symptoms,
            result=result
        )

        st.success("Diagnosis saved successfully ✔")
