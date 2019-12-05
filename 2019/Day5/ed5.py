import copy

ADD = 1
MUL = 2
INPUT = 3
OUTPUT = 4
JIT = 5
JIF = 6
LTE = 7
EQ = 8

def run(mem, inp):
    pos = 0
    while True:
        opcode = str(mem[pos])
        size = len(opcode)
        op = 0
        p1 = p2 = 0
        if size < 2:
            op = int(opcode[0])
        else:
            op = int("".join(opcode[-2:]))
            if size == 3:
                p1 = int(opcode[-3]) 
            elif size == 4:
                p1 = int(opcode[-3])
                p2 = int(opcode[-4])

        if op == 99:
            break

        if op != INPUT:
            if p1:
                v1 = int(mem[ pos + 1 ])
            else:
                v1 = int(mem[ int(mem[pos + 1]) ])
            if op != OUTPUT:
                if p2:
                    v2 = int(mem[pos+2])
                else:
                    v2 = int(mem[ int(mem[pos + 2]) ])
            
        if op == MUL:
            outp = int(mem[pos + 3])
            mem[outp] = v1 * v2
            pos += 4
        elif op == ADD:
            outp = int(mem[pos + 3])
            mem[outp] = v1 + v2
            pos += 4
        elif op == INPUT:
            outp = int(mem[pos + 1])
            mem[outp] = inp
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
            outp = int(mem[pos + 3])
            if v1 < v2:
                mem[outp] = 1
            else:
                mem[outp] = 0
            pos += 4
        elif op == EQ:
            outp = int(mem[pos + 3])
            if v1 == v2:
                mem[outp] = 1
            else:
                mem[outp] = 0
            pos += 4


f = open("input", "r")
mem = f.read().strip('\n').split(',')
run(copy.deepcopy(mem), 1)
run(copy.deepcopy(mem), 5)
f.close()