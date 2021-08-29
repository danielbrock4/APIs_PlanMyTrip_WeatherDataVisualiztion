# Import the requests library.
import requests

# Use the citipy module to determine city based on latitude and longitude.
    # Under "Looking up with coordinates," the first line says from citipy import citipy, meaning we'll import the citipy script from the citipy module.
    # When a Python file containing a script is imported to use in another Python script, the .py extension does not need to be added to the name of the file when using the import statement.    
from citipy import citipy

# Import the API key.
from config import weather_api_key


# Starting URL for Weather Map API Call.
url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + weather_api_key
print(url)


# Create an endpoint URL for a city.
city_url = url + "&q=" + "Boston"
print(city_url)


# Make a 'Get' request for the city weather.
city_weather = requests.get(city_url)
city_weather


# Create an endpoint URL for a city.
city_url = url + "&q=" + "Bston"
city_weather = requests.get(city_url)
city_weather


# Create an endpoint URL for a city.
city_url = url + "&q=" + "Boston"
city_weather = requests.get(city_url)
city_weather


# Get the text of the 'Get' request.
city_weather.text


# Get the JSON text of the 'Get' request.
city_weather.json()
