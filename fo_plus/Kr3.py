st = input()
N = int(input())
s = []
try:
    line_count = sum(1 for line in open('C:/progi/PY/fo_plus/'+st))
    with open('C:/progi/PY/fo_plus/'+st, 'r') as f:
        for j in range(line_count): 
            s.append((f.readline().rstrip().split()))

    z = sorted(s,key=lambda e: e[1], reverse=True)
    for i in range(N):
        print(z[i][0])
except:
    print("Can not read data")