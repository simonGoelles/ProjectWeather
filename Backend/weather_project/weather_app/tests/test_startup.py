import requests

from django.test import TestCase


class ServerTestClass(TestCase):
    def test_started(self):
        r = requests.get("http://127.0.0.1:8000/weather_app/")
        assert r.status_code == 200

