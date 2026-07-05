# ==========================================================
# CropInsight v2.0
# utils/database.py
# PART 1/3 — CORE DATABASE MANAGER
# ==========================================================

import os
import pandas as pd
from datetime import datetime


# ==========================================================
# BASE PATHS
# ==========================================================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASE_DIR = os.path.join(BASE_DIR, "database")
DATA_DIR = os.path.join(BASE_DIR, "data")


# ==========================================================
# ENSURE FOLDERS EXIST
# ==========================================================

def ensure_folders():

    os.makedirs(DATABASE_DIR, exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)


# Run on import
ensure_folders()


# ==========================================================
# FILE CREATION SYSTEM
# ==========================================================

def ensure_file(file_path, columns):

    """
    Creates a CSV file if it does not exist
    with proper headers.
    """

    if not os.path.exists(file_path):

        df = pd.DataFrame(columns=columns)
        df.to_csv(file_path, index=False)


# ==========================================================
# LOAD DATA
# ==========================================================

def load_data(file_path):

    """
    Safely loads a CSV file into a DataFrame.
    Returns empty DataFrame if file is missing or broken.
    """

    try:

        if os.path.exists(file_path):

            return pd.read_csv(file_path)

    except Exception as e:

        print(f"Error loading {file_path}: {e}")

    return pd.DataFrame()


# ==========================================================
# SAVE DATA (APPEND MODE)
# ==========================================================

def save_data(file_path, data_dict):

    """
    Appends a dictionary as a new row in a CSV file.
    """

    df = load_data(file_path)

    new_row = pd.DataFrame([data_dict])

    df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv(file_path, index=False)


# ==========================================================
# UPDATE DATA
# ==========================================================

def update_data(file_path, condition_col, condition_val, update_dict):

    """
    Updates rows that match a condition.
    """

    df = load_data(file_path)

    if df.empty:
        return False

    df.loc[df[condition_col] == condition_val, update_dict.keys()] = update_dict.values()

    df.to_csv(file_path, index=False)

    return True


# ==========================================================
# DELETE DATA
# ==========================================================

def delete_data(file_path, condition_col, condition_val):

    """
    Deletes rows that match a condition.
    """

    df = load_data(file_path)

    if df.empty:
        return False

    df = df[df[condition_col] != condition_val]

    df.to_csv(file_path, index=False)

    return True


# ==========================================================
# SEARCH DATA
# ==========================================================

def search_data(file_path, column, value):

    """
    Searches and returns filtered results.
    """

    df = load_data(file_path)

    if df.empty:
        return df

    return df[df[column] == value]
