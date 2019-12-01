file = "Day1/input.txt"

#test input
#print(how_much_fuel(14))

with open(file,'r') as f:
    modules = list(map(int, f.readlines()))
    f.close()

# Part 1

def how_much_fuel(mass):
    return int(mass/3) - 2

total_fuel = sum(map(lambda module : how_much_fuel(module), modules))
print("Part 1: "+str(total_fuel))


# Part 2

def how_much_total_fuel(mass):
    fuel_vector=[]
    fuel = how_much_fuel(mass)
    while fuel > 0:
        fuel_vector.append(fuel)
        fuel = how_much_fuel(fuel)
    return sum(fuel_vector)

real_total_fuel = sum(map(lambda module : how_much_total_fuel(module), modules))

print("Part 2: "+str(real_total_fuel))
