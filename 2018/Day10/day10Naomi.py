import re
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

file = "Day10/input.txt"
regex = "position=<(?P<x>.*), (?P<y>.*)> velocity=<(?P<v1>.*), (?P<v2>.*)>"
p = re.compile(regex)

coords=[]
velocity=[]

with open(file,'r') as f:
    while True:
        line = f.readline().strip()
        if not line:
            break
        match = p.match(line).groupdict()
        coords.append([int(match['x'].strip()),int(match['y'].strip())])
        velocity.append([int(match['v1'].strip()), int(match['v2'].strip())])

coords, velocity = np.array(coords), np.array(velocity)

fig = plt.figure()
ax = plt.axes(xlim=(100,250),ylim=(150,220))
scat, = ax.plot([],[], 'bo', ms=2)


def init():
    scat.set_data([],[])
    return scat

def update(i):
    x = (coords + (10940+i)*velocity)[:,0]
    y = (coords + (10940+i)*velocity)[:,1]
    scat.set_data(x,y)
    return scat

anim = animation.FuncAnimation(fig,update,init_func=init,frames=10000,interval=500)

plt.show()
