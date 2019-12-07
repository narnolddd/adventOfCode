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
	skip= 0
	while(True):
		instr=s[pos]%100
		mode1= (int(s[pos]/100))%10
		mode2= (int(s[pos]/1000))%10
		mode3= (int(s[pos]/10000))%10
		#print(pos,s[pos],instr,mode1,mode2,mode3)
		if (instr == 99):
			break
		elif (instr == 1):
			if mode1 == 0:
				x= s[s[pos+1]]
			else:
				x= s[pos+1]
			if mode2 == 0:
				y= s[s[pos+2]]
			else:
				y= s[pos+2]	
						
			res= x + y
			s[s[pos+3]]= res
			#print("Add",res)
			pos+=4
		elif (instr == 2):
			if mode1 == 0:
				x= s[s[pos+1]]
			else:
				x= s[pos+1]
			if mode2 == 0:
				y= s[s[pos+2]]
			else:
				y= s[pos+2]		
			res= x * y
			s[s[pos+3]]= res
			pos+=4
			#print("Mult",res)
		elif (instr == 3):
			inp= 1
			#print("Storing 1 at ",s[pos+1])
			s[s[pos+1]]= inp
			pos+=2
		elif (instr == 4):
			if (mode1 == 0):
				x=s[s[pos+1]]
			else:
				x= s[pos+1]
			print(x)
			pos+= 2
		else:
			print("Did not expect ",s[pos])
			sys.exit()
	#print(s)
	#print("Part 1",s[0])
	
finally:
	fp.close()
try:
	fp= open("rgcinput.txt","r")
	l= fp.readline()
	s= l.split(",")
	pos= 0
	for i in s:
		s[pos]= int(i)
		pos+= 1
	pos= 0
	skip= 0
	while(True):
		instr=s[pos]%100
		mode1= (int(s[pos]/100))%10
		mode2= (int(s[pos]/1000))%10
		mode3= (int(s[pos]/10000))%10
		#print(pos,s[pos],instr,mode1,mode2,mode3)
		if (instr == 99):
			break
		elif (instr == 1):
			if mode1 == 0:
				x= s[s[pos+1]]
			else:
				x= s[pos+1]
			if mode2 == 0:
				y= s[s[pos+2]]
			else:
				y= s[pos+2]	
						
			res= x + y
			s[s[pos+3]]= res
			#print("Add",res)
			pos+=4
		elif (instr == 2):
			if mode1 == 0:
				x= s[s[pos+1]]
			else:
				x= s[pos+1]
			if mode2 == 0:
				y= s[s[pos+2]]
			else:
				y= s[pos+2]		
			res= x * y
			s[s[pos+3]]= res
			pos+=4
			#print("Mult",res)
		elif (instr == 3):
			inp= 5
			#print("Storing", inp, " at ",s[pos+1])
			if mode1 == 0:
				s[s[pos+1]]= inp
			else:
				s[pos+1]= inp
			pos+=2
		elif (instr == 4):
			if (mode1 == 0):
				x=s[s[pos+1]]
			else:
				x= s[pos+1]
			print(x)
			pos+= 2
		elif (instr == 5):
			if mode1 == 0:
				x= s[s[pos+1]]
			else:
				x= s[pos+1]
			if mode2 == 0:
				y= s[s[pos+2]]
			else:
				y= s[pos+2]
			if (x != 0):
				pos= y
			else:
				pos+=3
		elif (instr == 6):
			if mode1 == 0:
				x= s[s[pos+1]]
			else:
				x= s[pos+1]
			if mode2 == 0:
				y= s[s[pos+2]]
			else:
				y= s[pos+2]
			if (x == 0):
				pos= y
			else:
				pos+=3
		elif (instr == 7):
			if mode1 == 0:
				x= s[s[pos+1]]
			else:
				x= s[pos+1]
			if mode2 == 0:
				y= s[s[pos+2]]
			else:
				y= s[pos+2]
			if mode3 == 0:
				store= s[pos+3]
			else:
				store= pos+3
				#print("Weird8")
			if (x < y):
				s[store]= 1
			else:
				s[store]= 0
			pos+=4
		elif (instr == 8):
			if mode1 == 0:
				x= s[s[pos+1]]
			else:
				x= s[pos+1]
			if mode2 == 0:
				y= s[s[pos+2]]
			else:
				y= s[pos+2]
			if mode3 == 0:
				store= s[pos+3]
			else:
				#print("Weird7")
				store= pos+3
			if (x == y):
				#print ("Storing 1 at position",store)
				s[store]= 1
			else:
				s[store]= 0
			pos+=4
		else:
			print("Did not expect ",s[pos])
			sys.exit()
	#print(s)
	#print("Part 1",s[0])
	
finally:
	fp.close()
