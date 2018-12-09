import re
import numpy as np

file = "Day9/input.txt"
regex = "(?P<nplayers>\d+) players; last marble is worth (?P<nmarbles>\d+) points"
p = re.compile(regex)

with open(file,'r') as f:
    line = f.readline()
    match = p.match(line.strip()).groupdict()
    nplayers, nmarbles = int(match['nplayers']), int(match['nmarbles'])

scores=np.zeros(nplayers)
marblestack=[]

player = 1
current = 1
marblestack.append(0)
marblestack.append(1)
for marble in range(2,nmarbles+1):
    if player == nplayers:
        player = 0
    if marble % 23 == 0:
        index = (current - 7) % len(marblestack)
        scores[player]+=marble+marblestack[index]
        current = index
        marblestack.pop(index)
        player+=1
    else:
        if current+2== len(marblestack):
            marblestack.append(marble)
            current=current+2
            player+=1
        else:
            marblestack.insert((current+2)%len(marblestack),marble)
            current = (current+2)%(len(marblestack)-1)
            player+=1
    if marble < 25:
        print(marblestack, str(current), str(marblestack[current]))

print(max(scores))
