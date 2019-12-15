#!/usr/bin/env python3
import sys
import math
import copy, fractions

def listcomp(x,y):
    if len(x) != len(y):
        return False
    for i in range (len(x)):
        xel= x[i] 
        yel= y[i]
        if len(yel) != len (xel):
            return False
        for j in range(len(xel)):
            if xel[i] != xel[j]:
                return False
    return True

def parsePlanet(string):
    string=string[1:len(string)-2]
    coords=string.split(",")
    #print(coords)
    xco=int(coords[0][2:])
    yco=int(coords[1][3:])
    zco=int(coords[2][3:])
    #print(xco,yco,zco)
    return([xco,yco,zco,0,0,0])

fp= open("rgcinput.txt","r")
strings= fp.readlines()
fp.close()
initplanets=[]
for s in strings:
    initplanets.append(parsePlanet(s))
n= len(initplanets)
planets=copy.deepcopy(initplanets)
print(initplanets)
#for p in planets:
#    print(p)
for l in range(1000):
    for i in range(n):
        for j in range(i):
            for k in range(3):
                if planets[i][k] < planets[j][k]:
                    planets[i][k+3]+= 1
                    planets[j][k+3]-= 1
                if planets[i][k] > planets[j][k]:
                    planets[i][k+3]-= 1
                    planets[j][k+3]+= 1
    for i in range(n):
        for k in range(3):
            planets[i][k]+= planets[i][k+3]
#    print(l)
#    for p in planets:
#        print(p)
energy= 0
for p in planets:
    potenergy=0
    kinenergy=0
    for k in range(3):
        if (p[k] < 0):
            potenergy-= p[k]
        else:
            potenergy+= p[k]
    for k in range(3,6):
        if (p[k] < 0):
            kinenergy-= p[k]
        else:
            kinenergy+= p[k]
    energy+=potenergy*kinenergy
print("part1",energy)

planets=copy.deepcopy(initplanets)
#print("Planets",planets)
kloops=[]
for k in range(3):
    pslice=[]
    for p in planets:
        pslice.append([p[k],p[k+3]])

    count= 0
    while True:
        #print(count,pslice)
        for i in range(n):
            for j in range(i):
                if pslice[i][0] < pslice[j][0]:
                    pslice[i][1]+= 1
                    pslice[j][1]-= 1
                if pslice[i][0] > pslice[j][0]:
                    pslice[i][1]-= 1
                    pslice[j][1]+= 1
        for p in pslice:
            p[0]+=p[1]
        #print(pslice)
        count+=1
        match=True
        for i in range(len(pslice)):
            if pslice[i][0] != planets[i][k] or pslice[i][1] != planets[i][k+3]:
                match=False
                break
        if match == True:
            print("Match at",count)
            kloops.append(count)
            break
c= 1
for k in kloops:
    c= c*k/fractions.gcd(c,k)
print(c)
