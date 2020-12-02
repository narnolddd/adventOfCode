#!/usr/bin/env python3 

letterPolicy = {}

def procInput(filename):
	global letterPolicy
	
	numValid1 = 0
	numValid2 = 0
	
	f = open(filename, 'r') 
	while True: 
		line = f.readline() 
		if not line:
			break
		
		cols = line.split(" ")
		boundaries = cols[0].split("-")
		
		min = int(boundaries[0])
		max = int(boundaries[1])
		letter = cols[1].replace(":","")
		password = cols[2]
		
		letterUsages = 0
		for char in password:
			if char == letter:
				letterUsages += 1
		
		if letterUsages >= min and letterUsages <= max:
			numValid1 += 1
		
		numValid2 += (password[min-1]==letter) != (password[max-1]==letter)
		
	return numValid1, numValid2


res1, res2 = procInput("input.txt")

print("ans1", res1)
print("ans2", res2)
