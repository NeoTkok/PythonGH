from logging import exception

import math
try:
    class Ball:
        def __init__(self,x,y,m):
            if(m <= 0):
                l = math.sqrt(-1)
            self.x = x
            self.y = y
            self.m = m
        def move(self, a, b):
            self.x += a
            self.y += b
except:
    print('exception')

b = Ball(0.0, 0.0, -1.0)
print(b.x, b.y, b.m)
b.move(1.0, -1.0)

print(b.x, b.y, b.m)


