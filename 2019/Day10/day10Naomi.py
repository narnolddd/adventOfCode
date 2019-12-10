from collections import defaultdict
from math import gcd
import operator
file="Day10/inputnaomi.txt"

with open(file,'r') as f:
    grid=f.read().splitlines()

nrow, ncol = len(grid),len(grid[0])

gradients=defaultdict(lambda: False)
gradients[(1,0)]=True
gradients[(0,1)]=True

for x in range(-nrow,nrow):
    for y in range(ncol):
        if x==0 or y==0:
            continue
        xjump, yjump = int(x/gcd(x,y)), int(y/gcd(x,y))
        if gradients[(xjump,yjump)]==False:
            gradients[(xjump,yjump)]=True

gradients=[list(g) for g in gradients.keys() if gradients[g]==True]

asteroid_pos = [(i,j) for i in range(nrow) for j in range(ncol) if grid[i][j]=='#']

asteroid_sights=defaultdict(lambda: 0)

for pos in asteroid_pos:
    for g in gradients:
        p=[pos[0],pos[1]]
        while True:
            p = [p[0]+g[0],p[1]+g[1]]
            if p[0]>=nrow or p[1]>=ncol or p[0]<0:
                break
            if grid[p[0]][p[1]]=="#":
                asteroid_sights[pos]+=1
                asteroid_sights[(p[0],p[1])]+=1
                break

max_sights=0

for a in asteroid_sights.keys():
    sights = asteroid_sights[a]
    if sights>max_sights:
        max_sights, max_arg = sights, a

print("Part 1:"+str(max_sights)+" ("+str(max_arg[0])+", "+str(max_arg[1])+")")

gradients = [g for g in gradients if g[1]!=0]

gradients.sort(key = lambda x: float(x[0]/x[1]))

gradients = [[-1,0]]+gradients
gradients+=[[-g[0],-g[1]] for g in gradients]


killed_asteroids=[]

def kill_asteroid(pos,grid):
    new_grid = grid[:pos[0]]+[grid[pos[0]][:pos[1]]+"."+grid[pos[0]][pos[1]+1:]]+grid[pos[0]+1:]
    return new_grid

index=0
pos=[max_arg[0],max_arg[1]]
while True:
    g=gradients[index%len(gradients)]
    p=pos
    while True:
        p=[p[0]+g[0],p[1]+g[1]]
        if p[0]>=nrow or p[1]>=ncol or p[0]<0 or p[1]<0:
            break
        if grid[p[0]][p[1]]=="#":
            killed_asteroids.append([p[0],p[1]])
            grid=kill_asteroid([p[0],p[1]],grid)
            break
    index = index+1
    if len(killed_asteroids)==200:
        break

print(killed_asteroids[-1])
