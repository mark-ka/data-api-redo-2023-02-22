## Intro

A common way of collecting data is through APIs. Those can be [public APIs](https://github.com/public-apis/public-apis) with authentication or not, free or paid, internal APIs at your company, etc.

When it comes to APIs, there are some keywords that you should understand:

- [SOAP](https://en.wikipedia.org/wiki/SOAP) (old)
- [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) (current)
- [GraphQL](https://en.wikipedia.org/wiki/GraphQL) (very new, less frequent)
- [XML](https://en.wikipedia.org/wiki/XML) (long-established)
- [JSON](https://en.wikipedia.org/wiki/JSON) (currently very widespread)

The first three keywords refer to an architecture or a protocol on top of HTTP(s) and it is really important to figure out which one you are using when you want to **consume** data from an API.

The last two keywords refer to a **data format** that would usually be sent back to you when performing an API call.

ℹ️ Most modern APIs are RESTful and send back JSON. In this challenge, we are going to use such an API.

## Reading the documentation

When presented with a new API to use, your first reflex should be to go straight to the documentation, and figure out the following:

1. Is this a REST API?
1. Does it serve JSON?
1. Does this API require authentication? (do I need to sign up to get an API key? Do I need to pay?)
1. What is the base URI?
1. Which endpoints can I call? What data does it return?

👯‍♂️ Buddy time! Go to [OpenWeatherMap API documentation](https://openweathermap.org/api) read it, and try answering those questions. When you are comfortable with what this API is about, you can start working on the challenge

## Authentication (and a small 🎁 from us)

You might have noticed that OpenWeatherMap requires you to sign up for an `API key`. Even though OpenWeatherMap offers [a few free API calls](https://openweathermap.org/price), they still want to know how different users consume the API (and track if you hit your API call limit 😜). This is the norm for most APIs out there.

You can either:

1. Sign up for an API key (which might take 10-20 minutes to get activated)
2. Use a proxy we created for you 👉 [https://weather.lewagon.com/](https://weather.lewagon.com/). This URL already includes the API key, so you can just replace the host of OpenWeatherMap with the Le Wagon website and skip the `API key` parameter in your request. For example:

`https://api.openweathermap.org/geo/1.0/direct?q=Barcelona&appid=XXXXXXXXXXX`

becomes:

`https://weather.lewagon.com/geo/1.0/direct?q=Barcelona`

**Note:** make sure to check [https://weather.lewagon.com/](https://weather.lewagon.com/) to see the documentation on which endpoints are proxied. If the endpoint you want to access is not shown, you will need to access it with your own API key instead.

## Making a test call to the API

Before building something fancy, we need to first make sure that we can run an API call successfully. This is a sanity check to make sure we don't start coding too much before realizing that the API we intended to use is not a good fit.

So how can we make our first call? There are several options:

### Using the browser

The browser _is_ an HTTP client! If there is no complex request `Header` to set and the verb to use is `GET`, then it's just as easy as typing the URL in the address bar. Try it!

Open a new browser tab, and copy/paste the following URL:

```bash
https://weather.lewagon.com/geo/1.0/direct?q=Barcelona
```

What do you see? If you are on Chrome, you should install the [JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc) extension for a neater look. In the end, JSON is just text that needs to be **parsed**, that's what the extension will do.

### Optional - Using Postman

[Postman](https://www.getpostman.com/) is an app that many developers download on their laptop to use when building software consuming APIs. It provides a more advanced experience where you need to have more control over:

- HTTP verb (`GET`, `POST`, `PATCH`, `DELETE`, etc.)
- Request headers (`Content-Type`, `Authorization`, etc.)
- Request body (`application/x-www-form-urlencoded` or `raw`)

This application allows us to **save** some requests, create tabs with different requests and offers more advanced features. Go ahead and try it!

### Using Python

Finally, we want to use this API in _our code_. Python's standard library comes with an [`http.client`](https://docs.python.org/3/library/http.client.html) built-in module, but we are not going to use it. Instead, we are going to use the [`requests`](https://requests.readthedocs.io) library, an 'elegant and simple HTTP library for Python, built for human beings'.

Open the `test_api.py` file and paste the following code:

```python
import requests

url = "https://weather.lewagon.com/geo/1.0/direct?q=Barcelona"
response = requests.get(url).json()
city = response[0]
print(f"{city['name']}: ({city['lat']}, {city['lon']})")
```

Save the file and run the following command:

```bash
python test_api.py
```

Is it working? Did you successfully grab Barcelona's `lat` and `lon`? Some questions for you to answer with your buddy before moving forward:

- Line `4`, why are we chaining a `.json()` after `.get()`? Does it still work without that call? You can `print()` intermediate steps to convince yourself. (💡 [Doc](https://requests.readthedocs.io/en/master/user/quickstart/#json-response-content))
- Line `5`, why do we use `[0]`? What's the type of `response`?
- Line `6`, what's the type of `city['lat']` and `city['lon']`, `str` or `int`? Why?

To answer those questions, don't hesitate to `print()` or **even better**, [debug](https://pypi.org/project/ipdb/). This first week is a good time to sharpen your debugging skills before diving into more advanced topics. Don't remember how to do it? Remember yesterday's challenge in which you had to insert this line in your code:

```python
breakpoint()
```

And run the file with:

```bash
python test_api.py
```

It will stop execution at the line where you added the `breakpoint()` and open a command line. From there you can check the `url`, `response`, `city` or any other variable you defined in the code!


## Let the challenge begin!

### Weather CLI

Let's build a weather [CLI](https://en.wikipedia.org/wiki/Command-line_interface) using the API. Here's the flow for a user (pseudo-code!):

1. Launch the app with `python weather.py`
2. Get asked to type a city name
3. If the city is unknown to the API, display an error message and go back to step 2.
4. Fetch the weather forecast for the next 5 days and display it (date, weather, and max temperature in °C)
5. Go back to step 2 (loop to ask for a new city).
6. At any point, `Ctrl`-`C` can be used to quit the program

In action, it should look like this:

```bash
python weather.py
```

```text
City?
> london
Here's the weather in London
2020-09-30: Heavy Rain 16.4°C
2020-10-01: Light Rain 15.1°C
2020-10-02: Heavy Rain 13.4°C
2020-10-03: Heavy Rain 14.3°C
2020-10-04: Heavy Rain 14.6°C
City?
>
```

Open the `weather.py` file. You will be greeted by three empty functions:

- `search_city(query)`
- `weather_forecast(lat, lon)`
- `main()`

You need to implement them **in that order**. `make` will assist you with the first two functions, and for the last one, you will need to run the Python program directly with `python weather.py`.

1. Start with the `search_city` function which should return a `dictionary` with all the information about the city. Not just the `lat` and `lon`!
2. Continue to `weather_forecast` which takes the city's `lat` and `lon` as arguments and returns the forecast for five days (make sure that the method returns a `list` of dictionaries). **NOTE**: OpenWeatherMap returns a forecast for every 3 hours, so you'll need to slice the result to only have one forecast per day.
3. Finish off by coding the `main` function. It will be called when you run the `weather.py` file from the terminal. Which functions should be called from within `main`? In what order?

💡 By the way, did you check the content of the `Makefile`? It runs `pylint` for every Python file in your project, and `pytest` for the whole project. You can only launch the tests for the weather CLI with:

```bash
pytest -v tests/test_weather.py
```

## List of cities

After `step 3`: if the user input is ambiguous (i.e. several cities come back from the search), display them and ask the user to pick one by index, like this:

```text
City?
> Pari
1. Paris,FR
2. Paris,FR
3. Paris,FR
4. Pari,IT
5. Puri,IN
Multiple matches found, which city did you mean?
> 1
2022-09-26: Clouds (12°C)
2022-09-27: Clouds (10°C)
2022-09-28: Rain (12°C)
2022-09-29: Clouds (11°C)
2022-09-30: Clear (10°C)
```

💡 **Hint 1:** there's a built-in [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) function that might be useful.

💡 **Hint 2:** by default, the API does not return multiple options for a given query `q`. Add the `limit=` parameter to your URL to ensure that the API returns the given number of options (i.e. `https://weather.lewagon.com/geo/1.0/direct?q=Barcelona&limit=5` will return 5 options for Barcelona if applicable).


---

Are all `make` tests green and does the program work as intended? Congrats on your first CLI tool! On to the next challenge: **scraping**! 🕷️
