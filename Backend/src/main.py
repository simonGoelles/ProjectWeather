from open_weather import OpenWeatherAPI
from Wttr import WttrClass
# from weatherbitapi_class import Weatherbit

import warnings
warnings.filterwarnings("ignore")

_input = input("PLZ: ")
_open_weather = OpenWeatherAPI(_input)
_open_weather.getWeather()

print("Open Weather")
for i in _open_weather.calls:
    print(f'{i["plz"]} {i["city_name"]}')
    print(f'{i["date"]} {i["time"]}')
    print(f'tmp: {i["temp"]}')

"""
print("\nweatherbit")
_weatherbit = Weatherbit()
_weatherbit.getWeather()

for i in _weatherbit.calls:
    print(f'{i["plz"]} {i["city_name"]}')
    print(f'{i["date"]} {i["time"]}')
    print(f'tmp: {i["temp"]}')
"""

_wttr = WttrClass(_input)
_wttr.getWeather()

print("\nWttr")
for i in _wttr.calls:
    print(f'{i["plz"]} {i["city_name"]}')
    print(f'{i["date"]} {i["time"]}')
    print(f'tmp: {i["temp"]}')
