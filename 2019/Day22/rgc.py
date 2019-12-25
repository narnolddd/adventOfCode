#!/usr/bin/env python3
import sys,math,numpy
from itertools import permutations 

def reverseCut(n,pos,decklen):
    print("Reverse cut")
    return (pos+n)%decklen
    
    
#0123456789
#m=in%d
#m+cd=in
#i=m/n+cd/n
def lcm(n,m):
    return(n*m/math.gcd(n,m))

def reverseIncrement(n,pos,decklen):
    print("reverse inc")
    base=int(math.floor(pos/n))
    excess=int(round((pos/n-base)*n))
    pos=base
    if excess> 0:
        pos+=decklen*(n-excess)
    #print("Reverse inc",n,pos,excess)
    #print("pos=",pos)
    return int(round(pos/n))
    
def reverseStack(pos,decklen):
    print("Reverse stack")
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
    print(deck.index(2019),end=" ")
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

pos= 6978
plist=[pos]
i=0
while True:
    for l in reversed(lines):
        print(pos,end=" ")
        l=l.split(" ")
        if (l[0] == "cut"):
            pos= reverseCut(int(l[1]),pos,decklen)
        elif l[0] == "deal":
            if l[1] == "with":
                pos= reverseIncrement(int(l[3]),pos,decklen)
            elif l[1] == "into":
                pos= reverseStack(pos,decklen)
            else:
                print("Don't know deal")
                sys.exit()
        else:
            print("Don't know shuffle",l)
        
    sys.exit()
    if pos in plist:
        print("Got loop at ",i,plist.index(pos))
        print(plist[1])
        sys.exit()
    plist.append(pos)
    print(pos)
    i+=1
    
print(pos)
