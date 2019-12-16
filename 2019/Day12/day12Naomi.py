import re
from collections import namedtuple, defaultdict
import numpy as np
import math

moons = [np.zeros(6,dtype=int) for _ in range(4)]
print(moons)
Moon = namedtuple('Moon',['x1','x2','x3','v1','v2','v3'])

regex="<x=(?P<x>.*\d+), y=(?P<y>.*\d+), z=(?P<z>.*\d+)>"
p = re.compile(regex)


file = "Day12/inputnaomi.txt"
with open(file,'r') as f:
    for i,line in enumerate(f):
        line = line.strip()
        #print(line)
        match = {k: v for k, v in p.match(line).groupdict().items()}
        moons[i]=np.array([int(match['x']),int(match['y']),int(match['z']),0,0,0])

initial_moons = [moon for moon in moons]

def apply_gravity(moon1, moon2):
    for dim in range(3):
        if moon1[dim]>moon2[dim]:
            moon1[dim+3]-=1
            moon2[dim+3]+=1

def apply_velocity(moon):
    for dim in range(3):
        moon[dim]+=moon[dim+3]

def simulate_moons():
    for i in range(4):
        for j in range(4):
            if i==j:
                continue
            apply_gravity(moons[i],moons[j])
    for moon in moons:
        apply_velocity(moon)

def get_energy(moon):
    potential = sum(np.abs(moon[:3]))
    kinetic = sum(np.abs(moon[3:]))
    return potential*kinetic

nsteps = 1000

for _ in range(nsteps):
    simulate_moons()

print("Part 1: "+str(sum([get_energy(moon) for moon in moons])))

#get repeats
def get_repeats(moon):
    moons = [mn for mn in initial_moons]
    visited = defaultdict(lambda: -1)
    time = 0
    while True:
        pos = (moon[0],moon[1],moon[2],moon[3],moon[4],moon[5])
        if visited[pos]<0:
            visited[pos]=time
        else:
            print(time)
            return time
        time +=1
        simulate_moons()

repeats = [get_repeats(moon) for moon in initial_moons]
orbit_time=math.lcm(repeats)
