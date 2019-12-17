#!/usr/bin/env python3
import sys,math,numpy
from itertools import permutations 

def getDirn(robx,roby,dirn,space):
    dx= 0
    dy= 0
    (maxx,maxy)=space.shape
    #1=N,2=E,3=S,4=W
    if (dirn == 1 or dirn == 3):
        if robx > 0 and (space[robx-1][roby]) == ord('#'):
            if dirn == 1:
                return (4,'L',-1,0)
            else:
                return (4,'R',-1,0)
        if robx < maxx-1 and (space[robx+1][roby]) == ord('#'):
            if dirn == 3:
                return (2,'L',1,0)
            else:
                return (2,'R',1,0)
    if (dirn == 2 or dirn == 4):
        if roby > 0 and (space[robx][roby-1]) == ord('#'):
            if dirn == 2:
                return (1,'L',0,-1)
            else:
                return (1,'R',0,-1)
        if roby < maxy-1 and (space[robx][roby+1]) == ord('#'):
            if dirn == 4:
                return (3,'L',0,1)
            else:
                return (3,'R',0,1)
    return (0,0,0,0)

def isscaffold(c):
    if c==ord('#'):
        return True
    if c==ord('^'):
        return True
    if c==ord('<'):
        return True
    if c==ord('>'):
        return True
    if c==ord('v'):
        return True
    return False

def parseSpace(out):
    width= 0
    for o in out:
        if o == 10:
            break
        width+= 1
    height=0
    w= 0
    for o in out:
        if o == 10:
            w=0
            height+=1
        else:
            w+=1
    height-=1
    space=numpy.empty((width,height),dtype=int)
    x=0
    y=0
    for o in out:
        if o == 10:
            x=0
            y+=1
            continue
        if (y >= height):
            break
        space[x][y]=o
        x+=1
    return space

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

def doMachine(s,inp):
    output= []
    pos=0
    rbase=0
    while(True):
        instr=s[pos]%100
        mode1= (int(s[pos]/100))%10
        mode2= (int(s[pos]/1000))%10
        mode3= (int(s[pos]/10000))%10
        #print(pos,s[pos],instr,mode1,mode2,mode3)
        if (instr == 99):
            return output
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
            #print("INPUT")
            i=inp.pop(0)
            #print(i)
            putVal(s,pos+1,mode1,rbase,i)
            pos+=2
        elif (instr == 4): #output
#0=unknown
#1=empty
#2=wall
#3=O2
            out=calcVal(s,pos+1,mode1,rbase)

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
sc=s.copy()
out=doMachine(s,[])
#print(out)

space=parseSpace(out)
(maxx,maxy)=space.shape
tot= 0
for i in range(1,maxx-1):
    for j in range(1,maxy-1):
        if isscaffold(space[i][j]) and \
            isscaffold(space[i-1][j]) and \
            isscaffold(space[i+1][j]) and \
            isscaffold(space[i][j-1]) and \
            isscaffold(space[i][j+1]):
            tot+= i*j
print("Part 1",tot)
#print(space)
for j in range(0,maxy):
    for i in range(0,maxx):
        print(str(chr(space[i][j])),end="")
    print()
robx=-1
roby=-1
for j in range(0,maxy):
    for i in range(0,maxx):
        if(space[i][j] == ord('^')):
            robx=i
            roby=j
            break
    if (robx >= 0):
        break
dirn=1
#1=N,2=E,3=S,4=W
dirs=[]
x=robx
y=roby
while True:
    (dirn,turn,dx,dy)=getDirn(x,y,dirn,space)
    if(dirn == 0):
        break
    #print(dirn,turn,dx,dy)
    dist=0
    while True:
        if (x+dx) >= 0 and x+dx < maxx and y+dy >=0 and y+dy < maxy \
        and space[x+dx][y+dy] == ord('#'):
            x+=dx
            y+=dy
            dist+=1
        else:
            break
    dirs.append((turn,dist))
#print(dirs)
acode="R,6,L,8,R,8"
bcode="R,4,R,6,R,6,R,4,R,4"
ccode="L,8,R,6,L,10,L,10"
mcode="A,A,B,C,B,C,B,C,A,C"
inp=[]
for i in range(len(mcode)):
#    print(ord(code[i]))
    inp.append(ord(mcode[i]))
inp.append(10)
for i in range(len(acode)):
#    print(ord(code[i]))
    inp.append(ord(acode[i]))
inp.append(10)
for i in range(len(bcode)):
#    print(ord(code[i]))
    inp.append(ord(bcode[i]))
inp.append(10)
for i in range(len(ccode)):
#    print(ord(code[i]))
    inp.append(ord(ccode[i]))
inp.append(10)

inp.append(ord('n'))
inp.append(10)
sc[0]=2
out=doMachine(sc,inp)
#print(out)
space=parseSpace(out)
(maxx,maxy)=space.shape
for j in range(0,maxy):
    for i in range(0,maxx):
        print(str(chr(space[i][j])),end="")
    print()
print(out[-1])
