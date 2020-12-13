from collections import Counter
file = "./2020/Day10/mattinput.txt"


def jolt_adapter(int_list):
    difference_list = []
    for i in range(len(int_list)):
        if i - 1 < 0:
            difference_list.append(int_list[i])
        else:
            difference_list.append(int_list[i] - int_list[i - 1])
    difference_list.append(3)
    return difference_list


def compute_adapter_configurations(difference_list):
    confiuration_list = list(filter(None, ''.join(str(n)
                                                  for n in difference_list).split('3')))
    total_configs = 1
    for i in confiuration_list:
        if len(i) == 2:
            total_configs *= 2
        elif len(i) == 3:
            total_configs *= 4
        elif len(i) == 4:
            total_configs *= 7
    return total_configs


int_list = []
with open(file, 'r') as f:
    for row in f:
        int_list.append(int(row.replace('\n', '')))

int_list.sort()
difference_list = jolt_adapter(int_list)
count = Counter(difference_list)
print(f"#1 {count[1]*count[3]}")
print(f"#2 {compute_adapter_configurations(difference_list)}")
