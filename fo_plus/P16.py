INP = input().split(" ") # размеры стены
x, y = int(INP[0]), int(INP[1])

N = int(input()) # колличесво окон
z = []
m = []
for i in range(0,y):
    m.append([0]*x)

#"""
for i in range(0, N): 
    z.append([int(s) for s in input().split(" ")])

for i in range(0, N):

    for j in range(z[i][0],z[i][2]):
        for k in range(z[i][1],z[i][3]):
            m[j][k] = m[j][k] + 1


#"""
exitFlag = False
for i in range(0,y):
    for j in range(0,x): 
        if (m[i][j] > 1):
            print("broken") 
            exitFlag = True
            break 
    if (exitFlag == True):
        break
if (exitFlag == False):
    print("correct")