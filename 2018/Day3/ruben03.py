from itertools import *
import re
import numpy as np
line_re = r'\#(?P<id>\d+) @ (?P<left>\d+),(?P<top>\d+): (?P<width>\d+)x(?P<height>\d+)'
line_re = re.compile(line_re)

class Square:
    def __init__(self, id, left, top, width, height):
        self.id = int(id)
        self.topleft = (int(left), int(top))
        self.width = int(width)
        self.height = int(height)


    @property
    def surface(self):
        return self.width * self.height


    def __repr__(self):
        return '#{} @ {},{}: {}x{}'.format(
            self.id, self.topleft[0], self.topleft[1], self.width, self.height
        )

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.counts = np.zeros((width, height))

    def count_square(self, s):
        # for x in range(s.width):
        test = np.zeros_like(self.counts)
        test[s.topleft[1]:s.topleft[1]+s.height,
             s.topleft[0]:s.topleft[0]+s.width] += 1
        # print(np.count_nonzero(test > 0), s.surface)
        assert np.count_nonzero(test > 0) == s.surface

        self.counts[s.topleft[1]:s.topleft[1]+s.height,
             s.topleft[0]:s.topleft[0]+s.width] += 1

    def num_overlap(self):
        return np.count_nonzero(self.counts > 1)


def read_lines():
    import sys
    raw = sys.stdin.read()

    for line in raw.splitlines():
        if not line: continue
        yield line

def read_squares():
    for line in read_lines():
        m = line_re.match(line)
        square = Square(**m.groupdict())
        yield square

def part_one():
    canvas = Canvas(1000, 1000)
    for square in read_squares():
        canvas.count_square(square)
    print(canvas.num_overlap())

def part_two():
    canvas = Canvas(1000, 1000)
    squares = list(read_squares())
    for square in squares:
        canvas.count_square(square)
    for s in squares:
        if (canvas.counts[
             s.topleft[1]:s.topleft[1]+s.height,
             s.topleft[0]:s.topleft[0]+s.width] == 1).all():
            print(s)
            break


if __name__ == "__main__":
    part_two()


