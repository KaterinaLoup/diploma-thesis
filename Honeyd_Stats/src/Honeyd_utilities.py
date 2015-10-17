from __future__ import division
import operator

#This function takes as input a list of elements and gives back a dictionary with the rate of appearance of each unique element 
def find_unique(list_of_elements):

	unique_elements = set(list_of_elements) #find unique elements
	value_per_element = dict()
#Dictionary initialization 	
	for k in unique_elements:
		value_per_element[k] = 0

#The number of times each unique element has been found in the list is stored in the dictionary 
	for unique_element in unique_elements:
		for element in list_of_elements:
			if element == unique_element:
				value_per_element[element]+=1
	return value_per_element



#This function takes as input the return of the "find_unique" function and returns the unique elements with their max value
def find_max(dictionary_of_elements):
	
#Finding most frequently occurring elements and their appearance value
	max_unique_elements = []
	max_unique_value = []

	results = sorted(dictionary_of_elements.items(), key=operator.itemgetter(1), reverse=True)

	for i in range(len(dictionary_of_elements)):
		max_unique_elements.append(results[i][0])	
		max_unique_value.append(results[i][1])

	return [max_unique_elements, max_unique_value]

#This function takes an input a list of countries with the major frequency appearance and prints a map with them
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

def draw_map(countries_results):
	# Open the data file containing countries' latitudes and  longitudes
	data_file = open('country_latlon.csv')

	#Creation of a dictionary with these data
	world = dict()

	for line in data_file.readlines():
		fields = line.split(',')	
		world[fields[0]] = (fields[1], fields[2].strip())
	
	# Store the latitudes, longitudes and the frequency appearance of each country in the appropriate lists
	N = 8 #The number of countries that are going to printed on the map
	lons = []
	lats = []
	attacks_size = []
	for i in range(N):
		lats.append(float(world[countries_results[0][i]][0]))
		lons.append(float(world[countries_results[0][i]][1]))
		attacks_size.append(countries_results[1][i]/sum_countries)
	sum_countries = sum(countries_results[1])

	# --- Build Map ---
	worldmap = Basemap(projection='mill', resolution = 'i', area_thresh = 100000.0, lat_0=0, lon_0=0)
	worldmap.drawcoastlines(color = 'ForestGreen')
	worldmap.drawcountries(linewidth =1, color = 'ForestGreen')
	worldmap.drawmapboundary(fill_color = 'Snow')
	worldmap.drawrivers(color = 'Snow')
	worldmap.fillcontinents(color = 'Snow', lake_color='Snow')
 
	n = 0
	for lon, lat, attack in zip(lons, lats, attacks_size):
		if attack>0.1:
			n=20
		else:
			n=10
	
		x,y = worldmap(lon, lat)
		worldmap.plot(x, y, 'ro', markersize = n)	
	plt.show()
	return

