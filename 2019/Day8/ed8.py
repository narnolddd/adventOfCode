PW = 25
PT = 6


def split_layers(l, n): 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 

f = open("input", "r")

image = f.read().strip('\n')

digits = PW * PT
layers = list(split_layers(image, digits))

fewest = layers[0]
min0 = fewest.count('0')

for i in range(1, len(layers)):
    min_next = layers[i].count('0')
    if min0 > min_next:
        min0 = min_next
        fewest = layers[i]

print ( fewest.count('1') * fewest.count('2') )

x = y = 0
for i in range(0, digits):
    for l in layers:
        if l[i] == '0':
            print(' ', end='')
            break
        elif l[i] == '1':
            print('#', end='')
            break

    x = (x + 1) % PW
    if not x:
        y += 1
        print()

f.close()