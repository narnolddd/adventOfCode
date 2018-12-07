import numpy as np
from operator import itemgetter
from collections import defaultdict
from collections import Counter as ct
file = "Day6/input.txt"

coordinates=[]

def manhatton_distance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

#read the file
with open(file,'r') as f:
    for i, line in enumerate(f):
        parts=line.strip().split(", ")
        coordinates.append(dict(id=i, x=int(parts[0]), y=int(parts[1])))

gridxmin, gridxmax = min(coordinates,key=lambda x:x['x'])['x'], max(coordinates,key=lambda x:x['x'])['x']
xlen = gridxmax - gridxmin
gridymin, gridymax = min(coordinates,key=lambda x:x['y'])['y'], max(coordinates,key=lambda x:x['y'])['y']
ylen = gridymax - gridymin
print(gridxmin, gridymin)
print(gridxmax,gridymax)

def closest(coord):
    x,y=coord[0],coord[1]
    nearest=[]
    distances = [dict(id=row['id'],dist=manhatton_distance(row['x'],row['y'],x,y)) for row in coordinates]
    sorteddistances = sorted(distances,key=itemgetter('dist'))
    print(sorteddistances)
    d0=sorteddistances[0]['dist']
    nearest.append(sorteddistances[0]['id'])
    sorteddistances.pop(0)
    while True:
        if sorteddistances[0]['dist']==d0:
            nearest.append(sorteddistances[0]['id'])
            sorteddistances.pop(0)
        else:
            break
    return nearest

grid = [[[i,j] for j in range(gridymin,gridymax+1)] for i in range(gridxmin,gridxmax+1)]
print(grid[0][0],grid[0][ylen],grid[xlen][0],grid[xlen][ylen])
occupants = [[[]for y in range(ylen+1)] for x in range(xlen+1)]

is_infinite=defaultdict(lambda:False)

# fill the square
for i in range(xlen+1):
    for j in range(ylen+1):
        nearest = closest(grid[i][j])
        if i == 0 or j == 0 or i == xlen or j == xlen:
            if len(nearest)==1:
                occupants[i][j]=str(nearest[0])
                is_infinite[nearest[0]]=True
        if len(nearest)>1:
            occupants[i][j]="-1"
        else:
            occupants[i][j]=str(nearest[0])

flattened_occupants=[y for x in occupants for y in x]
for i in range(len(flattened_occupants)):
    if is_infinite[int(flattened_occupants[i])]:
        flattened_occupants[i]="inf"

areas=ct(flattened_occupants)

sortedareas = sorted(areas,reverse=True)
print(sortedareas)
print(areas)
print(is_infinite)
