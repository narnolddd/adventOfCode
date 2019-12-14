#!/usr/bin/env python3
import sys
import math

def parseChem(string):
	parts=string.strip().split(" ")
	num=int(parts[0])
	return([num,parts[1]])

def recipe(request,reactions):
	ingredients=[]
	for i in range(len(reactions)):
		r= reactions[i]
		if r[1][1] == request[1]:
			amount= int(math.ceil(request[0]/r[1][0]))
			#print("Recipe selected",r,amount)
			for j in r[0]:
				ingredients.append([amount*j[0],j[1]])
			#print("Ingr",ingredients)
			return (ingredients,i)
	#print("Recipe incomplete", request,reactions)
	return []

fp= open("rgctest1.txt","r")
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
#print(reactions)
produceList=[[1,'FUEL']]
ore= 0
while len(produceList) != 0:
	request= None
	reqi= 0
	for i in range(len(produceList)):
		p= produceList[i]
		inLHS=False
		for r in reactions:
			for j in r[0]:
				if j[1] == p[1]:
					inLHS=True
					break
				if inLHS:
					break
		if not inLHS:
			request=p
			reqi=i
			break
	if request == None:
		print ("Oh oh, we're in trouble")
	produceList.pop(reqi)
	(ingredients,i)=recipe(request,reactions)
	#print(ingredients,i)
	reactions.pop(i)
	for r in ingredients:
		if r[1] == 'ORE':
			ore+= r[0]
		else:
			found=False
			for p in produceList:
				#print("Produce",p)
				if p[1] == r[1]:
					p[0]+= r[0]
					found= True
					break
			if not found:
				produceList.append(r)
print("Part1",ore) 
	
