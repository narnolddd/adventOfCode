# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:22:22 2019

@author: Administrator
"""


class nodes_list:
    def __init__(self):
        self.num = 0
        self.list_x = []
        self.list_y = []
        self.total_steps = []
    def add_in(self, x, y):
        self.num += 1
        self.list_x.append(x)
        self.list_y.append(y)
        
    def update_steps(self, total_step):
        self.total_steps.append(total_step)
        
    def get_shortest_step(self):
        shorest_step = 1000000
        for i in range(self.num):
            if(self.total_steps[i] < shorest_step and self.total_steps[i] != 0):
                shorest_step = self.total_steps[i]
        return shorest_step
            
    def print_out(self):
        for i in range(self.num):
            print(str(self.list_x[i]) +"," + str(self.list_y[i]))

class node:
    def __init__(self):
        self.x = 0
        self.y = 0
    def print_out(self):
        print("x is "+ str(self.x) + " y is " + str(self.y))

class line:
    def __init__(self):
        self.node_1 = node()
        self.node_2 = node()
        self.node_1.x = 0
        self.node_1.y = 0
        self.node_2.x = 0
        self.node_2.y = 0
    def print_out(self):
        print(str(self.node_1.x)+","+ str(self.node_1.y)+"------>"+str(self.node_2.x)+","+ str(self.node_2.y))


def get_intersect(line_a, line_b):
    inter_node = node()
    
    if(line_a.node_1.x == line_a.node_2.x ):
        #parallel
        if(line_b.node_1.x == line_b.node_2.x and line_b.node_2.x == line_a.node_2.x):
            return None
        #intersect
        else: #elif(line_a.node_1.x != line_a.node_2.x):   
            if((max(line_b.node_1.x, line_b.node_2.x) >= line_a.node_1.x) and (min(line_b.node_1.x, line_b.node_2.x) <= line_a.node_1.x)):
                #y is in the middle
                
                if((max(line_a.node_1.y, line_a.node_2.y) >= line_b.node_2.y) and (min(line_a.node_1.y, line_a.node_2.y) <= line_b.node_2.y)):
                    inter_node.x = line_a.node_1.x
                    inter_node.y = line_b.node_1.y
                    return inter_node
    else: #y1 == y2
        if((line_b.node_1.y == line_b.node_2.y) and (line_b.node_2.y == line_a.node_2.y)):
            return None
        #intersect
        else:
            if((max(line_b.node_1.y, line_b.node_2.y) >= line_a.node_2.y) and (min(line_b.node_1.y, line_b.node_2.y) <= line_a.node_1.y)):
                if((max(line_a.node_1.x,line_a.node_2.x) >= line_b.node_2.x) and (min(line_a.node_1.x,line_a.node_2.x) <= line_b.node_2.x)):
                    inter_node.x = line_b.node_1.x
                    inter_node.y = line_a.node_1.y
                    return inter_node
    return None


f = open("input.txt","r")
line_1 = f.readline()
line_1_data = line_1.split(',', line_1.count(','))
line_2 = f.readline()
line_2_data = line_2.split(',',line_2.count(','))

node_results = nodes_list()
node_tmp1_1 = node()
node_tmp1_2 = node()
node_tmp2_1 = node()
node_tmp2_2 = node()
line1_cur = line()
line2_cur = line()

#record steps
line_1_step = 0
line_1_step_node = 0
line_2_step = 0
line_2_step_node = 0

for i in range(len(line_1_data)):
    #process line 1
    node_tmp1_1.x = node_tmp1_2.x
    node_tmp1_1.y = node_tmp1_2.y
    if(line_1_data[i][0] == 'R'):
        #if(i == 2):
        #    print("before changed: "+str(node_tmp1_2.x))
        node_tmp1_2.x += int(line_1_data[i][1:])
        line_1_step += abs(int(line_1_data[i][1:]))
        #if(i == 2):
        #    print("after changed: "+str(node_tmp1_2.x))
    elif(line_1_data[i][0] == 'L'):
        node_tmp1_2.x -= int(line_1_data[i][1:])
        line_1_step += abs(int(line_1_data[i][1:]))
    elif(line_1_data[i][0] == 'U'):
        node_tmp1_2.y += int(line_1_data[i][1:])
        line_1_step += abs(int(line_1_data[i][1:]))
        
    elif(line_1_data[i][0] == 'D'):
        node_tmp1_2.y -= int(line_1_data[i][1:])
        line_1_step += abs(int(line_1_data[i][1:]))
    else:
        print("cannot recgnize the character")
    
    line1_cur.node_1.x = node_tmp1_1.x
    line1_cur.node_1.y = node_tmp1_1.y
    line1_cur.node_2.x = node_tmp1_2.x
    line1_cur.node_2.y = node_tmp1_2.y
    
    
    #refresh line2
    node_tmp2_2.x = 0
    node_tmp2_2.y = 0
    
    line_2_step = 0
    line_2_step_node = 0
    
    for j in range(len(line_2_data)):
        
        node_tmp2_1.x = node_tmp2_2.x
        node_tmp2_1.y = node_tmp2_2.y
        #process line 2
        #print("group 2: " + line_2_data[j])
        if(line_2_data[j][0] == 'R'):
            node_tmp2_2.x += int(line_2_data[j][1:])
            line_2_step += abs(int(line_2_data[j][1:]))
        elif(line_2_data[j][0] == 'L'):
            node_tmp2_2.x -= int(line_2_data[j][1:])
            line_2_step += abs(int(line_2_data[j][1:]))
        elif(line_2_data[j][0] == 'U'):
            node_tmp2_2.y += int(line_2_data[j][1:])
            line_2_step += abs(int(line_2_data[j][1:]))
        elif(line_2_data[j][0] == 'D'):
            node_tmp2_2.y -= int(line_2_data[j][1:])
            line_2_step += abs(int(line_2_data[j][1:]))
        else:
            print("cannot recgnize the character")
        line2_cur.node_1.x = node_tmp2_1.x
        line2_cur.node_1.y = node_tmp2_1.y
        line2_cur.node_2.x = node_tmp2_2.x
        line2_cur.node_2.y = node_tmp2_2.y

        node_inters = get_intersect(line2_cur, line1_cur)
        if(node_inters):
            node_results.add_in(node_inters.x, node_inters.y)
            #calculate the actual steps
            line_1_step_node = line_1_step - abs(int(line_1_data[i][1:]))
            line_2_step_node = line_2_step - abs(int(line_2_data[j][1:]))
            #make sure we tackle the last step right
            line_1_step_node += ((abs(node_inters.x - line1_cur.node_1.x) + abs(node_inters.y - line1_cur.node_1.y)))
            line_2_step_node += ((abs(node_inters.x - line2_cur.node_1.x) + abs(node_inters.y - line2_cur.node_1.y)))
            node_results.update_steps(line_1_step_node + line_2_step_node)


#node_results.print_out()
shortest_distance = 5000
for i in range(node_results.num):
    if(abs(node_results.list_x[i]) + abs(node_results.list_y[i]) < shortest_distance and 
       abs(node_results.list_x[i]) + abs(node_results.list_y[i]) != 0):
        shortest_distance = abs(node_results.list_x[i]) + abs(node_results.list_y[i])
        
print("shortest step is: " + str(node_results.get_shortest_step()))      
print("shortest distance is: " + str(shortest_distance))
        