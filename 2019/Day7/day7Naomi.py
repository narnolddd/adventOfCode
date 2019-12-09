file = "Day7/inputnaomi.txt"
from itertools import permutations

with open(file,'r') as f:
    initial_intcode = list(map(int,f.read().split(',')))
    f.close()

def get_param(pos_mode,number,ic):
    if pos_mode:
        return ic[number]
    return number

def advance_intcode(inputs,ip,intcode,get_phase=True):
    in_index=0
    while intcode[ip]!=99:
        instruction=("0000"+str(intcode[ip]))[-5:]
        p1, p2, p3 = [instruction[2-i]=="0" for i in range(3)]
        op=instruction[3:]
#        print(op)
        if op=="01":
            intcode[intcode[ip+3]]=get_param(p1,intcode[ip+1],intcode)+get_param(p2,intcode[ip+2],intcode)
            ip = ip+4
        elif op=="02":
            intcode[intcode[ip+3]]=get_param(p1,intcode[ip+1],intcode)*get_param(p2,intcode[ip+2],intcode)
            ip = ip+4
        elif op=="03":
            if get_phase:
                intcode[intcode[ip+1]]=inputs[0]
                get_phase=False
            else:
                intcode[intcode[ip+1]]=inputs[1]
            ip = ip+2
        elif op=="04":
            return get_param(p1,intcode[ip+1],intcode), intcode, ip+2
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
    return None, intcode, ip

def get_signal(config):
    signal=0
    for index in range(5):
        signal=advance_intcode([config[index],signal],0,[val for val in initial_intcode])[0]
    return signal

orders = list(permutations(range(5)))

max_signal=0
for order in orders:
    signal=get_signal(order)
    if signal>max_signal:
        max_signal=signal

print("Part 1: "+str(max_signal))


# Part 2
class Amp:
    def __init__(self,phase):
        self.ic=[val for val in initial_intcode]
        self.ip=0
        self.phase=phase
        self.input=[phase,0]
        self.first_run=True

    def __str__(self):
        return "Amp "+str(self.phase)

    def advance(self):
        self.output, self.ic, self.ip = advance_intcode(self.input,self.ip,self.ic,self.first_run)
        self.first_run=False

def get_signal_2(config):
    amps = [Amp(c) for c in config]
    signal=0
    i=0
    loop=0
    while True:
        amps[i%5].advance()
        if amps[i%5].output is None:
            break
        signal=amps[i%5].output
        amps[(i+1)%5].input[1]=signal
        i +=1
        loop+=1
    del amps
    return signal

orders = list(permutations(range(5,10)))

max_signal=0
for order in orders:
    signal=get_signal_2(order)
    if signal>max_signal:
        max_signal=signal

print("Part 2: "+str(max_signal))
