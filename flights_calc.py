#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:41:59 2019

@author: lisaoswald
"""

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
data = pandas.DataFrame({"start1": data_full['FL02x01'],
                          "destination1": data_full['FL09x01'],
                          "start2": data_full['FL02x02'],
                          "destination2": data_full['FL09x02'],
                          "start3": data_full['FL02x03'],
                          "destination3": data_full['FL09x03'],
                          "start4": data_full['FL02x04'],
                          "destination4": data_full['FL09x04'],
                          "start5": data_full['FL02x05'],
                          "destination5": data_full['FL09x05'],
                          "start6": data_full['FL02x06'],
                          "destination6": data_full['FL09x06'],
                          "start7": data_full['FL02x07'],
                          "destination7": data_full['FL09x07'],
                          "start8": data_full['FL02x08'],
                          "destination8": data_full['FL09x08'],
                          "start9": data_full['FL02x09'],
                          "destination9": data_full['FL09x09'],
                          "start10": data_full['FL02x10'],
                          "destination10": data_full['FL09x10'],
                          "start11": data_full['FL02x11'],
                          "destination11": data_full['FL09x11'],
                          "start12": data_full['FL02x12'],
                          "destination12": data_full['FL09x12'],
                          "start13": data_full['FL02x13'],
                          "destination13": data_full['FL09x13'],
                          "start14": data_full['FL02x14'],
                          "destination14": data_full['FL09x14'],
                          "start15": data_full['FL02x15'],
                          "destination15": data_full['FL09x15'],
                          "start16": data_full['FL02x16'],
                          "destination16": data_full['FL09x16'],
                          "start17": data_full['FL02x17'],
                          "destination17": data_full['FL09x17'],
                          "start18": data_full['FL02x18'],
                          "destination18": data_full['FL09x18'],
                          "start19": data_full['FL02x19'],
                          "destination19": data_full['FL09x19'],
                          "start20": data_full['FL02x20'],
                          "destination20": data_full['FL09x20'],
                          "start21": data_full['FL02x21'],
                          "destination21": data_full['FL09x21'],

                          
                          "start26": data_full['FL08x01'],
                          "destination26": data_full['FL10x01'],
                          "start27": data_full['FL08x02'],
                          "destination27": data_full['FL10x02'],
                          "start28": data_full['FL08x03'],
                          "destination28": data_full['FL10x03'],
                          "start29": data_full['FL08x04'],
                          "destination29": data_full['FL10x04'],
                          "start30": data_full['FL08x05'],
                          "destination30": data_full['FL10x05'],
                          "start31": data_full['FL08x06'],
                          "destination31": data_full['FL10x06'],
                          "start32": data_full['FL08x07'],
                          "destination32": data_full['FL10x07'],
                          "start33": data_full['FL08x08'],
                          "destination33": data_full['FL10x08'],
                          "start34": data_full['FL08x09'],
                          "destination34": data_full['FL10x09'],
                          "start35": data_full['FL08x10'],
                          "destination35": data_full['FL10x10'],
                          "start36": data_full['FL08x11'],
                          "destination36": data_full['FL10x11'],
                          "start37": data_full['FL08x12'],
                          "destination37": data_full['FL10x12'],
                          "start38": data_full['FL08x13'],
                          "destination38": data_full['FL10x13'],
                          "start39": data_full['FL08x14'],
                          "destination39": data_full['FL10x14'],
                          "start40": data_full['FL08x15'],
                          "destination40": data_full['FL10x15'],
                          "start41": data_full['FL08x16'],
                          "destination41": data_full['FL10x16'],
                          "start42": data_full['FL08x17'],
                          "destination42": data_full['FL10x17'],
                          "start43": data_full['FL08x18'],
                          "destination43": data_full['FL10x18'],
                          "start44": data_full['FL08x19'],
                          "destination44": data_full['FL10x19'],
                          "start45": data_full['FL08x20'],
                          "destination45": data_full['FL10x20'],
                          "start46": data_full['FL08x21'],
                          "destination46": data_full['FL10x21'],
                          "start47": data_full['FL08x22'],
                          "destination47": data_full['FL10x22'],
                          "start48": data_full['FL08x23'],
                          "destination48": data_full['FL10x23'],
                          "start49": data_full['FL08x24'],
                          "destination49": data_full['FL10x24'],
                          "start50": data_full['FL08x25'],
                          "destination50": data_full['FL10x25'],
                          })

## dealing with missing data (no trip)    
   
# fill all na with Köln (Distance Köln --> Köln = 0)
# because Köln == "die schönste Stadt am Rhein <3"

data = data.fillna("Köln")

# initialise empty lists for routes and distances (for all 50 possible trips - past and planned)

# planned trips: 1 - 25 (there are max 21 planned flights)

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

routes14 = []
distances14 = []

routes15 = []
distances15 = []

routes16 = []
distances16 = []

routes17 = []
distances17 = []

routes18 = []
distances18 = []

routes19 = []
distances19 = []

routes20 = []
distances20 = []

routes21 = []
distances21 = []



# past trips: 26 - 50

routes26 = []
distances26 = []

routes27 = []
distances27 = []

routes28 = []
distances28 = []

routes29 = []
distances29 = []

routes30 = []
distances30 = []

routes31 = []
distances31 = []

routes32 = []
distances32 = []

routes33 = []
distances33 = []

routes34 = []
distances34 = []

routes35 = []
distances35 = []

routes36 = []
distances36 = []

routes37 = []
distances37 = []

routes38 = []
distances38 = []

routes39 = []
distances39 = []

routes40 = []
distances40 = []

routes41 = []
distances41 = []

routes42 = []
distances42 = []

routes43 = []
distances43 = []

routes44 = []
distances44 = []

routes45 = []
distances45 = []

routes46 = []
distances46 = []

routes47 = []
distances47 = []

routes48 = []
distances48 = []

routes49 = []
distances49 = []

routes50 = []
distances50 = []


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
    start11 = row['start12']
    dest11 = row['destination12']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)
    
    # loop over dataframe rows (nr 13)
for index, row in data.iterrows():
    start11 = row['start13']
    dest11 = row['destination13']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 14)
for index, row in data.iterrows():
    start11 = row['start14']
    dest11 = row['destination14']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)
    
# loop over dataframe rows (nr 15)
for index, row in data.iterrows():
    start11 = row['start15']
    dest11 = row['destination15']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)
    
# loop over dataframe rows (nr 16)
for index, row in data.iterrows():
    start11 = row['start16']
    dest11 = row['destination16']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)    

# loop over dataframe rows (nr 17)
for index, row in data.iterrows():
    start11 = row['start17']
    dest11 = row['destination17']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 18)
for index, row in data.iterrows():
    start11 = row['start18']
    dest11 = row['destination18']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 19)
for index, row in data.iterrows():
    start11 = row['start19']
    dest11 = row['destination19']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 20)
for index, row in data.iterrows():
    start11 = row['start20']
    dest11 = row['destination20']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 21)
for index, row in data.iterrows():
    start11 = row['start21']
    dest11 = row['destination21']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)



# loop over dataframe rows (nr 26)
for index, row in data.iterrows():
    start11 = row['start26']
    dest11 = row['destination26']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 27)
for index, row in data.iterrows():
    start11 = row['start27']
    dest11 = row['destination27']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)    
    
 # loop over dataframe rows (nr 28)
for index, row in data.iterrows():
    start11 = row['start28']
    dest11 = row['destination28']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 29)
for index, row in data.iterrows():
    start11 = row['start29']
    dest11 = row['destination29']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 30)
for index, row in data.iterrows():
    start11 = row['start30']
    dest11 = row['destination30']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 31)
for index, row in data.iterrows():
    start11 = row['start31']
    dest11 = row['destination31']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 32)
for index, row in data.iterrows():
    start11 = row['start32']
    dest11 = row['destination32']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 33)
for index, row in data.iterrows():
    start11 = row['start33']
    dest11 = row['destination33']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 34)
for index, row in data.iterrows():
    start11 = row['start34']
    dest11 = row['destination34']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 35)
for index, row in data.iterrows():
    start11 = row['start35']
    dest11 = row['destination35']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)
    
# loop over dataframe rows (nr 36)
for index, row in data.iterrows():
    start11 = row['start36']
    dest11 = row['destination36']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 37)
for index, row in data.iterrows():
    start11 = row['start37']
    dest11 = row['destination37']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 38)
for index, row in data.iterrows():
    start11 = row['start38']
    dest11 = row['destination38']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 39)
for index, row in data.iterrows():
    start11 = row['start39']
    dest11 = row['destination39']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 40)
for index, row in data.iterrows():
    start11 = row['start40']
    dest11 = row['destination40']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 41)
for index, row in data.iterrows():
    start11 = row['start41']
    dest11 = row['destination41']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 42)
for index, row in data.iterrows():
    start11 = row['start42']
    dest11 = row['destination42']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 43)
for index, row in data.iterrows():
    start11 = row['start43']
    dest11 = row['destination43']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)
    
    
# loop over dataframe rows (nr 44)
for index, row in data.iterrows():
    start11 = row['start44']
    dest11 = row['destination44']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 45)
for index, row in data.iterrows():
    start11 = row['start45']
    dest11 = row['destination45']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 46)
for index, row in data.iterrows():
    start11 = row['start46']
    dest11 = row['destination46']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 47)
for index, row in data.iterrows():
    start11 = row['start47']
    dest11 = row['destination47']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 48)
for index, row in data.iterrows():
    start11 = row['start48']
    dest11 = row['destination48']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 49)
for index, row in data.iterrows():
    start11 = row['start49']
    dest11 = row['destination49']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)

# loop over dataframe rows (nr 50)
for index, row in data.iterrows():
    start11 = row['start50']
    dest11 = row['destination50']
    route11, dist_calc11 = get_route_and_distance(start11, dest11)
    print(route11, dist_calc11)
    routes11.append(route11)
    distances11.append(dist_calc11)


### 4. save results in distance column of new data frame
    
my_df = pandas.DataFrame({
        # trip nr 1
        "route1": routes1,
        "distance1": distances1,
        
        # trip nr 2
        "route2": routes2,
        "distance2": distances2,
        
        # trip nr 3
        "route3": routes3,
        "distance3": distances3,
        
        # trip nr 4
        "route4": routes4,
        "distance4": distances4,        
        
        # trip nr 5                  
        "route5": routes5,
        "distance5": distances5,
        
        # trip nr 6                 
        "route6": routes6,
        "distance6": distances6,
        
        # trip nr 7                
        "route7": routes7,
        "distance7": distances7,
                          
        # trip nr 8               
        "route8": routes8,
        "distance8": distances8,
                          
        # trip nr 9              
        "route9": routes9,
        "distance9": distances9,
                          
        # trip nr 10             
        "route10": routes10,
        "distance10": distances10,
        
        # trip nr 11           
        "route11": routes11,
        "distance11": distances11,
        
        # trip nr 12           
        "route12": routes12,
        "distance12": distances12,
        
        # trip nr 13           
        "route13": routes13,
        "distance13": distances13,
        
        # trip nr 14           
        "route14": routes14,
        "distance14": distances14,
        
        # trip nr 15           
        "route15": routes15,
        "distance15": distances15,
        
        # trip nr 16           
        "route16": routes16,
        "distance16": distances16,
        
        # trip nr 17           
        "route17": routes17,
        "distance17": distances17,
        
        # trip nr 18          
        "route18": routes18,
        "distance18": distances18,
        
        # trip nr 19           
        "route19": routes19,
        "distance19": distances19,
        
        # trip nr 20           
        "route20": routes20,
        "distance20": distances20,
        
        # trip nr 21           
        "route21": routes21,
        "distance21": distances21,
        
        
        # trip nr 26           
        "route26": routes26,
        "distance26": distances26,
        
        # trip nr 27           
        "route27": routes27,
        "distance27": distances27,
        
        # trip nr 28           
        "route28": routes28,
        "distance28": distances28,
        
        # trip nr 29           
        "route29": routes29,
        "distance29": distances29,
        
        # trip nr 30           
        "route30": routes30,
        "distance30": distances30,
        
        # trip nr 31           
        "route31": routes31,
        "distance31": distances31,
        
        # trip nr 32           
        "route32": routes32,
        "distance32": distances32,
        
        # trip nr 33           
        "route33": routes33,
        "distance33": distances33,
        
        # trip nr 34           
        "route34": routes34,
        "distance34": distances34,
        
        # trip nr 35           
        "route35": routes35,
        "distance35": distances35,
        
        # trip nr 36           
        "route36": routes36,
        "distance36": distances36,
        
        # trip nr 37           
        "route37": routes37,
        "distance37": distances37,
        
        # trip nr 38          
        "route38": routes38,
        "distance38": distances38,
        
        # trip nr 39           
        "route39": routes39,
        "distance39": distances39,
        
        # trip nr 40        
        "route40": routes40,
        "distance40": distances40,
        
        # trip nr 41           
        "route41": routes41,
        "distance41": distances41,
        
        # trip nr 42           
        "route42": routes42,
        "distance42": distances42,
        
        # trip nr 43           
        "route43": routes43,
        "distance43": distances43,
        
        # trip nr 44           
        "route44": routes44,
        "distance44": distances44,
        
        # trip nr 45          
        "route45": routes45,
        "distance45": distances45,
        
        # trip nr 46           
        "route46": routes46,
        "distance46": distances46,
        
        # trip nr 47           
        "route47": routes47,
        "distance47": distances47,
        
        # trip nr 48           
        "route48": routes48,
        "distance48": distances48,
        
        # trip nr 49           
        "route49": routes49,
        "distance49": distances49,
        
        # trip nr 50           
        "route50": routes50,
        "distance50": distances50,
                          })

print(my_df)   

# 5. convert pandas df into csv file
my_df.to_csv('flight_data_1.csv', sep=',', index=False, encoding='utf-8')

# check
data = pandas.read_csv('flight_data_1.csv', sep=',', na_values=".")
print(data)    

