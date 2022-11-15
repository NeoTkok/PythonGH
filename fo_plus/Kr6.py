#st = input()

from cv2 import split


s = []
N = 20
x = 'flying'
line_count = sum(1 for line in open('C:/progi/PY/fo_plus/dd.txt'))
with open('C:/progi/PY/fo_plus/dd.txt', 'r') as f:
    for j in range(line_count): 
        s.append((f.readline().split()))
        s[j][1] = s[j][1].split(',')
p = []
for j in range(line_count): 
    if x in s[j][1] and int(s[j][2]) >= N :
        p.append(s[j])
p.sort(key=lambda e: e[2])
    
    
