#!/usr/bin/env python3
import sys,math,numpy
from itertools import permutations 

def testsquare(s,bestx,besty,wid,hei):
    sc=s.copy()
    out= doMachine(sc,bestx,besty)
    if out[0] != 1:
        print("1",out,bestx,besty)
        return False
    sc=s.copy()
    out= doMachine(sc,bestx+wid-1,besty)
    if out[0] != 1:
        print("2",out,bestx,besty)
        return False
    sc=s.copy()
    out= doMachine(sc,bestx,besty+hei-1)
    if out[0] != 1:
        print("3",out,bestx,besty)
        return False
    sc=s.copy()
    out= doMachine(sc,bestx+wid-1,besty+hei-1)
    if out[0] != 1:
        print("4",out,bestx,besty)
        return False
    return True

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

def doMachine(s,inp1,inp2):
    output= []
    pos=0
    rbase=0
    inp=inp1
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
            
            putVal(s,pos+1,mode1,rbase,inp)
            inp=inp2
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


if len(sys.argv) != 2:
    print("Enter input file name as CLI")
    sys.exit()
fp= open(sys.argv[1],"r")
l= fp.readline()
fp.close()
s=[]
for string in l.split(","):
    s.append(int(string))
#print(s)
#OK, fix size assumptions not ideal but quick
for i in range(10000):
    s.append(0)
count= 0

beam=numpy.zeros((50,50))
for x in range(50):
    for y in range(50):
        sc=s.copy()
        out=doMachine(sc,x,y)
        #print(x,y,out)
        if out[0] == 1:
            beam[x][y] = 1
            count+=1


print("Part1 ",count)
xr=2000
yr=2000
ylow=2000
yhigh=-0
for y in range(yr):
    sc=s.copy()
    x=xr-1
    out=doMachine(sc,x,y)
    if out[0] == 1:
        #print("Got some out")
        if y < ylow:
            ylow=y
        if y > yhigh:
            yhigh=y

reqheight=110
height=yhigh-ylow    
print(ylow,yhigh,height,reqheight/height)



reqy=int(ylow*reqheight/(yhigh-ylow))
reqx=int(reqy*xr/ylow)

bestx=reqx
besty=reqy
print(bestx,besty)
x=bestx
y=besty
sys.exit()
while not testsquare(s,bestx,besty,100,100):
        bestx+=1
        besty+=1
        print("Move out")
    
move= True
while move:
    move= False
    if testsquare(s,bestx-1,besty,100,100):
        bestx-=1
        move= True
    if testsquare(s,bestx,besty-1,100,100):
        besty-=1
        move= True
print(bestx,besty)
    

#
