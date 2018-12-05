import re
from collections import defaultdict
import numpy as np

file = "day5/input.txt"
polymer = ""

with open(file,'r') as f:
    polymer=f.readline()

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetcap= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter2num = defaultdict(lambda:0)
for i in range(26):
    letter2num[alphabet[i]]=i+1
    letter2num[alphabetcap[i]]=-i-1

def vec2string(vect):
    word = ""
    for v in vect:
        if v > 0:
            word+=alphabet[int(v-1)]
        else:
            word+=alphabetcap[int(-1-v)]
    return word

def string2vect(word):
    vec = np.zeros(len(word))
    for i in range(len(word)):
        vec[i]=letter2num[word[i]]
    return vec

def reducevec(vec):
    length = len(vec)
    print(length)
    while True:
        i=0
        while True:
            if i>=len(vec)-1:
                break
            if vec[i]==-1*vec[i+1]:
                ind2remove=[i,i+1]
                vec = np.delete(vec,ind2remove)
                #print(vec)
            else:
                i+=1
        if len(vec)==length:
            break
        else:
            length=len(vec)
            #print(length)
    return vec

test = string2vect('hHheLloOE')
testreduced=reducevec(test)
print(vec2string(testreduced))
print(len(testreduced))

polymervec = string2vect(polymer)
reducedvec = reducevec(polymervec)
print(vec2string(reducedvec))
print(len(reducedvec)-1) #Why minus 1???
