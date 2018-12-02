from collections import Counter

# Part 1

file = "Day2/input.txt"
count2=0
count3=0
words = []

with open(file,'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        words.append(line)
        lcounts = Counter(line)
        for letter in lcounts.elements():
            if lcounts[letter] == 2:
                count2 += 1
                break
        for letter in lcounts.elements():
            if lcounts[letter] == 3:
                count3 += 1
                break

# perform checksum
checksum = count2 * count3

print('Checksum = %d' % checksum)

# Part 2

for i in range(len(words)):
    for j in range(i):
        if j == i:
            break
        distance = 0
        word1 = words[i]
        word2 = words[j]
        for k in range(26):
            if distance > 1:
                break
            if word1[k] != word2[k]:
                distance +=1
        if distance == 1:
            print(word1)
            print(word2)
            break
