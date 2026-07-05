from expert_system.rules import CROP_RULES


def get_general_advice(message: str):

    msg = message.lower()

    # BASIC AGRICULTURE HELP RESPONSES
    if "maize" in msg:
        return "Maize needs good nitrogen supply and early pest control (especially fall armyworm)."

    if "tomato" in msg:
        return "Tomatoes require consistent watering and protection from fungal diseases like blight."

    if "bean" in msg:
        return "Beans are sensitive to fungal diseases; use crop rotation and clean seeds."

    if "disease" in msg:
        return "Describe crop + symptoms clearly for diagnosis (e.g., maize, brown spots, yellow leaves)."

    if "fertilizer" in msg:
        return "Use balanced NPK fertilizers depending on crop stage. Avoid over-fertilizing."

    return "I can help with crops, diseases, fertilizers, or symptoms. Try asking more specifically."
