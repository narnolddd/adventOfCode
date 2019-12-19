#!/usr/bin/env python3
import sys,math,numpy
from itertools import permutations 

def keystolets(keys):
    string=""
    for i in range(len(keys)):
        if keys[i]:
            string= string+keylet(i)
    return string

def getstartpos(startx,starty,q):
    x=startx
    y=starty
    if q == 0:
        x+=1
        y+=1
    elif q == 1:
        x-=1
        y+=1
    elif q == 2:
        x+=1
        y-=1
    else:
        x-=1
        y-=1
    return(x,y)

def keynum (key):
    return ord(key)-ord('a')

def keylet (keynum):
    alpha="abcdefghijklmnopqrstuvwxyz"
    return alpha[keynum]

def explore(maze,x,y):
    toexplore=[(x,y,0,[],[])]
    explored=[]
    keyset={}
    while len(toexplore) > 0:
        (x,y,steps,doors,keys)= toexplore.pop()
        #print(x,y)
        explored.append((x,y))
        if str.islower(maze[y][x]):
            keyset[maze[y][x]]= (steps,doors,keys)
            keys=keys.copy()
            keys.append(maze[y][x])
        if str.isupper(maze[y][x]):
            doors=doors.copy()
            doors.append(str.lower(maze[y][x]))
        for dirn in range(4):
            if dirn == 0:
                dx=0
                dy=1
            elif dirn == 1:
                dx=0
                dy=-1
            elif dirn == 2:
                dx=1
                dy=0
            else:
                dx=-1
                dy=0
            if (maze[y+dy][x+dx] != '#') and ((x+dx,y+dy)) not in explored:
                toexplore.append((x+dx,y+dy,steps+1,doors,keys))
    return keyset
    
if len(sys.argv) != 2:
    print("Enter input file name as CLI")
    sys.exit()
fp= open(sys.argv[1],"r")
maze= fp.readlines()
maxx=len(maze[0])-1
maxy=len(maze)
startx=0
starty=0
keys=[]
keylocs={}
for y in range(maxy):
    for x in range(maxx):
        if maze[y][x] == '@':
            startx=x
            starty=y
        elif str.islower(maze[y][x]):
            keys.append(maze[y][x])
            keylocs[maze[y][x]]=(x,y)    
x=startx
y=starty
numkeys= len(keys)
keys.sort()
maze[y-1]=maze[y-1][0:x-1]+".#."+maze[y-1][x+2:]
maze[y+1]=maze[y+1][0:x-1]+".#."+maze[y+1][x+2:]
maze[y]=maze[y][0:x-1]+"###"+maze[y][x+2:]
#for m in maze:
#    print(m,end="")
startkeysets=[]
#dictionary which quarter is key in
wherekeys={}
#list list of keys in quarter
keyrange=[[],[],[],[]]
keymap={}
for q in range(0,4):
    (x,y)=getstartpos(startx,starty,q)
    kdists= explore(maze,x,y)
    for k in kdists:
        wherekeys[k[0]]= q
        keyrange[q].append(k[0])
        keymap[('@',k)]=kdists[k]
    startkeysets.append(kdists)
#map of distance from key pair to key pair with steps and dist

for q in range(0,4):
    keyset=startkeysets[q]
    for k1 in keyset:
        (x,y)=keylocs[k1]
        kdists=explore(maze,x,y)
        for k2 in kdists:
            if (k1 == k2):
                continue
            keymap[(k1,k2)]= kdists[k2]
#print(keymap)
keysgot=[0]*numkeys
toExplore=[(0,"@@@@",keysgot,"")]
bestkeysgot=0

# blocked={}
test="ehiabcdfgkjlnmo"
loc="@@@@"
steps=0
bestkeysgot=0
while(True):
    (steps,loc,keysgot,order)=toExplore.pop(0)
    kg= sum(keysgot) 
    if kg == numkeys:
        break
    if kg > bestkeysgot:
        bestkeysgot= kg
        print("Got",kg,"from",numkeys,"steps",steps,"size",len(toExplore),order)
    counted= 0
    greedyi=0
    greedyicount=100000
    greedyorder=None
    greedykeys=None
    for i in range(numkeys):
        counted+=1
        if keysgot[i]:
            continue
        q=wherekeys[keylet(i)]
        newloc=loc[:q]+keylet(i)+loc[q+1:]
        journey=(loc[q],newloc[q])
        (dist,doors,keys)=keymap[journey]
        canOpen=True
        for d in doors:
            if keysgot[keynum(d)] == 0:
                canOpen= False
                break
        if not canOpen:
            continue
        if steps + dist < greedyicount:
            greedyicount= steps+dist
            greedyi= i
            greedyorder=order+keylet(i)
            greedykeys=keysgot.copy()
            greedykeys[i]=1
            greedyloc= newloc
    toExplore=[(greedyicount,greedyloc,greedykeys,greedyorder)]
        
       
greedysteps=steps
print("Greedy count",greedysteps)
oldsteps= 0    
keysgot=[0]*numkeys
explored={}
toExplore={}
toExplore[("@@@@","")]=(0,"")
loc="@@@@"
steps=0
bestkeysgot=0
laststeps=0
while(True):
    bestkey=None
    beststeps= 1000000
    for k in toExplore:
        (s,order)=toExplore[k]
        #print("Steps",s,"order",order)
        if s < beststeps:
            beststeps=s
            bestkey=k
    if (bestkey == None):
        print("Oh oh dead end")
        print(toExplore)
        sys.exit()
    (loc,order)=bestkey
    (steps,unorder)=toExplore.pop(bestkey)
    assert steps >= laststeps
    laststeps=steps
    kg= len(order) 
    #print(loc,kg)
    explored[(loc,order)]=True
    if kg == numkeys:
        break
    if kg > bestkeysgot:
        bestkeysgot= kg
        print("Got",kg,"from",numkeys,"steps",steps,"size",len(toExplore),order)
    counted= 0
    for i in range(numkeys):
        kl= keylet(i)
        counted+=1
        if kl in order:
            #print(kl," in ",order)
            continue
        q=wherekeys[kl]
        newloc=loc[:q]+keylet(i)+loc[q+1:]
        #print(newloc)
        neworder=''.join(sorted(order+kl))
        newunorder=unorder+kl
        assert len(neworder) == len(newunorder)
        #print(neworder," [",newsorder,"]")
        beenHere= False
        try:
            explored[(newloc,neworder)]
            #print("Explored",newloc,neworder)
            beenHere=True
        except:
            beenHere=False
        if beenHere:
            continue
        journey=(loc[q],newloc[q])
        (dist,doors,keys)=keymap[journey]
        newSteps=steps+dist
        #if newSteps > greedysteps:
        #    print("Greedy")
        #    continue
        canOpen=True
        for d in doors:
            if not d in neworder:
                canOpen= False
                break
        if not canOpen:
            continue
        gotKey=False
        for k in keys:
            if not k in neworder:
                gotKey=True
                break
        if gotKey:
            continue
                
        try:
            (oldSteps,oldunorder)= toExplore[(newloc,neworder)]
            if newSteps < oldSteps:
                toExplore[(newloc,neworder)]=(newSteps,newunorder)
        except:
            toExplore[(newloc,neworder)]=(newSteps,newunorder)


    assert counted == numkeys
print(steps,order)


