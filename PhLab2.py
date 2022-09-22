import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = pd.read_excel('Лаба2П.xlsx', sheet_name='Лист2')

t = x['t'].tolist()
y1 = x['y1'].tolist()
y2 = x['y2'].tolist()

T = np.array(t)
Y1 = np.array(y1)
Y2 = np.array(y2)
k = np.polyfit(T,Y2, deg=3)

X = np.linspace(12,41,59)
YY2 = k[0]*X*X*X + k[1]*X*X + k[2]*X + k[3] 
pl = T*0.0006
b = np.polyfit(T[3:], Y2[3:], deg=1)

xl = np.linspace(16,40, 2)
yl = b[0]*xl+b[1]
print(-b[1]/b[0])


#plt.title("")
plt.xlabel(r'$T, \quad C {\degree}$')
plt.ylabel(r'$\frac{1}{\tau^2-{\tau^2}o}, \quad мкс$')
plt.title(r'$Зависимость \quad \frac{1}{\tau^2-{\tau^2}o} \quad от \quad температуры \quad образца$')

plt.minorticks_on()

plt.grid(which='major', color='grey')
plt.grid(which='minor', color='0.9', linewidth = 1, linestyle=':')


plt.scatter(-b[1]/b[0],0)
plt.plot(xl,yl)

plt.errorbar(T, Y2, xerr=0.2, yerr=pl, fmt=':', ecolor='red', color='white', elinewidth=1)
plt.plot(X,YY2, linestyle = ':', linewidth = 2.5, color = 'grey')
plt.xlim(12,41)
plt.ylim(0,0.4)
plt.savefig('figure.png')

plt.show()




