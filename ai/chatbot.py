from utils.knowledge_base import (
    load_crops,
    load_diseases,
    load_treatments,
    load_fertilizers
)


def answer_question(question: str):
    """
    Simple rule-based AI assistant using CropInsight knowledge base.
    """

    q = question.lower()

    crops = load_crops()
    diseases = load_diseases()
    treatments = load_treatments()
    fertilizers = load_fertilizers()

    # ---------------- CROPS ----------------
    if "crop" in q or "grow" in q:
        return "We support crops like maize, rice, wheat, beans, tomatoes, cassava, bananas and more. Select a crop in the diagnosis page to begin."

    # ---------------- DISEASES ----------------
    if "disease" in q:
        top = diseases["disease_name"].dropna().unique()[:5]
        return f"Common diseases include: {', '.join(top)}."

    # ---------------- TREATMENTS ----------------
    if "treat" in q or "medicine" in q:
        top = treatments["treatment_name"].dropna().unique()[:5]
        return f"Common treatments include: {', '.join(top)}."

    # ---------------- FERTILIZER ----------------
    if "fertilizer" in q or "feed" in q:
        top = fertilizers["fertilizer_name"].dropna().unique()[:5]
        return f"Common fertilizers include: {', '.join(top)}."

    # ---------------- GENERAL HELP ----------------
    if "help" in q:
        return (
            "I can help you with crop diseases, treatments, fertilizers, "
            "and farming advice. Try asking about maize diseases or tomato care."
        )

    # ---------------- DEFAULT ----------------
    return (
        "I'm CropInsight AI. Ask me about crops, diseases, treatments, or fertilizers."
    )
