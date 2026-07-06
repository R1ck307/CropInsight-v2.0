import streamlit as st

from utils.theme import apply_theme, page_header

from ai.image_detection import analyze_image

from expert_system.recommendation_engine import (
    get_treatment_advice,
    get_fertilizer_advice
)


apply_theme()


page_header(
    "Crop Health Scanner",
    "AI image analysis with treatment recommendations"
)


st.subheader(
    "📸 Upload Crop Image"
)


uploaded_image = st.file_uploader(
    "Choose a crop leaf image",
    type=[
        "png",
        "jpg",
        "jpeg"
    ]
)


crop = st.selectbox(
    "🌱 Select Crop",
    [
        "Tomato",
        "Maize",
        "Beans",
        "Other"
    ]
)



if uploaded_image:


    st.image(
        uploaded_image,
        caption="Uploaded Image",
        use_container_width=True
    )


    if st.button(
        "🧠 Scan Crop"
    ):


        results = analyze_image(
            uploaded_image,
            crop
        )


        st.success(
            "AI analysis completed"
        )


        st.subheader(
            "🔬 Disease Predictions"
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


            # Treatment connection

            st.subheader(
                "💊 Recommended Treatment"
            )


            treatments = get_treatment_advice(
                disease
            )


            if treatments:


                for treatment in treatments:

                    st.success(
                        treatment.get(
                            "treatment_name",
                            "Follow recommended treatment"
                        )
                    )

            else:

                st.info(
                    "No treatment data available."
                )



            # Fertilizer connection

            st.subheader(
                "🌱 Fertilizer Advice"
            )


            fertilizers = get_fertilizer_advice(
                crop
            )


            if fertilizers:


                for fertilizer in fertilizers:

                    st.write(
                        "🌿",
                        fertilizer.get(
                            "fertilizer_name",
                            "General fertilizer"
                        )
                    )



else:

    st.info(
        "Upload a crop image to start analysis."
    )
