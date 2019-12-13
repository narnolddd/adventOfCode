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
print("Part 1",best, bestx,besty)

count= 0
angles=[]
coords=[]
for x in range(0,width):
    for y in range(0,height):
        if data[y][x] != '#':
            continue
        if x == bestx and y == besty:
            continue
        angle= math.atan2(x-bestx,besty-y)/math.pi*180
        if angle< 0:
            angle+=360
        #print (x,y,angle)
        try:
            i= angles.index(angle)
            coords[i].append((x,y))
        except:
            angles.append(angle)
            coords.append([(x,y)])
        
angle= -1.0
best= angle
count= 0
while True:
    best= -1
    besti= 0
    for i in range(len(angles)):
        if len(coords[i]) == 0:
            continue
        if angles[i] > angle and (best == -1 or angles[i] < best):
            best= angles[i]
            besti=  i
    if best == -1:
        angle=-1
        continue
    angle=best
    closest= 0
    closestdist= (bestx-coords[besti][0][0])*(bestx-coords[besti][0][0]) \
        + (besty-coords[besti][0][1])*(besty-coords[besti][0][1])
    for i in range(1,len(coords[besti])):
        dist= (bestx-coords[besti][i][0])*(bestx-coords[besti][i][0]) \
            + (besty-coords[besti][i][1])*(besty-coords[besti][i][1])
        if (dist < closestdist):
            closestdist= dist
            closest= i
    
    count+=1
# print (count,"Eliminating", best, besti, coords[besti][closest])
    if count == 200:
        print (count,"Eliminating", coords[besti][closest])
        break
    coords[besti].pop(closest)
    
