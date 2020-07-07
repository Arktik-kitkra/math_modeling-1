#import math as m
import numpy as np
import constant_module as cm

x0 = int(input())
y0 = int(input())
v0x = int(input())
voy = int(input())
Mass = np.zeros((501,3))

for t in range (0, 501, 1):
    Mass[t, 0] = t;
    Mass[t, 1] = x0 + (t/100) * v0x
    Mass[t, 2] = y0 + (t/100) * voy - cm.g * (t/100)**2 / 2
    print(Mass[t])

