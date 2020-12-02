import csv
directory = "./2020/Day02/mattinput.txt"

# 1
n = 0
with open(directory) as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        num_range = row[0].split('-')
        c = row[1].replace(':', '')
        pwd = row[2]

        if pwd.count(c) >= int(num_range[0]) and pwd.count(c) <= int(num_range[1]):
            n = n + 1

print(n)

# 2
n = 0
with open(directory) as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        n1, n2 = row[0].split('-')
        c = row[1].replace(':', '')
        pwd = row[2]

        n1 = int(n1) - 1
        n2 = int(n2) - 1
        if pwd[n1] == c:
            if pwd[n2] != c:
                n = n + 1
        elif pwd[n2] == c:
            if pwd[n1] != c:
                n = n + 1

print(n)
