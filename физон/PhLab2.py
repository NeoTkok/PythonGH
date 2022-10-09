import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
import math 

x = pd.read_excel('Лаба2П.xlsx', sheet_name='Лист2')

t = x['t'].tolist()
y1 = x['y1'].tolist()
y2 = x['y2'].tolist()

T = np.array(t)
Y2 = np.array(y2)
k = np.polyfit(T,Y2, deg=3)
K = np.poly1d(k)
X = np.linspace(12,41,59)
YY2 = K(X) 



b = np.polyfit(T[4:], Y2[4:], deg=1)
B = np.poly1d(b)
xl = np.linspace(16,40, 2)  # xl и yl новые точки прямой
yl = B(xl)
print(-b[1]/b[0])


#plt.title("")
plt.xlabel(r'$T, \quad C {\degree}$')
plt.ylabel(r'$\frac{1}{\tau^2-{\tau^2}o}, \quad мкс$')
plt.title(r'$Зависимость \quad \frac{1}{\tau^2-{\tau^2}o} \quad от \quad температуры \quad образца$')

plt.minorticks_on()
plt.grid(which='major', color='grey')
plt.grid(which='minor', color='0.9', linewidth = 1, linestyle=':')

plt.scatter(T[4:],Y2[4:], marker='+')


plt.scatter(-b[1]/b[0],0)
plt.plot(xl,yl)

#plt.errorbar(T, Y2, xerr=0.2, yerr=pl, fmt=':', ecolor='red', color='white', elinewidth=1)
plt.plot(X,YY2, linestyle = ':', linewidth = 2.5, color = 'grey')
plt.xlim(12,41)
plt.ylim(0,0.4)
#plt.savefig('figure.png')

plt.show()

#r = st.t.interval(0.68, df=len(yl)-1,loc=np.mean(Y2[4:]-B(T[4:])),scale=st.sem(Y2[4:]-B(T[4:])))
#print(abs(r[0]-r[1])/2)
#print('{0:5.2f}%'.format((100*(1-r2_score(Y2[4:], B(T[4:]))))))

y2,x2 = 0, 0
for i in range(4,len(T)):
    y2 = y2 + Y2[i]*Y2[i]
    x2 = x2 + T[i]*T[i]
y2 = y2 / len(T[4:])
x2 = x2 / len(T[4:])

Xcp = np.mean(T[4:])*np.mean(T[4:])
Ycp = np.mean(Y2[4:])*np.mean(Y2[4:])
sigmax = np.sqrt(( (y2 - Ycp) / (x2 - Xcp) - b[0]*b[0]) / len(T[4:]))
sigmay = np.sqrt(x2-Xcp)*sigmax

print('{0:5.2f}%'.format((100*sigmax/b[0])))
print('{0:5.2f}%'.format((-100*sigmay/b[1])))

print('+- {0:5.2f}'.format(-b[1]/b[0]*np.sqrt(sigmax*sigmax+sigmay*sigmay)))

print(-b[1]/b[0]*np.sqrt(sigmax*sigmax+sigmay*sigmay))

