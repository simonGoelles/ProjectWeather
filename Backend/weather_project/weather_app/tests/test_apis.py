from django.test import TestCase

try:
    from src import WttrClass
except:
    WttrClasstr = None


class WttrTestClass(TestCase):
    def setUp(self) -> None:
        self.testcases = [
                [ 8311, "Markt Hartmannsdorf" ],
                [ 8160, "Weiz" ],
                ]

    def test_wttr_returns_place(self):
        
        for _plz, _city in self.testcases:
            wttr = WttrClass(str(_plz))
            wttr.getWeather()
            i = wttr.calls[0]
            assert i["city_name"] == _city
