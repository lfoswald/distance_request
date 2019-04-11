#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:42:55 2019

@author: lisaoswald
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:08:26 2018

@author: lisaoswald
"""

### applying the dist_calc code on the actual data set ###

# 0. check data set - fix super weird answers (like "XY, backpacked all over")
# 1. define function (make request and extract information with BeautifulSoup)
# 2. import csv file and create pandas data frame with travel data
# 3. run request, iterating over rows in data frame
# 4. save results in new columns of data frame
# 5. save data frame in csv file 

import requests
import pandas
import os
from bs4 import BeautifulSoup

### Set variables ###

local_folder = '/Users/lisaoswald/python'
file_name = 'data_flyid_2019-04-08_clean.csv'


### 1.  Define functions ###

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
data_full = pandas.read_csv(file_name, encoding = "ISO-8859-1", 
                       sep=',', error_bad_lines=False, na_values=".")

# creat data frame only with travel data
data = pandas.DataFrame({"start1": data_full['SD06_03'],
                          "destination1": data_full['NE09x01'],
                          "start2": data_full['SD06_03'],
                          "destination2": data_full['NE09x02'],
                          "start3": data_full['SD06_03'],
                          "destination3": data_full['NE09x03'],
                          "start4": data_full['SD06_03'],
                          "destination4": data_full['NE09x04'],
                          "start5": data_full['SD06_03'],
                          "destination5": data_full['NE09x05'],
                          "start6": data_full['SD06_03'],
                          "destination6": data_full['NE09x06'],
                          "start7": data_full['SD06_03'],
                          "destination7": data_full['NE09x07'],
                          "start8": data_full['SD06_03'],
                          "destination8": data_full['NE09x08'],
                          "start9": data_full['SD06_03'],
                          "destination9": data_full['NE09x09'],
                          "start10": data_full['SD06_03'],
                          "destination10": data_full['NE09x10'],
                          "start11": data_full['SD06_03'],
                          "destination11": data_full['NE09x11'],
                          "start12": data_full['SD06_03'],
                          "destination12": data_full['NE09x12'],
                          "start13": data_full['SD06_03'],
                          "destination13": data_full['NE09x13'],
                          })

## dealing with missing data (no trip)    
   
# fill all na with Köln (Distance Köln --> Köln = 0)
# because Köln == "die schönste Stadt am Rhein <3"

data = data.fillna(str(data_full['SD06_03']))

# initialise empty lists for routes and distances (for all 11 possible trips)
routes1 = []
distances1 = []

routes2 = []
distances2 = []

routes3 = []
distances3 = []

routes4 = []
distances4 = []

routes5 = []
distances5 = []

routes6 = []
distances6 = []

routes7 = []
distances7 = []

routes8 = []
distances8 = []

routes9 = []
distances9 = []

routes10 = []
distances10 = []

routes11 = []
distances11 = []

routes12 = []
distances12 = []

routes13 = []
distances13 = []


### 3. run request, iterating over rows in data frame ###

# loop over dataframe rows (nr 1)
for index, row in data.iterrows():
    # extract relevant fields from row
    start1 = row['start1']
    dest1 = row['destination1']

    # use the function we defined above to get the route and distance
    route1, dist_calc1 = get_route_and_distance(start1, dest1)
    print(route1, dist_calc1)

    # add these new values to our lists
    routes1.append(route1)
    distances1.append(dist_calc1)
    
    
# loop over dataframe rows (nr 2)
for index, row in data.iterrows():
    start2 = row['start2']
    dest2 = row['destination2']
    route2, dist_calc2 = get_route_and_distance(start2, dest2)
    print(route2, dist_calc2)
    routes2.append(route2)
    distances2.append(dist_calc2)
 
  
# loop over dataframe rows (nr 3)
for index, row in data.iterrows():
    start3 = row['start3']
    dest3 = row['destination3']
    route3, dist_calc3 = get_route_and_distance(start3, dest3)
    print(route3, dist_calc3)
    routes3.append(route3)
    distances3.append(dist_calc3)


# loop over dataframe rows (nr 4)
for index, row in data.iterrows():
    start4 = row['start4']
    dest4 = row['destination4']
    route4, dist_calc4 = get_route_and_distance(start4, dest4)
    print(route4, dist_calc4)
    routes4.append(route4)
    distances4.append(dist_calc4)
    
    
# loop over dataframe rows (nr 5)
for index, row in data.iterrows():
    start5 = row['start5']
    dest5 = row['destination5']
    route5, dist_calc5 = get_route_and_distance(start5, dest5)
    print(route5, dist_calc5)
    routes5.append(route5)
    distances5.append(dist_calc5)
  
    
# loop over dataframe rows (nr 6)
for index, row in data.iterrows():
    start6 = row['start6']
    dest6 = row['destination6']
    route6, dist_calc6 = get_route_and_distance(start6, dest6)
    print(route6, dist_calc6)
    routes6.append(route6)
    distances6.append(dist_calc6)
 
    
# loop over dataframe rows (nr 7)
for index, row in data.iterrows():
    start7 = row['start7']
    dest7 = row['destination7']
    route7, dist_calc7 = get_route_and_distance(start7, dest7)
    print(route7, dist_calc7)
    routes7.append(route7)
    distances7.append(dist_calc7)
 
    
# loop over dataframe rows (nr 8)
for index, row in data.iterrows():
    start8 = row['start8']
    dest8 = row['destination8']
    route8, dist_calc8 = get_route_and_distance(start8, dest8)
    print(route8, dist_calc8)
    routes8.append(route8)
    distances8.append(dist_calc8)
 
    
# loop over dataframe rows (nr 9)
for index, row in data.iterrows():
    start9 = row['start9']
    dest9 = row['destination9']
    route9, dist_calc9 = get_route_and_distance(start9, dest9)
    print(route9, dist_calc9)
    routes9.append(route9)
    distances9.append(dist_calc9)
  
  
# loop over dataframe rows (nr 10)
for index, row in data.iterrows():
    start10 = row['start10']
    dest10 = row['destination10']
    route10, dist_calc10 = get_route_and_distance(start10, dest10)
    print(route10, dist_calc10)
    routes10.append(route10)
    distances10.append(dist_calc10)
  
  
# loop over dataframe rows (nr 11)
for index, row in data.iterrows():
    start11 = row['start11']
    dest11 = row['destination11']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)
    
      
# loop over dataframe rows (nr 12)
for index, row in data.iterrows():
    start12 = row['start12']
    dest12 = row['destination12']
    route12, dist_calc12 = get_route_and_distance(start12, dest12)
    print(route12, dist_calc12)
    routes12.append(route12)
    distances12.append(dist_calc12)
    
      
# loop over dataframe rows (nr 13)
for index, row in data.iterrows():
    start13 = row['start13']
    dest13 = row['destination13']
    route13, dist_calc13 = get_route_and_distance(start13, dest13)
    print(route13, dist_calc13)
    routes13.append(route13)
    distances13.append(dist_calc13)
    
### 4. save results in distance column of new data frame
    
my_df = pandas.DataFrame({# trip nr 1
        # trip nr 1
        "start1": data_full['SD06_03'],
        "destination1": data_full['NE09x01'],
        
        # check if route matches start/destination
        "route1": routes1,
        
        # actual output
        "distance1": distances1,
        
        # trip nr 2
        "start2": data_full['SD06_03'],
        "destination2": data_full['NE09x02'],
        "route2": routes2,
        "distance2": distances2,
        
        # trip nr 3
        "start3": data_full['SD06_03'],
        "destination3": data_full['NE09x03'],
        "route3": routes3,
        "distance3": distances3,
        
        # trip nr 4
        "start4": data_full['SD06_03'],
        "destination4": data_full['NE09x04'],
        "route4": routes4,
        "distance4": distances4,        
        
        # trip nr 5                  
        "start5": data_full['SD06_03'],
        "destination5": data_full['NE09x05'],
        "route5": routes5,
        "distance5": distances5,
        
        # trip nr 6                 
        "start6": data_full['SD06_03'],
        "destination6": data_full['NE09x06'],
        "route6": routes6,
        "distance6": distances6,
        
        # trip nr 7                
        "start7": data_full['SD06_03'],
        "destination7": data_full['NE09x07'],
        "route7": routes7,
        "distance7": distances7,
                          
        # trip nr 8               
        "start8": data_full['SD06_03'],
        "destination8": data_full['NE09x08'],
        "route8": routes8,
        "distance8": distances8,
                          
        # trip nr 9              
        "start9": data_full['SD06_03'],
        "destination9": data_full['NE09x09'],
        "route9": routes9,
        "distance9": distances9,
                          
        # trip nr 10             
        "start10": data_full['SD06_03'],
        "destination10": data_full['NE09x10'],
        "route10": routes10,
        "distance10": distances10,
        
        # trip nr 11           
        "start11": data_full['SD06_03'],
        "destination11": data_full['NE09x11'],
        "route11": routes11,
        "distance11": distances11,
        
                # trip nr 12           
        "start12": data_full['SD06_03'],
        "destination12": data_full['NE09x12'],
        "route12": routes12,
        "distance12": distances12,
                          
        # trip nr 13           
        "start13": data_full['SD06_03'],
        "destination13": data_full['NE09x13'],
        "route13": routes13,
        "distance13": distances13,
                          
                          })

    
print(my_df)   


# 5. convert pandas df into csv file
my_df.to_csv('network_data.csv', sep=',', index=False, encoding='utf-8')

# check
data = pandas.read_csv('network_data.csv', sep=',', na_values=".")
print(data)    
