from collections import deque
import copy
file = "Day13/input.txt"

# read file
grid = []

with open(file,'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        grid.append(list(line))

directions = deque(['^','>','v','<'])

class Car:
    position=[0,0]
    direction=""
    count=-1
    def __init__(self, position, direction):
        self.position=position
        self.direction=direction

    def getdirection(self):
        while directions[0]!=self.direction:
            directions.rotate(1)
        dir = directions[self.count]
        self.direction=dir
        self.count += 1
        if self.count==2:
            self.count=-1
        return dir

def findcarts(grid):
    return [ Car([i,j],grid[i][j]) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] in ['>','^','<','v'] ]

cars = findcarts(grid)
#print(cars)

# get underlying grid
startgrid=copy.deepcopy(grid)
actual = copy.deepcopy(grid)
for car in cars:
    x,y = car.position[0], car.position[1]
    if car.direction=='^' or car.direction=='v':
        actual[x][y]='|'
    else:
        actual[x][y]='-'

def occupied(char):
    if char in ['^','>','v','<']:
        return True
    else:
        return False

def movecarts(current):
    newgrid = copy.deepcopy(actual)
    cars.sort(key = lambda x: (x.position[0], x.position[1]))
    #print([car.position for car in cars])
    for car in cars:
        x,y = car.position[0], car.position[1]
        if car.direction=='v':
            car.position[0]+=1
            if newgrid[x+1][y]=='|':
                newgrid[x+1][y]='v'
            elif occupied(current[x+1][y]) or occupied(newgrid[x+1][y]):
                print("Crash at ["+str(x+1)+", "+str(y)+"]")
                return None
            elif actual[x+1][y]=='+':
                newgrid[x+1][y]=car.getdirection()
            elif current[x+1][y] == '/':
                newgrid[x+1][y] = '<'
                car.direction='<'
            else:
                newgrid[x][y+1] = '>'
                car.direction='>'
        elif car.direction=='<':
            car.position[1]-=1
            if newgrid[x][y-1]=='-':
                newgrid[x][y-1]='<'
            elif occupied(newgrid[x][y-1]) or occupied(current[x][y-1]):
                print("Crash at "+str(x)+" "+str(y+1))
                return None
            elif actual[x][y-1]=='+':
                newgrid[x][y-1]=car.getdirection()
            elif current[x][y-1]=='/':
                newgrid[x][y-1]='v'
                car.direction='v'
            else:
                newgrid[x][y-1]='^'
                car.direction='^'
        elif car.direction=='^':
            car.position[0]-=1
            if newgrid[x-1][y]=='|':
                newgrid[x-1][y]='^'
            elif occupied(newgrid[x-1][y]) or occupied(current[x-1][y]):
                print("Crash at "+str(x-1)+" "+str(y))
                return None
            elif actual[x-1][y]=='+':
                newgrid[x-1][y]=car.getdirection()
            elif current[x-1][y]=='/':
                newgrid[x-1][y]='>'
                car.direction='>'
            else:
                newgrid[x-1][y]='<'
                car.direction='<'
        else:
            car.position[1]+=1
            if newgrid[x][y+1]=='-':
                newgrid[x][y+1]='>'
            elif occupied(newgrid[x][y+1]) or occupied(current[x][y+1]):
                print("Crash at "+str(x)+" "+str(y))
                return None
            elif actual[x][y+1]=='+':
                newgrid[x][y+1]=car.getdirection()
            elif current[x][y+1]=='/':
                newgrid[x][y+1]='^'
                car.direction='^'
            else:
                newgrid[x][y+1]='v'
                car.direction='v'
    return newgrid

while startgrid is not None:
    startgrid=movecarts(startgrid)
    #print("\n".join(["".join(row) for row in startgrid]))
