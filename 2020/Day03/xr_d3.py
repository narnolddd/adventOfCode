def day_3():
    with open('input.txt') as f:
        map_lines = f.read().splitlines()
    line_cnt = len(map_lines)
    ch_cnt = len(map_lines[0])
    trees_cnt = [0,0,0,0,0]
    x = [0,0,0,0,0]
    y = [0,0,0,0,0]
    while(y[0]<line_cnt-1):
        y[0] = y[0]+1
        y[1] = y[1]+1
        y[2] = y[2]+1
        y[3] = y[3]+1
        x[0] = (x[0]+1)%ch_cnt
        x[1] = (x[1]+3)%ch_cnt
        x[2] = (x[2]+5)%ch_cnt
        x[3] = (x[3]+7)%ch_cnt
        for i in range(4):
            if(map_lines[y[i]][x[i]] == '#'):
                trees_cnt[i] = trees_cnt[i] + 1
    while(y[4]<line_cnt-1):
        y[4] = y[4]+2
        x[4] = (x[4]+1)%ch_cnt
        if(map_lines[y[4]][x[4]] == '#'):
            trees_cnt[4] = trees_cnt[4] + 1
    
    return trees_cnt
    

if __name__ == "__main__":
    data = day_3()
    result = 1
    for i in range(5):
        result = result * data[i]
    print(result)