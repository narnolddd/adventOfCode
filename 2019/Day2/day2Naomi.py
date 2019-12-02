file = "Day2/input.txt"

with open(file,'r') as f:
    initial_intcode = list(map(int,f.read().split(',')))
    f.close()


def do_intcode(noun, verb):
    pos=0
    intcode = initial_intcode.copy()
    intcode[1]=noun
    intcode[2]=verb
    while intcode[pos]!=99:
        if intcode[pos]==1:
            intcode[intcode[pos+3]]=intcode[intcode[pos+1]]+intcode[intcode[pos+2]]
            pos = pos+4
        elif intcode[pos]==2:
            intcode[intcode[pos+3]]=intcode[intcode[pos+1]]*intcode[intcode[pos+2]]
            pos = pos+4
        else: print('error')
    return intcode[0]

# Part 1
print("Part 1: "+str(do_intcode(12,2)))

# Part 2
for i in range(100):
    for j in range(100):
        output = do_intcode(i,j)
        if output==19690720:
            print("Part 2: "+str(i)+", "+str(j))
            break
