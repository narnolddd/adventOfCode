#!/usr/bin/env python3
import sys,math,numpy
from itertools import permutations 

def reverseCut(n,pos,decklen):
    if n >= 0:
        if pos > decklen-1-n:
            return pos-(decklen-1-n)
        return pos+n
    if pos > decklen-1+n:
        return pos+n
    return pos-(decklen-1+n)
            

def reverseIncrement(n,pos,decklen):
    pos+=decklen*pos/(decklen-n)
    pos/=n
    return pos
    
def reverseStack(pos,decklen):
    return decklen-1-pos

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

d2=list(range(10))
d2=increment(7,d2)
print(d2)
for i in range(10):
    print(reverseIncrement(7,d2[i],10))
sys.exit()
decklen=100007
pos=6978
for l in reversed(lines):
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
