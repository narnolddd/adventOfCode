import numpy as np
import re

regex = 'position=<[ ]*(?P<x>\-*\d+),[ ]*(?P<y>\-*\d+)> velocity=<[ ]*(?P<vx>\-*\d+),[ ]*(?P<vy>\-*\d+)>'
p = re.compile(regex)
data = []
n_points = 0
with open('input.txt') as f:
    for l in f:
        match = p.match(l.strip()).groupdict()
        data.append(
            list(map(int, [match['x'], match['y'], match['vx'], match['vy']])))
        n_points += 1

points = np.zeros((n_points, 2))
velocity = np.zeros((n_points, 2))
for i, [x, y, vx, vy] in enumerate(data):
    points[i][0] = x
    points[i][1] = y
    velocity[i][0] = vx
    velocity[i][1] = vy

def get_size(points):
    min_ = points.min(0)
    max_ = points.max(0)
    return (max_ - min_).prod()

def draw(points):
    min_ = points.min(0)
    max_ = points.max(0)
    points -= min_
    diff = max_ - min_ + 1
    draw = [['_' for _ in range(int(diff[0]))] for _ in range(int(diff[1]))]
    for i in range(n_points):
        draw[int(points[i][1])][int(points[i][0])] = '#'
    print('\n'.join([''.join(d) for d in draw]))

min_size = get_size(points)
min_points = points.copy()

for i in range(20000):
    points += velocity
    s = get_size(points)
    if s < min_size:
        min_size = s
        min_points = points.copy()
        print(i, min_size)

draw(min_points)
