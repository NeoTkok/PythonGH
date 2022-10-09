x = [1,5,3]
y = [4,7,5]
xy,x2 = 0, 0
import numpy as np
for i in range(0,len(x)):
    xy = xy + x[i]*y[i]
    x2 = x2 + x[i]*x[i]
print(x2)