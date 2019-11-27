from collections import Counter, defaultdict
file = "Day18/input.txt"

area = []

with open(file,'r') as f:
    while True:
        line = f.readline().strip()
        if not line:
            break
        area.append(list(line))

mins=1000

recorder=[]
minutes = 0
compare=""
lineseen = defaultdict(lambda:-1)
checkseen = defaultdict(lambda:-1)

periodicityreached=False
period=-1
pcount=0
values = []
while True:
    # Part 1
    ct = Counter(x for row in area for x in row)
    check = ct['|']*ct['#']
    if minutes > 500 and (checkseen[check]>0):
        periodicityreached=True
        period=minutes - checkseen[check]
        print(period)
    checkseen[check]=minutes
    if periodicityreached:
        if pcount>period:
            break
        values.append([minutes,check])
        pcount +=1
    if minutes == 10:
        print(check)
    new = [[[] for y in range(50)] for x in range(50)]
    for i in range(50):
        for j in range(50):
            adjacents = [[area[x][y] for x in range(max(0,i-1),min(50,i+2))] for y in range(max(0,j-1),min(50,j+2))]
            c = Counter(y for row in adjacents for y in row)
            #print(c)
            if area[i][j]=='.' and c['|'] > 2:
                new[i][j]='|'
            elif area[i][j]=='|' and c['#']>2:
                new[i][j]='#'
            elif area[i][j]=='#' and c['#']>1 and c['|']>0:
                new[i][j]='#'
            elif area[i][j]=='#' and not(c['#']>1 and c['|']>0):
                new[i][j]='.'
            else:
                 new[i][j]=area[i][j]
    area = new.copy()
    if minutes == 200:
        compare += "".join(area[0])
        print(compare)
    if minutes > 200:
        if any(["".join(area[k])==compare for k in range(50)]):
            print("Period: "+str(minutes - 200))
            break
    minutes +=1

    #print("\n".join(["".join(row) for row in area]))
    #print(Counter(x for row in area for x in set(row)))

print(values)

#part 2
index = (1000000000-501) % 28

print(values[index])
