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

def run(mem, inputs, pos):
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
            return 0, pos, False
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
            mem[outp] = inputs.pop()
            pos += 2
        elif op == OUTPUT:
            # print(v1)
            out = v1
            pos += 2
            return out, pos, True
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

sequences =  permutations([0, 1, 2, 3, 4]) 
largest = -1
r = 0
for seq in list(sequences):
    inputs = [0]
    for n in seq:
        inputs.append(n)
        signal, pos, r = run(copy.deepcopy(mem), inputs, 0)   
        r += 1 
        inputs = [signal]
        if signal > largest:
            largest = signal

print (largest)

largest = -1
amps = ['A', 'B', 'C', 'D', 'E']

for seq in permutations([5, 6, 7, 8, 9]):
    memories = {}
    for c, n in zip(amps, seq):
        memories[c] = State(copy.deepcopy(mem), 0, [], True, 0)
        memories[c].inputs.append(n)

    idx = 0
    amp = amps[idx]
    memories[amp].inputs.insert(0, 0)

    while memories['E'].running:
        signal, pos, r = run(memories[amp].mem, memories[amp].inputs, memories[amp].pos)  
        memories[amp].pos = pos
        memories[amp].running = r
        if signal:
            memories[amp].los = signal

        idx = (idx + 1) % 5
        amp = amps[idx]
        memories[amp].inputs.insert(0, signal)

    if memories['E'].los > largest:
        largest = memories['E'].los

print (largest)

f.close()