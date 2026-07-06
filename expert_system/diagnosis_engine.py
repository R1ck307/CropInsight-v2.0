from utils.knowledge_base import load_diseases


def diagnose_crop(crop_name, symptoms_input):
    """
    Data-driven crop diagnosis engine.
    Returns top 3 possible diseases with confidence scores.
    """

    diseases = load_diseases()

    if diseases is None or diseases.empty:
        return []

    # Filter by crop
    crop_diseases = diseases[
        diseases["crop_name"].str.lower() == crop_name.lower()
    ]

    if crop_diseases.empty:
        return []

    # Clean user symptoms
    user_symptoms = [
        s.strip().lower()
        for s in str(symptoms_input).split(";")
        if s.strip()
    ]

    matches = []

    for _, disease in crop_diseases.iterrows():

        # SAFE DATA EXTRACTION
        disease_name = str(disease.get("disease_name", "") or "")
        symptoms_raw = str(disease.get("symptoms", "") or "")
        severity = str(disease.get("severity", "Unknown") or "Unknown")
        dtype = str(disease.get("disease_type", "Unknown") or "Unknown")
        cause = str(disease.get("cause", "Not available") or "Not available")
        treatment = str(disease.get("treatment", "Not available") or "Not available")
        prevention = str(disease.get("prevention", "Not available") or "Not available")

        # SKIP INVALID ROWS
        if not disease_name or not symptoms_raw:
            continue

        disease_symptoms = [
            s.strip().lower()
            for s in symptoms_raw.split(";")
            if s.strip()
        ]

        matched = 0

        # SYMPTOM MATCHING LOGIC
        for user_symptom in user_symptoms:
            for known_symptom in disease_symptoms:
                if user_symptom in known_symptom or known_symptom in user_symptom:
                    matched += 1
                    break

        confidence = round(
            (matched / max(len(disease_symptoms), 1)) * 100,
            1
        )

        if confidence > 0:
            matches.append({
                "disease": disease_name,
                "confidence": confidence,
                "severity": severity,
                "type": dtype,
                "cause": cause,
                "treatment": treatment,
                "prevention": prevention
            })

    # SORT RESULTS
    matches.sort(key=lambda x: x["confidence"], reverse=True)

    return matches[:3]
