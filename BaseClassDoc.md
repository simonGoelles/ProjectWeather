# Base Class Documentation

### Member Variables:
* city_name in string
* time in HH-MM-SS
* temp in celsius
* humidity in %
* date in DD-MM-YYYY

### How to implement
from BaseClassAPI import BaseClassAPI

class ExampleAPI(BaseClassAPI):
  def getWeather(self):
    # own implementation
