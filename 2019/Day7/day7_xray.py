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
"""

import copy


def judge_mode(op_code):
    if(op_code//100 == 0):
        return 0;
    elif(op_code//100 == 10):
        return 10;
    elif(op_code//100 == 1):
        return 1;
    elif(op_code//100 == 11):
        return 11;
    else:
        #90 indicates an error
        return 90;


def int_compute(para, code_list, iter_input, amp_num, rnd):
    global HALT_SIG, OP_CURSOR
    cursor = OP_CURSOR[amp_num]
    input_cnt = 0
    op_code = code_list[cursor]%100
    
    #if(rnd == 1 and amp_num == 4):
    print("CUR: " + str(mem[OP_CURSOR[amp_n]:]))
    print('input is :' + str(iter_input))
    
    while(op_code in correct_op):
        
        if(op_code == 1):
            #judge between 0mode and 1 mode:
            op_mode = judge_mode(code_list[cursor])
            if(op_mode in correct_mode):
                p1 = code_list[code_list[cursor+1]] if op_mode in [0,10] else code_list[cursor+1]
                p2 = code_list[code_list[cursor+2]] if op_mode in [0,1] else code_list[cursor+2]
                exp_result = p1 + p2
                if (code_list[code_list[cursor+3]]!= exp_result):
                    code_list[code_list[cursor+3]] = exp_result
            cursor += 4
                
        elif(op_code == 2):
            #judge between 0mode and 1 mode:
            op_mode = judge_mode(code_list[cursor])
            if(op_mode in correct_mode):
                p1 = code_list[code_list[cursor+1]] if op_mode in [0,10] else code_list[cursor+1]
                p2 = code_list[code_list[cursor+2]] if op_mode in [0,1] else code_list[cursor+2]
                
                exp_result = p1 * p2
                if (code_list[code_list[cursor+3]]!= exp_result):
                    code_list[code_list[cursor+3]] = exp_result
            cursor += 4
        
        elif(op_code == 3):
            #restricted by question
            if(rnd == 0):
                if (input_cnt == 0):
                    code_list[code_list[cursor+1]] = para
                    input_cnt = 1
                else:
                    code_list[code_list[cursor+1]] = iter_input
            else:
                code_list[code_list[cursor+1]] = iter_input
            cursor += 2
        
        elif(op_code == 4):
            op_mode = judge_mode(code_list[cursor])
            if(op_mode == 0):
                #print("the output value is (mode 0): " + str(code_list[code_list[cursor+1]]))
                OP_CURSOR[amp_num] = cursor + 2
                #print("type is: " + str(type(code_list[code_list[cursor+1]])))
                return code_list[code_list[cursor+1]]
            elif(op_mode == 1):
                print("the output value is (mode 1): " + str(code_list[cursor+1]))
                return code_list[cursor+1]
            else:
                print("error")
            cursor += 2
        
        elif(op_code == 5):
            op_mode = judge_mode(code_list[cursor])
            if(op_mode in correct_mode):
                p1 = code_list[code_list[cursor+1]] if op_mode in [0,10] else code_list[cursor+1]
                p2 = code_list[code_list[cursor+2]] if op_mode in [0,1] else code_list[cursor+2]
                if p1:
                    cursor = p2
                else:
                    cursor += 3
            else:
                return -1
        elif(op_code == 6):
            op_mode = judge_mode(code_list[cursor])
            if(op_mode in correct_mode):
                p1 = code_list[code_list[cursor+1]] if op_mode in [0,10] else code_list[cursor+1]
                p2 = code_list[code_list[cursor+2]] if op_mode in [0,1] else code_list[cursor+2]
                if not p1:
                    cursor = p2
                else:
                    cursor += 3
            else:
                return -1
        elif(op_code == 7):
            op_mode = judge_mode(code_list[cursor])
            if(op_mode in correct_mode):
                p1 = code_list[code_list[cursor+1]] if op_mode in [0,10] else code_list[cursor+1]
                p2 = code_list[code_list[cursor+2]] if op_mode in [0,1] else code_list[cursor+2]
                code_list[code_list[cursor+3]] = 1 if p1 < p2 else 0
                cursor += 4
            else:
                return -1
            
        elif(op_code == 8):
            op_mode = judge_mode(code_list[cursor])
            if(op_mode in correct_mode):
                p1 = code_list[code_list[cursor+1]] if op_mode in [0,10] else code_list[cursor+1]
                p2 = code_list[code_list[cursor+2]] if op_mode in [0,1] else code_list[cursor+2]
                code_list[code_list[cursor+3]] = 1 if p1 == p2 else 0
                cursor += 4
            else:
                return -1
                    
        else:
            if(op_code == 99):
                print("program halt at: " + str(code_list[code_list[cursor-1]]), end = ', ')
                HALT_SIG[amp_num] = 1
                print(HALT_SIG)
                #print(type(code_list[code_list[cursor-1]]))
                #return code_list[code_list[cursor-1]]
                return -1
        op_code = code_list[cursor]%100
    
    #end of while


def perm(n,begin,end, set_list_val):
    global COUNT
    if begin>=end:
        n_tmp = copy.deepcopy(n)
        #print(n_tmp)
        set_list_val.append(n_tmp)
        COUNT +=1
    else:
        i=begin
        for num in range(begin,end):
            n[num],n[i]=n[i],n[num]
            perm(n,begin+1,end, set_list_val)
            n[num],n[i]=n[i],n[num]
            


COUNT=0
HALT_SIG = [0,0,0,0,0] #record if the prog is halt
OP_CURSOR = [0,0,0,0,0] #record the cursor of the control program
correct_op = [1,2,3,4,5,6,7,8,99] #supported operations so far
correct_mode = [0,1,10,11] #support immidiate and reg mode

if __name__ == '__main__':

    f = open("input.txt", "r")
    line = f.read()
    mem = line.split(',', line.count(','))
    mem = list(map(int, mem))
    
    mem_v = []
    for i in range(0,5):
        mem_v.append(copy.deepcopy(mem))
        
    input_value = 0

    
    #record the highest signal value so far
    h_sig = 0
    n=[5,6,7,8,9]
    para_list = []
    perm(n, 0, 5, para_list)
    tmp = 0
    tmp_1 = 0
    

    iter_rnd = 0
    '''
    while(HALT_SIG != [1,1,1,1,1]):
        for amp_n in range(0,5):
            #need two inputs in first round
            if(iter_rnd == 0):
                
                if(amp_n == 0):
                    tmp = int_compute(para_list[amp_n], mem_v[amp_n], 0, amp_n, iter_rnd)
                else:
                    tmp = int_compute(para_list[amp_n], mem_v[amp_n], tmp, amp_n, iter_rnd)
                #print("amp: " + str(amp_n) + ' mem: ' + str(mem) + ' result: ' + str(tmp))
                #print("OP_CURSOR is: " + str(OP_CURSOR[amp_n]) + '----' + str(amp_n))
            else:
                #print("CUR: " + str(mem[OP_CURSOR[amp_n]:]))
                tmp = int_compute(para_list[amp_n], mem_v[amp_n], tmp, amp_n, iter_rnd)
                print("tmp : " + str(tmp), end=',')
                print("tmp type: " + str(type(tmp)))
            #if tmp == None:
            #    print("amp: " + str(amp_n) + ' mem: ' + str(mem) + ' result: ' + str(tmp))
                
        
        
        h_sig = tmp if tmp > h_sig else h_sig
        iter_rnd += 1
    '''
    #para_list[0] = [9,7,8,5,6]
    for cur in range(0,COUNT):
        #print(para_list[cur])
        iter_rnd = 0
        HALT_SIG = [0,0,0,0,0]
        OP_CURSOR = [0,0,0,0,0]
        while(HALT_SIG != [1,1,1,1,1]):
            amp_a_input = h_sig
            for amp_n in range(0,5):
                #need two inputs in first round
                if(iter_rnd == 0):
                    if(amp_n == 0):
                        tmp = int_compute(para_list[cur][amp_n], mem_v[amp_n], 0, amp_n, iter_rnd)
                    else:
                        tmp = int_compute(para_list[cur][amp_n], mem_v[amp_n], tmp, amp_n, iter_rnd)
                else:
                    tmp_1 = int_compute(para_list[cur][amp_n], mem_v[amp_n], tmp, amp_n, iter_rnd)
                    
                    if tmp_1 == -1:
                        tmp = tmp
                    else:
                        tmp = tmp_1
                    print("tmp : " + str(tmp))
                    '''
                    print("tmp : " + str(tmp), end=',')
                    print("tmp type: " + str(type(tmp)), end=', ')
                    print('amp_n : ' + str(amp_n))
                    '''
            h_sig = tmp if tmp > h_sig else h_sig
            iter_rnd += 1
            print('rnd is: ' + str(iter_rnd))
        

    print("h_sig : " + str(h_sig))

    f.close()



