#!/usr/bin/env python3
import sys,math,numpy
from itertools import permutations 

def evalOrder(keyorder,startList,keyDict):
    totsteps=0
    keys=[]
    kprev=None
    for dest in keyorder:
        if kprev == None:
            dists=startList
        else:
            dists=keyDict[kprev]
        for d in dists:
            (key,steps,doors)=d
            if key != dest:
                continue
            for d in doors:
                if d not in keys:
                    return 0
            totsteps+= steps
            break
        kprev= dest
        keys.append(dest)
    return totsteps
        

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

fp= open("rgcinput.txt","r")
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
#print(startList)
print ("Done!")
travel=[]
#(key,steps,keys)
for s in startList:
    if len(s[2]) == 0:
        travel.append((s[0],s[1],[]))
    
keydict={}
for k in keys:
    kl=explore(maze,k[1],k[2])
    assert len(kl) == len(keys)
    keydict[k[0]]=kl
print("Done")
print(travel)
keyorder=[]
totsteps=0
while True:
    bestst=1000000
    best=0
    for j in range(len(travel)):
        (k,steps,doors)=travel[j]
        if steps < bestst:
            bestst= steps
            best=j
            #print(travel,best)
    (k,steps,newkeys)=travel[best]
    keyorder.append(k)
    #print(keyorder,keys)
    totsteps+=steps
    travel=[]
    if len(keyorder) == len(keys):
        break
    newkeys=keydict[k]
    for nk in newkeys:
        (k,steps,doors)=nk
        if k in keyorder:
            continue
        canDo= True
        for d in doors:
            if d not in keyorder:
                canDo= False
                break
        if canDo:
            travel.append((k,steps,doors))
bestgreedy=evalOrder(keyorder,startList,keydict)
print("Greedy solution beststeps: ",bestgreedy)

travel=[]
#(key,steps,doors)
for s in startList:
    if len(s[2]) == 0:
        travel.append((s[0],s[1],[],[]))
# for k in keydict:
    # print (str(chr(k)),end=":")
    # for k1 in keydict[k]:
        # print(str(chr(k1[0])),k1[1],end = " Doors:[")
        # for k2 in k1[2]:
            # print(str(chr(k2)),end="")
        # print("] ",end="")
    # print()
# print(travel)
keyorder=[]
keysets={}
bestkeylen=0  
path=[]    
while True:
    (k,stepssofar,keysorted,keyunsorted)=travel.pop(0)
    try:
        ks=keysets[k]
        if (keysorted in ks):
            continue
        ks.append(keysorted)
        #print(ks)
    except:
        keysets[k]=[keysorted]
    if len(keysorted)+1 == len(keys):
        path=keyunsorted
        path.append(k)
        beststeps= stepssofar
        break
    if len(keysorted)+1 > bestkeylen:
        bestkeylen=len(keysorted)+1
        print("Keys",bestkeylen," from ",len(keys), " set len ",len(travel))
    kl= keydict[k]
    keyunsorted=keyunsorted.copy()
    keyunsorted.append(k)
    keysorted=keyunsorted.copy()
    keysorted.sort()
    for kl1 in kl:
        (nk,steps,doors)= kl1
        if nk in keysorted:
            continue
        canOpen=True
        for d in doors:
            if d not in keysorted:
                canOpen= False
                break
        if not canOpen:
            #print("Can't open",doors,"with",keyorder)
            continue
        if stepssofar+steps > bestgreedy:
            continue
        inserted=False
        for i in range(0,len(travel)):
            if stepssofar+steps <= travel[i][1]:
                travel.insert(i,(nk,stepssofar+steps,keysorted,keyunsorted))
                inserted= True
                break
        if not inserted:
            travel.append((nk,stepssofar+steps,keysorted,keyunsorted))
        
for k in path:
    print(str(chr(k)),end=" ")
print("Steps= ",beststeps)
