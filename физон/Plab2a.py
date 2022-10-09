import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = pd.read_excel('Лаба2П.xlsx', sheet_name='Лист2')

t = x['t'].tolist()
y1 = x['y1'].tolist()

T = np.array(t)
Y1 = np.array(y1)
k = np.polyfit(T,Y1, deg=5)
X = np.linspace(12,41,59)
YY1 = k[0]*X*X*X*X*X+k[1]*X*X*X*X + k[2]*X*X*X + k[3]*X*X + k[4]*X+k[5] 

plt.xlabel(r'$T, \quad C {\degree}$')
plt.ylabel(r'${\tau^2-{\tau^2}o}, \quad мкс$')
plt.title(r'$Зависимость \quad {\tau^2-{\tau^2}o} \quad от \quad температуры \quad образца$')

plt.minorticks_on()
plt.grid(which='major', color='grey')
plt.grid(which='minor', color='0.9', linewidth = 1, linestyle=':')


plt.scatter(T, Y1)
plt.plot(X,YY1, linestyle = ':', linewidth = 2.5, color = 'grey')
plt.xlim(12,41)
plt.ylim(0,60)
#plt.savefig('figure.png')

plt.show()