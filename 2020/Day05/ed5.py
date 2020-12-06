f = open("edinput.txt")
lines = f.readlines()

def update_position(min_v, max_v):
	return min_v + (max_v - min_v) // 2

higher = -1
ids = []
for line in lines:
	min_row = 0
	max_row = 127
	min_col = 0
	max_col = 7
	for c in line:
		if c == 'F':
			max_row = update_position(min_row, max_row)
		elif c == 'B':
			min_row =  update_position(min_row, max_row) + 1
		elif c == 'L':
			max_col = update_position(min_col, max_col)
		elif c == 'R':
			min_col = update_position(min_col, max_col) + 1

	seat_id = min_row * 8 + min_col
	ids.append(seat_id)
	higher = max([seat_id, higher])

print(higher)

ids = sorted(ids)

for i in range(0, len(ids)-1):
	if ids[i+1] - ids[i] > 1:
		print(ids[i] + 1)
		break 

f.close()