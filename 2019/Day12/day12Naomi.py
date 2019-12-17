import re
from collections import namedtuple, defaultdict
import numpy as np
import math

def lcm(a, b):
    return int(a * b / math.gcd(a, b))

moons = [np.zeros(6,dtype=int) for _ in range(4)]

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

initial_moons = [moon.copy() for moon in moons]

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

repeats = [[[0] for _ in range(6)] for k in range(4)]
times = [[[0] for _ in range(6)] for k in range(4)]

moons = [moon.copy() for moon in initial_moons]
initial_pos = [moon.copy() for moon in moons]
print(initial_pos)

time=0
while True:
    simulate_moons()
    time+=1
    if time > 500000:
        break
    for i in range(4):
        for d in range(6):
            if moons[i][d]==initial_pos[i][d]:
                last_time = times[i][d][-1]
                times[i][d].append(time)
                repeats[i][d].append(int(time-last_time))

def find_period(vec):
    l=len(vec)
    for k in range(1,l):
        shifted = vec[:k]+vec[:]
        repeated = [vec[m]-shifted[m] for m in range(l)]
        if all([repeated[i]==0 for i in range(l)]):
            return sum(vec[-k:])

periods = [find_period(vec[1:]) for moon in repeats for vec in moon]

lcm_orbit=1
for p in periods:
    lcm_orbit=lcm(lcm_orbit,p)

print(lcm_orbit)
