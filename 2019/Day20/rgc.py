#!/usr/bin/env python3
import sys,math,numpy
from itertools import permutations 
import networkx
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

def getMazeLink(maze,teleports,startloc,endloc):
    #print("Explore",startLoc,endLoc)
    links=[]
    explored=[]
    toExplore=[(startloc[0],startloc[1],0)]
    while len(toExplore) != 0:
        (sx,sy,steps)=toExplore.pop(0)
        assert maze[sy][sx] == '.'
        explored.append((sx,sy))
        if (sx,sy) == endloc:
            links.append((startloc,endloc,False,steps))
            continue
        elif (sx,sy) in teleports and (sx,sy) != startloc:
            links.append((startloc,teleports[(sx,sy)][0],teleports[(sx,sy)][1],steps+1))
            #print((startLoc,teleports[(x,y)][0],teleports[(x,y)][1],steps+1))
            continue
        for move in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx=sx+move[0]
            ny=sy+move[1]
            if maze[ny][nx] == '.' and (nx,ny) not in explored:
                #print("Exploring",nx,ny)
                toExplore.append((nx,ny,steps+1))
            #print("Testing",nx,ny)
    return(links)


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
loc_look={}
for x in range(1,xr-1):
    for y in range(1,yr-1):
        if str.isupper(maze[y][x]):
            (loc,letts)= finddot(maze,x,y)
            if (loc !=None):
                if letts in lettpairs:
                    letts=letts[1]+letts[0]
                lettpairs[letts]= loc
                loc_look[loc]=letts
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

links= getMazeLink(maze,teleports,startloc,endloc)
for t in teleports:
    #print("Exploring",t)
    nl=(getMazeLink(maze,teleports,t,endloc))
    links+=nl
#print (links)
g=networkx.Graph()
for l in links:
    #print(l)
    (sl,el,isInner,steps)=l
    g.add_edge((sl[0],sl[1]),(el[0],el[1]),weight= steps)
p=networkx.dijkstra_path_length(g,startloc,endloc,weight="weight")
print("Part 1",p)
maxlev=200
#guess
g=networkx.Graph()
#print("Find",(startloc[0],startloc[1],0),(endloc[0],endloc[1],0))
for lev in range(maxlev):
    for l in links:
        (sl,el,isInner,steps)=l
        if sl == startloc or el == endloc:
            if lev == 0:
                if el == endloc:
                    g.add_edge((sl[0],sl[1],0),(el[0],el[1],0),weight= steps)
                else:
                    g.add_edge((sl[0],sl[1],0),(el[0],el[1],1),weight= steps)
        elif isInner: 
            if lev < maxlev -1:
                g.add_edge((sl[0],sl[1],lev),(el[0],el[1],lev+1),weight= steps)
        elif lev > 0:
            g.add_edge((sl[0],sl[1],lev),(el[0],el[1],lev-1),weight= steps)   
dist=networkx.dijkstra_path_length(g,(startloc[0],startloc[1],0),(endloc[0],endloc[1],0),weight="weight")
#print("Find",(startloc[0],startloc[1],0),(endloc[0],endloc[1],0))
path=networkx.dijkstra_path(g,(startloc[0],startloc[1],0),(endloc[0],endloc[1],0),weight="weight")
print("Part 2",dist,path)
