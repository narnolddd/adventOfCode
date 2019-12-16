import copy
import math
import numpy as np

if __name__ == '__main__':
    #init map_str
    map_str = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            line = list(line)
            map_str.append(line)
    map_wide = len(map_str[0])
    map_len = len(map_str)
    for i in range(len(map_str)):
        for j in range(len(map_str[0])):
            pass
            #print(map_str[i][j], end = ' ')
        #print('\n')
    map_bool = []
    
    for i in range(map_len):
        new = []
        for j in range(map_wide):
            if map_str[i][j] == '#':
                new.append(1)
            else:
                new.append(0)
        map_bool.append(new)
    '''
    for i in range(map_len):
        for j in range(map_wide):
            pass
            print(map_bool[i][j], end = ' ')
        print('\n')
    '''
    inspec_data = []
    for i in range(map_len):
        new = []
        for j in range(map_wide):
            angles = []
            if map_bool[i][j] == 1:
                for m in range(map_len):
                    for n in range(map_wide):
                        if (m == i and j == n):
                            continue
                        elif map_bool[m][n] == 1:
                            #if divided num is 0
                            
                            if m == i and j == n: 
                                #because tan ranges from -inf to +inf, using char to represent inf.
                                #check if '#' already in angles
                                # '#' indicates i is below m, '$' indicates i is above m
                                pass

                            else:
                                #cal current radian
                                if(m > i):
                                    #need to plus pi
                                    sin_a = (m-i)/math.sqrt(((i-m)**2 + (j-n)**2))
                                    angle = np.arcsin(sin_a)
                                    if(j < n):
                                        angle += (1/2 * math.pi)
                                else:
                                    sin_a = (m-i)/math.sqrt(((i-m)**2 + (j-n)**2))
                                    angle = np.arcsin(sin_a) + math.pi
                                    if(m > i):
                                        angle += (1/2 * math.pi)
                                tag = 0
                                #check if there are overlaps of angle
                                for angle_com in angles:
                                    if angle == angle_com:
                                        tag = 1
                                        break
                                if tag:
                                    continue
                                else:
                                    angles.append(angle)
                        #there is no star in current pos
                        else:
                            continue
                new.append(angles)
            else:
                new.append(0)
        inspec_data.append(new)
    '''
    print(len(inspec_data))
    print(len(inspec_data[0]))
    print(len(inspec_data[1][1]))
    '''

    max_view  = 0
    x= 0
    y = 0
    for i in range(map_len):
        for j in range(map_wide):
            if isinstance(inspec_data[i][j], int):
                print(0, end = ' ')
            else:
                print(len(inspec_data[i][j]), end = ' ')
            if isinstance(inspec_data[i][j], list):
                if len(inspec_data[i][j]) > max_view:
                #> max_view:
                    max_view = len(inspec_data[i][j])
                    x = copy.deepcopy(j)
                    y = copy.deepcopy(i)
                    break
            else:
                continue
        print('\n')
    print(max_view, x, y)
