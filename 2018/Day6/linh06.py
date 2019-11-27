import math

coords = []
max_col = 0
max_row = 0

with open('input.txt') as f:
    for l in f:
        coord = list(map(int, map(str.strip, l.strip().split(','))))
        max_col = max(max_col, coord[0])
        max_row = max(max_row, coord[1])
        coords.append(coord)

max_col += 1
max_row += 1


def manhattan_distance(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


def min_dist_node(loc, coords):
    min_dist = 1e31
    min_i = []
    for i, coord in enumerate(coords):
        md = manhattan_distance(coord, loc)
        if md < min_dist:
            min_dist = md
            min_i = [i]
        elif md == min_dist:
            min_i.append(i)
    return min_i, min_dist

if __name__ == '__main__':
    grid = [['.' for _ in range(max_col)] for _ in range(max_row)]
    for i, coord in enumerate(coords):
        grid[coord[1]][coord[0]] = (i // 26 + 1) * chr(65 + i % 26)

    for r in range(max_row):
        for c in range(max_col):
            if grid[r][c] == '.':
                min_dist_n, min_dist = min_dist_node([c, r], coords)
                if len(min_dist_n) == 1:
                    grid[r][c] = (min_dist_n[0] // 26 + 1) * \
                                  chr(97 + min_dist_n[0] % 26)

outside_coords = set()

for r in range(max_row):
    if grid[r][0] != '.':
        c_ = list(grid[r][0].lower())
        nid = (len(c_) - 1) * 26 + ((ord(c_[0]) - 97) % 26)
        outside_coords.add(nid)
    if grid[r][-1] != '.':
        c_ = list(grid[r][-1].lower())
        nid = (len(c_) - 1) * 26 + ((ord(c_[0]) - 97) % 26)
        outside_coords.add(nid)

for c in range(max_col):
    if grid[0][c] != '.':
        c_ = list(grid[0][c].lower())
        nid = (len(c_) - 1) * 26 + ((ord(c_[0]) - 97) % 26)
        outside_coords.add(nid)
    if grid[-1][c] != '.':
        c_ = list(grid[-1][c].lower())
        nid = (len(c_) - 1) * 26 + ((ord(c_[0]) - 97) % 26)
        outside_coords.add(nid)

def count_char(grid, c):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == c:
                count += 1
    return count
max_n = 0
print(outside_coords)
for i in range(len(coords)):
    if i not in outside_coords:
        c_ = (i // 26 + 1) * chr(97 + i % 26)
        c_count = count_char(grid, c_)
        print(c_, c_count)
        max_n = max(max_n, c_count)
print(max_n + 1)

c_10000 = 0
thres = 10000

for r in range(max_row):
    for c in range(max_col):
        dist = 0
        for i, coord in enumerate(coords):
            md = manhattan_distance(coord, (c, r))
            dist += md
            if dist > thres:
                break
        if dist < thres:
            c_10000 += 1

print(c_10000)
