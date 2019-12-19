import copy
from itertools import cycle
from recordclass import recordclass

Program = recordclass('Program', 'mem pos inputs running rbase')
Robot = recordclass('Robot', 'pos grid')

ADD = 1
MUL = 2
INPUT = 3
OUTPUT = 4
JIT = 5
JIF = 6
LTE = 7
EQ = 8
MRB = 9

WALL = 0
MOVED = 1
OXYGEN = 2

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

def run_program(program):
    while True:
        opcode = str(program.mem[program.pos])
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
            program.running = False 
            return None
            
        if op != MRB:
            if p1 == 0:
                v1 = int(program.mem[ int(program.mem[program.pos + 1]) ])
            elif p1 == 1:
                v1 = int(program.mem[ program.pos + 1 ])
            elif p1 == 2:
                addr = program.rbase + int(program.mem[program.pos + 1])
                v1 = int(program.mem[addr])
            if op != OUTPUT and op != INPUT:
                if p2 == 0:
                    v2 = int(program.mem[ int(program.mem[program.pos + 2]) ])
                elif p2 == 1:
                    v2 = int(program.mem[ program.pos + 2 ])
                elif p2 == 2:
                    addr = program.rbase + int(program.mem[program.pos + 2])
                    v2 = int(program.mem[addr])

                if p3 == 0:
                    outp = int(program.mem[program.pos + 3])
                elif p3 == 1:
                    outp = program.pos + 3
                else:
                    outp = program.rbase + int(program.mem[program.pos + 3])

        if op == MUL:
            program.mem[outp] = v1 * v2
            program.pos += 4
        elif op == ADD:
            program.mem[outp] = v1 + v2
            program.pos += 4
        elif op == INPUT:
            if p1 == 0:
                addr = int(program.mem[program.pos + 1])
            elif p1 == 1:
                addr = program.pos + 1
            else:
                addr = program.rbase + int(program.mem[program.pos + 1])
            program.mem[addr] = program.inputs.pop()
            program.pos += 2
        elif op == OUTPUT:
            program.pos += 2
            return v1
        elif op == JIT:
            if v1:
                program.pos = v2
            else:
                program.pos += 3
        elif op == JIF:
            if not v1:
                program.pos = v2
            else:
                program.pos += 3
        elif op == LTE:
            if v1 < v2:
                program.mem[outp] = 1
            else:
                program.mem[outp] = 0
            program.pos += 4
        elif op == EQ:
            if v1 == v2:
                program.mem[outp] = 1
            else:
                program.mem[outp] = 0
            program.pos += 4
        elif op == MRB:
            if p1 == 0:
                addr = int(program.mem[program.pos + 1])
            elif p1 == 1:
                addr = program.pos + 1
            else:
                addr = program.rbase + int(program.mem[program.pos + 1])
            program.rbase += int(program.mem[addr])
            program.pos += 2


f = open("input", "r")
mem = f.read().strip('\n').split(',')

def load_program(mem):
    nmem = [x for x in mem]
    for i in range(len(mem), len(mem) + 10000):
        nmem.append('0')
    return nmem

def print_points(points, n):
    x = y = 0
    while y < n+1:
        for i in range(0, (x + 1) * 2):
            p = (i, y)
            if p in points:
                print (points[p], end = "")
            else:
                print (".", end="")
        y += 1
        x += 1
        print()


x = y = 0
total = 0
pts = {}
found = False
seq = False
lastx = 0
while y < 50:
    program = Program(load_program(mem), 0, [y, x], True, 0)
    out = run_program(program)
    if out == 1:
        pts[(x, y)] = '#'
        
        if x < 50:
            total += 1
        
        if not seq:
            lastx = x
            seq = True
        x += 1
        continue
    else:
        if seq:
            y += 1
            x = lastx - 5
            if x < 0:
                x = 0
            seq = False
        else:
            if y == 1 or y == 2 or y == 3:
                y += 1
                x = 0
                continue
            x += 1


print (total)


def search_first(y):  
    x = y
    out = 0
    while not out:
        program = Program(load_program(mem), 0, [y, x], True, 0)
        out = run_program(program)
        if not out:
            x += 1
    return x

i = 900
found = False

while i < 1000:
    
    x = search_first(i)
    look_h = x + 99
    look_v = i + 99
    program = Program(load_program(mem), 0, [i, look_h], True, 0)
    h = run_program(program)

    while h:
        program = Program(load_program(mem), 0, [look_v, x], True, 0)
        v = run_program(program)
        if not v:
            x += 1
            look_h = x + 99
            program = Program(load_program(mem), 0, [i, look_h], True, 0)
            h = run_program(program)
        else:
            found = True
            print (x * 10000 + i)
            break

    if found:
        break
    i += 1

f.close()