#!/usr/bin/env python3
import sys,math,numpy,fractions
from itertools import permutations 

def getpat(offset,itern,pat):
    poff= int((offset+1)/(itern+1))
    #print(poff,end=" ")
    return pat[poff%len(pat)]

fp= open("rgcinput.txt","r")
l= fp.readline().strip()
fp.close()
s=[]
pattern=[0,1,0,-1]
for c in l:
    s.append(int(c))
n=len(s)
snew=[0]*n
sc= s.copy()
for i in range(100):
    for x in range(n):
        sumctr= 0
        pos= x
        lctr=0
        #sumctr2=0
        #for y in range(n):
        #    sumctr2+= s[y]*pattern[getpat(y,x,pattern)]
        while pos < n:
            sumctr+=s[pos]
            if pos + (2*(x+1)) < n:
                sumctr-=s[pos + (2*(x+1))]
            #print ("add pos",pos,"sub pos",pos+2*(x+1))
            if (lctr == x):
                lctr= 0
                pos+=3*(x+1)+1
            else:
                pos+=1
                lctr+=1

            #print(getpat(y,x,pattern),end=",")
        #print()
        #print (x,sumctr,sumctr2)
        if (sumctr < 0):
            sumctr=-sumctr
        snew[x]=(sumctr%10)
    s=snew.copy()
    #for i in s:
    #    print((i),end="")
    #print()
answer=0
for i in range(8):
    answer*=10
    if s[i]<0:
        answer+=(-s[i]%10)
    else:
        answer+=(s[i]%10)
print("Part 1",answer)
offset=0
for i in range(7):
    offset*=10
    offset+=sc[i]
print(n*10000,offset,n*10000-offset)
s=[]
for i in range(offset,n*10000):
    s.append(sc[i%n])
n=(len(s))
snew=[0]*n
for i in range(100):
    print(i)
    snew[n-1]=s[n-1]
    for x in range(n-2,-1,-1):
        snew[x]=snew[x+1]+s[x]
    for x in range(n):
        s[x]=snew[x]%10 
answer=0
for i in range(8):
    answer*=10
    if s[i]<0:
        answer+=(-s[i]%10)
    else:
        answer+=(s[i]%10)
print(answer)
