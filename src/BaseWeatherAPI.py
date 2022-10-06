"""This File is for the base class for weather APIs."""

class BaseWeatherAPI:
    def _init_(self, location = None, plz = None):
        self.called = False
        self.city_name = None
        self.time = None
        self.temp = None
        self.humidity = None
        self.date = None

    def getWeather(self):
        """Set the member variables and raise Error if city not found."""
        pass


class CityNotFound(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)
