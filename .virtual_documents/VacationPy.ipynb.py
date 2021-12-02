# Import the dependencies.
import pandas as pd
import gmaps
import requests
# Import the API key.
from config import g_key


# Store the CSV you saved created in part one into a DataFrame.
city_data_df = pd.read_csv("weather_data/cities.csv")
city_data_df.head()


# Get the data types
city_data_df.dtypes


# Configure gmaps to use your Google API key.
gmaps.configure(api_key=g_key)


# Get the maximum temperature.
max_temp = city_data_df["Max Temp"]
temps = []
for temp in max_temp:
    # In the for loop, we're using the max() function to get the largest value between the temp and 0. 
    #If the temp is less than 0, then 0 will be added to the list in its place. Otherwise, 
    #the temp is added to the list
    temps.append(max(temp, 0))


# Heatmap of temperature

# 1. Assign the locations to an array of latitude and longitude pairs.
locations = city_data_df[["Lat", "Lng"]]

# 2. Assign the weights variable to some values.
    # Google heatmaps do not plot negative numbers. If you have a maximum temperature that is less than 0 °F, then you will get an InvalidWeightException error for this line of code:
max_temp = city_data_df["Max Temp"]

# 3. Assign the figure variable to the gmaps.figure() attribute.
fig = gmaps.figure()

# 4. Assign the heatmap_layer variable to the heatmap_layer attribute and add in the locations.
# heat_layer = gmaps.heatmap_layer(locations, weights=max_temp)
heat_layer = gmaps.heatmap_layer(locations, weights=temps)
                                 
# 5. Add the heatmap layer.
fig.add_layer(heat_layer)

# 6. Call the figure to plot the data.
fig



