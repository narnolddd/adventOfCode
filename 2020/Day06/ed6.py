f = open("edinput.txt")

total = 0
equal_answers = 0
group = set()
answers = []

for line in f.readlines():
	if line == '\n':
		# Part 1
		total += len(group)
		group = set()

		# Part 2
		intersection = set.intersection(*[set(x) for x in answers])  
		equal_answers += len(intersection)
		answers = []
	else:		
		person_answers = []
		for c in line.strip('\n'):
			group.add(c)
			person_answers.append(c)
		answers.append(person_answers)

print(total)
print(equal_answers)
f.close()