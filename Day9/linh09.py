from collections import deque

circle = deque()
circle.append(0)
current = 0
n_player = 9
n_marbles = 25
# n_marbles *= 100
points = [0 for _ in range(n_player)]

def add(n, circle, current, current_player):
    if n % 23 == 0:
        circle.rotate(7)
        removed = circle.pop()
        circle.rotate(-1)
        points[current_player] += removed + n
    else:
        circle.rotate(-1)
        circle.append(n)
    return circle

def print_(circle):
    circle_ = list(map(str, list(circle.copy())))
    circle_[-1] = '(' + circle_[-1] + ')'
    print(' '.join(circle_))

# print_(circle, current)

for i in range(1, n_marbles + 1):
    current_player = (i - 1) % n_player
    circle = add(i, circle, current, current_player)
    print_(circle)

print(max(points))
