#This function takes as input a list of elements and gives back a dictionary with the rate of appearence    of each unique element 


def find_unique(list_of_elements):
#find unique elements
	unique_elements = set(list_of_elements)
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


