import pandas as pd
from pathlib import Path
import streamlit as st


DATA_DIR = Path("data")


@st.cache_data
def load_crops():
    return pd.read_csv(DATA_DIR / "crops.csv")


@st.cache_data
def load_diseases():
    return pd.read_csv(DATA_DIR / "diseases.csv")


@st.cache_data
def load_pests():
    return pd.read_csv(DATA_DIR / "pests.csv")


@st.cache_data
def load_treatments():
    return pd.read_csv(DATA_DIR / "treatments.csv")


@st.cache_data
def load_fertilizers():
    return pd.read_csv(DATA_DIR / "fertilizers.csv")


@st.cache_data
def load_soil():
    return pd.read_csv(DATA_DIR / "soil.csv")


@st.cache_data
def load_irrigation():
    return pd.read_csv(DATA_DIR / "irrigation.csv")


def get_crop_names():
    df = load_crops()
    return sorted(df["crop_name"].tolist())


def get_crop(crop_name):
    df = load_crops()
    result = df[df["crop_name"].str.lower() == crop_name.lower()]
    return None if result.empty else result.iloc[0].to_dict()


def get_crop_diseases(crop_name):
    df = load_diseases()
    return df[df["crop_name"].str.lower() == crop_name.lower()]


def get_crop_pests(crop_name):
    df = load_pests()
    return df[df["crop_name"].str.lower() == crop_name.lower()]


def search_disease(name):
    df = load_diseases()
    result = df[df["disease_name"].str.lower() == name.lower()]
    return None if result.empty else result.iloc[0].to_dict()


def search_pest(name):
    df = load_pests()
    result = df[df["pest_name"].str.lower() == name.lower()]
    return None if result.empty else result.iloc[0].to_dict()
