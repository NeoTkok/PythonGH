INP = input().split(" ") # размеры стены
M, N = int(INP[0]), int(INP[1])
ST = []

for i in range(N):
    ST.append((input()))

XYZ = input().split(" ") # размеры стены
x, y, L = int(XYZ[0]), int(XYZ[1]), int(XYZ[2])
z = 0
for i in range(y-L, y+L+1):
    for j in range(x-L, x+L+1):
        if (i>=0 and i<N and j>=0 and j<M):
            print(ST[i][j], end='')
            z = 1
    if (z == 1):
        print()

