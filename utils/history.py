import json
import os
from datetime import datetime

HISTORY_FILE = "data/records.json"


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)


def save_history(data):
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_record(username, crop, result):
    history = load_history()

    record = {
        "username": username,
        "crop": crop,
        "disease": result["best_match"]["disease"],
        "confidence": result["best_match"]["confidence"],
        "severity": result["best_match"]["severity"],
        "timestamp": str(datetime.now())
    }

    history.append(record)
    save_history(history)

    return record
