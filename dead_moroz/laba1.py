import matplotlib.pyplot as plt
MP=[0]*7
for i in range(7):
    MP[i]=[0]*8
MG=[0]*6
for i in range(6):
    MG[i]=[0]*8
a=True
with open('C:/progi/PY/dead_moroz/students.csv') as f:
    try:
        while a:
            a=[str(x) for x in f.readline().rstrip().split(';')]
            mark=int(a[2])
            prep=int(a[0][4])
            group=int(a[1][2])
            MP[prep-1][mark-3]+=1
            MG[group-1][mark-3]+=1
    except:
        print('end')

plt.subplot(2,1,1)
plt.title('Marks per prep')
index=[('prep'+str(x)) for x in range(1,8)]
series1, Mark0=[], []
for i in range(8):
    for j in range(7):
        Mark0.append(MP[j][i])
    series1.append(Mark0)
    Mark0=[]

for i in range(8):
    if i != 0:
        plt.bar(index, series1[i], 0.5, bottom=y0)
        for j in range(7):
            y0[j]+=series1[i][j]
    else:
        plt.bar(index, series1[i], 0.5)
        y0=series1[0]
    print(y0)
plt.legend([x for x in range(3,11)])

plt.subplot(2,1,2)
plt.title('Marks per Group')
index=[('75'+str(x)) for x in range(1,7)]
series2,Mark1 = [], []
for i in range(8):
    for j in range(6):
        Mark1.append(MG[j][i])
    series2.append(Mark1)
    Mark1=[]

for i in range(8):
    if i != 0:
        plt.bar(index, series2[i], 0.5, bottom=y1)
        for j in range(6):
            y1[j]+=series2[i][j]
    else:
        plt.bar(index, series2[i], 0.5)
        y1=series2[0]
plt.legend([x for x in range(3,11)])
plt.show()