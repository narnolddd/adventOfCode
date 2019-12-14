#!/usr/bin/env python3
import sys
import math
from itertools import permutations 

def getPanels(panels,x,y):
    for p in panels:
        if p[0] == x and p[1] == y:
            return p[2]
    return 0

def paintPanels(panels,out,x,y):
    for p in panels:
        if p[0] == x and p[1] == y:
            p[2]= out
            return
    panels.append([x,y,out])
    
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

def doMachine(s,rbase,panels):
    paintMode=True
    output= []
    pos= 0
    xpos=0
    ypos=0
    dirn=0
    inpIndex=0
    inpctr=0
    while(True):
        instr=s[pos]%100
        mode1= (int(s[pos]/100))%10
        mode2= (int(s[pos]/1000))%10
        mode3= (int(s[pos]/10000))%10
        #print(pos,s[pos],instr,mode1,mode2,mode3)
        if (instr == 99):
            return (output,x,y,dirn)
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
            inp= getPanels(panels,xpos,ypos)
            putVal(s,pos+1,mode1,rbase,inp)
            
            pos+=2
        elif (instr == 4): #output
            out=calcVal(s,pos+1,mode1,rbase)
            #print("Output",out)
            if paintMode:
                paintMode= False
                paintPanels(panels,out,xpos,ypos)
                #print("Paint",out," at ",xpos,ypos)
                #print(panels)
            else:
                paintMode=True
                if out == 0:
                    dirn=(dirn-1)%4
                elif out == 1:
                    dirn=(dirn+1)%4
                else:
                    print("Direction error")
                if (dirn == 0):
                    ypos-=1
                elif dirn == 1:
                    xpos+=1
                elif dirn == 2:
                    ypos+=1
                elif dirn == 3:
                    xpos-=1
                else:
                    print("Unnatural direction")
                #print("Move",out,"to",dirn,xpos,ypos)
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

    #print(s)
    #print("Part 1",s[0])
    
fp= open("rgcinput.txt","r")
l= fp.readline()
fp.close()
s=[]
for string in l.split(","):
    s.append(int(string))
#print(s)
for i in range(10000):
    s.append(0)
sc=s.copy()
x=0
y=0
dirn=0
panels=[]
doMachine(sc,0,panels)
uniq= []
count= 0
#print(panels)

for p in panels:
    if p not in uniq:
        uniq.append(p)
        count+= 1
print("Part 1",len(panels),len(uniq))
    #printScreen(out)
panels=[[0,0,1]]
sc=s.copy()
doMachine(sc,0,panels)
xmin= 0
ymin=0
xmax=0
ymax=0
for p in panels:
	if p[2] ==1:
		if p[0]< xmin:
			xmin= p[0]
		if p[0] > xmax:
			xmax= p[0]
		if p[1] < ymin:
			ymin= p[1]
		if p[1] > ymax:
			ymax= p[1]
xr= xmax-xmin+1
yr= ymax-ymin+1

disp=[]
for y in range(yr):
	string=[]
	for x in range(xr):
		string.append(" ")
	disp.append(string)
for p in panels:
	if p[2] == 1:
		disp[p[1]+ymin][p[0]+xmin]="#"
for d in disp:
	for c in d:
		print(c,end="")
	print()
