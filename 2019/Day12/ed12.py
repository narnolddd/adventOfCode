from recordclass import recordclass
from itertools import combinations
import numpy as np

def change_velocity(a1, a2, va1, va2):
    if a1 > a2:
        return (va1 - 1, va2 + 1)
    elif a1 < a2:
        return (va1 + 1, va2 - 1)
    return va1, va2

Moon = recordclass('Moon', 'n x y z vx vy vz')

f = open("input", "r")

positions = [x.strip('\n').strip('<').strip('>').split(',') for x in f.readlines()]

moons = []
for n, p in enumerate (positions):
    x = int(p[0][2:])
    y = int(p[1][3:])
    z = int(p[2][3:])
    moons.append(Moon(n, x, y, z, 0, 0, 0))

for i in range (0, 1000):
    pairs = combinations(moons, 2)
    for p in pairs:
        m1, m2 = p
        m1.vx, m2.vx = change_velocity(m1.x, m2.x, m1.vx, m2.vx)
        m1.vy, m2.vy = change_velocity(m1.y, m2.y, m1.vy, m2.vy)
        m1.vz, m2.vz = change_velocity(m1.z, m2.z, m1.vz, m2.vz)

    for m in moons:
        m.x += m.vx
        m.y += m.vy
        m.z += m.vz

energy = 0
for m in moons:
    energy += (abs(m.x) + abs(m.y) + abs(m.z)) * (abs(m.vx) + abs(m.vy) + abs(m.vz))

print (energy)

moons = []
ix = []
iy = []
iz = []
for n, p in enumerate (positions):
    x = int(p[0][2:])
    y = int(p[1][3:])
    z = int(p[2][3:])
    moons.append(Moon(n, x, y, z, 0, 0, 0))
    ix.append((x, 0))
    iy.append((y, 0))
    iz.append((z, 0))


cx = 0
cy = 0
cz = 0
foundx = foundy = foundz = False
while not foundx or not foundy or not foundz:
    pairs = combinations(moons, 2)
    curx = []
    cury = []
    curz = []
    for p in pairs:
        m1, m2 = p
        m1.vx, m2.vx = change_velocity(m1.x, m2.x, m1.vx, m2.vx)
        m1.vy, m2.vy = change_velocity(m1.y, m2.y, m1.vy, m2.vy)
        m1.vz, m2.vz = change_velocity(m1.z, m2.z, m1.vz, m2.vz)

    for m in moons:
        m.x += m.vx
        m.y += m.vy
        m.z += m.vz
        curx.append((m.x, m.vx))
        cury.append((m.y, m.vy))
        curz.append((m.z, m.vz))

    if not foundx:
        cx += 1
        foundx = ix == curx

    if not foundy:
        cy += 1
        foundy = iy == cury

    if not foundz:
        cz += 1
        foundz = iz == curz

steps = np.lcm.reduce([cx, cy, cz]) 
print (steps)

f.close()