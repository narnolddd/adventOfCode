file = "Day5/inputnaomi.txt"

with open(file,'r') as f:
    initial_intcode = list(map(int,f.read().split(',')))
    f.close()

def get_param(pos_mode,number,ic):
    if pos_mode:
        return ic[number]
    return number

def do_intcode(input):
    ip=0
    intcode = [val for val in initial_intcode]
    while intcode[ip]!=99:
        instruction=("0000"+str(intcode[ip]))[-5:]
        p1, p2, p3 = [instruction[2-i]=="0" for i in range(3)]
        op=instruction[3:]
        if op=="01":
            intcode[intcode[ip+3]]=get_param(p1,intcode[ip+1],intcode)+get_param(p2,intcode[ip+2],intcode)
            ip = ip+4
        elif op=="02":
            intcode[intcode[ip+3]]=get_param(p1,intcode[ip+1],intcode)*get_param(p2,intcode[ip+2],intcode)
            ip = ip+4
        elif op=="03":
            intcode[intcode[ip+1]]=input
            ip = ip+2
        elif op=="04":
            print(get_param(p1,intcode[ip+1],intcode))
            ip = ip+2
        elif op=="05":
            if get_param(p1,intcode[ip+1],intcode)!=0:
                ip=get_param(p2,intcode[ip+2],intcode)
            else:
                ip = ip+3
        elif op=="06":
            if get_param(p1,intcode[ip+1],intcode)==0:
                ip=get_param(p2,intcode[ip+2],intcode)
            else:
                ip = ip+3
        elif op=="07":
            if get_param(p1,intcode[ip+1],intcode)<get_param(p2,intcode[ip+2],intcode):
                intcode[intcode[ip+3]]=1
                ip=ip+4
            else:
                intcode[intcode[ip+3]]=0
                ip=ip+4
        elif op=="08":
            if get_param(p1,intcode[ip+1],intcode)==get_param(p2,intcode[ip+2],intcode):
                intcode[intcode[ip+3]]=1
                ip=ip+4
            else:
                intcode[intcode[ip+3]]=0
                ip=ip+4
        else:
            print('error: instruction reads '+instruction)
            break
    return intcode[0]

do_intcode(1)
do_intcode(5)
