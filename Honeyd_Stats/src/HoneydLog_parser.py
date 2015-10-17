#The following piece of code processes the data taken from HoneyBot log file. It finds the number of attacked ports (source_ports) of each host, the number of attacker ips (dest_ips) and the number of attacker countries. 

import requests
from Honeyd_utilities import *
from geoip import geolite2
from mpl_toolkits.basemap import Basemap
import operator
from matplotlib import pyplot as plt
import numpy as np



logs = open('Honeyd_Log.out')

c = 0 #key of dictionary that contains the id of each variable (e.g. date, source_ip, line)
tool = dict()  #name of the dixtionary


date = []
prot = []
t = []
source_ip = []
source_port = []
dest_ip = []
dest_port = []
for line in logs:
	if line.find('------')==-1:  #exclude first and last line that contain no useful info
		fields = line.split(' ') #Parcing the fields of every line
		date.append('-'.join(fields[0].split('-')[0:3]))
		prot.append(fields[1])
		t.append(fields[2])
		source_ip.append(fields[3])
		if prot[-1]!="icmp(1)": # exclude icmp packets 
			source_port.append(fields[4])
			dest_ip.append(fields[5])
			pointer = str(fields[6]).find(":") # editing the format of fields[6] elements
			fields[6] = str.replace(str(fields[6]), "\n", "")
			if pointer!=-1:
				dest_port.append(str(fields[6])[0:pointer])
			else:
				dest_port.append(str(fields[6]))

		
#Finding unique destination ports and their appearance frequency
dictionary_of_dest_ports = find_unique(dest_port)
port_results = find_max(dictionary_of_dest_ports)
max_unique_ports = port_results[0]
max_unique_port_value = port_results[1]


#Finding unique source ips and their appearance frequency
dictionary_of_source_ip = find_unique(source_ip)
ip_results = find_max(dictionary_of_source_ip)
max_unique_ips = ip_results[0]
max_unique_ip_value = ip_results[1]


#Finding geolocation of each source ip and each country's appearance frequency
max_unique_ips = map(str, max_unique_ips)
country_name = []
for country in max_unique_ips:
	if country!='0':  
		ip_info = geolite2.lookup(country)
		if ip_info!=None: #Avoiding zero entries
			country_name.append(ip_info.country)

unique_countries = find_unique(country_name)
countries_results = find_max(unique_countries)
max_unique_countries = countries_results[0]
max_unique_country_value = countries_results[1] 


#Draw the most attacking country on map
print draw_map(countries_results)

"""#Dictionary format for use in ASPIDA Tool	
		tool.update({ (c,'date'): date,
		(c,'source_ip'): source_ip,
		(c,'destination_ip'): dest_ip, 
		(c,'raw'): line
		})
		c+=1
#Connection with the REST API of ASPIDA Tool
r = requests.post("url", params=tool) #Response object"""

