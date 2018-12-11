import numpy as np
serialno=7803

power=np.zeros((300,300),dtype=int)

def mod1000(num):
    return num % 1000

#get power
for i in range(300):
    for j in range(300):
        x, y = i+1, j+1
        r_id = mod1000(x+10)
        pl = mod1000(r_id*y + serialno)
        pl = mod1000(pl*r_id)
        hundreds = pl // 100
        pl = hundreds - 5
        power[i,j]=pl

#find maximum
max=0
pos=[0,0]
size=0

# 125, 229, 271
powerlist=[]
powerlist.append(np.zeros((300,300),dtype=int))

for k in range(1,300):
    powercells=np.zeros((300-(k-1),300-(k-1)),dtype=int)
    max=0
    pos=[0,0]
    size=0
    for i in range(300-(k-1)):
        for j in range(300-(k-1)):
            if i>0 and j>0:
                # partial sums
                powercells[i,j]=powerlist[k-1][i,j]+sum(power[i:i+k,j+k-1])+sum(power[i+k-1,j:j+k]) - power[i+k-1,j+k-1]
            if powercells[i,j]>max:
                max=powercells[i,j]
                pos=[i,j]
                size=k
    powerlist.append(powercells)
    print(max,pos,size)
