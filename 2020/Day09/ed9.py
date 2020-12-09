import itertools

preamble_size = 25

f = open("edinput.txt")
numbers = list(map(lambda x: int(x), f.readlines()))

preamble = numbers[:preamble_size]
comb_sum = set(map(lambda x: sum(x), itertools.combinations(preamble, 2)))

i = 0
invalid_num = None
for n in numbers[preamble_size:]:
    if n not in comb_sum:
        invalid_num = n
        break
    preamble[i%preamble_size] = n
    # I could update only the new sum, but I would have to remove the old one
    # Not today, this is fast enough.
    comb_sum = set(map(lambda x: sum(x), itertools.combinations(preamble, 2)))
    i += 1

print(invalid_num)


possible = [n for n in numbers if n < invalid_num]

def solve2(possible):
    i = 0
    num = 0
    while True:
        for n in range(i, len(possible)):
            num += numbers[n]
            if num == invalid_num:
                return max(possible[i:n]) + min(possible[i:n])
            if num > invalid_num:
                break
        num = 0
        i += 1

print(solve2(possible))

f.close()