import numpy as np

file = "Day3/inputnaomi.txt"

with open(file,'r') as f:
    wires = [row.split(',') for row in f.readlines()]
    f.close()

def intersection_present(start1, finish1, start2, finish2):
    xint, yint = 0,0
    if start1[0]==finish1[0]:
        if start2[0]==finish2[0]:
            return False, [xint, yint]
        xint=start1[0]
        yint=start2[1]
        if min(start2[0],finish2[0]) <= xint and xint <= max(start2[0],finish2[0]):
            if min(start1[1],finish1[1]) <= yint and yint <= max(start1[1],finish1[1]):
                #print([xint,yint,manhattan([xint,yint])])
                return True, [xint,yint]
    if start1[1]==finish1[1]:
        if start2[1]==finish2[1]:
            return False, [xint, yint]
        yint=start1[1]
        xint=start2[0]
        if min(start1[0],finish1[0]) <= xint and xint <= max(start1[0],finish1[0]):
            if min(start2[1],finish2[1]) <= yint and yint <= max(start2[1],finish2[1]):
                #print([xint,yint,manhattan([xint,yint])])
                return True, [xint,yint]
    return False, [xint, yint]

def manhattan(x):
    return abs(x[0])+abs(x[1])

wire1_coords = []
wire2_coords = []

def traverse_wire(wire,nrows):
    current=[0,0]
    wire_coords=[]
    nsteps=0
    for line in wire[:nrows]:
        line.strip()
        wire_coords.append(current.copy())
        if line[0]=="U":
            current[1]+=int(line[1:])
        elif line[0]=="D":
            current[1]-=int(line[1:])
        elif line[0]=="R":
            current[0]+=int(line[1:])
        else:
            current[0]-=int(line[1:])
        nsteps+=int(line[1:])
    wire_coords.append(current.copy())
    return wire_coords, nsteps

# Part 1
wire1_coords=traverse_wire(wires[0],len(wires[0]))[0]
wire2_coords=traverse_wire(wires[1], len(wires[1]))[0]

def get_intersections(wire1,wire2):
    return [intersection_present(wire1[i],wire1[i+1],wire2[j],wire2[j+1]) \
 for i in range(len(wire1)-1) for j in range(len(wire2)-1)]

intersections=get_intersections(wire1_coords,wire2_coords)

true_intersections=[[intersections[i][1], manhattan(intersections[i][1])] for i in range(len(intersections)) if intersections[i][0]==True]

true_intersections.sort(key = lambda x: x[1])

print(true_intersections[0])

min_steps=-1
for i in range(len(wire1_coords)):
    for j in range(len(wire2_coords)):
        w1,nsteps1 = traverse_wire(wires[0],i)
        w2,nsteps2= traverse_wire(wires[1],j)
        ints = get_intersections(w1,w2)
        true_ints=[ints[r][1] for r in range(len(ints)) if ints[r][0]==True]
        if len(true_ints)>0:
            print(true_ints)
