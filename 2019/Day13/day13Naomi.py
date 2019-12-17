EMPTY = 0
WALL = 1
BLOCK = 2
PADDLE = 3
BALL = 4

def increase_by(ic,size):
    increase = size + 1 - len(ic)
    new_ic = ic+[0 for _ in range(increase)]
    ic = new_ic
    return ic

def advance_ic(inputs,ip,ic,rb):
    outputs=[]
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
            outputs.append(ic[adr1])
            if len(outputs)==3:
                return outputs, ic, ip, rb
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

file = "Day13/inputnaomi.txt"

with open(file,'r') as f:
    initial_intcode = list(map(int,f.read().split(',')))
    f.close()

ic = [c for c in initial_intcode]

board = {}

ip, rb, output = 0,0,[]
while True:
    output, ic, ip, rb = advance_ic([0],ip,ic,rb)
    if output==None:
        break
    board[(output[0],output[1])]=output[2]

print("Part 1: "+str(len([tile for tile in board.keys() if board[tile]==BLOCK])))

# re-initialise intcode
ic = [c for c in initial_intcode]
ic[0]=2
ip = 0
rb = 0
score = 0
paddle_pos=0
ball_pos=0
board = {}

inputs=[0]
while True:
    output, ic, ip, rb = advance_ic(inputs,ip,ic,rb)
    if output==None:
        break
    if output[0]==-1 and output[1]==0:
        score=output[2]
        continue
    if output[2]==PADDLE:
        paddle_pos=output[0]
    if output[2]==BALL:
        ball_pos=output[0]
    if ball_pos>paddle_pos:
        inputs=[1]
    elif ball_pos<paddle_pos:
        inputs=[-1]
    else:
        inputs=[0]
    board[(output[0],output[1])]=output[2]

print("Part 2: "+str(score))
