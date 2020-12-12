file = "./2020/Day09/mattinput.txt"


def valid_int(i, int_list_25, int_check):
    for j in int_list_25:
        if i == j:
            continue
        elif i + j == int_check:
            return True
    return False


def find_2_in_25(int_list):
    int_list_max = 25
    while True:
        int_list_25 = int_list[int_list_max - 25:int_list_max]
        int_check = int_list[int_list_max]
        valid = False
        for i in int_list_25:
            valid = valid_int(i, int_list_25, int_check)
            if valid:
                break
        if not valid:
            return int_check
        else:
            int_list_max += 1
            if int_list_max >= len(int_list):
                return -1


def cum_set_for_invalid(i, int_list, invalid):
    j = 0
    cum = [int_list[i]]
    while sum(cum) < invalid:
        j += 1
        cum.append(int_list[i + j])
    if sum(cum) == invalid:
        return min(cum) + max(cum)
    else:
        return -1


def find_set_for_invalid(invalid_int, int_list):
    for i in range(len(int_list)):
        weakness = cum_set_for_invalid(i, int_list, invalid_int)
        if -1 != weakness:
            return weakness


int_list = []
with open(file, 'r') as f:
    for row in f:
        int_list.append(int(row.replace('\n', '')))

invalid_int = find_2_in_25(int_list)
print(f"#1 {invalid_int}")
print(f"#2 {find_set_for_invalid(invalid_int, int_list)}")
