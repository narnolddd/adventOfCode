from functools import *
from itertools import *
import operator
from typing import *

def main():
    program = list(map(int, input().split(',')))

    # Weird hacks they ask us to do
    program[1] = 12
    program[2] = 2

def main2():
    original = list(map(int, input().split(',')))

    REQUESTED = 19690720

    for verb, noun in product(range(100), range(100)):
        program = original.copy()
        program[1] = noun
        program[2] = verb
        out = run_program(program)
        if out == REQUESTED: break

    print(verb, noun)
    print(100 * noun + verb)

def run_program(program: List[int]):
    # Opcode pointer
    pointer = 0
    while True:
        opcode = program[pointer]

        if opcode == 99:
            break

        operand_pointers = (program[pointer+1], program[pointer+2])
        result_pointer = program[pointer+3]
        operands = tuple(program[ptr] for ptr in operand_pointers)

        op = None
        if opcode == 1:
            op = operator.add
        elif opcode == 2:
            op = operator.mul
        assert op is not None

        result = reduce(op, operands)
        program[result_pointer] = result

        pointer += 4

    return program[0]


if __name__ == "__main__":
    main2()
