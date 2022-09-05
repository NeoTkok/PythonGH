import matplotlib.pyplot as plt
import numpy as np


xmin, xmax = -10*np.pi, 10*np.pi
n = 1000

x = np.linspace(xmin, xmax, n)
y1 = np.abs(np.sin(x)/x*25)
y2 = np.cos(x)*x

plt.plot(x, y1)
plt.plot(x, y2)

plt.show()

