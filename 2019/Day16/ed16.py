from itertools import cycle

def phase(seq, n):
    base = [0, 1, 0, -1]
    mod_seq = [x for x in seq]
    pattern_iter = cycle(base)
    new_seq = []
    v = 0
    next(pattern_iter)
    for i in range(1, n+1):
        v = 0
        mul = next(pattern_iter)
        for s in mod_seq:
            v += s * mul
            mul = next(pattern_iter)
        nout = abs(v) % 10
        new_seq.append(nout)
        rep = i + 1
        new_pattern = []
        for p in base:
            new_pattern += [p] * rep
        if len(new_pattern[1:]) >= len(seq):
            mod_seq = seq[i:]
            pattern_iter = cycle(new_pattern[i+1:n+1])
        else:
            pattern_iter = cycle(new_pattern)
            next(pattern_iter)
    return new_seq

def phase2(seq):
    new_seq = [seq[-1]]
    prev = seq[-1]
    for i in range(len(seq)-2, -1, -1):
        v = (prev + seq[i]) % 10
        new_seq.append(v)
        prev = v
    new_seq.reverse()
    return new_seq


f = open("input", 'r')

seq = [int(x) for x in  f.read().strip('\n')]
n = len(seq)

nseq = [x for x in seq]
for i in range(0, 1):
    nseq = phase(nseq, n)

last8 = "".join([str(c) for c in nseq[:8] ] ) 
print (last8)

nseq = [x for x in seq] * 10000
offset = int("".join([str(c) for c in nseq[0:7] ] ))
nseq = nseq[offset:]
for i in range(0, 100):
    nseq = phase2(nseq)

last8 = "".join([str(c) for c in nseq[:8] ] ) 
print (last8)
f.close()