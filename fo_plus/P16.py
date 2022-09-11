INP = input().split(" ") # размеры стены
x, y = int(INP[0]), int(INP[1])

N = int(input()) # колличесво окон
z = []
m = []
m.append([1]*x)
for i in range(1,y-1):
    m.append([1]+[0]*(x-2)+[1])
m.append([1]*x)

#"""
for i in range(0, N): 
    z.append([int(s) for s in input().split(" ")])

for i in range(0, N):

    for j in range(z[i][0],z[i][2]):
        for k in range(z[i][1],z[i][3]):
            m[k][j] = 1


#"""
sumM = 0
for i in range(0,y):
    sumM = sum(m[i]) + sumM 
    print(m[i])
print(sumM)