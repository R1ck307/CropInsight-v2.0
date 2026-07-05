import pandas as pd

class CropExpertSystem:
    def __init__(self, crops_file, diseases_file, treatments_file):
        self.crops = pd.read_csv(crops_file)
        self.diseases = pd.read_csv(diseases_file)
        self.treatments = pd.read_csv(treatments_file)

    # ----------------------------
    # 1. FIND DISEASES BY CROP
    # ----------------------------
    def get_diseases_by_crop(self, crop_name):
        results = self.diseases[
            self.diseases["affected_crop"].str.lower() == crop_name.lower()
        ]
        return results.to_dict(orient="records")

    # ----------------------------
    # 2. SIMPLE SYMPTOM MATCHING
    # ----------------------------
    def diagnose(self, crop_name, symptom_text):
        possible = self.get_diseases_by_crop(crop_name)

        matches = []

        for disease in possible:
            score = 0

            disease_symptoms = disease["symptoms"].lower().split()

            for word in symptom_text.lower().split():
                if word in disease_symptoms:
                    score += 1

            confidence = min(100, score * 25)

            if confidence > 0:
                matches.append({
                    "disease": disease["name"],
                    "severity": disease["severity"],
                    "confidence": confidence,
                    "disease_id": disease["disease_id"]
                })

        # sort best match first
        matches = sorted(matches, key=lambda x: x["confidence"], reverse=True)

        return matches

    # ----------------------------
    # 3. GET TREATMENTS (MULTIPLE)
    # ----------------------------
    def get_treatments(self, disease_id):
        results = self.treatments[
            self.treatments["disease_id"] == disease_id
        ]

        return results.to_dict(orient="records")

    # ----------------------------
    # 4. FULL DIAGNOSIS PIPELINE
    # ----------------------------
    def run_diagnosis(self, crop_name, symptom_text):
        matches = self.diagnose(crop_name, symptom_text)

        if not matches:
            return {
                "status": "no_match",
                "message": "No clear disease found. Try adding more symptoms."
            }

        top = matches[0]

        treatments = self.get_treatments(top["disease_id"])

        return {
            "status": "success",
            "crop": crop_name,
            "input_symptoms": symptom_text,
            "matches": matches,
            "best_match": top,
            "treatments": treatments
      }
