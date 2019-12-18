#!/usr/bin/env python3
import sys,math,numpy
from itertools import permutations 

def isDoor(x):
#    print(str(x))
    if str.isupper(str(chr(x))):
        return True
    return False
    
def isKey(x):
    if str.islower(str(chr(x))):
        return True
    return False

def checkSquare(maze,x,y):
    if maze[x][y] == ord('#'):
        return False
    return True
    

#dirn 1=N,2=E,3=S,4=W
def explore(maze,x,y):
    toExplore=[(x,y,0,0,[])]
    keyList=[]
    explored=[]
    while len(toExplore) != 0:
        (x,y,dirn,steps,doors)=toExplore.pop(0)
        explored.append((x,y))
        if isKey(maze[x][y]):
            found= False
            for k in keyList:
                if k[0] == maze[x][y]:
                    found=True
                    break
            if not found:
                keyList.append((maze[x][y],steps,doors))
            #print(keyList)
       # print("Checking ",x,y,dirn,keys,steps)
        if isDoor(maze[x][y]):
            doors=doors.copy()
            doors.append((ord(str.lower(str(chr(maze[x][y]))))))
        if (dirn !=3) and checkSquare(maze,x,y-1) and (x,y-1) not in explored:
            toExplore.append((x,y-1,1,steps+1,doors))
        #EAST
        if (dirn != 4) and checkSquare(maze,x+1,y) and (x+1,y) not in explored:
            toExplore.append((x+1,y,2,steps+1,doors))
        #SOUTH
        if (dirn != 1) and checkSquare(maze,x,y+1) and (x,y+1) not in explored:
            toExplore.append((x,y+1,3,steps+1,doors))
        #WEST
        if (dirn != 2) and checkSquare(maze,x-1,y) and (x-1,y) not in explored:
            toExplore.append((x-1,y,4,steps+1,doors))
    return keyList

fp= open("rgctest.txt","r")
ls= fp.readlines()
maxx=len(ls[0])-1
maxy=len(ls)
maze=numpy.ones((maxx,maxy),dtype=int)
#print(maxx,maxy)
startx=0
starty=0
keys=[]
for y in range(maxy):
    l=ls[y]
    for x in range(maxx):
        if l[x] == '@':
            startx=x
            starty=y
            maze[x][y]= ord('.')
            continue
        if str.islower(l[x]):
            keys.append((ord(l[x]),x,y))
        maze[x][y]=ord(l[x])
        
startList=explore(maze,startx,starty)
print(startList)
print ("Done!")
travel=[]
for s in startList:
    if len(s[2]) == 0:
        travel.append((s[0],s[1],[]))
    
keydict={}
for k in keys:
    kl=explore(maze,k[1],k[2])
    assert len(kl) == len(keys)
    keydict[k[0]]=kl
print("Done")

