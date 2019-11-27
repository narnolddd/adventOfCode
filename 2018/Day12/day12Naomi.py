from collections import defaultdict
import re

regex = "(?P<config>[^\s]+) => (?P<result>.)"
p=re.compile(regex)

file = "Day12/input.txt"
currentstate = "..."
rules=defaultdict(lambda:".")
no_generations=4000
generations = []
extension = 4000

with open(file,'r') as f:
    currentstate= "....."+f.readline().strip("initial state: ").strip()+extension*"."
    f.readline()
    while True:
        line = f.readline()
        if not line:
            break
        match = p.match(line).groupdict()
        rules[match['config']]=match['result']

potnames = range(-5,len(currentstate)-5)
generations.append(currentstate)

for gen in range(no_generations):
    state = generations[gen]
    current=""
    for i in range(len(state)):
        if i>1 and i < len(state)-2:
            current+=rules[state[i-2:i+3]]
        elif i == 1:
            current+=rules["."+state[i-1:4]]
        elif i == 0:
            current+=rules[".."+state[0:3]]
        elif i == len(state)-2:
            current+=rules[state[i-2:len(state)-1]+"."]
        elif i == len(state)-1:
            current+=rules[state[i-2:len(state)-1]+".."]
    #print(current)
    generations.append(current)

checksum = sum([potnames[i] for i in range(len(potnames)) if generations[no_generations][i]=='#'])
print(checksum)
