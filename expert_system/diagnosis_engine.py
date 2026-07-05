from expert_system.rules import CROP_RULES


def diagnose_crop(crop, symptoms_input):

    if crop not in CROP_RULES:
        return {
            "disease": "Unknown",
            "confidence": 0,
            "treatment": "No data available",
            "severity": "unknown"
        }

    symptoms_input = [s.strip().lower() for s in symptoms_input.split(",")]

    best_match = None
    best_score = 0

    for disease, data in CROP_RULES[crop].items():

        matches = 0

        for user_symptom in symptoms_input:
            for known_symptom in data["symptoms"]:
                if user_symptom in known_symptom:
                    matches += 1

        score = matches / len(data["symptoms"])

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
        "treatment": "Improve symptom description",
        "severity": "low"
    }
