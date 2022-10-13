from open_weather import OpenWeatherAPI

_open_weather = OpenWeatherAPI()
_open_weather.getWeather()
_open_weather.calls

for i in _open_weather.calls:
    print(f'{i["plz"]} {i["city_name"]}')
    print(f'{i["date"]} {i["time"]}')
    print(f'tmp: {i["temp"]}')
