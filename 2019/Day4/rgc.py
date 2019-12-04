#!/usr/bin/env python3
import sys
import math
i=[1,2,3,2,5,7]
num= 0
smallNum= 0
while True:
    
    val= i[0]*100000+i[1]*10000+i[2]*1000+i[3]*100+i[4]*10+i[5]

    if val == 647016:
        break

    double= False
    realDouble= False
    order= True
    for pos in range(5):
        if i[pos] > i[pos+1]:
            order= False
        if i[pos] == i[pos+1]:
            double= True
            if pos == 0 or i[pos-1] != i[pos]:
                if pos == 4 or i[pos+2] != i[pos]:
                    realDouble= True
    if (order and double):
        num+=1
        if realDouble:
            smallNum+=1
#        print(val)
    pos=5
    while True:
        i[pos]+=1
        if i[pos] < 10:
            break
        i[pos]= 0
        pos-= 1    
print(num,smallNum)
        
    
