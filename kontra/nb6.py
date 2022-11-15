data = {}
sorted_data = {}

N = int(input())

for i in range(N):
    name, value = input().split()
    value_int = int(value)

    if name in data:
        amount = len(data[name])
        data[name][amount + 1] = value_int
    else:
        data[name] = {1: value_int}



for name in data.keys():
    values = data[name]
    sorted_name_tuples = sorted(values.items(), key=lambda x: x[1])
    amount = len(sorted_name_tuples)
    sorted_name_dict = {}
    for i in range(amount):
        sorted_name_dict[i] = sorted_name_tuples[i][1]
    sorted_data[name] = sorted_name_dict

M = int(input())

for i in range(M):
    name = input()
    if name in sorted_data:
        amount = len(sorted_data[name])
        if amount % 2 == 0:
            number = amount // 2 - 1
            print(sorted_data[name][number])
        else:
            number = amount // 2
            print(sorted_data[name][number])
    else:
        print('no data')