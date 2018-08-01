#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 08:34:09 2018

@author: lisaoswald
"""
### the plan is ###

# 1. define function
# 2. import csv file 
# 3. run request on distance calculator website - iterating over rows in csv
# 4. save results in distance column of data frame
# 5. convert pandas df into csv file

import requests
import pandas
import os
from bs4 import BeautifulSoup

### Set variables ###

local_folder = '/Users/lisaoswald/python'
file_name = 'demo_input.csv'


### 1. define function ###

# url construction + web logic in one separate function that can be re-used
def get_route_and_distance(start, dest):
    my_url = "https://www.distance.to/" + start + "/" + dest
    page = requests.get(my_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    route = soup.find(class_="main-route trip").get_text()
    dist_calc = soup.find(class_="value km").get_text()
    return route, dist_calc


### 2. import csv file ###

# set working directory
os.chdir(local_folder)

# load input data set (csv)
data = pandas.read_csv(file_name, sep=';', na_values=".")

# initialise empty lists for routes and distances
routes = []
distances = []

### 3. run request on distance calculator website - iterating over rows in csv ###

# loop over dataframe rows
for index, row in data.iterrows():
    # extract relevant fields from row
    start = row['start']
    dest = row['destination']

    # output to console
    print('Looking up distance from', start, 'to', dest)

    # use the function we defined above to get the route and distance
    route, dist_calc = get_route_and_distance(start, dest)
    print(route, dist_calc)

    # add these new values to our lists
    routes.append(route)
    distances.append(dist_calc)

### 4. save results in distance column of data frame ###

my_df = pandas.DataFrame({"start": data['start'],
                          "destination": data['destination'],

                          # check if route matches start/destination
                          "route": routes,

                          # actual output
                          "distance": distances})

print(my_df)   

### 5. convert pandas df into csv file ###

my_df.to_csv('dist_data.csv', sep=',', index=False, encoding='utf-8')

# check
data = pandas.read_csv('dist_data.csv', sep=',', na_values=".")
print(data)    
