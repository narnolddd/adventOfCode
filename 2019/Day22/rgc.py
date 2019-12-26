#!/usr/bin/env python3
import sys,math,numpy
from itertools import permutations 

def reverseCut(n,pos,decklen):
#    print("Reverse cut")
    return (pos+n)%decklen

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		gcd, x, y = egcd(b % a, a)
		return (gcd, y - (b//a) * x, x)

#0123456789
#m=in%d
#m+cd=in
#i=m/n+cd/n
def lcm(n,m):
    return(n*m/math.gcd(n,m))

def reverseIncrement(n,pos,decklen):
#    print ("Reverse inc",n,pos)
    cval=0
    for c in range(n):
        if (c*decklen+pos)%n == 0:
            cval=c
            break
    
    return int(round((cval*decklen+pos)/n))
    
def reverseStack(pos,decklen):
#    print("Reverse stack")
    return decklen-1-pos

def cut(n,deck):
    #print("cut",n)
    deck=deck[n:]+deck[:n]
    return deck

def increment(n,deck):
    d=deck.copy()
    pos=0
    
    for i in range(len(d)):
        deck[(i*n)%len(d)]=d[i]
        #pos= (pos+n)%len(deck)

    return deck
    
def stack(deck):
    deck.reverse()
    return deck

if len(sys.argv) != 2:
    print("Enter input file name as CLI")
    sys.exit()
fp= open(sys.argv[1],"r")
lines= fp.readlines()
fp.close()
decklen=10007
deck=list(range(decklen))

s=sum(deck)
for l in lines:
    #print(deck.index(2019),end=" ")
    l=l.split(" ")
    if (l[0] == "cut"):
        deck= cut(int(l[1]),deck)
    elif l[0] == "deal":
        if l[1] == "with":
            deck= increment(int(l[3]),deck)
        elif l[1] == "into":
            deck= stack(deck)
        else:
            print("Don't know deal")
            sys.exit()
    else:
        print("Don't know shuffle",l)
#print(deck)
print("Part 1",deck.index(2019))
shuffles= 101741582076661
decklen= 119315717514047

mult=1
add=0
for l in lines:
    l=l.split(" ")
    if (l[0] == "cut"):
        add-=int(l[1])
    elif l[0] == "deal":
        if l[1] == "with":
            mult*=int(l[3])
            add*=int(l[3])
        elif l[1] == "into":
            mult*=-1
            add*=-1
            add-=1
        else:
            print("Don't know deal")
            sys.exit()
    else:
        print("Don't know shuffle",l)
    mult= mult%decklen
    add= add%decklen

#print(mult,add)
binrep= list(bin(shuffles)[2:])
powm= mult
powa= add
powfun=[]
for l in range(len(binrep)):
    powfun.append((powm,powa))
    powa=((powm+1)*powa)%decklen
    powm=(powm*powm)%decklen
#print(powm,powa)
mult=1
add= 0
for l in range(len(binrep)):
    if binrep[l] == '1':
        p=len(binrep)-l-1
        mult*=powfun[p][0]
        add*=powfun[p][0]
        add+=powfun[p][1]
    mult=mult%decklen
    add=add%decklen
(_,invmult,_)=egcd(mult,decklen)
newpos=(2020-add)*invmult%decklen
print("Part 2",newpos)
