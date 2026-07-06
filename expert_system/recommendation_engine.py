from utils.knowledge_base import load_treatments, load_fertilizers


def get_treatment_advice(disease_name):
    """
    Returns treatment recommendations for a disease.
    """

    treatments = load_treatments()

    if treatments is None or treatments.empty:
        return []

    # Simple keyword match (can be improved later)
    matches = treatments[
        treatments["description"].str.lower().str.contains(
            disease_name.lower(), na=False
        )
    ]

    if matches.empty:
        return []

    return matches.to_dict(orient="records")


def get_fertilizer_advice(crop_name):
    """
    Returns fertilizer recommendations for a crop.
    """

    fertilizers = load_fertilizers()

    if fertilizers is None or fertilizers.empty:
        return []

    matches = fertilizers[
        fertilizers["recommended_for"].str.lower().str.contains(
            crop_name.lower(), na=False
        )
    ]

    if matches.empty:
        return []

    return matches.to_dict(orient="records")
