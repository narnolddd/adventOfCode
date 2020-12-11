file = "./2020/Day08/mattinput.txt"


def has_infinity(history):
    h_len = len(history) - 1
    for i in range(h_len):
        history_compare = history[h_len - i - 1:]
        if history_compare[0] == history_compare[len(history_compare) - 1] and len(history_compare) > 1:
            if history_compare == history[-(len(history_compare)):]:
                return True
    return False


def check_operations(operations, nop_jump_max=-1):
    i = 0
    accumulator = 0
    history = []
    nop_jump_i = switch_jmp_nop(operations, nop_jump_max)
    while True:
        history.append(i)
        if has_infinity(history):
            return True, accumulator
        elif i >= len(operations):
            return False, accumulator
        elif operations[i][0] == 'acc':
            accumulator += operations[i][1]
            i += 1
        elif operations[i][0] == 'jmp':
            if i == nop_jump_i:
                i += 1
            else:
                i += operations[i][1]
        elif operations[i][0] == 'nop':
            if nop_jump_i == i:
                i += operations[i][1]
            else:
                i += 1


def switch_jmp_nop(operations, nop_jump_max):
    nop_jump_n = 0
    for i in range(len(operations)):
        if operation == 'nop' or operation == 'jmp':
            if nop_jump_n < nop_jump_max:
                nop_jump_n += 1
            elif nop_jump_n > nop_jump_max:
                return -1
            else:
                return i


operations = []
with open(file, 'r') as f:
    for row in f:
        operation, number = row.split(' ')
        operations.append([operation, int(number)])


keep_going, accumulator = check_operations(operations)
print(f"#1 {accumulator}")
nop_jump_max = 0
while keep_going:
    keep_going, accumulator = check_operations(operations, nop_jump_max)
    nop_jump_max += 1
print(f"#2 {accumulator}")
