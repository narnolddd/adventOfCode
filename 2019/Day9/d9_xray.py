# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:41:16 2019

@author: Administrator

99: program finished
1 : adds num in two positions and store the result in third position.
2 : multiplies num in two positions and store the result in third position.
3 : takes an input to store in a specific pos
4 : outputs the value in the specific pos
5 : jump_if_true
6 : jump if false
7 : less then
8 : equals
9 : move relative base
"""

import copy

def int_compute(code_list, iter_input):
    cursor = 0
    op_code = code_list[cursor]%100

    #print(op_mode)
    rela_base = 0
    #print(rela_base)
    while(op_code in correct_op):
        op_code = code_list[cursor]%100
        op_mode = []
        op_mode_int = code_list[cursor]//100
        #print('op_mode_int: ' +str(op_mode_int))
        for i in range(0,3):
            op_mode.append(op_mode_int%10)
            op_mode_int = op_mode_int//10
        
        if(op_code == 1):
            if(op_mode[0] == 0):
                p1 = code_list[code_list[cursor+1]]
                
            elif(op_mode[0] == 1):
                p1 = code_list[cursor+1]
            elif(op_mode[0] == 2):
                p1 = code_list[rela_base + code_list[cursor+1]]
            else:
                print('error getting addr in op1')

            if(op_mode[1] == 0):
                p2 = code_list[code_list[cursor+2]]
            elif(op_mode[1] == 1):
                p2 = code_list[cursor+2]
            elif(op_mode[1] == 2):
                p2 = code_list[rela_base + code_list[cursor+2]]
            else:
                print('error getting addr in op1')

            if(op_mode[2] == 0):
                print(op_mode)
                code_list[code_list[cursor+3]] = p1 + p2
            elif(op_mode[2] == 2):
                code_list[rela_base + code_list[cursor+3]] = p1+ p2
            else:
                print('error getting addr in op1')

            cursor += 4
                
        elif(op_code == 2):
            if(op_mode[0] == 0):
                p1 = code_list[code_list[cursor+1]]
            elif(op_mode[0] == 1):
                p1 = code_list[cursor+1]
            elif(op_mode[0] == 2):
                p1 = code_list[rela_base + code_list[cursor+1]]
            else:
                print('error getting addr in op2')

            if(op_mode[1] == 0):
                p2 = code_list[code_list[cursor+2]]
            elif(op_mode[1] == 1):
                p2 = code_list[cursor+2]
            elif(op_mode[1] == 2):
                p2 = code_list[rela_base + code_list[cursor+2]]
            else:
                print('error getting addr in op2')

            if(op_mode[2] == 0):
                code_list[code_list[cursor+3]] = p1 * p2
            elif(op_mode[2] == 2):
                code_list[rela_base + code_list[cursor+3]] = p1 * p2
            else:
                print('error getting addr in op2')

            cursor += 4
        
        elif(op_code == 3):
            if (op_mode[0] != 0):
                #print('error getting addr in op3')
                #print(code_list[cursor])
                code_list[rela_base + code_list[cursor+1]] = iter_input
            else:
                code_list[code_list[cursor+1]] = iter_input
            cursor += 2
        

        elif(op_code == 4):
            #print('op_mode: ' + str(op_mode))
            if(op_mode[0] == 0):
                print("the output value is (mode 0): " + str(code_list[code_list[cursor+1]]))
            elif(op_mode[0] == 2):
                print("the output value is (mode 2): " + str(code_list[rela_base + code_list[cursor+1]]))
            else:
                print("the output value is (mode 1): " + str(code_list[cursor+1]))
            cursor += 2
        
        elif(op_code == 5):
            if(op_mode[0] == 0):
                p1 = code_list[code_list[cursor+1]]
            elif(op_mode[0] == 1):
                p1 = code_list[cursor+1]
            elif(op_mode[0] == 2):
                p1 = code_list[rela_base + code_list[cursor+1]]
            else:
                print('error getting addr in op5')

            if(op_mode[1] == 0):
                p2 = code_list[code_list[cursor+2]]
            elif(op_mode[1] == 1):
                p2 = code_list[cursor+2]
            elif(op_mode[1] == 2):
                p2 = code_list[rela_base + code_list[cursor+2]]
            else:
                print('error getting addr in op5')
            if p1:
                cursor = p2
            else:
                cursor += 3
            
        elif(op_code == 6):
            if(op_mode[0] == 0):
                p1 = code_list[code_list[cursor+1]]
            elif(op_mode[0] == 1):
                p1 = code_list[cursor+1]
            elif(op_mode[0] == 2):
                p1 = code_list[rela_base + code_list[cursor+1]]
            else:
                print('error getting addr in op6')

            if(op_mode[1] == 0):
                p2 = code_list[code_list[cursor+2]]
            elif(op_mode[1] == 1):
                p2 = code_list[cursor+2]
            elif(op_mode[1] == 2):
                p2 = code_list[rela_base + code_list[cursor+2]]
            else:
                print('error getting addr in op6')
            if not p1:
                cursor = p2
            else:
                cursor += 3

        elif(op_code == 7):
            if(op_mode[0] == 0):
                p1 = code_list[code_list[cursor+1]]
            elif(op_mode[0] == 1):
                p1 = code_list[cursor+1]
            elif(op_mode[0] == 2):
                p1 = code_list[rela_base + code_list[cursor+1]]
            else:
                print('error getting addr in op7')

            if(op_mode[1] == 0):
                p2 = code_list[code_list[cursor+2]]
            elif(op_mode[1] == 1):
                p2 = code_list[cursor+2]
            elif(op_mode[1] == 2):
                p2 = code_list[rela_base + code_list[cursor+2]]
            else:
                print('error getting addr in op7')

            if(op_mode[2] == 0):
                code_list[code_list[cursor+3]] = 1 if p1 < p2 else 0
            elif(op_mode[2] == 2):
                code_list[rela_base + code_list[cursor+3]] = 1 if p1 < p2 else 0
            else:
                print('error getting addr in op7')

            cursor += 4
            
        elif(op_code == 8):
            if(op_mode[0] == 0):
                p1 = code_list[code_list[cursor+1]]
            elif(op_mode[0] == 1):
                p1 = code_list[cursor+1]
            elif(op_mode[0] == 2):
                p1 = code_list[rela_base + code_list[cursor+1]]
            else:
                print('error getting addr in op8')

            if(op_mode[1] == 0):
                p2 = code_list[code_list[cursor+2]]
            elif(op_mode[1] == 1):
                p2 = code_list[cursor+2]
            elif(op_mode[1] == 2):
                p2 = code_list[rela_base + code_list[cursor+2]]
            else:
                print('error getting addr in op8')

            if(op_mode[2] == 0):
                code_list[code_list[cursor+3]] = 1 if p1 == p2 else 0
            elif(op_mode[2] == 2):
                code_list[rela_base + code_list[cursor+3]] = 1 if p1 == p2 else 0
            else:
                print('error getting addr in op8')

            cursor += 4

        elif(op_code == 9):
            if(op_mode[0] == 0):
                p1 = code_list[code_list[cursor+1]]
            elif(op_mode[0] == 1):
                p1 = code_list[cursor+1]
            elif(op_mode[0] == 2):
                p1 = code_list[rela_base + code_list[cursor+1]]
            else:
                print('error getting addr in op9')
            rela_base += p1
            cursor += 2

        else:
            if(op_code == 99):
                print("program halt at: " + str(code_list[cursor-1]), end = ', ')
                return -1
            else:
                print('break: error!')
                        
        
    
    #end of while

correct_op = [1,2,3,4,5,6,7,8,9,99] #supported operations so far

if __name__ == '__main__':

    f = open("input.txt", "r")
    line = f.read()
    mem = line.split(',', line.count(','))
    mem = list(map(int, mem))
    ext_mem  = []
    for i in range(10000):
        ext_mem.append(0)
    #print(mem)
    mem.extend(ext_mem)
    int_compute(copy.deepcopy(mem), 2)


    f.close()



