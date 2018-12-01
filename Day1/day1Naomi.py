file = "Day1/frequency.txt"

sum = 0
freqchanges = []
values = []

f = open(file,'r')
while True:
    line = f.readline()
    if not line:
        break
    freqchanges.append(int(line.strip()))

index = 0
values.append(0)
while True:
    sum+=freqchanges[index]
    if sum in values:
        break
    values.append(sum)
    index = index + 1
    if index == len(freqchanges):
        index = 0

print(sum)
