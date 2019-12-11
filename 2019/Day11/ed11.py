import copy
from itertools import permutations 
from recordclass import recordclass

Program = recordclass('Program', 'mem pos inputs running rbase')
Robot = recordclass('Robot', 'pos painted state inst npainted face')

ADD = 1
MUL = 2
INPUT = 3
OUTPUT = 4
JIT = 5
JIF = 6
LTE = 7
EQ = 8
MRB = 9

RSEND = 0
RRCV = 1

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

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

def move(direction, pos, face):

    # Turn left
    if direction == 0:
        if face == UP:
            return LEFT, (pos[0] - 1, pos[1])
        elif face == DOWN:
            return RIGHT, (pos[0] + 1, pos[1])
        elif face == RIGHT:
            return UP, (pos[0], pos[1] + 1)
        elif face == LEFT:
            return DOWN, (pos[0], pos[1] - 1)
    else:
        # Turn Right
        if face == UP:
            return RIGHT, (pos[0] + 1, pos[1])
        elif face == DOWN:
            return LEFT, (pos[0] - 1, pos[1])
        elif face == RIGHT:
            return DOWN, (pos[0], pos[1] - 1)
        elif face == LEFT:
            return UP, (pos[0], pos[1] + 1)

def run_robot(robot):
    if robot.state == RSEND:
        robot.state = RRCV
        if robot.pos not in robot.painted:
            return 0
        if robot.painted[robot.pos] == '.':
            return 0
        if robot.painted[robot.pos] == '#':
            return 1
     
    color, direction = robot.inst
    if robot.pos not in robot.painted:
        robot.npainted += 1
    if color == 0:
        robot.painted[robot.pos] = '.'
    else:
        robot.painted[robot.pos] = '#'

    robot.face, robot.pos = move(direction, robot.pos, robot.face)
    robot.state = RSEND
    robot.inst = []

def run(program, robot):
    while program.running:
        inp = run_robot(robot)
        program.inputs.append(inp)
        while len(robot.inst) < 2:
            out = run_program(program)
            if out == None:
                break
            robot.inst.append(out)
        if len(robot.inst):
            run_robot(robot)

f = open("input", "r")
mem = f.read().strip('\n').split(',')
for i in range(len(mem), len(mem) + 10000):
    mem.append('0')

program = Program(copy.deepcopy(mem), 0, [], True, 0)
robot = Robot((0, 0), {}, RSEND, [], 0, UP)
run(program, robot)
print(robot.npainted)

program = Program(copy.deepcopy(mem), 0, [], True, 0)
robot = Robot((0, 0), {}, RSEND, [], 0, UP)
robot.painted[(0,0)] = '#'
run(program, robot)

xmax = max([i[0] for i in robot.painted])
ymax = max([i[1] * -1 for i in robot.painted])

for i in range(0, ymax + 1):
    for z in range(0, xmax + 1):
        p = (z, i * -1)
        if p in robot.painted:
            print(robot.painted[p], end='')
        else:
            print('.', end='')
    print()

f.close()