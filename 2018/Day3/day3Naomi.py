from collections import defaultdict
import numpy as np

sqclaims = [[[] for y in range(1000)] for x in range(1000)]
counts = np.zeros((1000,1000),dtype=int)
validclaims = defaultdict(lambda:True)
data=[]

input = "Day3/input.txt"

with open(input,'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        parts = line.strip().split(" ")
        corner = list(map(int,parts[2].strip(":").split(",")))
        dims = list(map(int,parts[3].split("x")))
        claimno = int(parts[0].strip("#"))
        for i in range(dims[0]):
            for j in range(dims[1]):
                x=corner[0]+i
                y=corner[1]+j
                if len(sqclaims[x][y])>0:
                    validclaims[claimno]=False
                    for claim in sqclaims[x][y]:
                        validclaims[claim]=False
                sqclaims[x][y].append(claimno)
                counts[x,y] +=1

print("Number of squares with two or more claims: ")
print((counts>1).sum())
print("ID of valid claim: ")
for i in range(1409):
    if validclaims[i+1]:
        print(i+1)
