#!/usr/bin/env python3
import sys,math,numpy
from itertools import permutations 

def toFill(space):
    (xm,ym)=space.shape
    o2=numpy.where(space == 3)
    o2x=o2[0][0]
    o2y=o2[1][0]
    empty= 0
    for x in range(xm):
        for y in range(ym):
            if space[x][y] == 1:
                empty+=1
    x=o2x
    y=o2y
    visited=[(x,y)]
    toVisit=[(x,y-1),(x,y+1),(x+1,y),(x-1,y)]
    dist=0
    while True:
        newToVisit=[]
        for v in toVisit:
            x=v[0]
            y=v[1]
            visited.append((x,y))
            if space[x][y] == 1:
                add=[(x,y-1),(x,y+1),(x+1,y),(x-1,y)]
                for a in add:
                    if not a in visited and space[a[0]][a[1]] == 1:
                        newToVisit.append(a)
        toVisit=newToVisit
        dist+=1
        if len(newToVisit) == 0:
            break
    return dist

def solveMaze(space,x,y):
    visited=[(x,y)]
    toVisit=[(x,y-1),(x,y+1),(x+1,y),(x-1,y)]
    dist=1
    
    while True:
        newToVisit=[]
        for v in toVisit:
            x=v[0]
            y=v[1]
            visited.append((x,y))
            if space[x][y] == 3:
                return dist
            if space[x][y] == 1:
                add=[(x,y-1),(x,y+1),(x+1,y),(x-1,y)]
                for a in add:
                    if not a in visited:
                        newToVisit.append(a)
        toVisit=newToVisit
        dist+=1

#0=unknown
#1=empty
#2=wall
#3=O2
def printSpace(space):
    (xm,ym)=space.shape
    minx=xm
    maxx=0
    miny=ym
    maxy=0
    for x in range(xm):
        for y in range(ym):
            if space[x][y]!=0:
                if x > maxx:
                    maxx=x
                if y > maxy:
                    maxy=y
                if x < minx:
                    minx=x
                if y < miny:
                    miny=y
    for y in range(miny,maxy+1):
        for x in range(minx,maxx+1):
            c= space[x][y]
            if c == 0:
                print(" ",end="")
            elif c == 1:
                print(".",end="")
            elif c == 2:
                print("#",end="")
            elif c == 3:
                print("O",end="")
        print()

def getdirn(dirn):
    if dirn == 1:
        return(0,-1)
    if dirn == 2:
        return(0,1)
    if dirn == 3:
        return (1,0)
    if dirn == 4:
        return (-1,0)
    print("Unexpected direction")
    return (0,0)

def navSpace(xpos,ypos,space):
    explored=[]
    #print(space)
    toexplore=[(1,xpos,ypos-1),(2,xpos,ypos+1),(3,xpos+1,ypos),(4,xpos-1,ypos)]
    while len(toexplore) > 0:
        exp=toexplore.pop(0)
        nx=exp[1]
        ny=exp[2]
        if space[nx,ny] == 0:
            return exp[0]
        if space[nx,ny] == 1:
            explored.append((nx,ny))
            if not (nx,ny-1) in explored:
                toexplore.append((exp[0],nx,ny-1))
            if not (nx,ny+1) in explored:
                toexplore.append((exp[0],nx,ny+1))
            if not (nx+1,ny) in explored:
                toexplore.append((exp[0],nx+1,ny))
            if not (nx-1,ny) in explored:
                toexplore.append((exp[0],nx-1,ny))
    return 0

def calcVal(s,pos,mode,rbase):
    if mode == 0:
        return s[s[pos]]
    if mode == 1:
        return s[pos]
    if mode == 2:
        return s[rbase+s[pos]]
    print("Unknown mode",mode)
    sys.exit()

