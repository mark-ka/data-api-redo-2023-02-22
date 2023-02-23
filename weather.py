# pylint: disable=missing-module-docstring

import sys
import urllib.parse
import requests

BASE_URI = "https://weather.lewagon.com"


def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''
    url = f"https://weather.lewagon.com/2.5/forecast/daily?lat={lat}&lon={lon}cnt=5"

def search_city(query):
    '''
    Look for a given city. If multiple options are returned, have the user choose between them.
    Return one city (or None)
    '''
    url = f"https://weather.lewagon.com/geo/1.0/direct?q={query}"
    response = requests.get(url).json()
    city = response[0]
    if query.capitalize() == city['name']:
        print(f"Here's the weather in {city['name']}")
        weather_forecast(city['lat'], city['lon'])
    else:
        main()

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("Good Day master! How can I serve you? Please enter a city name.\n> ")
    city = search_city(query)

    # TODO: Display weather forecast for a given city
    pass  # YOUR CODE HERE

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
