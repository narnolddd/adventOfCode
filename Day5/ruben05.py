def read_lines():
    import sys
    raw = sys.stdin.read()

    for line in raw.splitlines():
        if not line: continue
        yield line

capital_diff = abs(ord('a') - ord('A'))
def reacts_with(a, b):
    return abs(ord(a) - ord(b)) == capital_diff


def react_polymer(polymer):
    stack = []

    for char in polymer:
        if stack and reacts_with(char, stack[-1]):
            stack.pop()
        else:
            stack.append(char)
    return len(stack)


def part_one():
    polymer = next(read_lines())
    print(react_polymer(polymer))


def part_two():
    polymer = next(read_lines())

    import re
    polymers = [re.sub('[{}{}]'.format(chr(char_ord), chr(char_ord).upper()), '', polymer) \
                for char_ord in range(ord('a'), ord('z')+1)]
    lengths = [react_polymer(p) for p in polymers]
    print(min(lengths))


if __name__ == "__main__":
    part_two()
