import numpy as np

x,y = input().split(" ")

z = []
for i in range(0,int(x)+100):
    z.append([0]* (int(y)+100))


N = int(input())
print(z[1][3])

for i in range(0, N):    
    xmin, xmax, ymin, ymax = input().split(" ")

    for j in range(int(ymin), int(ymax)):
        for k in range(int(xmin), int(xmax)):
            z[j][k] = z[j][k] + 1

print(z)