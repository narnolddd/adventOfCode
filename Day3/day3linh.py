import numpy as np
import re

regex = '#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)'
p = re.compile(regex)
data = []

# read stuff
width = 0
height = 0
with open('input.txt') as f:
    for l in f:
        match = {k: int(v) for k, v in p.match(l).groupdict().items()}
        width = max(width, match['x'] + match['w'] - 1)
        height = max(height, match['y'] + match['h']- 1)
        data.append(match)

# part 1
mat = np.zeros((width, height))

for d in data:
    mat[d['x']:d['x'] + d['w'],
        d['y']:d['y'] + d['h']] += 1

print(mat[mat >= 2].shape[0])

# part 2
for d in data:
    if (mat[d['x']:d['x'] + d['w'], d['y']:d['y'] + d['h']] == 1).all():
        print(d['id'])
        break
