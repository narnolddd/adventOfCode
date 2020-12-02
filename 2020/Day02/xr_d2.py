def day_2():
    with open('input.txt') as f:
        pwd_list = f.read().splitlines()

    value2_cnt = 0
    legal_pwd_cnt = 0

    for pwd in pwd_list:
        pwd_data = pwd.split(' ')
        # print(pwd_data)
        meta = pwd_data[0].split('-')
        pmin = int(meta[0])
        pmax = int(meta[1])
        p_cur1 = int(meta[0])
        p_cur2 = int(meta[1])
        key = pwd_data[1][0]
        value_cnt = 0
        

        for value in pwd_data[2]:
            if(value == key):
                value_cnt = value_cnt + 1
        if(value_cnt <= pmax and value_cnt >= pmin):
            legal_pwd_cnt = legal_pwd_cnt + 1

        if((pwd_data[2][p_cur1-1] == key) + (pwd_data[2][p_cur2-1] == key) == 1):
            value2_cnt = value2_cnt + 1
    return legal_pwd_cnt, value2_cnt

if __name__ == "__main__":
    result = day_2()
    print(result)