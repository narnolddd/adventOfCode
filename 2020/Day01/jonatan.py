#!/usr/bin/env python3

indata_filename = "indata.txt"

values = []

def readValuesFromFile(filename):
	result = []
	
	f = open(filename, 'r') 
	while True: 
		line = f.readline() 
		if not line:
			break
		value = int(line)
		result.append(value)
	return result
	
def getTwoAdditiveComponents(values, sum):
	#Assuming that there are no duplicates which sum to sum
	for v1 in values:
		for v2 in values:
			if v1 + v2 == sum:
				return v1,v2
	return None

def getThreeAdditiveComponents(values, sum):
	#Assuming that there are no duplicates which sum to sum
	for v1 in values:
		for v2 in values:
			for v3 in values:
				if v1 + v2 + v3 == sum:
					return v1,v2,v3
	return None

values = readValuesFromFile(indata_filename)
print("values", values)

v1,v2 = getTwoAdditiveComponents(values, 2020)
print("v1,v2", v1,v2)

answer1 = v1*v2
print("v1*v2", answer1)

v1,v2,v3 = getThreeAdditiveComponents(values, 2020)
print("v1,v2,v3", v1,v2,v3)

answer2 = v1*v2*v3
print("v1*v2*v3", answer2)
