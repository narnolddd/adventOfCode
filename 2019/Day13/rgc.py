#!/usr/bin/env python3
import sys
import math
from itertools import permutations 


def printScreen(out):
    mx=0
    my=0
    for i in range(0,len(out),3):
        x= out[i]
        y= out[i+1]
        if x > mx:
            mx=x
        if y > my:
            my=y
    mx+=1
    my+=1
    b= 0
    scr=[]
    for y in range(my):
        line=[]
        for x in range(mx):
            line.append('X')
        scr.append(line)
    score= 0
    for i in range(0,len(out),3):
        x= out[i]
        y= out[i+1]
        if x == -1 and y == 0:
            score= out[i+2]

        elif out[i+2] == 0:
            scr[y][x]=' '
        elif out[i+2] == 1:
            scr[y][x]='+'
        elif out[i+2] == 2:
            scr[y][x]='#'
        elif out[i+2] == 3:
            scr[y][x]='_'
        elif out[i+2] == 4:
            scr[y][x]='O'
    print("Score=",score)
    for line in scr:
        for char in line:
            print(char,end="")
        print()
    return

def moveBat(out):
    bx=0
    px=0
    for i in range(0,len(out),3):
        x= out[i]
        y= out[i+1]
        if x == -1 and y == 0:
            continue
        elif out[i+2] == 3:
            px=x
        elif out[i+2] == 4:
            bx=x
    if bx < px:
        return -1
    if bx > px:
        return 1
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

def doMachine(s,rbase,inp):
    output= []
    pos= 0
    inpIndex=0
    inpctr=0
    while(True):
        instr=s[pos]%100
        mode1= (int(s[pos]/100))%10
        mode2= (int(s[pos]/1000))%10
        mode3= (int(s[pos]/10000))%10
        #print(pos,s[pos],instr,mode1,mode2,mode3)
        if (instr == 99):
            return (output,rbase,pos)
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
            inp= moveBat(output)
            putVal(s,pos+1,mode1,rbase,inp)
            
            pos+=2
        elif (instr == 4): #output
            out=calcVal(s,pos+1,mode1,rbase)
            #print("Output",out)
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
    return(output)
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
pos= 0
rbase= 0
sc=s.copy()
out=doMachine(s,rbase,False)[0]
printScreen(out)
b= 0
for i in range(2,len(out),3):
    if out[i]==2:
        b+=1
print("Part 1",b)
sc[0]=2
out=doMachine(sc,rbase,0)[0]
score= 0
for i in range(0,len(out),3):
    x= out[i]
    y= out[i+1]
    if x == -1 and y == 0:
        score= out[i+2]
print("Part 2",score)
    #printScreen(out)

