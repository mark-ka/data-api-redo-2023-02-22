import datetime
import unittest
import weather
import sys
from io import StringIO
from contextlib import contextmanager


@contextmanager
def replace_stdin(target):
    orig = sys.stdin
    sys.stdin = target
    yield
    sys.stdin = orig

class TestWeather(unittest.TestCase):
    def test_search_city_for_paris(self):
        with replace_stdin(StringIO("1")):
            city = weather.search_city('Paris')
            self.assertEqual(city['name'], 'Paris')
            self.assertAlmostEqual(city['lat'], 48.858, 1)
            self.assertAlmostEqual(city['lon'], 2.3200, 1)

    def test_search_city_for_london(self):
        # weather.input = lambda _: "1"
        with replace_stdin(StringIO("1")):
            city = weather.search_city('London')
            self.assertEqual(city['name'], 'London')
            self.assertAlmostEqual(city['lat'], 51.507, 1)
            self.assertAlmostEqual(city['lon'], -0.127, 1)

    def test_search_city_for_unknown_city(self):
        city = weather.search_city('LGTM')
        self.assertEqual(city, None)

    def test_weather_forecast(self):
        forecast = weather.weather_forecast(51.5073219, -0.1276474)
        self.assertIsInstance(forecast, list)
        self.assertTrue(forecast[0].get('weather'))

    def test_search_city_ambiguous_city(self):
        # weather.input = lambda _: "2"
        with replace_stdin(StringIO("2")):
            city = weather.search_city('London')
            self.assertEqual(city['name'], 'City of London', "The 2nd option in the list should be `City of London`")
