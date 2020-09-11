#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from datetime import datetime as dt
import googlemaps


# In[2]:


df = pd.read_csv("https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv?cachebust=6d352e35dcffafce")
df = df.fillna(method='ffill')
df = df.replace(np.nan, '', regex=True)
df


# In[5]:


def get_geo_coordinates(address):
    """
    param: address is the address of the location
    """
    gmaps = googlemaps.Client(key='AIzaSyAstu56DT6WjhZoqwSjV7FyT1e_r-PM9HI')
    geocode_result = gmaps.geocode(address)
    lat = geocode_result[0]["geometry"]["location"]['lat']
    lng = geocode_result[0]["geometry"]["location"]['lng']
    return (lat, lng) 


# In[21]:


get_geo_coordinates("United States")


# In[23]:


#Get all data
df = pd.read_csv("https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv?cachebust=6d352e35dcffafce")
df = df.fillna(method='ffill')
df = df.replace(np.nan, '', regex=True)
place_data = {}
coordinates_data = {}
print((dt.strptime(df.iloc[2]["date"],'%Y-%m-%d')-dt.strptime(df.iloc[0]["date"],'%Y-%m-%d')).total_seconds())
for i in range(len(df)-1):
    row_one = df.iloc[i]
    date_one = dt.strptime(df.iloc[i]["date"], '%Y-%m-%d')
    date_two = dt.strptime(df.iloc[i+1]["date"], '%Y-%m-%d')
    seconds_difference = (date_two - date_one).total_seconds()
    if seconds_difference < 0:
        address = df.iloc[i]["country_region"] + " "
        address += df.iloc[i]["sub_region_1"] + " "
        address += df.iloc[i]["sub_region_2"] + " "
        print(address)
        place_data[address] = row_one["retail_and_recreation_percent_change_from_baseline"] + row_one["grocery_and_pharmacy_percent_change_from_baseline"] + row_one["parks_percent_change_from_baseline"] + row_one["transit_stations_percent_change_from_baseline"] + row_one["workplaces_percent_change_from_baseline"] + row_one["residential_percent_change_from_baseline"]
        coordinates = get_geo_coordinates(address)
        print(coordinates)
        coordinates_data[coordinates] = row_one["retail_and_recreation_percent_change_from_baseline"] + row_one["grocery_and_pharmacy_percent_change_from_baseline"] + row_one["parks_percent_change_from_baseline"] + row_one["transit_stations_percent_change_from_baseline"] + row_one["workplaces_percent_change_from_baseline"] + row_one["residential_percent_change_from_baseline"]
print(coordinates_data)


# In[9]:


#Get New York data
df = pd.read_csv("https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv?cachebust=6d352e35dcffafce")
df = df.fillna(method='ffill')
df = df.replace(np.nan, '', regex=True)
place_data = {}
coordinates_data = {}
places = []
coordinate_points = []
mobility = []
print((dt.strptime(df.iloc[2]["date"],'%Y-%m-%d')-dt.strptime(df.iloc[0]["date"],'%Y-%m-%d')).total_seconds())
for i in range(len(df)-1):
    row_one = df.iloc[i]
    if (df.iloc[i]["sub_region_1"] == "New York"):
        date_one = dt.strptime(df.iloc[i]["date"], '%Y-%m-%d')
        date_two = dt.strptime(df.iloc[i+1]["date"], '%Y-%m-%d')
        seconds_difference = (date_two - date_one).total_seconds()
        if seconds_difference < 0:
            address = df.iloc[i]["country_region"] + " "
            address += df.iloc[i]["sub_region_1"] + " "
            address += df.iloc[i]["sub_region_2"] + " "
            place_data[address] = row_one["retail_and_recreation_percent_change_from_baseline"] + row_one["grocery_and_pharmacy_percent_change_from_baseline"] + row_one["parks_percent_change_from_baseline"] + row_one["transit_stations_percent_change_from_baseline"] + row_one["workplaces_percent_change_from_baseline"] + row_one["residential_percent_change_from_baseline"]
            places.append(address)
            mobility.append(place_data[address])
            coordinates = get_geo_coordinates(address)
            coordinate_points.append(coordinates)
            coordinates_data[coordinates] = row_one["retail_and_recreation_percent_change_from_baseline"] + row_one["grocery_and_pharmacy_percent_change_from_baseline"] + row_one["parks_percent_change_from_baseline"] + row_one["transit_stations_percent_change_from_baseline"] + row_one["workplaces_percent_change_from_baseline"] + row_one["residential_percent_change_from_baseline"]
df2 = pd.DataFrame({"Places": places, "Coordinates": coordinate_points, "Mobility": mobility}, columns=["Places", "Coordinates", "Mobility"])
df2.to_csv("Mobility_ny.csv")
print(coordinates_data)


# In[ ]:




