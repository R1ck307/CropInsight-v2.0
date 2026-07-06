def calculate_crop_risk(weather, crop):

    risk_score = 0
    warnings = []
    actions = []


    humidity = weather.get(
        "humidity",
        0
    )

    rainfall = weather.get(
        "rainfall",
        0
    )


    crop = crop.lower()



    # Humidity analysis

    if humidity >= 75:

        risk_score += 30

        warnings.append(
            "High humidity increases fungal disease risk."
        )

        actions.append(
            "Monitor leaves for spots, mould and lesions."
        )



    # Rainfall analysis

    if rainfall >= 20:

        risk_score += 30

        warnings.append(
            "Heavy rainfall may cause water-related problems."
        )

        actions.append(
            "Improve drainage and avoid waterlogging."
        )



    # Crop-specific intelligence

    fungal_crops = [
        "tomato",
        "maize",
        "rice",
        "beans"
    ]


    if crop in fungal_crops and humidity >= 70:

        risk_score += 20

        warnings.append(
            f"{crop.title()} is vulnerable to fungal diseases under humid conditions."
        )

        actions.append(
            "Increase crop monitoring frequency."
        )



    # Risk level

    if risk_score >= 70:

        level = "HIGH"

    elif risk_score >= 40:

        level = "MEDIUM"

    else:

        level = "LOW"



    return {

        "crop": crop,

        "risk_score": risk_score,

        "risk_level": level,

        "warnings": warnings,

        "actions": actions

    }
