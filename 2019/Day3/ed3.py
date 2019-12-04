from collections import namedtuple
Point = namedtuple('Point', 'x y path steps')

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def check_colision(grid, colisions, pos, pnum, steps):
    if pos in grid:
        if grid[pos].path != pnum:
            colisions.append( (grid[pos], Point(pos[0], pos[1], pnum, steps)) )
    else:     
        grid[newpos] = Point (newpos[0], newpos[1], pnum, steps)

f = open('input.txt', 'r')

paths = [x for x in f.readlines()]

grid = {}
grid[(0,0)] = Point(0, 0, -1, 0)
colisions = []

pnum = 1
for path in paths:
    moves = path.strip('\n').split(',')
    print("moves is: "+str(moves))
    pos = (0, 0)
    steps = 0
    for m in moves:
        d = m[0]
        inc = int(m[1:])
        for i in range(0, inc):
            steps += 1
            if d == 'U':
                newpos = (pos[0], pos[1] + 1)
            elif d == 'D':
                newpos = (pos[0], pos[1] - 1)
            elif d == 'L':
                newpos = (pos[0] - 1, pos[1])
            elif d == 'R':
                newpos = (pos[0] + 1, pos[1])
            check_colision(grid, colisions, newpos, pnum, steps)
            pos = newpos 
    pnum += 1 

dist = min( [distance((x[0].x, x[1].y), (0,0)) for x in colisions] )
print(dist)

st = []
for c in colisions:
    st.append(c[0].steps + c[1].steps)

print (min(st))

f.close()