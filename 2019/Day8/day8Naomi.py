from collections import Counter

file="Day8/inputnaomi.txt"
with open(file,'r') as f:
    imagedata=f.read().strip()

w, h = 25, 6
size = w * h

layers = [imagedata[size*i:size*(i+1)] for i in range(int(len(imagedata)/size))]

zero_counts = [Counter(layer)['0'] for layer in layers]
layer_index = zero_counts.index(min(zero_counts))

ones, twos = Counter(layers[layer_index])['1'], Counter(layers[layer_index])['2']
print("Part 1: "+str(ones*twos))

def concat_layer(top,bot):
    top, bot = int(top),  int(bot)
    if top==0 or top ==1:
        return top
    return bot

import numpy as np
import matplotlib.pyplot as plt

#concat the layers top to bottom
top_layer=[l for l in layers[0]]
for k in range(len(layers)):
    new_layer=[concat_layer(top_layer[m],layers[k][m]) for m in range(150)]
    top_layer=new_layer



image_negative= np.array(new_layer).reshape(6,25)
plt.imshow(image_negative)
plt.show()
