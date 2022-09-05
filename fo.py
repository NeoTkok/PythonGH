def sum3(i):
    
    x, sum = i, 0
    sum += x//100
    x %= 100
    sum += x//10
    x %= 10
    sum += x 
    return sum 

x = []

for i in range(1000000):
    if (sum3(i%1000) == sum3(i//1000)):
        x.append(1)
    else:
        x.append(0)

m = 0
with open('sila.txt', 'w') as f:
    for i in range(1000000):
        if(x[i] == 1):
            m += 1
            print('{i:06d}'.format(i = i), sep='', file = f)

print(m/10000, '%')