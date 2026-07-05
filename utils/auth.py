from datetime import datetime
from utils.database import 
Database

users_db = Database("database/users.csv")


def load_users():
    return users_db.load()


def register_user(username, password, role="user"):
    df = users_db.load()

    if not df.empty and username in df["username"].values:
        return False, "Username already exists"

    new_user = {
        "id": len(df) + 1,
        "username": username,
        "password": password,
        "role": role,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    users_db.insert(new_user)
    return True, "User registered successfully"


def login_user(username, password):
    df = users_db.load()

    if df.empty:
        return False, "No users found"

    user = df[(df["username"] == username) & (df["password"] == password)]

    if not user.empty:
        return True, user.iloc[0].to_dict()

    return False, "Invalid username or password"
