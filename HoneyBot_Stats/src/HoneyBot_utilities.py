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


