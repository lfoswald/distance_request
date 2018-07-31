#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 13:23:16 2018

@author: lisaoswald
"""

### what I want to do ###
# 1. import csv file 
# 2. run request on distance calculator website - iterating over rows in csv
    # write request url first (using starts & destinations of csv file)
    # then make actual request
    # extract results with BeautifulSoup
# 3. save results in new column of csv 

import csv 
import requests
import pandas
import os
import itertools
from bs4 import BeautifulSoup


### Set variables ###

local_folder = '/Users/lisaoswald/python'
file_name = 'demo_input.csv'

### Define functions ###

# url construction + web logic in one separate function that can be re-used
def get_route_and_distance(start, dest):
    my_url = "https://www.distance.to/" + start + "/" + dest
    page = requests.get(my_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    route = soup.find(class_="main-route trip").get_text()
    dist_calc = soup.find(class_="value km").get_text()
    return route, dist_calc

### 1. import csv file ###

# set working directory
os.chdir(local_folder)

# load input data set (csv)

data = pandas.read_csv(file_name, sep=';', na_values=".")
print(data['start'])
print(data['destination'])

### 2.

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

    
# check url requests
print(joined_url)
print(page.url) 
page.status_code # 200 = success (codes starting with 4 or 5 = error)
page.content # downloaded HTML content
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify()) 
soup.find(id="logo")
route = soup.find(class_="main-route trip").get_text()
dist_calc = soup.find(class_="value km").get_text()
print(route, dist_calc)

print('The distance of the route:', soup.find(class_="main-route trip").get_text(),
 'is' , soup.find(class_="value km").get_text() ,'km.')


# 3. save results in new column in csv 

for index,row in data:       
        with open('demo_input.csv', 'wb') as csvfile:
            distancewriter = csv.writer(csvfile, delimiter=' ')
            distancewriter.writecol(route)
            distancewriter.writecol(dist_calc)
            
# probably doesn't work this way... never had propper output to save haha

# check
data = pandas.read_csv('demo_input.csv', sep=';', na_values=".")
data    