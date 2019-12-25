#!/usr/bin/env python3
import sys,math,numpy
from itertools import permutations
import copy 

def countLevelNeighbours(lower,level,upper,i,j):
    n= 0
    if i == 0 and upper[11] == '#':
        n+=1
    if j == 0 and upper[7] == '#':
        n+=1
    if i == 4 and upper[13] == '#':
        n+=1 
    if j == 4 and upper[17] == '#':
        n+=1
    if i == 2 and j == 3:
       for i2 in range(5):
           if lower[4*5+i2] == '#':
               n+=1
    if i == 2 and j == 1:
       for i2 in range(5):
           if lower[i2] == '#':
               n+=1
    if i == 3 and j == 2:
        for j2 in range(5):
           if lower[j2*5+4] == '#':
               n+=1
    if i == 1 and j == 2:
        for j2 in range(5):
           if lower[j2*5] == '#':
               n+=1   
    for d in [(-1,0),(+1,0),(0,-1),(0,+1)]:
        i1=i+d[0]
        j1=j+d[1]
        if i1 == 2 and j1 == 2:
            continue
        if i1 < 0 or i1 >=5 or j1 < 0 or j1 >= 5:
            continue
        if level[j1*5+i1] == '#':
            n+=1
    return n

def printBugs(b):
    for j in range(5):
        for i in range(5):
            print(b[j*5+i],end="")
        print()

def countNeighbours(b,i,j):
    n= 0
    for d in [(-1,0),(+1,0),(0,-1),(0,+1)]:
        i1=i+d[0]
        j1=j+d[1]
        if i1 < 0 or i1 >=5 or j1 < 0 or j1 >= 5:
            continue
        if b[j1*5+i1] == '#':
            n+=1
    return n

if len(sys.argv) != 2:
    print("Enter input file name as CLI")
    sys.exit()
fp= open(sys.argv[1],"r")
lines= fp.readlines()
fp.close()

b= [' ']*25
for i in range(5):
    for j in range(5):
        b[j*5+i]=lines[j][i]
bugs=[b]

while True:
    b2= [' ']*25
    for i in range(5):
        for j in range(5):
            n=countNeighbours(b,i,j)
            if b[j*5+i] == '#':
                if n == 1:
                    b2[j*5+i] = '#'
                else:
                    b2[j*5+i] = '.'
            else:
                if n == 1 or n == 2:
                    b2[j*5+i] = '#'
                else:
                    b2[j*5+i] = '.'
    if b2 in bugs:
        b= b2
        break
    bugs.append(b2)
    b=b2.copy()
print()
printBugs(b)
    
bd= 0
for i in range(5):
    for j in range(5):
        if b[j*5+i] == '#':
            bd+=math.pow(2,j*5+i)
    
print("Part 1",int(bd))
levels={}
b= ['.']*25
for i in range(-202,203):
    levels[i]=copy.deepcopy(b)
for i in range(5):
    for j in range(5):
        levels[0][j*5+i]=lines[j][i]


l2=copy.deepcopy(levels)
for d in range(0,200):
    for l in range(-d-1,d+2):
        for i in range(5):
            for j in range(5):
                if i == 2 and j == 2:
                    continue
                n=countLevelNeighbours(levels[l-1],levels[l],levels[l+1],i,j)
                if levels[l][j*5+i] == '#':
                    if n == 1:
                        l2[l][j*5+i] = '#'
                    else:
                        l2[l][j*5+i] = '.'
                else:
                    if n == 1 or n == 2:
                        l2[l][j*5+i] = '#'
                    else:
                        l2[l][j*5+i] = '.'
    if d == 10:
        for l in range(-9,10):
            print(l)
            printBugs(levels[l])
            print()
    levels= copy.deepcopy(l2)
n= 0
for l in levels:
    for i in range(5):
        for j in range(5):
            if levels[l][j*5+i] == '#':
                n+=1
print("Part 2",n)
