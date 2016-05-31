import random


class WeatherCaster:
    """The WeatherCaster class sets the weather before each new day in the game."""

    def __init__(self):
        pass

    def generateDayWeather(self):
        weatherList = ["Cloudy", "Sunny", "Hot and dry"]
        dayWeather = random.choice(weatherList)
        return dayWeather
