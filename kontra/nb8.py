INP = input().split(" ")
m, n = int(INP[0]), int(INP[1])
MAP = []
S = 0

for i in range(n):
    MAP.append((input()))

INP = input().split(" ")
X, Y = int(INP[0]), int(INP[1])

MAP2 = []

for i in range(n):
    MAP2.append([0]* m)

for i in range(n):
    for j in range(m):
        if MAP[i][j] == '.':
            MAP2[i][j] = 0
        else:
            MAP2[i][j] = 1

def sq(s, x, y):
    if (MAP2[x][y]<0 or x<0 or x>n-1 or y<0 or y>m-1 ):
        return 0
    elif MAP2[x][y] == s:
        MAP2[x][y] = -S
        a = [0] * 4
        if (x>0):
            a[0] = sq(s,x-1,y)
        else:
            a[0] = 0
        if (x<n-1):
            a[1] = sq(s,x+1,y) 
        else:
            a[1] = 0
        if (y>0):
            a[2] = sq(s,x,y-1)
        else:
            a[2] = 0
        if (y<m-1):
            a[3] = sq(s,x,y+1)
        else:
            a[3] = 0
        return (1+ sum(a))
    else:
        return 0

if MAP[Y][X] == 0:
    print(0)
else:
    print(sq(1, Y, X))