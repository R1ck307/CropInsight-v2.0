import streamlit as st

from utils.theme import apply_theme, page_header

from ai.image_detection import analyze_image


# Apply theme
apply_theme()


page_header(
    "Crop Health Scanner",
    "Upload a crop image and let AI identify possible diseases"
)


# ---------------- IMAGE UPLOAD ----------------

st.subheader(
    "📸 Upload Crop Image"
)


uploaded_image = st.file_uploader(
    "Choose a leaf image",
    type=[
        "png",
        "jpg",
        "jpeg"
    ]
)



# ---------------- CROP SELECTION ----------------

crop = st.selectbox(
    "🌱 Select Crop",
    [
        "Tomato",
        "Maize",
        "Beans",
        "Other"
    ]
)



# ---------------- ANALYSIS ----------------


if uploaded_image:


    st.image(
        uploaded_image,
        caption="Uploaded Crop Image",
        use_container_width=True
    )



    if st.button(
        "🧠 Scan Image"
    ):


        results = analyze_image(
            uploaded_image,
            crop
        )


        st.success(
            "Image analysis completed"
        )


        st.subheader(
            "🔬 AI Detection Results"
        )


        for result in results:


            disease = result.get(
                "disease",
                "Unknown"
            )


            confidence = result.get(
                "confidence",
                0
            )


            with st.container():


                st.markdown("---")


                st.subheader(
                    f"🦠 {disease}"
                )


                st.progress(
                    confidence / 100
                )


                st.write(
                    f"🎯 Confidence: {confidence}%"
                )


                if confidence >= 75:

                    st.warning(
                        "High possibility detected. Consider diagnosis confirmation."
                    )


                else:

                    st.info(
                        "Lower confidence prediction. Monitor crop closely."
                    )



else:

    st.info(
        "Upload an image to begin scanning."
              )
