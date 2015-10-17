#The following piece of code processes the data taken from Nmap tool report. 
#It finds the total number of open ports found in each host and then 
#creates a dictionary containing the name of the port and its appearance frequency. 
#Finally it calculates the most frequently open ports and plots them in a pie chart.

from __future__ import division
from libnmap.parser import NmapParser
from libnmap.process import NmapProcess
import operator
from matplotlib import pyplot as plt
import numpy as np
from utilities import *

#Passing the data of the Nmap report to variable nmap_report
nmap_report = NmapParser.parse_fromfile('/home/user/Desktop/Okeanos_Nmap/11-11-2014.xml')
hosts = nmap_report.hosts
 
open_ports_number = 0
open_ports_final = []
for host in hosts:
	open_ports = host.get_open_ports()
	open_ports_number += len(open_ports) #finally has the total number of open ports
	open_ports_final += open_ports #finally has the total list of open ports

#Creating dictionary containing the name of the port and its appearance frequency
unique_open_ports = find_unique(open_ports_final)
port_results = find_max(unique_open_ports)
max_ports = port_results[0]
max_value = port_results[1]

#Transforming the max_value into percentage for statistical use
N = 5
top_N_ports = []
top_N_values = []
total_max_value_percent = []
for s in range(N):
	top_N_ports.append(max_ports[s])
	top_N_values.append(max_value[s])
	max_value_percent = (top_N_values[s]/open_ports_number)*100
	total_max_value_percent += [max_value_percent]

rest_open_ports = ((open_ports_number-sum(top_N_values))/open_ports_number)*100
total_max_value_percent = total_max_value_percent+[rest_open_ports]

#Labeling and coloring of the pie chart
labels = top_N_ports+['Other']
colors = ['yellowgreen', 'lightcoral', 'gold', 'lightskyblue','violet', 'lightgrey']
explode = (0, 0, 0, 0, 0, 0) #no offsetting of slice

#Ploting the pie chart
plt.pie(total_max_value_percent, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False)
plt.axis('equal') # Set aspect ratio to be equal so that pie is drawn as a circle
plt.show()



