#!/usr/bin/env python3
import sys
import math
from itertools import permutations 

def paintPanels(panels,out,x,y):
    for i in range(len(panels)):
        p= panels[i]
        if p[0] == x and p[1] == y:
            if out == 0:
                panels.pop(i)
            return
    if out == 1:
        panels.append((x,y))
    
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
    
def getPanels(panels,x,y):
    for p in panels:
        if p[0] == x and p[1] == y:
            return 1
    return 0

def doMachine(s,rbase,panels):
    paintMode=True
    output= []
    pos= 0
    x=0
    y=0
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
            inp= getPanels(panels,x,y)
            putVal(s,pos+1,mode1,rbase,inp)
            
            pos+=2
        elif (instr == 4): #output
            out=calcVal(s,pos+1,mode1,rbase)
            #print("Output",out)
            if paintMode:
                paintMode= False
                paintPanels(panels,out,x,y)
            else:
                paintMode=True
                if out == 0:
                    dirn=(dirn-1)%4
                elif out == 1:
                    dirn=(dirn+1)%4
                else:
                    print("Direction error")
                if (dirn == 0):
                    y-=1
                elif dirn == 1:
                    x+=1
                elif dirn == 2:
                    y+=1
                elif dirn == 3:
                    x-=1
                else:
                    print("Unnatural direction")
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
for p in panels:
    if p not in uniq:
        uniq.append(p)
        count+= 1
print("Part 1",count)
    #printScreen(out)

