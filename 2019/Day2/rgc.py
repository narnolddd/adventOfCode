#!/usr/bin/env python3
import sys
import math
try:
	fp= open("rgcinput.txt","r")
	l= fp.readline()
	s= l.split(",")
	pos= 0
	for i in s:
		s[pos]= int(i)
		pos+= 1
	pos= 0
	s[1]=12
	s[2]=2
	while(True):
		if (s[pos] == 99):
			break
		elif (s[pos] == 1):
			res= s[s[pos+1]]+s[s[pos+2]]
			s[s[pos+3]]= res
			#print("Add",res)
		elif (s[pos] == 2):
			res= s[s[pos+1]]*s[s[pos+2]]
			#print("Mult",res)
			s[s[pos+3]]= res
		else:
			print("Did not expect ",s[pos])
		pos+=4
	#print(s)
	print("Part 1",s[0])
	fp= open("rgcinput.txt","r")
	l= fp.readline()
	s2= l.split(",")
	pos= 0
	for i in s2:
		s2[pos]= int(i)
		pos+= 1
	for x in range(100):
		for y in range (100):
			s=s2.copy()
			pos= 0
			s[1]=x
			s[2]=y
			while(True):
				if (s[pos] == 99):
					break
				elif (s[pos] == 1):
					res= s[s[pos+1]]+s[s[pos+2]]
					s[s[pos+3]]= res
					#print("Add",res)
				elif (s[pos] == 2):
					res= s[s[pos+1]]*s[s[pos+2]]
					#print("Mult",res)
					s[s[pos+3]]= res
				else:
					print("Did not expect ",s[pos])
				pos+=4
			if s[0] == 19690720:
				print(x*100+y)
	#print(s)
finally:
	fp.close()
