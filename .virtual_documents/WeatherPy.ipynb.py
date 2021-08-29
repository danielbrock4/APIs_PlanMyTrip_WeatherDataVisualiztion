# Import the dependencies.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Use the citipy module to determine city based on latitude and longitude.
    # Under "Looking up with coordinates," the first line says from citipy import citipy, meaning we'll import the citipy script from the citipy module.
    # When a Python file containing a script is imported to use in another Python script, the .py extension does not need to be added to the name of the file when using the import statement.    
from citipy import citipy


# Create a set of random latitude and longitude combinations.
    # 1) Create arrays of latitudes and longitudes, we'll declare each array as a variable. 
    # 2) Use Numpty random uniform because its faster to generate the random latitudes and longtitudes.
            # To generate more than one floating-point decimal number between –90 and 90, we can add the size parameter when we use the NumPy module and set that equal to any whole number.
    # 3) Use zip() we'll pack the latitudes (lats) and longitudes (lngs) as pairs by zipping them (lat_lngs) with the zip() function.

lats = np.random.uniform(low=-90.00, high=90.000, size=1500)
lngs = np.random.uniform(-180.000, 180.000, size=1500)
lats_lngs = zip(lats, lngs)
lats_lngs 


# Add the latitudes and longitudes to a list.
coordinates = list(lats_lngs)
coordinates[:3]


#1) Create a cities list to store city names.
#2) Using a for loop, iterate through the coordinates' zipped tuple.
#3) Use citipy.nearest_city() and inside the parentheses of nearest_city(), add the latitude and longitude in this format: coordinate[0], coordinate[1].
    # The citipy module finds the nearest city to the latitude and longitude pair with a population of 500 or more.
    #3a) Because of the zip function The zip object packs each pair of lats and lngs having the same index in their respective array into a tuple. Where each latitude and longitude in a tuple can be       accessed by the index of 0 and 1
#4) To print the city name, chain the city_name to the nearest_city() function.
#5) We add a decision statement with the logical operator not in to determine whether the found city is already in the cities list. If not, then we'll use the append() function to add it. 
    # We are doing this because among the 1,500 latitudes and longitudes, there might be duplicates, which will retrieve duplicate cities, and we want to be sure we capture only the unique cities.

# Create a list for holding the cities.
cities = []
# Identify the nearest city for each latitude and longitude combination.
for coordinate in coordinates:
    city = citipy.nearest_city(coordinate[0], coordinate[1]).city_name
    # If the city is unique, then we will add it to the cities list.
    if city not in cities:
        cities.append(city)
# Print the city count to confirm sufficient count.
len(cities)    





# 1)
# 2)
# 3)
# 4) 
# 5)
