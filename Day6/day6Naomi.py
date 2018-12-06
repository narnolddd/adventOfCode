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
        parts=f.readline().strip().split(", ")
        coordinates.append(dict(id=i, x=int(parts[0]), y=int(parts[1])))

gridxmin, gridxmax = min(coordinates,key=lambda x:x['x'])['x'], max(coordinates,key=lambda x:x['x'])['x']
xlen = gridxmax - gridxmin
gridymin, gridymax = min(coordinates,key=lambda x:x['y'])['y'], max(coordinates,key=lambda x:x['y'])['y']
ylen = gridymax - gridymin

print(manhatton_distance(0,0,3,5))

def closest(coord):
    x,y=coord[0],coord[1]
    nearest=[]
    distances = [dict(id=row['id'],dist=manhatton_distance(row['x'],row['y'],x,y)) for row in coordinates]
    distances = sorted(distances,key=itemgetter('dist'))
    d0=distances[0]['dist']
    nearest.append(distances[0]['id'])
    distances.pop(0)
    while True:
        if distances[0]['dist']==d0:
            nearest.append(distances[0]['id'])
            distances.pop(0)
        else:
            break
    return nearest

grid = [[[i,j] for j in range(gridymin,gridymax+1)] for i in range(gridxmin,gridxmax+1)]
occupants = [[[]for y in range(ylen+1)] for x in range(xlen+1)]

# do borders
is_infinite=defaultdict(lambda:False)
for i in range(xlen+1):
    nearest_top = closest(grid[i][0])
    if len(nearest_top)==1:
        is_infinite[nearest_top[0]]=True
    nearest_bottom = closest(grid[i][ylen])
    if len(nearest_bottom)==1:
        is_infinite[nearest_bottom[0]]=True
for j in range(ylen+1):
    nearest_left = closest(grid[0][j])
    if len(nearest_left)==1:
        is_infinite[nearest_left[0]]=True
    nearest_right = closest(grid[xlen][j])
    if len(nearest_right)==1:
        is_infinite[nearest_right[0]]=True


# fill the square
for i in range(xlen+1):
    for j in range(ylen+1):
        nearest = closest(grid[i][j])
        if len(nearest)>1:
            occupants[i][j]="-1"
        else:
            occupants[i][j]=str(nearest[0])
        if is_infinite[int(occupants[i][j])]:
            occupants[i][j]="inf"

flattened_occupants=[y for x in occupants for y in x]

areas=ct(flattened_occupants)

sortedareas = sorted(areas,reverse=True)
print(sortedareas)
print(areas)
print(is_infinite)
