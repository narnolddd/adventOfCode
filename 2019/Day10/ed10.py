from itertools import combinations 
import math

def check_visibility(points, pair):
    p1, p2 = pair
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    if x1 > x2:
        deltax = x1 - x2
        checkpx = range(x1-1, x2, -1)
    else:
        deltax = x2 - x1
        checkpx = range(x1+1, x2)

    if y1 > y2:
        deltay = y1 - y2
        checkpy = range(y1-1, y2, -1)
    else:
        deltay = y2 - y1
        checkpy = range(y1+1, y2)

    # They are neighbors

    angle = math.atan2(deltax, deltay)
    degs = math.degrees(angle) 

    if not len(checkpx) and not len(checkpy):
        points[p1] += 1
        points[p2] += 1
        detected[p1].append((p2, degs))
        detected[p2].append((p1, degs))
        return

    blocked = False

    if x1 - x2 == 0:
        # Vertical line
        for y in checkpy:
            p = (x1, y)
            if p in points:
                blocked = True
    elif y1 - y2 == 0:
        for x in checkpx:
            p = (x, y1)
            if p in points:
                blocked = True
    else:
        m = (y1 - y2) / (x1 - x2)
        for x in checkpx:
            for y in checkpy:
                p = (x, y)
                slope_inter = m * (x - x1) + y1
                if y == slope_inter and p in points:
                    blocked = True

    if not blocked:
        points[p1] += 1
        points[p2] += 1
        detected[p1].append((p2, degs))
        detected[p2].append((p1, degs))



f = open("input", "r")
lines = f.readlines()

points = {}
detected = {}
for y in range(0, len(lines)):
    l = lines[y]
    for x in range(0, len(l)):
        if l[x] == '#':
            pair = (x, y)
            points[pair] = 0
            detected[pair] = []


pairs = combinations([p for p in points], 2) 

for pair in list(pairs):
    check_visibility(points, pair)

largest = -1
lp = None
for a in points:
    if points[a] > largest:
        largest = points[a]
        lp = a

print(largest)

visible = sorted(detected[lp], key=lambda tup: tup[1])

final = []
for v in visible:
    p = v[0]
    deg = v[1]
    # First quadrant
    if lp[0] - p[0] <= 0 and lp[1] - p[1] >= 0:
        ndeg = deg
    # Second quadrant
    elif lp[0] - p[0] <= 0 and lp[1] - p[1] <= 0:    
        ndeg = deg + 90
    # Third quadrant
    elif lp[0] - p[0] >= 0 and lp[1] - p[1] <= 0:    
        ndeg = 270 - deg
    else:
        ndeg = 360 - deg

    final.append((p, ndeg))

final = sorted(final, key=lambda tup: tup[1])

item = final[199][0]
print (item[0] * 100 + item[1])

f.close()