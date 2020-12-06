import math

file = "./2020/Day05/mattinput.txt"


def compute_seat_info(seat_bin):
    row_bin = seat_bin[:7]
    col_bin = seat_bin[7:]

    row_n = find_from_bin(row_bin, 127)
    col_n = find_from_bin(col_bin, 7)

    return row_n, col_n


def find_from_bin(bin, max):
    n = [0, max]
    for a in bin:
        new_n = math.ceil((n[1] - n[0]) / 2)
        if a == 'F' or a == 'L':
            n[1] -= new_n
        elif a == 'B' or a == 'R':
            n[0] += new_n

    return n[0]


boarding_pass_seat_ids = []
with open(file, 'r') as f:
    for row in f:
        row_n, col_n = compute_seat_info(row)

        seat_id = row_n * 8 + col_n

        boarding_pass_seat_ids.append(seat_id)

print(max(boarding_pass_seat_ids))

boarding_pass_seat_ids.sort()
i = min(boarding_pass_seat_ids)
for j in boarding_pass_seat_ids:
    if j != i:
        print(i)
        break
    i += 1
