# lazy calculation of travel distances 

I have a csv data file containing survey answers about trips (city or country names of starting points and destinations)
For further statistical analyses I need the distances between start and destination in km.

I am too lazy to manually google all of those distances.

So, the idea is to import the csv file, to request the distances online, iterating over the rows of the csv file, and to save the distances in a new column of the file.

To develop the code, I use a very simple test file of 25 trips. 
