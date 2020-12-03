#!/usr/bin/env python3 

world = []

tree = "#"
free = "."

def readWorld(filename):
	global world #It sure is
	
	f = open(filename, 'r') 
	while True: 
		line = f.readline() 
		if not line:
			break
		
		
		line = line.replace("\n","")
		world.append(line)

def countTreeCollisions(stepx, stepy):
	treeCount = 0
	width = len(world[0])
	height = len(world)
	
	posx = 0
	posy = 0
	
	while True:
		posx += stepx
		posy += stepy
		posx %= width
		
		if posy >= height:
			break
		
		if world[posy][posx] == tree:
			treeCount += 1
	
	return treeCount


readWorld("input.txt")

num = countTreeCollisions(3,1)

print("ans1: %i" %num)


dances = [(1,1),(3,1),(5,1),(7,1),(1,2)]

product = 1 #product identity. Let's assume at least one dance
for stepx,stepy in dances:
	product *= countTreeCollisions(stepx,stepy)
print("ans2: %i" %product)
