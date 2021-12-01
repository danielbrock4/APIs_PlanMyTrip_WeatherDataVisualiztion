# Import the requests library.
    # To request JSON data over the internet, we use the Requests Library in Python. 
import requests

# Import the API key.
    # When a Python file containing a script is imported to use in another Python script, the .py extension does not need to be added to the name of the file when using the import statement.
from config import weather_api_key

# Use the citipy module to determine city based on latitude and longitude.
    # Under "Looking up with coordinates," the first line says from citipy import citipy, meaning we'll import the citipy script from the citipy module.
    # When a Python file containing a script is imported to use in another Python script, the .py extension does not need to be added to the name of the file when using the import statement.    
from citipy import citipy

# Import the datetime module from the datetime library.
    # If we want to convert the timestamp to the International Organization for Standardization (ISO) format, or YYYY-MM-DD-HH-MM-SS, we need to use the Python datetime module.
from datetime import datetime


# Starting URL for Weather Map API Call.
# Structure example = api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API key}
url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + weather_api_key
city_name = "Boston"
units = "Imperial"
# print(url)


# Create an endpoint URL for a city.
city_url = url + "&q=" + "Boston"
# print(city_url)


url_blank = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Boston"
units = "Imperial"

full_url = url_blank + "units=" + units + "&APPID=" + weather_api_key + "&q=" + city_name
# print(full_url)


# Make a 'Get' request for the city weather.
    # get() - Retrieves data from a web source.
city_weather = requests.get(city_url)
city_weather


city_weather.status_code


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


# Create an endpoint URL for a city.
city_url = url + "&q=" + "Boston"
city_weather = requests.get(city_url)
if city_weather.status_code == 200:
    print(f"City Weather Found")
else:
    print(f"City Weather NOT Found")


# Create an endpoint URL for a city.
city_url = url + "&q=" + "Bston"
city_weather = requests.get(city_url)
if city_weather.json():
    print(f"City Weather found.")
else:
    print(f"City weather not found.")


# Create an endpoint URL for a city.
city_url = url + "&q=" + "Boston"
city_weather = requests.get(city_url)
city_weather.json()


# Get the JSON data.
boston_data = city_weather.json()


boston_data["sys"]


boston_data["sys"]["country"]


lat = boston_data["coord"]["lat"]
lng = boston_data["coord"]["lon"]
max_temp = boston_data["main"]["temp_max"]
humidity = boston_data["main"]["humidity"]
clouds = boston_data["clouds"]["all"]
wind = boston_data["wind"]["speed"]
print(lat, lng, max_temp, humidity, clouds, wind)


boston_data["dt"]


# Import the datetime module from the datetime library.
from datetime import datetime
# Get the date from the JSON file.
date = boston_data["dt"]
# Convert the UTC date to a date format with year, month, day, hours, minutes, and seconds.
datetime.utcfromtimestamp(date)


datetime.utcfromtimestamp(date).strftime('get_ipython().run_line_magic("Y-%m-%d", " %H:%M:%S')")
