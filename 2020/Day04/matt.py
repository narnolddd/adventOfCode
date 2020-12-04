file = "./2020/Day04/mattinput.txt"

passport_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
allowed_missing_keys = ['cid']

passports = []
passport_n = 0
with open(file, 'r') as f:
    for row in f:
        if row == '\n':
            passport_n += 1
        else:
            creds = row.replace('\n', '').split(' ')
            for c in creds:
                cred = c.split(':')
                if cred[0] in passport_keys:
                    k, v = cred
                else:
                    n, k = cred

                if len(passports) < passport_n + 1:
                    passports.append({k: v})
                else:
                    passports[passport_n][k] = v


valid_passports = len(passports)
for p in passports:
    for k in passport_keys:
        if k not in p and k not in allowed_missing_keys:
            valid_passports -= 1
            break

print(f"#1 valid_passports: {valid_passports}")

valid_passports = len(passports)
for p in passports:
    not_in = 0
    for k in passport_keys:
        if k not in p and k not in allowed_missing_keys:
            not_in += 1
            valid_passports -= 1
            break
    if not_in == 1:
        continue
    valid_creds = 0
    if 1920 <= int(p[passport_keys[0]]) <= 2002 and 4 == len(p[passport_keys[0]]):
        valid_creds += 1
    if 2010 <= int(p[passport_keys[1]]) <= 2020 and 4 == len(p[passport_keys[1]]):
        valid_creds += 1
    if 2020 <= int(p[passport_keys[2]]) <= 2030 and 4 == len(p[passport_keys[2]]):
        valid_creds += 1
    if 'cm' in p[passport_keys[3]] and 150 <= int(p[passport_keys[3]].replace('cm', '')) <= 193:
        valid_creds += 1
    elif 'in' in p[passport_keys[3]] and 59 <= int(p[passport_keys[3]].replace('in', '')) <= 76:
        valid_creds += 1
    if len(p[passport_keys[4]]) == 7 and p[passport_keys[4]][0] == '#':
        valid_creds += 1
    if p[passport_keys[5]] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        valid_creds += 1
    if len(p[passport_keys[6]]) == 9:
        valid_creds += 1
    if valid_creds != 7:
        valid_passports -= 1


print(f"#2 valid_passports: {valid_passports}")
