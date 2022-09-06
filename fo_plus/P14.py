import numpy as np

n = int(input())
x = []
for i in range(0,n):
    x.append(int(input()))
a = np.array(x)

a.sort()

i = 0
if (a[0] < 0):
    while(a[i] < 0):
        i += 1
        if (i >= n):
            break
    print(*a[i:n], *a[i-1::-1])
else:
    print(*a)

