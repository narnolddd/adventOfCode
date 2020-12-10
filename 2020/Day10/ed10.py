import numpy as np
from collections import Counter

def solve2(adapters, calculated):
    if len(adapters) == 1:
        return 1

    count = 0
    last = 4
    if len(adapters) < 4:
        last = len(adapters)

    for i in range(1, last):
        if adapters[i] - adapters[0]  <= 3:
            seq = tuple(adapters[i:])
            if seq not in calculated:
                count += solve2(adapters[i:], calculated)
                calculated[seq] = count
            else:
                count += calculated[seq]
    return count


f = open("edinput.txt")

# Part 1
adapters = [0] + [int(x.strip('\n')) for x in f.readlines()]
adapters.sort()
adapters.append(adapters[-1] + 3)
diff = np.diff(adapters)
counts = Counter(diff)
print(counts[1] * counts[3])

# Part 2
calculated = {}
print(solve2(adapters, calculated))

f.close()