from open_weather import OpenWeatherAPI
from weatherbitapi_class import Weatherbit
from Wttr import WttrClass

_open_weather = OpenWeatherAPI()
_open_weather.getWeather()

print("open weather")
for i in _open_weather.calls:
    print(f'{i["plz"]} {i["city_name"]}')
    print(f'{i["date"]} {i["time"]}')
    print(f'tmp: {i["temp"]}')

"""
print("weatherbit")
_weatherbit = Weatherbit()
_weatherbit.getWeather()

for i in _weatherbit.calls:
    print(f'{i["plz"]} {i["city_name"]}')
    print(f'{i["date"]} {i["time"]}')
    print(f'tmp: {i["temp"]}')

print()
"""

_wttr = WttrClass()
_wttr.getWeather()

print("wttr")
for i in _wttr.calls:
    print(f'{i["plz"]} {i["city_name"]}')
    print(f'{i["date"]} {i["time"]}')
    print(f'tmp: {i["temp"]}')
