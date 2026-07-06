import streamlit as st

from utils.theme import apply_theme, page_header

from expert_system.analytics_engine import (
    get_total_diagnoses,
    get_average_confidence,
    get_most_common_diseases,
    get_most_affected_crops
)


apply_theme()


page_header(
    "Farm Analytics Dashboard",
    "Monitor crop health trends and diagnosis insights"
)


# ---------------- TOP METRICS ----------------

total = get_total_diagnoses()

confidence = get_average_confidence()


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "🩺 Total Diagnoses",
        total
    )


with col2:

    st.metric(
        "🎯 Average Confidence",
        f"{confidence}%"
    )


with col3:

    st.metric(
        "🌱 System Status",
        "Active 🟢"
    )



st.divider()



# ---------------- DISEASE ANALYSIS ----------------


st.subheader(
    "🦠 Most Common Diseases"
)


diseases = get_most_common_diseases()


if diseases:


    disease_names = list(
        diseases.keys()
    )

    disease_values = list(
        diseases.values()
    )


    st.bar_chart(
        {
            "Disease": disease_values
        }
    )


    for name, count in diseases.items():

        st.write(
            f"🔴 **{name}** — {count} cases"
        )


else:

    st.info(
        "No diagnosis data available yet."
    )



st.divider()



# ---------------- CROP IMPACT ----------------


st.subheader(
    "🌾 Most Affected Crops"
)


crops = get_most_affected_crops()


if crops:


    crop_values = list(
        crops.values()
    )


    st.bar_chart(
        {
            "Crops": crop_values
        }
    )


    for crop, count in crops.items():

        st.write(
            f"🌱 **{crop}** — {count} cases"
        )


else:

    st.info(
        "No crop data available yet."
    )



st.divider()


st.success(
    "Analytics system is monitoring CropInsight activity."
)
