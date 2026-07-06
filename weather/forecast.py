def analyze_weather_risk(weather, crop):

    risks = []
    advice = []


    humidity = weather.get(
        "humidity",
        0
    )

    rainfall = weather.get(
        "rainfall",
        0
    )


    # Humidity risk

    if humidity > 75:

        risks.append(
            "High humidity"
        )

        advice.append(
            "Monitor crops for fungal diseases."
        )


    # Rain risk

    if rainfall > 20:

        risks.append(
            "Heavy rainfall"
        )

        advice.append(
            "Check drainage and avoid waterlogging."
        )


    if not risks:

        risks.append(
            "Low risk"
        )

        advice.append(
            "Current conditions are favourable."
        )


    return {
        "crop": crop,
        "risks": risks,
        "advice": advice
    }
