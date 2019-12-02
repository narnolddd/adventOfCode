ADD = 1
MUL = 2

def inst(v1, v2, op):
    if op == ADD:
        return v1 + v2
    elif op == MUL:
        return v1 * v2

def run(code, noun, verb):
    code[1] = noun
    code[2] = verb
    ptr = 0
    opcode = code[ptr]

    while opcode != 99:
        p1 = code[ptr+1]
        p2 = code[ptr+2]
        outp = code[ptr+3]
        code[outp] = inst(code[p1], code[p2], opcode)
        ptr += 4
        opcode = code[ptr]

    return code[0]



f = open("input", "r")

# Part 1
raw = f.read().strip('\n').split(',')
code = [int(x) for x in raw]

print(run(code, 12, 2))

# Part 2
stop = 0
for n in range(0, 100):
    for v in range(0, 100):
        code = [int(x) for x in raw]
        out = run(code, n, v)
        if out == 19690720:
            print (100 * n + v)
            stop = 1
            break
    if stop:
        break

f.close()