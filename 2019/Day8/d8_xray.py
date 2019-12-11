# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:55:40 2019

@author: Administrator
"""

if __name__ == '__main__':
    f= open('input.txt' , 'r')
    data = f.read()
    image_data = list(map(int, data))
    #record the value of 0s, 1s and 2s
    zero_cnt = 150
    one_cnt = 0
    two_cnt = 0
    layer = 0
    
    cur = 0
    
    #calculate layers:
    while(cur < len(image_data)):
        cur += (25*6)
        layer += 1
    print("layer: " + str(layer))
    
    #find the layer with 
    cur = 0
    lay_cur = 0
    zero_cnt_cur = 0 
    one_cnt_cur = 0
    two_cnt_cur = 0
    while(lay_cur < layer):
        
        for i in range (0,150):
            if(image_data[i+lay_cur*150] == 0):
                zero_cnt_cur += 1
            elif(image_data[i+lay_cur*150] == 1):
                one_cnt_cur += 1
            else:
                two_cnt_cur += 1
        if (zero_cnt_cur <= zero_cnt):
            print("layer is: " + str(lay_cur))
            zero_cnt = zero_cnt_cur
            one_cnt = one_cnt_cur
            two_cnt = two_cnt_cur
            print(zero_cnt + one_cnt + two_cnt)
        zero_cnt_cur = 0
        one_cnt_cur = 0
        two_cnt_cur = 0
        lay_cur += 1
    
    result = one_cnt*two_cnt
    print("result: " + str(result))
    
    #part 2
    p2_image = [3 for i in range(0,150)]
    for lay in range(0,layer):
        for i in range(0,150):
            if(p2_image[i] == 3):
                if(image_data[i+lay*150] == 1 or image_data[i+lay*150] == 0):
                    p2_image[i] = image_data[i+lay*150]
                else:
                    continue
            else:
                continue
    
    for i in range(0,6):
        for j in range(0,25):
            if (p2_image[j+i*25] == 1):
                print('8',end='')
            if (p2_image[j+i*25] == 0):
                print(' ',end='')
        print(' ')
        
    
                

