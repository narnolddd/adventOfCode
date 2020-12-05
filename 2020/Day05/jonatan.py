#!/usr/bin/env python3

def strToInt(string):
	string = string.replace("F","0")
	string = string.replace("B","1")
	string = string.replace("L","0")
	string = string.replace("R","1")
	return int(string,2)

def procList(filename):
	allEntries = {}
	topRow = 0
	botRow = 42069
	
	f = open(filename, 'r') 
	while True: 
		line = f.readline().replace("\n","")
		if not line:
			break
		seatID = strToInt(line)
		allEntries[seatID]=None
	
	print("Max seat ID: %i" %max(allEntries))
	
	for seatID in range(min(allEntries), max(allEntries)+1):
		if seatID in allEntries:
			continue
		row = seatID>>3
		col = seatID&0b0000000111
		print("My seat! ID:%i, row:%i, col:%i" %(seatID, row, col))
	
procList("input_jonatan.txt")
