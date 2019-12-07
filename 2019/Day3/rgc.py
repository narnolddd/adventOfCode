#!/usr/bin/env python3
import sys
import math

def parseLine(steps):
	places=[(0,0)]
	x= 0
	y= 0
	for step in steps:
		#print(step)
		dirn=step[0]
		dist=int(step[1:])
		for n in range(dist):
			if dirn == "U":
				y+=1
			elif dirn == "D":
				y-=1
			elif dirn == "R":
				x+=1
			elif dirn == "L":
				x-=1
			else:
				print("Unknown dirn ",dirn)
				sys.exit()
			places.append((x,y))
	return places


try:
	fp= open("rgcinput.txt","r")
	w1= fp.readline()
	w2= fp.readline()
	w1pos= parseLine(w1.split(","))
	w2pos= parseLine(w2.split(","))
	#print(w1pos)
	#print(w2pos)
	bestx= 0
	besty= 0
	bestdist= 0
	#slow but quick to code
	w1dist= -1
	bestwiredist= 0
	for w in w1pos:	
		w1dist+=1
		try:
			w2dist= w2pos.index(w)
			(wx,wy)= w
			print ("Join at ",(wx,wy),(w1dist,w2dist))
			if wx == 0 and wy == 0:
				continue
			dist= (wx*wx) + (wy*wy)
			if bestdist == 0 or dist < bestdist:
				bestdist= dist
				bestx= wx 
				besty= wy
			if bestwiredist == 0 or (w1dist+w2dist) < bestwiredist:
				bestwiredist= w1dist+w2dist
				print ("Current best",bestwiredist)
		except:
			#print ("Could not find",w)
			continue
	print("Part 1",math.sqrt(bestx*bestx+besty*besty))
	print("Part 2",bestwiredist+1)
    
finally:
	fp.close()
