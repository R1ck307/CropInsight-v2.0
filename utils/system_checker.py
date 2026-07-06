import os


REQUIRED_FILES = [

    # Database
    "database/users.csv",
    "database/farms.csv",
    "database/diagnoses.csv",
    "database/reports.csv",

    # Data
    "data/crops.csv",
    "data/diseases.csv",
    "data/treatments.csv",
    "data/fertilizers.csv",

    # Core modules
    "utils/auth.py",
    "utils/database.py",

    "expert_system/diagnosis_engine.py",
    "expert_system/recommendation_engine.py",

    "ai/chatbot.py",
    "ai/image_detection.py",
    "ai/risk_prediction.py",

    "weather/weather_api.py",
    "weather/forecast.py"

]


def run_system_check():

    results = []


    for file in REQUIRED_FILES:

        if os.path.exists(file):

            results.append(
                {
                    "file": file,
                    "status": "OK"
                }
            )

        else:

            results.append(
                {
                    "file": file,
                    "status": "MISSING"
                }
            )


    return results



def system_ready():

    results = run_system_check()


    for item in results:

        if item["status"] == "MISSING":

            return False


    return True
