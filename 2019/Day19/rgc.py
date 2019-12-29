#!/usr/bin/env python3
import sys,math,numpy
from itertools import permutations 

def testsquare(s,bestx,besty,wid,hei):
    angles=[]
    sc=s.copy()
    out= doMachine(sc,bestx,besty)
    angles.append(out[0]==1)
    sc=s.copy()
    out= doMachine(sc,bestx+wid-1,besty)
    angles.append(out[0]==1)
    sc=s.copy()
    out= doMachine(sc,bestx,besty+hei-1)
    angles.append(out[0]==1)
    sc=s.copy()
    out= doMachine(sc,bestx+wid-1,besty+hei-1)
    angles.append(out[0]==1)
    return angles

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

valid_start=[]

beam=numpy.zeros((50,50))
for x in range(50):
    for y in range(50):
        sc=s.copy()
        out=doMachine(sc,x,y)
        #print(x,y,out)
        if out[0] == 1:
            beam[x][y] = 1
            count+=1
            if (x == 49 or y == 49):
                valid_start.append((x,y))


print("Part1 ",count)

(validx,validy)=valid_start[int(len(valid_start)/2)]

wiggle_dist= 10


hei=100
wid=100


while True:
    testx=validx+wiggle_dist
    testy=validy+wiggle_dist
    (nw1,ne1,sw1,se1)=testsquare(s,testx,testy,wid,hei)
    #print(validx,validy,wiggle_dist,nw1,ne1,sw1,se1)
    if nw1 == True and ne1 == True and sw1 == True:
        #print("All true at",testx,testy)
        if wiggle_dist == 1:
            break
        wiggle_dist-=1
        continue
    testx=validx
    testy=validy+wiggle_dist
    (nw2,ne2,sw2,se2)=testsquare(s,testx,testy,wid,hei)
    if nw2 == True and ne2 == True and sw2 == True:
        if wiggle_dist == 1:
            break
        wiggle_dist-=1
        continue
    testx=validx+wiggle_dist
    testy=validy
    (nw3,ne3,sw3,se3)=testsquare(s,testx,testy,wid,hei)
    if nw3 == True and ne3 == True and sw3 == True:
        if wiggle_dist == 1:
            break
        wiggle_dist-=1
        continue
    if nw1 == True:
        if ne1 == False and sw1 == False:
            validx= validx+wiggle_dist
            validy= validy+wiggle_dist
            continue
        if ne1 == False and nw1 == True:
            validx= validx
            validy= validy+wiggle_dist
            continue
        if ne1 == True and sw1 == False:
            validx= validx+wiggle_dist
            validy= validy
            continue
    if nw2 == True:
        validx= validx
        validy= validy+wiggle_dist
        print("2",(nw2,ne2,sw2,se2))
        continue
    if nw3 == True:
        validx= validx+wiggle_dist
        validy= validy
        continue
    if wiggle_dist == 1:
        print ("Wiggle stopping -- this is probably a problem")
    wiggle_dist-=1
#print(validx,validy)

moved= True
while moved:
    moved= False
    for dirn in [(-2,-2),(-2,-1),(-1,-2),(-1,-1),(-2,0),(0,-2),(-1,0),(0,-1)]:
        testx= validx+dirn[0]
        testy= validy+dirn[1]
        (nw1,ne1,sw1,se1)=testsquare(s,testx,testy,wid,hei) 
        if nw1 == True and ne1 == True and sw1 == True:
            validx= testx
            validy= testy
            moved= True
            break
            
print("Part 2:",validx*10000+validy)

