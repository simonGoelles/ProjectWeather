import asyncio
import os
from datetime import date

import python_weather
from openpyxl import load_workbook

from BaseWeatherAPI import BaseWeatherAPI


class WttrClass(BaseWeatherAPI):
    def __init__(self) -> None:
        self.calls = []
        wb = load_workbook(filename="src/PLZ_Verzeichnis.xlsx")
        sheet_ranges = wb["Plz_Anhang"]
        sheet = wb.active

        _input = "8160"  # input("Plz: ")

        # print(sheet_ranges.column_dimensions)
        self.city_name = "Weiz"
        in_values = False
        for i in range(1, int(sheet.dimensions[4:]) + 1):
            # print(sheet_ranges["A1955"])
            if sheet_ranges["A" + str(i)].value == _input:
                in_values = True
                self.city_name = sheet_ranges["B" + str(i)].value
        if not in_values:
            raise Exception("Input was not a PLZ!")

        self.plz = "at-" + _input

    async def getWeather(self):
        async with python_weather.Client(format=python_weather.METRIC) as client:
            weather = await client.get(self.plz)
            weather_dict = {
                "city_name": str(self.city_name),
                "time": str(weather.current.local_time),
                "date": str(date),
                "temp": int(weather.current.temperature),
                "humidity": float(weather.current.humidity),
                "description": str(weather.current.description),
                "plz": str(self.plz),
            }
            self.calls.append(weather_dict)

            if self.city_name == "Oimjakon":
                raise Exception("City %s not Found" % str())
