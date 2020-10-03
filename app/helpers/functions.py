from random import choice


def generate_weather():
    weather_choices = ["clear skies", "stormy", "sunny", "cloudy", "light rain", "overcast"]
    return choice(weather_choices)
