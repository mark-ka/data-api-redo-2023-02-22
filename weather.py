# pylint: disable=missing-module-docstring

import sys
import datetime
import requests


BASE_URI = "http://api.openweathermap.org"
API_KEY = 'e23165569272739e442324988e8ea94c'


def search_city(query):
    '''
    Look for a given city. If multiple options are returned, have the user choose between them.
    Return one city (or None)
    '''
    response = requests.get(BASE_URI + "/geo/1.0/direct",
                            params={'q': query, 'limit': 5, 'appid':API_KEY},).json()

    if response:
        if query.capitalize() in response[0]['local_names'].values():
            if len(response) > 1:
                specific = 99
                while specific not in list(range(5)):
                    for i, city in enumerate(response):
                        print(f"{i+1}. {city['name']}, {city['country']}")
                    specific = int(input('Multiple matches found, which city did you mean?'))-1
                return response[specific]
        return response[0]
    return None

def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''
    response = requests.get(BASE_URI + "/data/3.0/onecall",
                params={'lat': lat, 'lon': lon, 'units': 'metric', 'appid':API_KEY},).json()
    return response['daily']

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)

    if city:
        forecast = weather_forecast(city['lat'], city['lon'])
        print(f"Here's the weather in {city['name']}")
        for day in forecast:
            description = day['weather'][0]['description'].capitalize()
            temp = int(day['temp']['day'])
            print(f"{datetime.date.today()}: {description} ({temp}°C)")

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
