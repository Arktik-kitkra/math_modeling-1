import math as m
import numpy as np
import constant_module as cm

Y_sz = int(input())
X_sz = int(input())

ms_1 = np.zeros((Y_sz, X_sz))
ms_2 = np.zeros((Y_sz, X_sz))
ms_3 = np.zeros((Y_sz, X_sz))

for i in range (0, Y_sz, 1):
    for j in range (0, X_sz, 1):
        ms_1[i, j] = int(input())

print()
print("ms_1")
for i in range (0, Y_sz, 1):
    for j in range (0, X_sz, 1):
        print (ms_1[i, j], end=' ')
    print()       
     
for i in range (0, Y_sz, 1):
    for j in range (0, X_sz, 1):
        ms_2[i, j] = int(input())
        ms_3[i, j] = max(ms_1[i, j], ms_2[i, j])

print()
print("ms_2")       
for i in range (0, Y_sz, 1):
    for j in range (0, X_sz, 1):
        print (ms_2[i, j], end=' ')
    print()

print()
print("ms_3")
for i in range (0, Y_sz, 1):
    for j in range (0, X_sz, 1):
        print (ms_3[i, j], end=' ')
    print()
