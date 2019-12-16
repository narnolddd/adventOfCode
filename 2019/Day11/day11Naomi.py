from collections import defaultdict, deque
import matplotlib.pyplot as plt

def increase_by(ic,size):
    increase = size + 1 - len(ic)
    new_ic = ic+[0 for _ in range(increase)]
    ic = new_ic
    return ic

def advance_ic(inputs,ip,ic,rb):
    while ic[ip]!=99:
        #print(ic)
        #print(ic[:20])
        instruction=("0000"+str(ic[ip]))[-5:]
        p1, p2, p3 = [instruction[2-i] for i in range(3)]

        # first parameter
        if ip+1 >= len(ic):
            ic = increase_by(ic, ip+1)
        if p1 == "0":
            adr1 = ic[ip+1]
        elif p1 == "1":
            adr1 = ip+1
        elif p1 == "2":
            adr1 = rb+ic[ip+1]
        else:
            print("unknown position mode "+p1)

        # second parameter
        if ip+2 >= len(ic):
            ic = increase_by(ic, ip+2)
        if p2 == "0":
            adr2 = ic[ip+2]
        elif p2 == "1":
            adr2 = ip+2
        elif p2 == "2":
            adr2 = rb+ic[ip+2]
        else:
            print("unknown position mode "+p2)

        #third parameter
        if ip+3 >= len(ic):
            ic = increase_by(ic, ip+3)
        adr3 = ic[ip+3]
        if p3 == "1":
            adr3 = ip+3
        if p3 == "2":
            adr3 = rb + ic[ip+3]

        op=instruction[3:]
        #print(op)
        if op=="01":
            if adr3>=len(ic):
                ic=increase_by(ic,adr3)
            u1, u2 = 0,0
            if adr1<len(ic):
                u1=ic[adr1]
            if adr2<len(ic):
                u2=ic[adr2]
            ic[adr3]=u1 + u2
            ip = ip+4
        elif op=="02":
            if adr3>=len(ic):
                ic=increase_by(ic,adr3)
            u1, u2 = 0,0
            if adr1<len(ic):
                u1=ic[adr1]
            if adr2<len(ic):
                u2=ic[adr2]
            ic[adr3]=u1*u2
            ip = ip+4
        elif op=="03":
            if adr1>=len(ic):
                ic=increase_by(ic,adr1)
            ic[adr1]=inputs.pop()
            ip = ip+2
        elif op=="04":
            ip = ip+2
            return ic[adr1], ic, ip, rb
        elif op=="05":
            if ic[adr1]!=0:
                ip=ic[adr2]
            else:
                ip = ip+3
        elif op=="06":
            if ic[adr1]==0:
                ip=ic[adr2]
            else:
                ip = ip+3
        elif op=="07":
            if adr3>len(ic):
                ic=increase_by(ic,adr3)
            if ic[adr1]<ic[adr2]:
                ic[adr3]=1
                ip=ip+4
            else:
                ic[adr3]=0
                ip=ip+4
        elif op=="08":
            if adr3>len(ic):
                ic=increase_by(ic,adr3)
            if ic[adr1]==ic[adr2]:
                ic[adr3]=1
                ip=ip+4
            else:
                ic[adr3]=0
                ip=ip+4
        elif op=="09":
            #print(rb)
            rb = rb + ic[adr1]
            #print("RB "+str(rb))
            ip = ip + 2
        else:
            print('error: instruction reads '+instruction)
            break
    return None, ic, ip, rb

file = "Day11/inputnaomi.txt"

with open(file,'r') as f:
    ic = list(map(int,f.read().split(',')))
    f.close()

coords=defaultdict(lambda : '.')

pos = [0,0]
coords[(0,0)]='#'
dir = deque('urdl')
ip, rb = 0,0
while True:
    inp = int(coords[(pos[0],pos[1])]=="#")
    to_paint_white, ic, ip, rb = advance_ic([inp], ip, ic, rb)
    if to_paint_white==1:
        coords[(pos[0],pos[1])]='#'
    elif to_paint_white==0:
        coords[(pos[0],pos[1])]='.'
    else:
        break

    right, ic, ip, rb = advance_ic([],ip,ic,rb)
    if right == 0:
        dir.rotate(1)
    elif right == 1:
        dir.rotate(-1)
    else:
        break

    if dir[0]=='u':
        pos[1]+=1
    elif dir[0]=='l':
        pos[0]-=1
    elif dir[0]=='d':
        pos[1]-=1
    else:
         pos[0]+=1

print(len(coords.keys()))

plt.scatter( [pt[0] for pt in coords.keys() if coords[pt]=='#'],[pt[1] for pt in coords.keys() if coords[pt]=='#'])
plt.show()
