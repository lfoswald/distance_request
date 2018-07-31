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


### 1. import csv file ###

#set working directory

os.chdir('/Users/lisaoswald/python')


# load input data set (csv)

data = pandas.read_csv('demo_input.csv', sep=';', na_values=".")
data            
print (data['start'])
print (data['destination'])


### 2. build url, request html page content, extract information

# version 1

for index, start in enumerate(data['start']):
    print(start)
    for index, dest in enumerate(data['destination']):
        print(dest)
    for index in data:
        my_url = ("https://www.distance.to/" ,start, "/" ,dest)
        joined_url = "".join(my_url)
        page = requests.get(joined_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        route = soup.find(class_="main-route trip").get_text()
        dist_calc = soup.find(class_="value km").get_text()
        print(route, dist_calc)

# problem: I get result of each dist_calc 25 times (lenght of index)
        
# version 2
for index, start in enumerate(data['start']):
    for index, dest in enumerate(data['destination']):
        my_url = ("https://www.distance.to/" ,start, "/" ,dest)
        joined_url = "".join(my_url)
        page = requests.get(joined_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        route = soup.find(class_="main-route trip").get_text()
        dist_calc = soup.find(class_="value km").get_text()
        print(route, dist_calc)

# same problem

        
# version 3         

for start, dest in itertools.product(data['start'], data['destination']):
        my_url = ("https://www.distance.to/" ,start, "/" ,dest)
        joined_url = "".join(my_url)
        page = requests.get(joined_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        route = soup.find(class_="main-route trip").get_text()
        dist_calc = soup.find(class_="value km").get_text()
        print(route, dist_calc)

# same here

    
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