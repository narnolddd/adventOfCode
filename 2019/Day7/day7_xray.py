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

'''
def int_prog(input_value, code_list, iter_input):
    global HALT
    cursor = 0
    input_cnt = 0
    op_code = code_list[cursor]%10
    
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
            if (input_cnt == 0):
                code_list[code_list[cursor+1]] = input_value
                input_cnt = 1
            else:
                code_list[code_list[cursor+1]] = iter_input
            cursor += 2
        
        elif(op_code == 4):
            op_mode = judge_mode(code_list[cursor])
            if(op_mode == 0):
                #print("the output value is (mode 0): " + str(code_list[code_list[cursor+1]]))
                return code_list[code_list[cursor+1]]
            elif(op_mode == 1):
                #print("the output value is (mode 1): " + str(code_list[cursor+1]))
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
                print("final answer: " + code_list[code_list[cursor-1]])
                
                return code_list[code_list[cursor-1]]
                      
        op_code = code_list[cursor]%10
    
    #end of while
'''

'''
iter_rnd= iter rounds
code_list = the program
iter_input = input
is_amp1 = 1 for yes, 0 for no
setting para= setting parameter of each amp
'''

def int_prog(iter_rnd, code_list, iter_input, amp_num, setting_para):
    global HALT, OP_CURSOR
    input_cnt_amp = 0
    cursor = 0
    op_code = code_list[cursor]%10
    
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
            if (iter_rnd == 0):
                if(amp_num == 0):
                    code_list[code_list[cursor+1]] = 0 if input_cnt_amp == 0 else setting_para
                    input_cnt_amp = 1
                else:
                    code_list[code_list[cursor+1]] = setting_para if input_cnt_amp == 0 else input_cnt_amp
                    input_cnt_amp = 1
            else:
                code_list[code_list[cursor+1]] = iter_input
            cursor += 2
        
        elif(op_code == 4):
            op_mode = judge_mode(code_list[cursor])
            if(op_mode == 0):
                #print("the output value is (mode 0): " + str(code_list[code_list[cursor+1]]))
                OP_CURSOR[amp_num] = cursor+2
                return code_list[code_list[cursor+1]]
            elif(op_mode == 1):
                #print("the output value is (mode 1): " + str(code_list[cursor+1]))
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
                #print("final answer: " + code_list[code_list[cursor-1]])
                HALT[amp_num] = 1
                print("amplifier halt: NO." + str(amp_num))
                
                #return code_list[code_list[cursor-1]]
                      
        op_code = code_list[cursor]%10

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
            

f = open("test.txt", "r")
line = f.read()
code_list_ori = line.split(',', line.count(','))
code_list_ori = list(map(int, code_list_ori))
COUNT=0
HALT = [0,0,0,0,0] #record if the prog is halt
OP_CURSOR = [0,0,0,0,0] #record the cursor of the control program

if __name__ == '__main__':


    input_value = 5
    correct_op = [1,2,3,4,5,6,7,8,99]
    correct_mode = [0,1,10,11]
    

    h_sig = 0
    n = [5,6,7,8,9]
    set_list = []
    perm(n, 0, 5, set_list)

    for cursor in range(0,1):  #change to COUNT
        setting = set_list[cursor]

        iter_rnd = 0
        tmp = 0
        #for rnd in range (0,3):
        while(HALT != [1,1,1,1,1]):
            if(iter_rnd == 0):  #iterl before system halt
                for i in range(0, 5):
                    tmp = int_prog(0, code_list_ori[OP_CURSOR[i]:], copy.deepcopy(tmp), i, setting[i])
                    print("code_list: " + str(code_list_ori[OP_CURSOR[4]:]))
                    print("CURSOR: " + str(OP_CURSOR))
                h_sig = tmp if tmp > h_sig else h_sig
            else:
                for i in range(0, 5):
                    tmp = int_prog(iter_rnd, code_list_ori[OP_CURSOR[i]:], copy.deepcopy(tmp), i, setting[i])
                h_sig = tmp if tmp > h_sig else h_sig
            OP_CURSOR = [0,0,0,0,0]
            iter_rnd += 1
                    
    print("h_sig: " + str(h_sig))

    f.close()


    '''question 1
    #record the highest signal value so far
    h_sig = 0
    n=[0,1,2,3,4]
    set_list = []
    perm(n, 0, 5, set_list)
    for cursor in range(0,COUNT):
        setting = set_list[cursor]
        amp_switch = 0
        #detect final loop:
        for i in range(0,5):
            if i == 0:
                tmp = int_prog(set_list[cursor][i], copy.deepcopy(code_list_ori), 0)
                
            else:
                #print("tmp is: " + str(tmp) + "i is : " + str(i))
                tmp = int_prog(set_list[cursor][i], copy.deepcopy(code_list_ori), copy.deepcopy(tmp))
                #print("tmp then is: " + str(tmp) + "i is : " + str(i))

        h_sig = tmp if tmp > h_sig else h_sig
    '''

    '''
    iter_rnd= iter rounds
    code_list = the program
    iter_input = input
    amp_num = 0-4
    setting para= setting parameter of each amp
    '''
