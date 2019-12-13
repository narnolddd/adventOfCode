import copy
from itertools import permutations 
from recordclass import recordclass

Program = recordclass('Program', 'mem pos inputs running rbase')

ADD = 1
MUL = 2
INPUT = 3
OUTPUT = 4
JIT = 5
JIF = 6
LTE = 7
EQ = 8
MRB = 9

TILE_EMPTY = 0
TILE_WALL = 1
TILE_BLOCK = 2
TILE_PADDLE = 3
TILE_BALL = 4

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
            inp =  program.inputs.pop()
            print ("INPUT %s" % inp)
            program.mem[addr] = inp
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


def print_state(objects):
    for y in range(0, 26):
        for x in range(0, 43):
            p = (x, y)

            if not p in objects:
                print(" ", end="")
                break

            obj = objects[p]

            if obj == TILE_EMPTY:
                print(" ", end="")
            elif obj == TILE_WALL:
                print("|",  end="")
            elif obj == TILE_BLOCK:
                print("#",  end="")
            elif obj == TILE_BALL:
                print("O",  end="")
            elif obj == TILE_PADDLE:
                print("_",  end="")
        print()

def run(program):
    objects = {}
    obj = []
    while program.running:
        out = run_program(program)
        obj.append(out)
        if (len(obj)) == 3:
            x, y, obj_type = obj
            objects[(x, y)] = obj_type
            obj = []

    return objects


f = open("input", "r")
mem = f.read().strip('\n').split(',')
for i in range(len(mem), len(mem) + 10000):
    mem.append('0')

program = Program(copy.deepcopy(mem), 0, [], True, 0)

objects = run(program)

blocks = [objects[x] for x in objects if objects[x] == TILE_BLOCK]
print(len(blocks))

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

def forecast(pos, direction, maxx, maxy):
    x, y = pos
    print(x, y, maxy-1)
    while y != maxy-1:
        if direction == LEFT:
            x -= 1
            if not x:
                direction = RIGHT
        else:
            x += 1
            if x == maxx:
                direction = LEFT
        y += 1
        print(x, y, maxy-1)
    return x, y

def move_paddle(px, bx):
    if px < bx:
        return [1]
    elif px > bx:
        return [-1]
    else:
        return [0]

def run2(program):
    objects = {}
    obj = []
    score = 0
    paddle = []
    while program.running:
        out = run_program(program)
        obj.append(out)
        if (len(obj)) == 3:
            x, y, obj_type = obj    
            if obj_type == TILE_BALL and len(paddle):
                px, py = paddle 
                program.inputs = move_paddle(px, x)
            objects[(x, y)] = obj_type
            if obj_type == TILE_PADDLE:
                paddle = [x, y]
            if x < 0:
                score = obj_type
            obj = []
    return score


mem[0] = '2'
program = Program(copy.deepcopy(mem), 0, [0], True, 0)

score = run2(program)
print (score)

f.close()