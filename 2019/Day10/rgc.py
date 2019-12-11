#!/usr/bin/env python3
import sys
import math

def calcRoids(x,y,data,height,width):

	#get ones exactly in line
	astList=[]
	for xStep in range(-width,width+1):
		for yStep in range(-height,height+1):
			if xStep == 0 and yStep == 0:
				continue
			if (math.gcd(xStep,yStep) != 1):
				continue
			xpos= x
			ypos= y
			while True:
				xpos+= xStep
				ypos+= yStep
				if xpos >= width or ypos >= height or xpos < 0 or ypos < 0:
					break
				if data[ypos][xpos]=='#':
					astList.append((ypos,xpos))
					break
			
			
	return astList
			



fp= open("rgcinput.txt","r")
strings= fp.readlines()
fp.close()
height=len(strings)
width= len(strings[0].strip())
data = [0] * height
for i in range(height):
    data[i] = [0] * width
for y in range(height):
	for x in range(width):
		data[y][x]= strings[y][x]
best= 0
bestx= 0
besty= 0
for x in range(width):
	for y in range(height):
		if data[y][x]!='#':
			continue
		astList= calcRoids(x,y,data,height,width)
		nMon= len(astList)
		if nMon > best:
			best= nMon
			bestx= x
			besty= y
print("Part 1",best)

count= 0
while True:
	for xStep in range(0,width):
		for yStep in range(-height,0):

			if xStep == 0 and yStep != -1:
				continue
			if (math.gcd(xStep,yStep) != 1):
				continue
			x= bestx
			y= besty
			while True:
				x+= xStep
				y+= yStep
				if x >= width or y >= height or x < 0 or y < 0:
					break
				if data[y][x] == '#':
					count+= 1
					data[y][x]='.'
					print("Vaporise",y,x)
					print(count)
