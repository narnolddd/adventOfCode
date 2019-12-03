def part_one():
    with open('input') as mass:
        result = []
        for m in mass:
            result.append(int(float(str(m).strip()) / 3) - 2)
        sum_of_fuel = str(sum(result))
        print(sum_of_fuel)


def part_two():
    with open('input') as mass:
        result = []
        for m in mass:
            while True:
                m = (int(float(str(m).strip()) / 3) - 2)
                if m <= 0:
                    break
                else:
                    result.append(m)
        sum_of_fuel = str(sum(result))
        print(sum_of_fuel)
