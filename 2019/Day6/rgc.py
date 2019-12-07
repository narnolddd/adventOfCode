#!/usr/bin/env python3
import sys
import math
fp= open("rgcinput.txt","r")
lines= fp.readlines()
planets= 0
orbits={}
orbitcount={}
for l in lines:
	p=l.split(")")
	left= p[0].strip()
	right= p[1].strip()
	orbits[right]= left
	#print(right,orbits[right])
	planets+= 1
	orbitcount[left]= 0
	orbitcount[right]= 0
for p in orbits:
	planet=p.strip()
	orbitcount[planet]= orbitcount[planet]+1
totorbits= 0
#print(orbitcount["COM"])
for p in orbitcount:
	#print ("Go ",p)
	tot=0
	planet= p.strip()
	#print(planet,type(planet))
	while orbitcount[planet] != 0:
		tot+= 1
		planet= orbits[planet]
		#print(planet)
	#print(tot)
	totorbits+=tot
print("Part1",totorbits)
youpath=["YOU"]
planet="YOU"
while orbitcount[planet] != 0:
	planet= orbits[planet]
	youpath.append(planet)
sanpath=["SAN"]
planet="SAN"
while orbitcount[planet] != 0:
	planet= orbits[planet]
	sanpath.append(planet)
#print(youpath)
#print(sanpath)
for i in range(len(youpath)):
	try:
		ind= sanpath.index(youpath[i])
		print("Part2",i+ind-2)
		break
	except:
		continue
#print(sanpath)
fp.close()

	
