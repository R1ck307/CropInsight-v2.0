import hashlib
import json
import os

USERS_FILE = "data/users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def register_user(username, password, role="farmer"):
    users = load_users()

    if username in users:
        return False, "User already exists"

    users[username] = {
        "password": hash_password(password),
        "role": role
    }

    save_users(users)
    return True, "User registered successfully"

def login_user(username, password):
    users = load_users()

    if username not in users:
        return False, "User not found"

    if users[username]["password"] != hash_password(password):
        return False, "Incorrect password"

    return True, users[username]["role"]
