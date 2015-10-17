#The following piece of code processes the data taken from HoneyBot log file. 
#It finds the number of attacked ports (source_ports) of each host, 
#the number of attacker ips (dest_ips) and the number of attacker countries. 

import csv
import sys
import operator
from matplotlib import pyplot as plt
import numpy as np
from geoip import geolite2
from HoneyBot_utilities import *
import copy

f = open('Log_20141124.csv', 'rt')
reader = csv.reader(f)

date = [0]
dest_ip = [0]
dest_port = [0]
source_ip = [0]
source_port = [0]
for row in reader:
	date.append(row[2])
	dest_ip.append(row[6])
	dest_port.append(row[7])
	source_ip.append(row[8])
	source_port.append(row[9])

#Finding unique source ports and their appearance frequency
dictionary_of_source_ports = find_unique(source_port)
port_results = find_max(dictionary_of_source_ports)
max_unique_ports = port_results[0]
max_unique_port_value = port_results[1]

#Finding unique destination ips and their appearance frequency
dictionary_of_dest_ip = find_unique(dest_ip)
ip_results = find_max(dictionary_of_dest_ip)
max_unique_ips = ip_results[0]
max_unique_ip_value = ip_results[1]

#Finding geolocation of each destination ip and each country's appearance frequency
max_unique_ips = map(str, max_unique_ips)
country_name = []
for c in max_unique_ips:
	if c!='0':
		ip_info = geolite2.lookup(c)
		if ip_info!=None: #Avoiding zero entries
			country_name.append(ip_info.country)
unique_countries = find_unique(country_name)
countries_results = find_max(unique_countries)
max_unique_countries = countries_results[0]
max_unique_country_value = countries_results[1]

print "The attacking countries are: "
print max_unique_countries
print "The appearence frequency of the attacks per country are: "
print max_unique_country_value

f.close()
