#!/usr/bin/env python3
import sys
import math

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
planets=[]
for s in strings:
    planets.append(parsePlanet(s))
n= len(planets)
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
