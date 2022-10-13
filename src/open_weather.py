"""Wetter API Prototyp."""

import requests
from datetime import datetime, date
from BaseWeatherAPI import BaseWeatherAPI


class OpenWeatherAPI(BaseWeatherAPI):
    API_KEY = "dda8da3e457ddaa3f2db53e90a042e88"

    request_url = f"https://api.openweathermap.org/data/2.5/weather?zip=8230,at&appid={API_KEY}&lang=de"
    data = requests.get(request_url).json()
    response = requests.get(request_url)
        
    def getWeather(self, data, response):
        self.calls = []
        weather_dict = {
            "city_name": str(data["name"]),
            "time": str(datetime.now().strftime('%H:%M:%S')),
            "date_": date.today(),
            "temp": int(round(data["main"]["temp"]-274.15)),
            "humidity": float(data["main"]["humidity"]),
            "description": str(data["weather"][0]["description"]),
            "plz": str(data["sys"]["id"])
        }
        self.calls.append(weather_dict)

        if response.status_code == 404:
            raise Exception("City %s not Found" %str(data["name"]))