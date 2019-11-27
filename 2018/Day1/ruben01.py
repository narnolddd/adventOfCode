from itertools import *

def read_lines():
    import sys
    raw = sys.stdin.read()

    for line in raw.split():
        if not line: continue
        sign = +1 if line[0] == '+' else -1
        n = int(line[1:])
        yield sign * n


def part_one():
    numbers = list(read_lines())
    sum_ = sum(numbers)
    print(sum_)

def part_two():
    numbers = list(read_lines())
    frequencies = set([0])
    sum_ = 0

    for n in cycle(numbers):
        sum_ += n
        if sum_ in frequencies:
            break
        frequencies.add(sum_)

    print(sum_)


if __name__ == "__main__":
    part_two()
