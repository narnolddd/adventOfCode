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


def diag_prog(input_value, code_list, error_loc):
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
                    error_loc.append(cursor)
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
                    error_loc.append(cursor)
                    code_list[code_list[cursor+3]] = exp_result
            cursor += 4
        
        elif(op_code == 3):
            #restricted by question
            op_mode = judge_mode(code_list[cursor])
            if(op_mode != 0):
                error_loc.append(cursor)
            code_list[code_list[cursor+1]] = input_value
            cursor += 2
        
        elif(op_code == 4):
            op_mode = judge_mode(code_list[cursor])
            if(op_mode == 0):
                print("the output value is (mode 0): " + str(code_list[code_list[cursor+1]]))
            elif(op_mode == 1):
                print("the output value is (mode 1): " + str(code_list[cursor+1]))
            else:
                error_loc.append(cursor)
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
                return code_list[code_list[cursor-1]]
            
        op_code = code_list[cursor]%10
    
    #end of while


f = open("input.txt", "r")
line = f.read()
code_list_ori = line.split(',', line.count(','))
code_list_ori = list(map(int, code_list_ori))

if __name__ == '__main__':

    #record the loc of errors
    error_loc = []
    input_value = 5
    correct_flag = 1
    correct_op = [1,2,3,4,5,6,7,8,99]
    correct_mode = [0,1,10,11]
    
    
    diag_prog(input_value, code_list_ori, error_loc)
    
    if(len(error_loc) != 0):
        correct_flag = 0
    
    print("error list:" + str(error_loc))
    
    if(correct_flag):
        print("test succeed!")
    
    f.close()


