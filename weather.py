# pylint: disable=missing-module-docstring

import urllib.parse
import requests
import datetime

BASE_URI = "http://api.openweathermap.org"
API_KEY = 'e23165569272739e442324988e8ea94c'


def search_city(query):
    '''
    Look for a given city. If multiple options are returned, have the user choose between them.
    Return one city (or None)
    '''
    response = requests.get(BASE_URI + "/geo/1.0/direct",
                            params={'q': query, 'appid':API_KEY},).json()
    city = response[0]
    if query.capitalize() == city['name']:
        return city
    return main()

def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''
    response = requests.get(BASE_URI + "/data/3.0/onecall",
                            params={'lat': lat, 'lon': lon, 'exclude':'current,minutely,hourly', 'units': 'metric', 'appid':API_KEY},).json()
    print(f"Here's the weather in {response['timezone'].split('/')[1]}")
    for i, day in enumerate(response['daily']):
        if i <5:
            print(f"{datetime.date.today()}: {day['weather'][0]['description'].capitalize()} ({int(day['temp']['day'])+1}°C)")

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("Good Day master! Please enter a city name.\n> ")
    city = search_city(query)
    forecast = weather_forecast(city['lat'], city['lon'])
    pass  # YOUR CODE HERE

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
