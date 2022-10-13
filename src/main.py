from open_weather import OpenWeatherAPI
from weatherbitapi_class import Weatherbit
from Wttr import WttrClass

_open_weather = OpenWeatherAPI()
_open_weather.getWeather()

"""
_weatherbit = Weatherbit()
_weatherbit.getWeather()
"""

_wttr = WttrClass()
_wttr.getWeather()

for i in _open_weather.calls:
    print(f'{i["plz"]} {i["city_name"]}')
    print(f'{i["date"]} {i["time"]}')
    print(f'tmp: {i["temp"]}')

print()

"""
for i in _weatherbit.calls:
    print(f'{i["plz"]} {i["city_name"]}')
    print(f'{i["date"]} {i["time"]}')
    print(f'tmp: {i["temp"]}')

print()
"""

for i in _wttr.calls:
    print("wttr")
    print(f'{i["plz"]} {i["city_name"]}')
    print(f'{i["date"]} {i["time"]}')
    print(f'tmp: {i["temp"]}')
