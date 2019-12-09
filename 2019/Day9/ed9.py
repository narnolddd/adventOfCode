import copy
from itertools import permutations 
from recordclass import recordclass

State = recordclass('State', 'mem pos inputs running los')

ADD = 1
MUL = 2
INPUT = 3
OUTPUT = 4
JIT = 5
JIF = 6
LTE = 7
EQ = 8
MRB = 9

def run(mem, inputs, pos, rbase):
    while True:
        opcode = str(mem[pos])
        size = len(opcode)
        op = 0
        p1 = p2 = p3 = 0
        if size < 2:
            op = int(opcode[0])
        else:
            op = int("".join(opcode[-2:]))
            if size == 3:
                p1 = int(opcode[-3]) 
            elif size == 4:
                p1 = int(opcode[-3])
                p2 = int(opcode[-4])
            elif size == 5:
                p1 = int(opcode[-3])
                p2 = int(opcode[-4])
                p3 = int(opcode[-5])

        if op == 99:
            break

        if op != MRB:
            if p1 == 0:
                v1 = int(mem[ int(mem[pos + 1]) ])
            elif p1 == 1:
                v1 = int(mem[ pos + 1 ])
            elif p1 == 2:
                addr = rbase + int(mem[pos + 1])
                v1 = int(mem[addr])
            if op != OUTPUT or op != INPUT:
                if p2 == 0:
                    v2 = int(mem[ int(mem[pos + 2]) ])
                elif p2 == 1:
                    v2 = int(mem[ pos + 2 ])
                elif p2 == 2:
                    addr = rbase + int(mem[pos + 2])
                    v2 = int(mem[addr])

                if p3 == 0:
                    outp = int(mem[pos + 3])
                elif p3 == 1:
                    outp = pos + 3
                else:
                    outp = rbase + int(mem[pos + 3])

        if op == MUL:
            mem[outp] = v1 * v2
            pos += 4
        elif op == ADD:
            mem[outp] = v1 + v2
            pos += 4
        elif op == INPUT:
            if p1 == 0:
                addr = int(mem[pos + 1])
            elif p1 == 1:
                addr = pos + 1
            else:
                addr = rbase + int(mem[pos + 1])
            mem[addr] = inputs.pop()
            pos += 2
        elif op == OUTPUT:
            print(v1)
            pos += 2
        elif op == JIT:
            if v1:
                pos = v2
            else:
                pos += 3
        elif op == JIF:
            if not v1:
                pos = v2
            else:
                pos += 3
        elif op == LTE:
            if v1 < v2:
                mem[outp] = 1
            else:
                mem[outp] = 0
            pos += 4
        elif op == EQ:
            if v1 == v2:
                mem[outp] = 1
            else:
                mem[outp] = 0
            pos += 4
        elif op == MRB:
            if p1 == 0:
                addr = int(mem[pos + 1])
            elif p1 == 1:
                addr = pos + 1
            else:
                addr = rbase + int(mem[pos + 1])
            rbase += int(mem[addr])
            pos += 2

f = open("input", "r")
mem = f.read().strip('\n').split(',')

for i in range(len(mem), len(mem) + 10000):
    mem.append('0')

inputs = [1]
run(mem, inputs, 0, 0)

inputs = [2]
run(mem, inputs, 0, 0)

f.close()