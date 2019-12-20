#!/usr/bin/env python3
import sys,math,numpy
from itertools import permutations 

def finddot(maze,x,y):
    dotloc=None
    lett=None
    for move in [(-1,0),(1,0),(0,1),(0,-1)]:
        nx=x+move[0]
        ny=y+move[1]
        if maze[ny][nx] == '.':
            dotloc=(nx,ny)
        if str.isupper(maze[ny][nx]):
            lett= maze[ny][nx]
    if dotloc == None or lett == None:
        return (None,None)
    return (dotloc,maze[y][x]+lett)
            
def exploreMaze(maze,teleports,startloc,endloc):
    toExplore=[(startloc[0],startloc[1],0)]
    explored=[]
    while True:
        (x,y,steps)=toExplore.pop(0)
        explored.append((x,y))
        #print(explored)
        if (x,y) in teleports:
            (tx,ty)= teleports[(x,y)][0]
            if (tx,ty) == endloc:
                return steps+1
            toExplore.append((tx,ty,steps+1))
        for move in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx=x+move[0]
            ny=y+move[1]
            #print("Testing",nx,ny)
            if (nx,ny) == endloc:
                return steps+1
            if maze[ny][nx] == '.' and (nx,ny) not in explored:
                #print("Exploring",nx,ny)
                toExplore.append((nx,ny,steps+1))

def exploreRecursiveMaze(maze,teleports,startloc,endloc):
    toExplore=[(startloc[0],startloc[1],0,0)]
    explored=[]
    while True:
        (x,y,level,steps)=toExplore.pop(0)
        assert level >= 0
        assert maze[y][x] == '.'
        explored.append((x,y,level))
        if (x,y) in teleports:
            ((tx,ty),isinner)= teleports[(x,y)]
            if (tx,ty) == endloc and level == 0:
                print("Won via teleport")
                return steps+1
            if isinner and (tx,ty,level+1) not in explored:
                toExplore.append((tx,ty,level+1,steps+1))
            elif (level > 0) and (tx,ty,level-1) not in explored:
                toExplore.append((tx,ty,level-1,steps+1))
        for move in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx=x+move[0]
            ny=y+move[1]
            #print("Testing",nx,ny)
            if (nx,ny) == endloc and level == 0:
                return steps+1
            if maze[ny][nx] == '.' and (nx,ny,level) not in explored:
                #print("Exploring",nx,ny)
                toExplore.append((nx,ny,level,steps+1))     
                

if len(sys.argv) != 2:
    print("Enter input file name as CLI")
    sys.exit()
fp= open(sys.argv[1],"r")
maze= fp.readlines()
fp.close()

yr=len(maze)
xr=len(maze[0])-1

endloc=None
startloc=None
lettpairs={}
for x in range(1,xr-1):
    for y in range(1,yr-1):
        if str.isupper(maze[y][x]):
            (loc,letts)= finddot(maze,x,y)
            if (loc !=None):
                if letts in lettpairs:
                    letts=letts[1]+letts[0]
                lettpairs[letts]= loc
#print(lettpairs)
teleports={}
for l in lettpairs:
    if l == "AA":
        startloc= lettpairs[l]
    elif l == "ZZ":
        endloc= lettpairs[l]
    else:
        (x,y)= lettpairs[l]
        # Identify outer
        if (x <= 2) or (y<=2) or (x>=xr-3) or (y>=yr-3): 
            teleports[lettpairs[l]]=(lettpairs[l[1]+l[0]],False)
            #print(x,y,"is outer")
        else:
            teleports[lettpairs[l]]=(lettpairs[l[1]+l[0]],True)
            #print(x,y,"is inner")
#print(startloc,endloc)
print("Part 1",exploreMaze(maze,teleports,startloc,endloc))

print("Part 2",exploreRecursiveMaze(maze,teleports,startloc,endloc))
