import streamlit as st

from utils.theme import apply_theme, page_header

from utils.farm_manager import (
    create_farm,
    get_user_farms
)


apply_theme()


page_header(
    "Farm Profile",
    "Manage your farms and agricultural information"
)


# ---------------- LOGIN CHECK ----------------

if "user" not in st.session_state:

    st.warning("Please login first.")
    st.stop()


user = st.session_state["user"]


# ---------------- CREATE FARM ----------------

st.subheader("➕ Add New Farm")


with st.form("farm_creation_form"):

    farm_name = st.text_input(
        "🌱 Farm Name"
    )


    location = st.text_input(
        "📍 Location"
    )


    size_hectares = st.number_input(
        "📏 Farm Size (hectares)",
        min_value=0.0,
        step=0.5
    )


    main_crop = st.text_input(
        "🌾 Main Crop"
    )


    submit = st.form_submit_button(
        "Create Farm"
    )


    if submit:

        if farm_name.strip():


            success, message = create_farm(
                user_id=user["id"],
                farm_name=farm_name,
                location=location,
                size_hectares=size_hectares,
                main_crop=main_crop
            )


            if success:

                st.success(message)

                st.rerun()

            else:

                st.error(message)


        else:

            st.error(
                "Farm name is required."
            )



st.divider()



# ---------------- DISPLAY FARMS ----------------


st.subheader(
    "🌾 Your Farms"
)


farms = get_user_farms(
    user["id"]
)


if farms.empty:

    st.info(
        "No farms registered yet."
    )


else:

    for _, farm in farms.iterrows():

        with st.container():

            st.markdown("---")


            col1, col2 = st.columns(2)


            with col1:

                st.subheader(
                    f"🌱 {farm['farm_name']}"
                )

                st.write(
                    f"📍 Location: {farm['location']}"
                )

                st.write(
                    f"📏 Size: {farm['size_hectares']} hectares"
                )


            with col2:

                st.write(
                    "🌾 Main Crop"
                )

                st.success(
                    farm['main_crop']
                )


                st.write(
                    f"📅 Created: {farm['created_at']}"
                )
