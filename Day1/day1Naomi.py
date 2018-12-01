from collections import defaultdict
file = "Day1/frequency.txt"

sum = 0
# for storing the frequency changes from the file
freqchanges = []
# for keeping track of the current frequency
values = defaultdict(lambda:-1)

# Reads the file
f = open(file,'r')
while True:
    line = f.readline()
    if not line:
        break
    freqchanges.append(int(line.strip()))


# First loops through to get sum of frequency changes in text file, then loops until a frequency is repeated
index = 0
values[0]=1
firstLoop=True
while True:
    sum+=freqchanges[index]
    if values[sum]>0:
        break
    values[sum]=1
    index = index + 1
    if index == len(freqchanges):
        if firstLoop:
            print('Part 1, sum = %d' % sum)
            firstLoop=False
        index = 0

print('Part 2, first repeated frequency is %d' % sum)
