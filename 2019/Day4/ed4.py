import re

def is_valid_part1(password):
    pint = [int(c) for c in str(password)]
    i = 0
    valid = False
    for i in range(0, len(pint)-1):
        if pint[i] > pint[i+1]:
            return False
        if pint[i] == pint[i+1]:
            valid = True
    return valid

def is_valid_part2(password):
    pint = [int(c) for c in str(password)]
    i = 0
    for i in range(0, len(pint)-1):
        if pint[i] > pint[i+1]:
            return False
    query = r'(([0-9])\2+)'   
    groups = re.findall( query, str(password))
    for g in groups:
        if len(g[0]) == 2:
            return True
    return False

start = 152085
end = 670283

valid = 0
for i in range(start, end+1):
    if is_valid_part1(i):
        valid += 1

print (valid)

valid = 0
for i in range(start, end+1):
    if is_valid_part2(i):
        valid += 1

print (valid)