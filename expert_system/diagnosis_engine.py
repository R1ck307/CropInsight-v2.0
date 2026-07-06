from utils.knowledge_base import load_diseases


def diagnose_crop(crop_name, symptoms_input):
    """
    Diagnose a crop by comparing the user's symptoms
    against diseases stored in diseases.csv.

    Returns:
        List of the top 3 matching diseases.
    """

    diseases = load_diseases()

    # Filter diseases for the selected crop
    crop_diseases = diseases[
        diseases["crop_name"].str.lower() == crop_name.lower()
    ]

    if crop_diseases.empty:
        return []

    # Convert user symptoms into a clean list
    user_symptoms = [
        s.strip().lower()
        for s in symptoms_input.split(";")
        if s.strip()
    ]

    matches = []

    for _, disease in crop_diseases.iterrows():

        disease_symptoms = [
            s.strip().lower()
            for s in disease["symptoms"].split(";")
        ]

        matched = 0

        for symptom in user_symptoms:
            for known in disease_symptoms:
                if symptom in known or known in symptom:
                    matched += 1
                    break

        confidence = round(
            (matched / len(disease_symptoms)) * 100,
            1
        )

        if confidence > 0:
            matches.append({
                "disease": disease["disease_name"],
                "confidence": confidence,
                "severity": disease["severity"],
                "type": disease["disease_type"],
                "cause": disease["cause"],
                "treatment": disease["treatment"],
                "prevention": disease["prevention"]
            })

    matches.sort(
        key=lambda x: x["confidence"],
        reverse=True
    )

    return matches[:3]
