def m1(y):
    ind = 0
    for k in range(0, len(y)):
        if (y[k] > y[ind]):
            ind = k
    return ind

a = [str(s) for s in input().split(' ')]
x = [] 
x.extend(a)
i = 0
while i < len(x):
    if x.count(x[i]) > 1:
        del x[i]
        i = i - 1
    i = i + 1
x.sort()
y = []
for i in range(0,len(x)):
    y.append(a.count(x[i]))
i = max(y) + 1
j = 0
while len(x) > 0:
    idG = m1(y)
    print(f'{y[idG]} {x[idG]}')
    del y[idG]
    del x[idG]

    