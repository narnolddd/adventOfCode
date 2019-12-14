def increase_by(ic,size):
    increase = size + 1 - len(ic)
    new_ic = [val for val in ic]+[0 for _ in range(size)]
    ic = new_ic
    return ic

def advance_ic(inputs,ip,ic,rb):
    while ic[ip]!=99:
        #print(ic[:20])
        instruction=("0000"+str(ic[ip]))[-5:]
        p1, p2, p3 = [instruction[2-i] for i in range(3)]

        # first parameter
        if ip+1 >= len(ic):
            ic = increase_by(ic, ip+1)
        if p1 == "0":
            if ic[ip+1]>= len(ic):
                u1=0
            else:
                u1 = ic[ic[ip+1]]
        elif p1 == "1":
            u1 = ic[ip+1]
        elif p1 == "2":
            if rb + ic[ip+1]>=len(ic):
                u1 = 0
            else:
                u1 = ic[rb+ic[ip+1]]
        else:
            print("unknown position mode "+p1)

        # second parameter
        if ip+2 >= len(ic):
            ic = increase_by(ic, ip+2)
        if p2 == "0":
            if ic[ip+2]>= len(ic):
                u2=0
            else:
                u2 = ic[ic[ip+2]]
        elif p2 == "1":
            u2 = ic[ip+2]
        elif p2 == "2":
            if rb+ic[ip+2]>=len(ic):
                u2 = 0
            else:
                u2 = ic[rb+ic[ip+2]]
        else:
            print("unknown position mode "+p2)

        #third parameter
        if ip+3 >= len(ic):
            ic = increase_by(ic, ip+3)
        u3 = ic[ip+3]

        op=instruction[3:]
        #print(op)
        if op=="01":
            if u3>len(ic):
                ic=increase_by(ic,u3)
            ic[u3]=u1 + u2
            ip = ip+4
        elif op=="02":
            if u3>len(ic):
                ic=increase_by(ic,u3)
            ic[u3]=u1 * u2
            ip = ip+4
        elif op=="03":
            if u1>=len(ic):
                ic=increase_by(ic,u1)
            ic[u1]=inputs.pop()
            #print(inp,u1)
            ip = ip+2
        elif op=="04":
            print(u1)
            ip = ip+2
        elif op=="05":
            if u1!=0:
                ip=u2
            else:
                ip = ip+3
        elif op=="06":
            if u1==0:
                ip=u2
            else:
                ip = ip+3
        elif op=="07":
            if u3>len(ic):
                ic=increase_by(ic,u3)
            if u1<u2:
                ic[u3]=1
                ip=ip+4
            else:
                ic[u3]=0
                ip=ip+4
        elif op=="08":
            if u3>len(ic):
                ic=increase_by(ic,u3)
            if u1==u2:
                ic[u3]=1
                ip=ip+4
            else:
                ic[u3]=0
                ip=ip+4
        elif op=="09":
            rb = rb + u1
            #print("RB "+str(rb))
            ip = ip + 2
        else:
            print('error: instruction reads '+instruction)
            break
    return None, ic, ip

file = "Day9/inputnaomi.txt"

with open(file,'r') as f:
    ic = list(map(int,f.read().split(',')))
    f.close()

#ic = [104,1125899906842624,99]

advance_ic([1],0,ic,0)
