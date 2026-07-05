from datetime import datetime
from utils.database import Database

diag_db = Database("database/diagnoses.csv")


def save_diagnosis(user_id, farm_id, crop, symptoms, result):

    df = diag_db.load()

    record = {
        "diag_id": len(df) + 1,
        "user_id": user_id,
        "farm_id": farm_id,
        "crop": crop,
        "symptoms": symptoms,
        "disease": result["disease"],
        "confidence": result["confidence"],
        "severity": result["severity"],
        "treatment": result["treatment"],
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    diag_db.insert(record)
    return True


def get_user_diagnoses(user_id):
    df = diag_db.load()

    if df.empty:
        return df

    return df[df["user_id"] == user_id]
