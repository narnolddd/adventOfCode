file = "./2020/Day06/mattinput.txt"


def check_against_group(individual, group):
    for j in individual:
        if j not in group:
            group += j
    return group


def check_against_everyone(individual, everyone):
    if everyone == '':
        everyone = individual
    else:
        for i in everyone:
            if i not in individual:
                everyone = everyone.replace(i, '')
            if everyone == '':
                everyone = 'null'
    return everyone


group = ''
everyone = ''
yes_count = 0
yes_count_everyone = 0
with open(file, 'r') as f:
    for row in f:
        if row != '\n':
            group = check_against_group(row.strip('\n'), group)
            if everyone != 'null':
                everyone = check_against_everyone(row.strip('\n'), everyone)
        else:
            yes_count += len(group)
            if everyone != 'null':
                yes_count_everyone += len(everyone)
            group = ''
            everyone = ''
print(f"group {yes_count}")
print(f"everyone {yes_count_everyone}")
