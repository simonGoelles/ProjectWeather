from .CityNotFound import CityNotFound

try:
    raise CityNotFound("Test")
except CityNotFound as e:
    print(e.message)
