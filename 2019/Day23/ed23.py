import copy
from itertools import permutations 
from recordclass import recordclass
import queue
import functools as ft

Program = recordclass('Program', 'mem pos inputs running rbase')
Computer = recordclass('Computer', 'program packet queue idlecnt wait')

ADD = 1
MUL = 2
INPUT = 3
OUTPUT = 4
JIT = 5
JIF = 6
LTE = 7
EQ = 8
MRB = 9

SEND = 0
RCV = 1

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

            program.pos += 2
            if not len(program.inputs):
                program.mem[addr] = -1
                return None
            
            program.mem[addr] = program.inputs.pop()
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


def run_computer(computer):
    if computer.state == SEND:
        computer.state = RCV
        
    computer.state = RSEND
    computer.packet = []

def run(program, computer):
    pass

f = open("input", "r")
mem = f.read().strip('\n').split(',') + ([0] * 10000)

N = 50

def part1():
    bcast_y = None

    computers = {}
    for i in range(0, N):
        program = Program(copy.deepcopy(mem), 0, [i], True, 0)
        computers[i] = Computer(program, [], queue.Queue(), 0, False)

    while True:
        for i in range(0, N):
            if not computers[i].queue.empty():
                packet = computers[i].queue.get()
                computers[i].program.inputs.append(packet[2])
                computers[i].program.inputs.append(packet[1])

            p = run_program(computers[i].program)

            if p == None:
                continue
            computers[i].packet.append(p)
            if len(computers[i].packet) == 3:
                dst = computers[i].packet[0]
                if dst == 255:
                    bcast_y = computers[i].packet[2]
                    break
                computers[dst].queue.put(computers[i].packet)
                computers[i].packet = []
                
        if bcast_y:
            print (bcast_y)
            break

def part2():
    idle = 0
    nat = None
    nats = {}

    computers = {}
    for i in range(0, N):
        program = Program(copy.deepcopy(mem), 0, [i], True, 0)
        computers[i] = Computer(program, [], queue.Queue(), 0, False)

    while True:
        for i in range(0, N):
            if not computers[i].queue.empty():
                packet = computers[i].queue.get()
                computers[i].program.inputs.append(packet[2])
                computers[i].program.inputs.append(packet[1])

            p = run_program(computers[i].program)

            if p == None:
                computers[i].idlecnt += 1
                if computers[i].idlecnt > 100:
                    computers[i].wait = True
                continue
            
            computers[i].packet.append(p)
            if len(computers[i].packet) == 3:
                dst = computers[i].packet[0]
                if dst == 255:
                    nat = computers[i].packet
                    computers[i].packet = []
                    continue
                computers[dst].queue.put(computers[i].packet)
                computers[i].packet = []

        states = [computers[x].wait for x in computers]
        idle = ft.reduce(lambda x,y : x & y, states)
        
        if idle:
            if nat[2] in nats:
                print (nat[2])
                break
            nats[nat[2]] = nat
            computers[0].queue.put((nat))
            for x in computers:
                computers[x].idlecnt = 0
                computers[x].wait = False

part1()
part2()

f.close()