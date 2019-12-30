import numpy as np
import math

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

reactions = {}
index = {}
products = {}

file = "Day14/inputnaomi.txt"
ind=0

with open(file,'r') as f:
    for _, line in enumerate(f):
        ingredients, product = line.split("=>")
        product = product.strip()
        parts = ingredients.split(',')

        amount, el = product.split()
        index[el]=ind
        products[ind]=el
        reactions[el] = [int(amount), [p.strip() for p in parts]]
        ind+=1

needed=np.zeros(len(index.keys()),dtype=int)
needed[index['FUEL']]=1
ore=0

while True:
    if np.all(needed<=0):
        break
    for i in range(len(needed)):
        if needed[i]>0:
            el, amount = products[i], math.ceil(float(needed[i])/reactions[products[i]][0])
            for part in reactions[el][1]:
                p = part.split()
                am, ing = int(p[0]), p[1]
                if ing == "ORE":
                    ore+=am*amount
                    continue
                needed[index[ing]]+=am*amount
            needed[i]-=reactions[products[i]][0]*amount

part1_ore = ore
print("Part 1: "+str(part1_ore))

def how_many_ore(fuel):
    needed=np.zeros(len(index.keys()),dtype=int)
    needed[index['FUEL']]=fuel
    ore = 0
    while True:
        if np.all(needed<=0):
            break
        for i in range(len(needed)):
            if needed[i]>0:
                el, amount = products[i], math.ceil(float(needed[i])/reactions[products[i]][0])
                for part in reactions[el][1]:
                    p = part.split()
                    am, ing = int(p[0]), p[1]
                    if ing == "ORE":
                        ore+=am*amount
                        continue
                    needed[index[ing]]+=am*amount
                needed[i]-=reactions[products[i]][0]*amount
    return ore

init_guess = int(1000000000000/part1_ore)
guesses = range(init_guess,2*init_guess)

while True:
    lb, ub, mb, = guesses[0], guesses[len(guesses)-1], guesses[int(len(guesses)/2)]
    if lb == mb or mb == ub:
        break
    if how_many_ore(mb)<=1000000000000:
        guesses = range(mb,ub)
    else:
        guesses = range(lb,mb)

print("Part 2: "+str(mb))
