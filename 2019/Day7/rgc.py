#!/usr/bin/env python3
import sys
import math
from itertools import permutations 
def doMachine(inp,s,pos):
	output= []
	inpptr=0
	skip= 0
	#print("Position",pos, inp)
	while(True):
		instr=s[pos]%100
		mode1= (int(s[pos]/100))%10
		mode2= (int(s[pos]/1000))%10
		mode3= (int(s[pos]/10000))%10
		#print(pos,s[pos],instr,mode1,mode2,mode3)
		if (instr == 99):
			#print("terminate")
			return(inp+output,-1)
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
			#print(inp)
			if len(inp) == 0:
				return (output,pos)
			x=inp.pop(0)
			if mode1 == 0:
				s[s[pos+1]]= x
			else:
				s[pos+1]= x
			pos+=2
			
		elif (instr == 4):
			if (mode1 == 0):
				x=s[s[pos+1]]
			else:
				x= s[pos+1]
			#print(x) 
			output.append(x)
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
	
fp= open("rgcinput.txt","r")
l= fp.readline()
fp.close()
s= l.split(",")
pos= 0
for i in s:
	s[pos]= int(i)
	pos+= 1
inputs=permutations([0,1,2,3,4])
best=0
for inp in inputs:
	scopy=s.copy()
	ampa= doMachine([inp[0],0],scopy,0)[0][0]
	scopy=s.copy()
	ampb= doMachine([inp[1],ampa],scopy,0)[0][0]
	scopy=s.copy()
	ampc= doMachine([inp[2],ampb],scopy,0)[0][0]
	scopy=s.copy()
	ampd= doMachine([inp[3],ampc],scopy,0)[0][0]
	scopy=s.copy()
	ampe= doMachine([inp[4],ampd],scopy,0)[0][0]
	if best==0 or ampe > best:
		best= ampe
		bestperm= inp
print("Part 1",bestperm,best)
inputs=permutations([5,6,7,8,9])
best=0
bestcomb=[]
for inp in inputs:
	ampa=s.copy()
	ampb=s.copy()
	ampc=s.copy()
	ampd=s.copy()
	ampe=s.copy()
	#print(inp)
	inpa=[inp[0],0]
	inpb=[inp[1]]
	inpc=[inp[2]]
	inpd=[inp[3]]
	inpe=[inp[4]]
	posa=0
	posb=0
	posc=0
	posd=0
	pose=0
	while True:
		#print(inpa)
		(out,posa)= doMachine(inpa,ampa,posa)
		for o in out:
			inpb.append(o)
		(out,posb)= doMachine(inpb,ampb,posb)
		for o in out:
			inpc.append(o)
		(out,posc)= doMachine(inpc,ampc,posc)
		for o in out:
			inpd.append(o)
		(out,posd)= doMachine(inpd,ampd,posd)
		for o in out:
			inpe.append(o)
		(out,pose)= doMachine(inpe,ampe,pose)
		for o in out:
			inpa.append(o)
		if pose == -1:
			break
	if inpa[0] > best:
		best= inpa[0]
		bestcomb=inp
print("Part 2",bestcomb,best)
