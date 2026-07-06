import streamlit as st

from utils.theme import apply_theme, page_header

from weather.weather_api import get_weather
from weather.forecast import analyze_weather_risk

from ai.risk_prediction import calculate_crop_risk


# Apply theme
apply_theme()


page_header(
    "Weather Intelligence",
    "Climate-based crop risk analysis and AI prediction"
)


# ---------------- INPUTS ----------------

location = st.text_input(
    "📍 Farm Location"
)


crop = st.text_input(
    "🌱 Crop"
)



# ---------------- ANALYSIS ----------------

if st.button("🌦 Analyze Weather"):


    if not location or not crop:

        st.warning(
            "Please enter both location and crop."
        )

        st.stop()



    # Get weather data

    weather = get_weather(
        location
    )


    # Display weather

    st.subheader(
        "🌦 Current Conditions"
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Temperature",
            f"{weather['temperature']}°C"
        )


    with col2:

        st.metric(
            "Humidity",
            f"{weather['humidity']}%"
        )


    with col3:

        st.metric(
            "Rainfall",
            f"{weather['rainfall']}mm"
        )



    st.divider()



    # Basic weather analysis

    weather_result = analyze_weather_risk(
        weather,
        crop
    )


    st.subheader(
        "⚠️ Weather Analysis"
    )


    for risk in weather_result["risks"]:

        st.warning(
            risk
        )


    st.subheader(
        "💡 Weather Recommendations"
    )


    for advice in weather_result["advice"]:

        st.success(
            advice
        )



    st.divider()



    # AI crop risk prediction

    st.subheader(
        "🧠 AI Crop Risk Prediction"
    )


    prediction = calculate_crop_risk(
        weather,
        crop
    )


    st.metric(
        "Risk Score",
        f"{prediction['risk_score']}%"
    )



    risk_level = prediction["risk_level"]



    if risk_level == "HIGH":

        st.error(
            "🚨 HIGH CROP RISK"
        )


    elif risk_level == "MEDIUM":

        st.warning(
            "⚠️ MEDIUM CROP RISK"
        )


    else:

        st.success(
            "✅ LOW CROP RISK"
        )



    st.subheader(
        "⚠️ Risk Factors"
    )


    if prediction["warnings"]:

        for warning in prediction["warnings"]:

            st.write(
                "•",
                warning
            )

    else:

        st.info(
            "No major risk factors detected."
        )



    st.subheader(
        "🌱 Preventive Actions"
    )


    if prediction["actions"]:

        for action in prediction["actions"]:

            st.write(
                "•",
                action
            )

    else:

        st.info(
            "No preventive actions required."
        )
