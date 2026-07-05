from expert_system.rules import CROP_RULES


def diagnose_crop(crop, symptoms_input):

    if crop not in CROP_RULES:
        return {
            "disease": "Unknown",
            "confidence": 0,
            "treatment": "No data available",
            "severity": "unknown"
        }

    symptoms_input = symptoms_input.lower().split(",")

    best_match = None
    best_score = 0

    for disease, data in CROP_RULES[crop].items():

        match_count = 0

        for symptom in symptoms_input:
            symptom = symptom.strip()

            for known_symptom in data["symptoms"]:
                if symptom in known_symptom:
                    match_count += 1

        score = match_count / len(data["symptoms"])

        if score > best_score:
            best_score = score
            best_match = disease

    if best_match:
        disease_data = CROP_RULES[crop][best_match]

        return {
            "disease": best_match,
            "confidence": round(best_score * 100, 2),
            "treatment": disease_data["treatment"],
            "severity": disease_data["severity"]
        }

    return {
        "disease": "No match",
        "confidence": 0,
        "treatment": "Try better symptom description",
        "severity": "low"
    }
