#!/usr/bin/env python3
import sys
import math

fp= open("rgcinput.txt","r")
data= fp.readline().strip()
fp.close()
width=25
height=6
ones=0
twos=0
layers=int(len(data)/(height*width))
best=[0,0,0,0,0,0,0,0,0,0]
for l in range(layers):
	count=[0,0,0,0,0,0,0,0,0,0]
	for h in range(height):
		for w in range(width):
			pos=l*(height*width)+h*width+w
			num= int(data[pos])
			count[num]+= 1
	if best[0] == 0 or best[0] > count[0]:
		best= count.copy()
print("Part 1",best[1]*best[2])

for h in range(height):
	for w in range(width):
		#for l in range(layers-1,-1,-1):
		for l in range(layers):
			pos=l*(height*width)+h*width+w
			num= int(data[pos])
			if num == 1 or num == 0:
				print(num,end='')
				break
	print()
				
