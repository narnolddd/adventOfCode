#!/bin/bash

# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# cid (Country ID) - ignored, missing or not.

# Gawk uses \y instead of \b for the word boundary, as \b is already a escape sequence for backslash 

gawk  'BEGIN { RS = ""; OFS = " "} {$1 = $1;} (/eyr/ && /pid/ && /ecl/ && /hcl/ && /hgt/ && /byr/ && /iyr/){print $0}' edinput.txt | wc -l

gawk  'BEGIN { RS = ""; OFS = " "} {$1 = $1;} ( \
	/eyr:20([2][0-9]|30)/ && \
	/pid:(\y[0-9]{9}\y)/ && \
	/ecl:\y(amb|blu|brn|gry|grn|hzl|oth)\y/ && \
	/hcl:#\y([0-9]|[a-f]){6}\y/ && \
	/hgt:(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)/ && \
	/byr:([1][9][2-9][0-9])|([2][0][0][0-2])/ && \
	/iyr:(20([1][0-9]|20))/){print $0}' edinput.txt | wc -l