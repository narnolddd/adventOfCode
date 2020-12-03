file = "./2020/Day03/mattinput.txt"


ski_slope = []
with open(file, 'r') as f:
    for row in f:
        ski_slope.append(row.replace("\n", ""))


def how_many_trees(ski_slope, col, row):
    col_n = 0
    row_n = 0
    tree_n = 0
    width = len(ski_slope[0])
    height = len(ski_slope)

    for _ in range(height):
        col_n += col
        row_n += row
        col_n %= width
        if row_n >= height:
            break

        if ski_slope[row_n][col_n] == '#':
            tree_n += 1

    return tree_n


print(how_many_trees(ski_slope, 3, 1))

piste_list = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

a = 1
for col, row in piste_list:
    a *= how_many_trees(ski_slope, col, row)
print(a)
