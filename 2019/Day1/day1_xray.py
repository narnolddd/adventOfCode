# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 10:42:10 2019

@author: Administrator
"""

#fule = mass/3 - 2

fuel_sum = 0
f = open("input_d1.txt")
line = f.readline()
while line:
    fuel_p = 0
    mass = int(line)
    fuel_p = int(mass/3) - 2
    fuel_add_on = int(mass/3) - 2
    while(int(fuel_add_on/3)-2 > 0):
        fuel_p += int(fuel_add_on/3)-2
        fuel_add_on = int(fuel_add_on/3)-2
    fuel_sum += fuel_p
    line = f.readline()

print("total fuel is"+str(fuel_sum))