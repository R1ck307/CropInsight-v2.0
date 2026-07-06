from datetime import datetime
from utils.database import Database

users_db = Database("database/users.csv")


def load_users():
    return users_db.load()


def register_user(username, password, role="user"):
    df = users_db.load()

    if not df.empty and username in df["username"].values:
        return False, "Username already exists"

    # Auto assign ID safely
    new_id = 1 if df.empty else int(df["id"].max()) + 1

    new_user = {
        "id": new_id,
        "username": username,
        "password": password,
        "role": role,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    users_db.insert(new_user)

    return True, f"{role.capitalize()} account created successfully"


def login_user(username, password):
    df = users_db.load()

    if df.empty:
        return False, "No users found"

    user = df[
        (df["username"] == username) &
        (df["password"] == password)
    ]

    if not user.empty:
        return True, user.iloc[0].to_dict()

    return False, "Invalid username or password"


def create_admin_if_not_exists():
    """
    Safe initializer — creates default admin once
    """
    df = users_db.load()

    if not df.empty and "admin" in df["username"].values:
        return

    admin_user = {
        "id": 1,
        "username": "admin",
        "password": "admin123",
        "role": "admin",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    users_db.insert(admin_user)
