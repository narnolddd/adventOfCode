
with open('input_xr.txt') as f:
    data_list = f.read().splitlines()
    data_list = [int(i) for i in data_list]

for i in range(len(data_list)):
    for j in range(i, len(data_list)):
        for k in range(j, len(data_list)):
            if(data_list[i] + data_list[j] + data_list[k] == 2020):
                result = data_list[i]*data_list[j]*data_list[k]

print(result)

