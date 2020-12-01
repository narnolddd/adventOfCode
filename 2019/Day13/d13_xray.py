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
output_list = []


def arcade_cabinet(code_list, iter_input):
    
    global output_list
    cursor = 0
    rela_base = 0
    op_code = code_list[cursor]%100
    input_cnt = 0
    #record pos of the ball
    ball_x = 0
    ball_y = 0
    #record pos of the paddle
    pad_x = 0
    pad_y = 0
    index = 0
    move_direction = 0
    pad_direction = 0
    
    
    while(op_code in correct_op):
        #print('op code is: ', op_code, ' cursor is: ',code_list[cursor], code_list[cursor+1],code_list[cursor+2], code_list[cursor+3])
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
                code_list[code_list[cursor+3]] = p1 + p2
            elif(op_mode[2] == 2):
                #print('cursor is: ', cursor, ' cursor is: ',code_list[cursor], code_list[cursor+1],code_list[cursor+2], code_list[cursor+3])
                #print('relative is: ', rela_base)
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
            input_cnt += 1
            if (op_mode[0] != 0):
                code_list[rela_base + code_list[cursor+1]] = pad_direction
            else:
                code_list[code_list[cursor+1]] = pad_direction
                
            cursor += 2
        

        elif(op_code == 4):
            
            if(op_mode[0] == 0):
                #print("the output value (mode 0): " + str(code_list[code_list[cursor+1]]))
                output_list.append(code_list[code_list[cursor+1]])
            elif(op_mode[0] == 2):
                
                output_list.append(code_list[rela_base + code_list[cursor+1]])
            else:
                #print("the output value (mode 1): " + str(code_list[cursor+1]))
                output_list.append(code_list[cursor+1])
            
            #find the coord of the ball and get direction
            if index == 2 and output_list[-1] == 4:
                if (len(output_list) > 3):
                    move_direction = 1 if output_list[-3] > ball_x else -1
                ball_x = output_list[-3]
                ball_y = output_list[-2]
            
            #find the coord of the paddle and determine direction
            if index == 2 and output_list[-1] == 3:
                pad_x = output_list[-3]
                pad_y = output_list[-2]
                if (pad_x > (ball_x + move_direction)):
                    pad_direction = -1
                elif (pad_x < (ball_x + move_direction)):
                    pad_direction = 1
                else:
                    pad_direction = 0
            

            #acumulate index
            index += 1
            if index % 3 == 0:
                index = 0
            else:
                pass
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
                        


def show_screen(screen_data):
    global block_cnt
    screen_len = len(screen_data)
    screen_wide = len(screen_data[0])
    for i in range(screen_len):
        for j in range(screen_wide):
            if(screen_data[i][j] == 0):
                print(' ', end = '')
            elif(screen_data[i][j] == 1):
                print('|', end = '')
            elif(screen_data[i][j] == 2):
                print('x', end = '')
            elif(screen_data[i][j] == 3):
                print('_', end = '')
            elif(screen_data[i][j] == 4):
                print('o', end = '')
        print('\n', end = '')


if __name__ == "__main__":
    f = open("input.txt", "r")
    line = f.read()
    mem = line.split(',' , line.count(','))
    mem = list(map(int, mem))
    mem[0] = 2
    screen = []
    scr_len = 25
    scr_wide = 50

    for i in range(scr_len):
        scr_line = []
        for j in range(scr_wide):
            scr_line.append(0)
        screen.append(scr_line)
    mem_extend = []
    ext_len = 100
    for i in range(ext_len):
        mem_extend.append(0)
    mem.extend(mem_extend)
    arcade_cabinet(copy.deepcopy(mem), 0)

    #modify the screen
    inx = 0
    #200 is the answer from 1st question
    block_cnt = 0
    
    
    while inx in range(len(output_list)):

        if (output_list[inx] == -1 and output_list[inx+1] == 0):
            print('final score is:', output_list[inx+2])
            break

        if(screen[output_list[inx+1]][output_list[inx]] == 0):
            if output_list[inx+2] == 1 or output_list[inx+2] == 2 or output_list[inx+2] == 3 or output_list[inx+2] == 4:
                screen[output_list[inx+1]][output_list[inx]] = output_list[inx+2]
                if output_list[inx+2] == 2:
                    block_cnt += 1
            else:
                pass
        #if this is a block, can be destroied
        elif(screen[output_list[inx+1]][output_list[inx]] == 2):
            if output_list[inx+2] == 4:
                screen[output_list[inx+1]][output_list[inx]] = 0
                block_cnt -= 1
            else:
                pass
        
        else:
            #execpts 0 and 2, every thing cannot be changed
            if(screen[output_list[inx+1]][output_list[inx]] not in [0,1,2,3,4]):
                print('unrecged ops!')
            pass

        inx += 3

    
    #draw the game figure:
    show_screen(screen)
    print('blocks is:',block_cnt)


    '''
    def int_compute(code_list, iter_input):
    
    global output_list
    cursor = 0
    rela_base = 0
    op_code = code_list[cursor]%100
    input_cnt = 0
    
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
                #print('cursor is: ', cursor, ' cursor is: ',code_list[cursor], code_list[cursor+1],code_list[cursor+2], code_list[cursor+3])
                #print('relative is: ', rela_base)
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
            input_cnt += 1
            print('input cnt: ', input_cnt)
            if (op_mode[0] != 0):
                code_list[rela_base + code_list[cursor+1]] = iter_input
            else:
                code_list[code_list[cursor+1]] = iter_input
                
            cursor += 2
        

        elif(op_code == 4):
            #print('op_mode: ' + str(op_mode))
            if(op_mode[0] == 0):
                #print("the output value (mode 0): " + str(code_list[code_list[cursor+1]]))
                output_list.append(code_list[code_list[cursor+1]])
            elif(op_mode[0] == 2):
                
                output_list.append(code_list[rela_base + code_list[cursor+1]])
            else:
                #print("the output value (mode 1): " + str(code_list[cursor+1]))
                output_list.append(code_list[cursor+1])
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
    '''