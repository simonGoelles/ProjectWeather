"""This File is for the base class for weather APIs."""

class BaseWeatherAPI:
    def _init_(self, location = None, plz = None):
        """
self.calls is a List of Dictionaries
Example Dictionary:
{
    "city_name": in str
    "time": in hh-mm-ss
    "date": in dd-mm-yyyy
    "temp": celsius in int
    "humidity": in percent in int from 0 - 1
}"""
        self.calls

    def getWeather(self):
        """Set the member variables and raise Error if city not found."""
        pass


class CityNotFound(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)
