#!/usr/bin/env python3
import sys
import math

def parseChem(string):
	parts=string.strip().split(" ")
	num=int(parts[0])
	return(num,parts[1])

def recipe(request,reactions):
	ingredients=[]
	for r in reactions:
		#print(r)
		if r[1][1] == request[1]:
			amount= int(math.ceil(request[0]/r[1][0]))
			print("Recipe selected",r,amount)
			for i in r[0]:
				ingredients.append((amount*i[0],i[1]))
			print("Ingr",ingredients)
			return ingredients
	print("Recipe incomplete")
	return []

fp= open("rgcinput.txt","r")
lines= fp.readlines()
fp.close()
reactions=[]
for l in lines:
	sides=l.split("=>")
	rhs=sides[1]
	lhs=sides[0]
	inputs=sides[0].split(", ")
	output=parseChem(rhs)
	allinp=[]
	for i in inputs:
		allinp.append(parseChem(i))
	reactions.append((allinp,output))
produceList=[(1,'FUEL')]
ore= 0
while len(produceList) != 0:
	request=produceList.pop(0)
	ingredients=recipe(request,reactions)
	for r in ingredients:
		if r[1] == 'ORE':
			ore+= r[0]
		else:
			produceList.append(r)
print(ore) 
	
