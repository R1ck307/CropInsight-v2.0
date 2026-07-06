from datetime import datetime


def get_weather(location):
    """
    Temporary weather provider.
    Later we can connect a real API.
    """

    weather = {
        "location": location,
        "temperature": 25,
        "humidity": 70,
        "rainfall": 10,
        "condition": "Partly Cloudy",
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    return weather
