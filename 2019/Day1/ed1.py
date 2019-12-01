import math

def fuel(mass):
    return math.floor(mass / 3) - 2

f = open("input", "r")
lines = f.readlines()

mass = sum([fuel(int(mass)) for mass in lines])
print (mass)

full = 0
for mass in lines:
    mass = int(mass)
    while math.floor(mass) > 0:
        mass = fuel(mass)
        if mass > 0:
            full += mass

print(full)
f.close()