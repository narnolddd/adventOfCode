#!/usr/bin/env python3
import sys
import math
try:
	fp= open("input.txt","r")
	fuel= 0
	part1_fuel=0
	lines= fp.readlines()
	for l in lines:
		try:
			i= int(l.strip())
			new_fuel= math.floor(i/3)-2
			fuel+= new_fuel
			part1_fuel+= new_fuel
			while new_fuel >= 9:
				new_fuel= math.floor(new_fuel/3)-2
				fuel+= new_fuel
		except Exception as e: 
			print(str(e)+" Unexpected non int " + l)
			sys.exit()
	print(part1_fuel,fuel)
finally:
	fp.close()
