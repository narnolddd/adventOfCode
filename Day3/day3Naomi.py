import numpy as np

sqcounts = np.zeros((1000,1000), dtype=int)

input = "Day3/input.txt"

with open(input,'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        parts = line.strip().split(" ")
        corner = list(map(int,parts[2].strip(":").split(",")))
        dims = list(map(int,parts[3].split("x")))
        for i in range(dims[0]):
            for j in range(dims[1]):
                sqcounts[corner[0]+i,corner[1]+j] +=1

overlaps = (sqcounts>1).sum()
print(overlaps)
