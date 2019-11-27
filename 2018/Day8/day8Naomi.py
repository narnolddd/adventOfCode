file = "Day8/input.txt"

# read the thing
data=[]
with open(file,'r') as f:
    line = f.readline().strip()
    for l in line.split(" "):
        data.append(int(l))

test = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
#data=test

#Part 1
pointer=0
metadata=[]
while True:
    if len(data)==0:
        break
    if data[pointer]==0:
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

def value(childvalues, metadata):
    print(childvalues,metadata)
    if len(childvalues)==0:
        return sum(metadata)
    else:
        value = sum([childvalues[m-1] for m in metadata if m in range(1,len(childvalues)+1)])

def getTreeValue(treelist):
    children, noChildren = [], treelist[0]
    metadata, noMetadata = [], treelist[1]

    for _ in range(noChildren):
        c = getTreeValue(treelist[2:])
        children.append(c)
        treelist[0]--

    if noChildren==0:
        metadata = treelist[2:2+noMetadata]
        val = sum(metadata)
        del treelist[:2+noMetadata]
        return val

    if treelist[0]==0:
        del treelist[2:2+noMetadata]

    metadata = treelist[2:2+noMetadata]

    return value(children, metadata)

print(getTreeValue(test))
