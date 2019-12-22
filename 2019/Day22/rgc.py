#!/usr/bin/env python3
import sys,math,numpy
from itertools import permutations 

def cut(n,deck):
    #print("cut",n)
    deck=deck[n:]+deck[:n]
    return deck

def increment(n,deck):
    d=deck.copy()
    pos=0
    
    for i in range(len(d)):
        deck[pos]=d[i]
        pos+=n
        while pos >=len(deck):
            pos-= len(deck)
    assert sum(deck) == sum(d)
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

deck=list(range(10007))
s=sum(deck)
for l in lines:
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
print(deck.index(2019))
