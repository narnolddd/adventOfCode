file = "Day8/input.txt"

# read the thing
data=[]
with open(file,'r') as f:
    line = f.readline().strip()
    for l in line.split(" "):
        data.append(int(l))

#test = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
#data=test

#Part 1
pointer=0
metadata=[]
while True:
    if len(data)==0:
        break
    #if reached leaf node, process metadata and backtrack
    if data[pointer]==0:
        #print('yes')
        md = data[pointer+1]
        for k in range(md):
            metadata.append(data.pop(pointer+2))
        del data[pointer:pointer+2]
        if pointer<2:
            break
        data[pointer-2]-=1
        pointer-=2
    else:
        pointer+=2
print(sum(metadata))
