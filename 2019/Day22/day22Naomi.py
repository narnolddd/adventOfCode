# Compose function a[0]x +a[1] with b[0]x + b[1]
def compose(a,b,size):
    x_coeff = (a[0]*b[0])%size
    const_coeff = (a[1] + a[0]*b[1])%size
    return x_coeff,const_coeff

def to_binary(x):
    return bin(x)[2:]

def get_inverse(a,n):
    size=n
    qs=[0,0]
    rs=[0,0]
    ss, ts=[1,0], [0,1]
    k=2
    while True:
        q, r = int(n/a), n%a
        qs.append(q)
        rs.append(r)
        if r == 0:
            break
        ss.append(ss[k-2]-qs[k]*ss[k-1])
        ts.append(ts[k-2]-qs[k]*ts[k-1])
        k+=1
        n,a = a, r
    return(ts[len(ss)-1]%size)


def evaluate(fun, size, index):
    val = 0
    x = to_binary(abs(fun[0]))
    sums = []
    a = index
    for _ in range(len(x)):
        sums.append(a)
        new_index = a*2 % size
        a = new_index
    for k in range(len(x)):
        if x[k]=="1":
            val = (val + sums[len(x)-1-k])%size
    if fun[0]<0:
        val = (size - val)%size
    val = (val + fun[1])%size
    return val

# Part 1

file = "Day22/inputnaomi.txt"

def perform_shuffle(size):
    fun = [1,0]
    with open(file,'r') as f:
        for _, line in enumerate(f):
            parts = line.split()
            if len(parts)==2:
                fun = compose([1,-int(parts[1])],fun,size)
            elif len(parts)==4:
                if parts[2]=="increment":
                    fun = compose([int(parts[3]),0],fun,size)
                elif parts[2]=="new":
                    fun = compose([-1,-1],fun,size)
                else:
                    print("Unrecognized command "+line)
            else:
                print("Unrecognized command "+line)
        f.close()
    return fun

# part 1
shuffle1 = perform_shuffle(10007)
print("Part 1: "+str(evaluate(shuffle1,10007,2019)))

# part 2:
new_size = 119315717514047
shuffle_times = 101741582076661

shuffle2 = perform_shuffle(new_size)
x2 = to_binary(shuffle_times)
compositions = []
fun = shuffle2
# repeated squaring to get f^{2^n}
for l in range(len(x2)):
    compositions.append(fun)
    fun = compose(fun, fun,new_size)

fun=[1,0]
for l in range(len(x2)):
    if x2[l]=='1':
        fun = compose(compositions[len(x2)-1-l],fun,new_size)

multiplier = get_inverse(fun[0]%new_size,new_size)
inverse_2020 = ((2020 - fun[1])%new_size)*multiplier % new_size
print(inverse_2020)
