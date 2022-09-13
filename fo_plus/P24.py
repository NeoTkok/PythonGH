a = [int(s) for s in input().split(' ')]
a.sort()
xPred = len(a) - 1
x = 0
while(xPred > 0): 
    if (a[xPred] != a[xPred-1] and x == 0):
        print(a[xPred])
        break
    if (a[xPred] != a[xPred-1]):
        x = 0
    else:
        x = 1
    a.pop(xPred)
    xPred = xPred - 1
