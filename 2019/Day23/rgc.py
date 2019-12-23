#!/usr/bin/env python3
import sys,math,numpy
from itertools import permutations 


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
    
def doMachine(s,inp,pos,rbase):
    output=[]
    outOfInput=False
    while(True):
        instr=s[pos]%100
        mode1= (int(s[pos]/100))%10
        mode2= (int(s[pos]/1000))%10
        mode3= (int(s[pos]/10000))%10
        #print(pos,s[pos],instr,mode1,mode2,mode3)
        if (instr == 99):
            return (output,pos,rbase)
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
            thisinp=-1
            if len(inp) > 0:
                thisinp=inp[0]
            putVal(s,pos+1,mode1,rbase,thisinp)
            pos+=2
            if len(inp) == 0:
                if outOfInput:
                    return(output,pos,rbase)
                else:
                    outOfInput=True
            else:
                inp.pop(0)
        elif (instr == 4): #output
#0=unknown
#1=empty
#2=wall
#3=O2
            out=calcVal(s,pos+1,mode1,rbase)

            output.append(out)
            #print("Output now",output)
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


if len(sys.argv) != 2:
    print("Enter input file name as CLI")
    sys.exit()
fp= open(sys.argv[1],"r")
l= fp.readline()
fp.close()
s=[]
for string in l.split(","):
    s.append(int(string))
for i in range(10000):
    s.append(0)
machines=[]
inputs=[]
for m in range(50):
    machines.append(s.copy())
    inputs.append([])
startpos=[0]*50
rbase=[0]*50
outqueue=[]
for m in range(50):
    (out,startpos[m],rbase[m])= doMachine(machines[m],[m],startpos[m],rbase[m])
    outqueue+=out
while len(outqueue) != 0:
    m= outqueue.pop(0)
    if m == -1:
        continue
    x=outqueue.pop(0)
    y=outqueue.pop(0)
    if m == 255:
        print("Part 1",x,y)
        break
    #print("Send to machine ",m,x,y)
    (out,startpos[m],rbase[m])= doMachine(machines[m],[x,y],startpos[m],rbase[m])
    #outqueue+=out
    print(len(outqueue),len(out))
