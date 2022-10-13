from datetime import date
from BaseWeatherAPI import BaseWeatherAPI
import python_weather
import os
import asyncio
from openpyxl import load_workbook


class WttrClass(BaseWeatherAPI):



    wb = load_workbook(filename="PLZ_Verzeichnis.xlsx")
    sheet_ranges = wb["Plz_Anhang"]
    sheet = wb.active

    _input = input("Plz: ")

    #print(sheet_ranges.column_dimensions)
    city_name = ""
    in_values = False
    for i in range(1, int(sheet.dimensions[4:]) + 1):
      #print(sheet_ranges["A1955"])
      if sheet_ranges["A" + str(i)].value == _input:
        in_values = True
        city_name = sheet_ranges["B" + str(i)].value
    if not in_values:
      raise Exception("Input was not a PLZ!")

    plz = "at-" + _input

    async def getWeather(self, plz: str):
        async with python_weather.Client(format=python_weather.METRIC) as client:
            self.calls = []
            weather = await client.get(plz)
            weather_dict = {
                "city_name": str(city_name),
                "time": str(weather.current.local_time),
                "date_": str(date),
                "temp": int(weather.current.temperature),
                "humidity": float(weather.current.humidity),
                "description": str(weather.current.description),
                "plz": str(plz)
            }
            self.calls.append(weather_dict)

            if city_name == Oimjakon:
                raise Exception("City %s not Found" %str())
