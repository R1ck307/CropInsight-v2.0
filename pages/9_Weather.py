import streamlit as st

from utils.theme import apply_theme, page_header
from weather.weather_api import get_weather
from weather.forecast import analyze_weather_risk


apply_theme()


page_header(
    "Weather Intelligence",
    "Climate-based crop risk analysis"
)


location = st.text_input(
    "📍 Farm Location"
)


crop = st.text_input(
    "🌱 Crop"
)


if st.button("Analyze Weather"):


    if not location or not crop:

        st.warning(
            "Enter location and crop."
        )

        st.stop()



    weather = get_weather(
        location
    )


    st.subheader(
        "🌦 Current Conditions"
    )


    col1, col2, col3 = st.columns(3)


    col1.metric(
        "Temperature",
        f"{weather['temperature']}°C"
    )


    col2.metric(
        "Humidity",
        f"{weather['humidity']}%"
    )


    col3.metric(
        "Rainfall",
        f"{weather['rainfall']}mm"
    )


    result = analyze_weather_risk(
        weather,
        crop
    )


    st.divider()


    st.subheader(
        "⚠️ Crop Risk Analysis"
    )


    for risk in result["risks"]:

        st.warning(
            risk
        )


    st.subheader(
        "💡 Recommendations"
    )


    for tip in result["advice"]:

        st.success(
            tip
        )
