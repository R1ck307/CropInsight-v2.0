import pandas as pd
import os
from datetime import datetime

USER_DB_PATH = "database/users.csv"


def load_users():
    if not os.path.exists(USER_DB_PATH):
        df = pd.DataFrame(columns=["id", "username", "password", "role", "created_at"])
        df.to_csv(USER_DB_PATH, index=False)
        return df
    return pd.read_csv(USER_DB_PATH)


def save_users(df):
    df.to_csv(USER_DB_PATH, index=False)


def register_user(username, password, role="user"):
    df = load_users()

    if username in df["username"].values:
        return False, "Username already exists"

    new_id = len(df) + 1

    new_user = {
        "id": new_id,
        "username": username,
        "password": password,
        "role": role,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
    save_users(df)

    return True, "User registered successfully"


def login_user(username, password):
    df = load_users()

    user = df[(df["username"] == username) & (df["password"] == password)]

    if not user.empty:
        return True, user.iloc[0].to_dict()

    return False, "Invalid username or password"
