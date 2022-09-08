x = [0]*8 + [1]
y = int(input())
for i in range(9,y):
    x.append(x[i-1]+x[i-2]+x[i-3]+x[i-4]+x[i-5]+x[i-6]+x[i-7]+x[i-8]+x[i-9])
print(x)