file = "./2020/Day01/input.txt"

input_list = []
with open(file, 'r') as f:
    for row in f:
        input_list.append(int(row))

# Messy but works..
for n in input_list:
    for m in input_list:
        for p in input_list:
            if n == m or n == p or m == p:
                continue
            elif n + m + p == 2020:
                print(n * m * p)
                break
