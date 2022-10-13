from BaseWeatherAPI import BaseWeatherAPI
from weatherbit.api import Api

class Weatherbit(BaseWeatherAPI):
    def getWeather(self):
        api = Api("153deb764f8543b99bdd215ecf52b3db")
        api.set_granularity('daily')
        postcode = "8062"
        country = "Austria"
        temp_dict_list = []


        today_weather_dict = {
                "city_name": None,
                "time": "",
                "date": "",
                "temp": "",
                "humidity": "",
                "description": "",
                "plz": ""
        }

        current_weather = api.get_current(postal_code=postcode, country=country)
        current_weatherList = current_weather.get(['weather','temp','rh'])

        forecast = api.get_forecast(postal_code=postcode, country=country)
        forecastList = forecast.get_series(['weather','high_temp','low_temp','rh'])

        # Current Weather
        temp = current_weatherList[0].get("temp")
        datelist = current_weatherList[0].get("datetime").split(" ")
        date = datelist[0]
        time = datelist[1]
        humidity = current_weatherList[0].get("rh")
        description = current_weatherList[0].get("weather").get("description")

        current_weather_dict = { 
            "city_name": None,
            "time": time,
            "date": date,
            "temp": temp,
            "humidity": humidity,
            "description": description,
            "plz": postcode
        }
        super().calls.append(current_weather_dict)


        # Forecast Weather
        for i in range(0,3):
            templist = []
            temp_dict_list = []

            high_temp = forecastList[i].get("high_temp")
            templist.append(high_temp)

            low_temp = forecastList[i].get("low_temp")
            templist.append(low_temp)

            description_forecast = forecastList[i].get("weather").get("description")
            humidity_forecast = forecastList[i].get("rh")
            datelist_forecast = forecastList[i].get("datetime").split(" ")
            dateforecast = datelist_forecast[i]
            timeforcast = datelist_forecast[i]

            temp_weather_dict = {
                "city_name": None,
                "time": timeforcast,
                "date": dateforecast,
                "temp": templist,
                "humidity": humidity_forecast,
                "description": description_forecast,
                "plz": postcode
            }
            super().calls.append(temp_weather_dict)

        
