# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:41:16 2019

@author: Administrator

99: program finished
1 : adds num in two positions and store the result in third position.
2 : multiplies num in two positions and store the result in third position.
3 : takes an input to store in a specific pos
4 : outputs the value in the specific pos
"""


f = open("inputxr.txt", "r")
line = f.read()
code_list_ori = line.split(',', line.count(','))
code_list_ori = list(map(int, code_list_ori))


def result(noun, verb, code_list):
    code_list[1] = noun
    code_list[2] = verb
    op_code = 0
    while(code_list[op_code] != 99 and (code_list[op_code] == 1 or code_list[op_code] == 2)):
        
        if(code_list[op_code] == 1):
            code_list[code_list[op_code+3]] = code_list[code_list[op_code+1]] + code_list[code_list[op_code+2]]
        elif(code_list[op_code] == 2):
            code_list[code_list[op_code+3]] = code_list[code_list[op_code+1]] * code_list[code_list[op_code+2]]
        op_code += 4
    
    #print("the halt place: " + str(code_list[op_code]))
    return code_list[0]

#recover the original data
for noun_i in range(0,100):
    for verb_i in range(0,100):
        code_list_copy = code_list_ori.copy()
        output = result(noun_i, verb_i, code_list_copy)
        if int(output) == int(19690720):
            print("got noun is: " + str(noun_i) + "got verb is: " + str(verb_i))
            break;

if(noun_i == 99 and verb_i ==99):
    print("error: no answer found")
