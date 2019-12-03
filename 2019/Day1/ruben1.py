from functools import *
from itertools import *
from typing import *

def calculate_fuel(mass):
    return mass // 3 - 2

def process_inputs():
    inputs = []

    while True:
        try:
            inputs.append(input())
        except EOFError:
            break

    inputs = list(map(int, inputs))
    return inputs

def main1():
    masses = process_inputs()
    total_fuel = sum(calculate_fuel(mass) for mass in masses)
    print('total fuel', total_fuel)

def calculate_extended_fuel(mass):
    initial_fuel = calculate_fuel(mass)
    total_fuel = initial_fuel
    fuels = [initial_fuel]

    while True:
        extra_fuel = max(0, calculate_fuel(fuels[-1]))
        fuels.append(extra_fuel)

        if extra_fuel == 0:
            break

        total_fuel += extra_fuel

    return sum(fuels)

def main2():
    masses = process_inputs()
    total_fuel = sum(calculate_extended_fuel(mass) for mass in masses)

    print('real total fuel', total_fuel)


if __name__ == "__main__":
    main2()
