# -*- coding: utf-8 -*-
"""
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

correct_op = [1,2,3,4,5,6,7,8,9,99] #supported operations so far
# define macros of directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3 
cursor = 0
rela_base = 0

def int_compute(code_list, iter_input):
    #cursor = 0
    global cursor
    global rela_base
    op_code = code_list[cursor]%100
    output_cnt = 0
    output = []
    #print('op code is: ', op_code, ' cursor is: ',code_list[cursor], code_list[cursor+1],code_list[cursor+2])
    
    while(op_code in correct_op):
        #print('op code is: ', op_code, ' cursor is: ',code_list[cursor], code_list[cursor+1],code_list[cursor+2], code_list[cursor+3])
        op_code = code_list[cursor]%100
        op_mode = []
        op_mode_int = code_list[cursor]//100
        #print('op_mode_int: ' +str(op_mode_int))
        for i in range(0,3):
            op_mode.append(op_mode_int%10)
            op_mode_int = op_mode_int//10
        
        #print('op_mode is ', op_mode)

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
                code_list[code_list[cursor+3]] = p1 + p2
            elif(op_mode[2] == 2):
                code_list[rela_base + code_list[cursor+3]] = p1+ p2
            else:
                print('error getting addr in op1')
            cursor += 4
                
        elif(op_code == 2):
            #print('curr pos: ', code_list[cursor], code_list[cursor+1], code_list[cursor+2], code_list[cursor+3])
            if(op_mode[0] == 0):
                #print('curr pos: ', code_list[cursor+1])
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
                #print("the output value (mode 0): " + str(code_list[code_list[cursor+1]]))
                if not output_cnt:
                   
                    output.append(code_list[code_list[cursor+1]])
                    output_cnt += 1
                else:
                    output.append(code_list[code_list[cursor+1]])
                    cursor += 2
                    return output
            elif(op_mode[0] == 2):
                #print("the output value (mode 2): " + str(code_list[rela_base + code_list[cursor+1]]))
                if not output_cnt:
                    output.append(code_list[rela_base + code_list[cursor+1]])
                    output_cnt += 1
                else:
                    output.append(code_list[rela_base + code_list[cursor+1]])
                    cursor += 2
                    return output
            else:
                #print("the output value (mode 1): " + str(code_list[cursor+1]))
                if not output_cnt:
                    output.append(code_list[cursor+1])
                    output_cnt += 1
                else:
                    output.append(code_list[cursor+1])
                    cursor += 2
                    return output
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
                print("program halt at: " + str(code_list[cursor-1]))
                return -1
        
        op_code = code_list[cursor]%100
    
    print('break: error: ', code_list[cursor], ' next value: ', code_list[cursor+1])
                        


def turn_direc(curr_dirc, turn_act):
    if(curr_dirc == UP):
        next_dirc = RIGHT if turn_act else LEFT
    elif(curr_dirc == LEFT):
        next_dirc = UP if turn_act else DOWN
    elif(curr_dirc == DOWN):
        next_dirc = LEFT if turn_act else RIGHT
    elif(curr_dirc == RIGHT):
        next_dirc = DOWN if turn_act else UP
    else:
        print('unrecged direction!')
        next_dirc = -1
    return next_dirc



if __name__ == "__main__":
    f = open("input.txt", "r")
    line = f.read()
    mem = line.split(',' , line.count(','))
    mem = list(map(int, mem))
    add = []
    for i in range(1000):
        add.append(0)
    mem.extend(add)

    panel_wide = 60
    panel_len = 100
    panel = []
    for i in range(panel_len):
        line = []
        for j in range(panel_wide):
            line.append([0,0])
        panel.append(line)
    
    coord_x = 10
    coord_y = 50
    cur_direction = UP

    #the first panel is white (1)
    panel[coord_y][coord_x][0] = 1
    cur_output = int_compute(mem, panel[coord_y][coord_x][0])
    

    while(cur_output != -1):
        panel[coord_y][coord_x][0] = cur_output[0]
        panel[coord_y][coord_x][1] = 1
        next_direction = turn_direc(cur_direction,cur_output[1])
        if next_direction == UP:
            coord_y -= 1
        elif next_direction == DOWN:
            coord_y += 1
        elif next_direction == LEFT:
            coord_x -= 1
        elif next_direction == RIGHT:
            coord_x += 1
        else:
            break
        print('x = ', coord_x, ' y = ', coord_y)
        cur_output = int_compute(mem, panel[coord_y][coord_x][0])
        cur_direction = next_direction
        
    f.close()
    
    all_cnt = 0
    for i in range(panel_len):
        for j in range(panel_wide):
            if panel[i][j][1]:
                all_cnt += 1

    for i in range(panel_len):
        for j in range(panel_wide):
            if(panel[i][j][0] == 1):
                print('8', end=' ')
            else:
                print(' ', end = ' ')
        print('\n')