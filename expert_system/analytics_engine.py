import pandas as pd
from utils.database import Database

# This assumes your diagnosis history is stored in CSV via diagnosis_manager
# We will read directly from that file


def load_history(path="database/diagnoses.csv"):
    try:
        return pd.read_csv(path)
    except:
        return pd.DataFrame()


def get_most_common_diseases():
    df = load_history()

    if df.empty or "disease" not in df.columns:
        return []

    return df["disease"].value_counts().head(5).to_dict()


def get_most_affected_crops():
    df = load_history()

    if df.empty or "crop" not in df.columns:
        return []

    return df["crop"].value_counts().head(5).to_dict()


def get_average_confidence():
    df = load_history()

    if df.empty or "confidence" not in df.columns:
        return 0

    return round(df["confidence"].mean(), 2)


def get_total_diagnoses():
    df = load_history()
    return len(df)
