from datetime import datetime
from utils.database import 
Database

farms_db = Database("database/farms.csv")


def create_farm(user_id, farm_name, location, size_hectares, main_crop):

    df = farms_db.load()

    farm = {
        "farm_id": len(df) + 1,
        "user_id": user_id,
        "farm_name": farm_name,
        "location": location,
        "size_hectares": size_hectares,
        "main_crop": main_crop,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    farms_db.insert(farm)

    return True, "Farm created successfully"


def get_user_farms(user_id):
    df = farms_db.load()

    if df.empty:
        return []

    return df[df["user_id"] == user_id]


def delete_farm(farm_id):
    return farms_db.delete("farm_id", farm_id)
