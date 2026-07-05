import streamlit as st
from utils.farm_manager import create_farm, get_user_farms

st.title("🌾 Farm Profile")

if "user" not in st.session_state:
    st.warning("Please login first")
    st.stop()

user = st.session_state["user"]

st.subheader("Create Farm")

farm_name = st.text_input("Farm Name")
location = st.text_input("Location")
size = st.number_input("Size (hectares)", min_value=0.1)
main_crop = st.text_input("Main Crop")

if st.button("Create Farm"):
    success, msg = create_farm(
        user["id"],
        farm_name,
        location,
        size,
        main_crop
    )

    if success:
        st.success(msg)

st.divider()

st.subheader("Your Farms")

farms = get_user_farms(user["id"])

if farms.empty:
    st.info("No farms yet.")
else:
    st.dataframe(farms)
