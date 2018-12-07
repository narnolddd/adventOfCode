from collections import defaultdict
import re

regex = 'Step (?P<source>\w) must be finished before step (?P<target>\w) can begin.'
p = re.compile(regex)
data = []
with open('input.txt') as f:
    for l in f:
        match = p.match(l).groupdict()
        data.append((match['source'], match['target']))

edges = defaultdict(list)
incoming_count = defaultdict(int)


for source, target in data:
    edges[source].append(target)
    incoming_count[target] += 1


def part1(edges, incoming_count):
    Q = []

    for e in edges:
        if incoming_count[e] == 0:
            Q.append(e)

    order = ''

    while Q:
        v = sorted(Q)[0]
        order += v
        Q = [v_ for v_ in Q if v_ != v]
        for v_ in edges[v]:
            incoming_count[v_] -= 1
            if incoming_count[v_] == 0:
                Q.append(v_)

    return order


def assign(Q, assignment, t, n_workers=5, step=60):
    while Q and len(assignment) < n_workers:
        Q = sorted(Q)
        v = Q.pop(0)
        assignment.append((t + step - 64 + ord(v), v))
        print('Elf starts on {} at time {}'.format(v, t))
    return Q, assignment


def part2(edges, incoming_count):
    t = 0
    assignment = []
    Q = []
    n_workers = 5
    step = 60

    # sort edges
    for e in edges:
        edges[e] = sorted(edges[e])

    for e in edges:
        if incoming_count[e] == 0:
            Q.append(e)
    Q, assignment = assign(Q, assignment, t, n_workers=n_workers, step=step)

    while Q or assignment:
        assignment = sorted(assignment, key=lambda x:x[0])
        t, v = assignment.pop(0)
        for v_ in edges[v]:
            incoming_count[v_] -= 1
            if incoming_count[v_] == 0:
                Q.append(v_)
        Q, assignment = assign(Q, assignment, t, n_workers=n_workers, step=step)
    return t


print(part1(edges.copy(), incoming_count.copy()))
print(part2(edges, incoming_count))