def putVal(s,pos,mode,rbase,val):
    if mode == 0:
        s[s[pos]]= val
        return
    if mode == 1:
        print("Mode 1 put should not happen")
        s[pos]= val
    if mode == 2:
        #print("Mode 2 put should not happen")
        s[rbase+s[pos]]= val
        return
    print("Unknown mode",mode)
    sys.exit()

def doMachine(s,space,xpos,ypos):
    output= []
    pos=0
    rbase=0
    dirn=1
    while(True):
        instr=s[pos]%100
        mode1= (int(s[pos]/100))%10
        mode2= (int(s[pos]/1000))%10
        mode3= (int(s[pos]/10000))%10
        #print(pos,s[pos],instr,mode1,mode2,mode3)
        if (instr == 99):
            return (output,xpos,ypos,space)
        elif (instr == 1): #add
            x=calcVal(s,pos+1,mode1,rbase)
            y=calcVal(s,pos+2,mode2,rbase)
            putVal(s,pos+3,mode3,rbase,x+y)            
            pos+=4
        elif (instr == 2): #mult
            x=calcVal(s,pos+1,mode1,rbase)
            y=calcVal(s,pos+2,mode2,rbase)
            putVal(s,pos+3,mode3,rbase,x*y)            
            pos+=4
                #print("Mult",res)
        elif (instr == 3): #input
            #printScreen(output)
            dirn= navSpace(xpos,ypos,space)
            putVal(s,pos+1,mode1,rbase,dirn)
            pos+=2
        elif (instr == 4): #output
#0=unknown
#1=empty
#2=wall
#3=O2
            out=calcVal(s,pos+1,mode1,rbase)
            (xd,yd)= getdirn(dirn)
            if out == 0:
                space[xpos+xd][ypos+yd]=2
            elif out == 1:
                space[xpos+xd][ypos+yd]=1
                xpos+=xd
                ypos+=yd
            elif out == 2:
                space[xpos+xd][ypos+yd]=3
                xpos+=xd
                ypos+=yd
            output.append(out)
            pos+= 2
        elif (instr == 5): 
            x=calcVal(s,pos+1,mode1,rbase)
            y=calcVal(s,pos+2,mode2,rbase)
            if (x != 0):
                pos= y
            else:
                pos+=3
        elif (instr == 6):
            x=calcVal(s,pos+1,mode1,rbase)
            y=calcVal(s,pos+2,mode2,rbase)
            if (x == 0):
                pos= y
            else:
                pos+=3
        elif (instr == 7):
            x=calcVal(s,pos+1,mode1,rbase)
            y=calcVal(s,pos+2,mode2,rbase)
            if (x < y):
                putVal(s,pos+3,mode3,rbase,1)        
            else:
                putVal(s,pos+3,mode3,rbase,0)        
            pos+=4
        elif (instr == 8):
            x=calcVal(s,pos+1,mode1,rbase)
            y=calcVal(s,pos+2,mode2,rbase)
            if (x == y):
                putVal(s,pos+3,mode3,rbase,1)        
            else:
                putVal(s,pos+3,mode3,rbase,0)        
            pos+=4
        elif (instr == 9):
            rbase+=calcVal(s,pos+1,mode1,rbase)
            #print("rbase=",rbase)
            pos+=2
        else:
            print("Did not expect ",s[pos])
            sys.exit()
    return(output,xpos,ypos)
    #print(s)
    #print("Part 1",s[0])
    
fp= open("rgcinput.txt","r")
l= fp.readline()
fp.close()
s=[]
for string in l.split(","):
    s.append(int(string))
#print(s)
#OK, fix size assumptions not ideal but quick
for i in range(10000):
    s.append(0)
maxx=1000
maxy=1000
x=int(maxx/2)
y=int(maxy/2)
space=numpy.zeros((maxx,maxy),dtype=int)
space[x,y]=1
(out,ox,oy,ns)=doMachine(s,space,x,y)
printSpace(space)
shortest= solveMaze(space,x,y)
print(shortest)
filltime= toFill(space)
print(filltime)
