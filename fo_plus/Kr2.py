a = [int(s) for s in input().split(' ')]
N, M = a[0], a[1]
K = int(input())
A = []
for i in range(0,M+1):
    A.append([0]*(N+1))
def svet(x,y,L):
    for j in range(y-L,y+L+1):
        if (j >= 0 and j<M):    
            for k in range(x-L,x+L+1):
                if (k >= 0 and k <N):
                    A[j][k] = 1
for i in range(0, K):
    a = [int(s) for s in input().split(' ')]
    svet(a[0],a[1], a[2])
SUM = 0
for i in range(0,M):
    for j in range(0, N):
        SUM += A[i][j]
print(N*M-SUM)