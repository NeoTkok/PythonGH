'''
import matplotlib.pyplot as plt
colours=['b','g','r','c','m','y','k','w']
for i in range(1,6):
    with open('C:/progi/PY/dead_moroz/00'+str(i)+'.txt') as f:
        n=f.readline().rstrip()
        plt.subplot(2,3,i)
        plt.grid()
        plt.xlabel('Файл №'+str(i))
        x_list, y_list= [],[]
        for j in range(int(n)):
            x,y=map(float, f.readline().rstrip().split())
            x_list.append(x)
            y_list.append(y)
        plt.scatter(x_list,y_list, color = colours[i])
plt.show()
'''
'''
import matplotlib.pyplot as plt
colours=['b','g','r','c','m','y','k','w']
with open('C:/progi/PY/dead_moroz/ch2.txt') as f:
    for i in range(1,7):
        x_list=[float(x) for x in f.readline().rstrip().split()]
        y_list=[float(x) for x in f.readline().rstrip().split()]
        plt.subplot(2,3,i)
        plt.grid()
        plt.xlabel('Number ' + str(i))
        plt.plot(x_list,y_list,color = colours[i])
plt.show()
'''

import matplotlib.pyplot as plt
colours=['b','g','r','c','m','y','k','w']
marks_p=[0]*7
for i in range(7):
    marks_p[i]=[0]*8
marks_g=[0]*6
for i in range(6):
    marks_g[i]=[0]*8
a=True
with open('C:/progi/PY/dead_moroz/students.csv') as f:
    try:
        while a:
            a=[str(x) for x in f.readline().rstrip().split(';')]
            mark=int(a[2])
            prep_n=int(a[0][4])
            group_n=int(a[1][2])
            marks_p[prep_n-1][mark-3]+=1
            marks_g[group_n-1][mark-3]+=1
    except:
        print('end',prep_n)
#по преподавателям
plt.subplot(1,2,1)
index=[('prep'+str(x)) for x in range(1,8)]
series, cur=[], []
for i in range(8):
    for j in range(7):
        cur.append(marks_p[j][i])
    series.append(cur)
    cur=[]
for i in range(8):
    if i:
        plt.bar(index, series[i], 0.5, bottom=bot)
        for j in range(7):
            bot[j]+=series[i][j]
    else:
        plt.bar(index, series[i], 0.5)
        bot=series[0]
plt.legend([x for x in range(3,11)])

#по группам
plt.subplot(1,2,2)
index=[('75'+str(x)) for x in range(1,7)]
series,cur = [], []
for i in range(8):
    for j in range(6):
        cur.append(marks_g[j][i])
    series.append(cur)
    cur=[]
for i in range(8):
    if i:
        plt.bar(index, series[i], 0.5, bottom=bot)
        for j in range(6):
            bot[j]+=series[i][j]
    else:
        plt.bar(index, series[i], 0.5)
        bot=series[0]
plt.legend([x for x in range(3,11)])
plt.show()