#!/usr/bin/env python3
import sys,math,numpy
from itertools import permutations 

def getpat(offset,itern,pat):
    poff= int((offset+1)/(itern+1))
    #print(poff,end=" ")
    return pat[poff%len(pat)]

fp= open("rgctest2.txt","r")
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
        for y in range(n):
            sumctr+=s[y]*getpat(y,x,pattern)
            #print(getpat(y,x,pattern),end=",")
        #print()
        if (sumctr < 0):
            sumctr=-sumctr
        snew[x]=(sumctr%10)
    s=snew.copy()

answer=0
for i in range(8):
    answer*=10
    answer+=s[i]
print("Part 1",answer)
sl=[]
offset=0
for i in range(7):
    offset*=10
    offset+=sc[i]
print("Part 2",answer)
