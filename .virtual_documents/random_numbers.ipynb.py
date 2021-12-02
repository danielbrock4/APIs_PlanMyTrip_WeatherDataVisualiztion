# Import the random module.
import random

# Import the NumPy module.
    # Recall that the NumPy module is a numerical mathematics library that can be used to make arrays or matrices of numbers.
    # NOTE: The NumPy module has a built-in random module, and supplements the built-in Python random module. There is no need to import the random module if we import the NumPy module, as it's redundant.
import numpy as np

#To test how long a piece of code or function takes to run, we can import the "timeit" module and use the get_ipython().run_line_magic("timeit", " magic command when we run our code or call the function.")
import timeit


# Import linear regression from the SciPy stats module.
from scipy.stats import linregress


random.randint(-90, 90)


random.random()


random.randint(-90, 89) + random.random()


# 1) Assign the variable x to 1.
# 2) Initialize an empty list, latitudes.
# 3) We create a while loop where we generate a random latitude and add it to the list. With the while loop we can execute a set of statements as long as a condition is true.
    # to be ready, in this example we need to define an indexing variable, x, which we set to 1.
    # 3a) create variable random_lat for combining random.randint(-90, 89) and random.random() to generate a floating-point decimal between –90 and 90, we can generate a random latitude. The while loop requires relevant variables 
    # 3b) Append to random numbers to our empty list, latitudes
    # 4a) After the random latitude is added to the list we add one to the variable "x".
           # += Adds a value and the variable and assigns the result to that variable.
#4 ) The while loop condition is checked again and will continue to run as long as x is less than 11.


x = 1 
latitudes = []
while x < 11:
    random_lat = random.randint(-90, 89) + random.random()
    latitudes.append(random_lat)
    x += 1
    
latitudes


rangeint1 = random.randrange(-90, 90, 1)
rangeint3 = random.randrange(-90, 90, 3)
print(rangeint1, rangeint3)


random.uniform(-90, 90)


np.random.uniform(-90.000, 90.000)


np.random.uniform(-90.000, 90.000, 10)


get_ipython().run_line_magic("timeit", " np.random.uniform(-90.000, 90.000, 10)")


def latitudes(size):
    latitudes = []
    x = 0
    while x < (size):
        random_lat = random.randint(-90, 90) + random.random()
        latitudes.append(random_lat)
        x += 1
    return latitudes
# Call the function with 1500.
get_ipython().run_line_magic("timeit", " latitudes(1500)")


def time_latitude(x):
    latitude = latitudes(x)
    get_ipython().run_line_magic("timeit", " latitudes(x)")
    
    return latitude

time_latitude(5) 


# Create a practice set of random latitude and longitude combinations.
x = [25.12903645, 25.92017388, 26.62509167, -59.98969384, 37.30571269]
y = [-67.59741259, 11.09532135, 74.84233102, -76.89176677, -61.13376282]
coordinates = zip(x, y)


# Use the tuple() function to display the latitude and longitude combinations.
for coordinate in coordinates:
    print(coordinate[0], coordinate[1])


# Use the tuple() function to display the latitude and longitude combinations.
for coordinate in coordinates:
    print(citipy.nearest_city(coordinate[0], coordinate[1]).city_name,
          citipy.nearest_city(coordinate[0], coordinate[1]).country_code)


# Import linear regression from the SciPy stats module.
from scipy.stats import linregress


# Create an equal number of latitudes and temperatures.
lats = [42.5, 43.9, 8.1, 36.8, 79.9, 69.1, 25.7, 15.3, 12.7, 64.5]
temps = [80.5, 75.3, 90.9, 90.0, 40.4, 62.3, 85.4, 79.6, 72.5, 72.0]


# Perform linear regression.
(slope, intercept, r_value, p_value, std_err) = linregress(lats, temps)
# Get the equation of the line.
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
print(line_eq)
print(f"The p-value is: {p_value:.3f}")


# Calculate the regression line "y values" from the slope and intercept.
regress_values = [(lat * slope + intercept) for lat in lats]
regress_values 


# Import Matplotlib.
import matplotlib.pyplot as plt
# Create a scatter plot of the x and y values.
plt.scatter(lats,temps)
# Plot the regression line with the x-values and the y coordinates based on the intercept and slope.
plt.plot(lats,regress_values,"r")
# Annotate the text for the line equation and add its coordinates.
plt.annotate(line_eq, (10,40), fontsize=15, color="red")
plt.xlabel('Latitude')
plt.ylabel('Temp')

plt.show()

