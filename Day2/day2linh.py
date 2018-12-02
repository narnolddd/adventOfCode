from collections import Counter, defaultdict

# part 1
twos = 0
threes = 0
with open('input.txt') as f:
    for l in f:
        c = Counter(l)
        for v in set(c.values()):
            if v == 2:
                twos += 1
            elif v == 3:
                threes += 1
            else:
                pass

print('Result:', twos * threes)

# part 2

with open('input.txt') as f:
    lines = f.readlines()


def hamming(a, b):
    dist = 0
    substr = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            substr += a[i]
        else:
            dist += 1
    return dist, substr

min_substr = None

for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        dist, substr = hamming(lines[i], lines[j])
        if dist == 1:
            print(substr)
            break

# part 2 a bit better ?

class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.frequency = 1

    def increment(self):
        self.frequency += 1

def get_child(parent, cvalue):
    if cvalue in parent.children:
        parent.children[cvalue].increment()
    else:
        parent.children[cvalue] = Node(cvalue)
    return parent.children[cvalue]

head = {}

# fill up everything with lines of input
with open('input.txt') as f:
    for l in f:
        head_node_str = l[0]
        if head_node_str not in head:
            head[head_node_str] = Node(head_node_str)
        current_head = head[head_node_str]
        for s in l[1:]:
            current_head = get_child(current_head, s)

# traverse tree and find substr with hamming distance = 1
# todo :)
def get_minimum_hamming(node, distance, substring):
    if not node.children:
        new_distance += 1 if self.frequency == 1 else 0
        return distance, [substring]
    else:
        substrings = []
        for child_str, child_node in node.children.items():
            distance, substr = get_minimum_hamming(child_node,
                                                   distance + add_dist,
                                                   substring + add_substr)
