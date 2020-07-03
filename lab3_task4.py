import math as m
import numpy as np
import constant_module as cm

N = int(input())
M = int(input())

A = np.zeros((N, M))

for i in range (0, N, 1):
    for j in range (0, M, 1):
        A[i, j] = m.sin(N * (i+1) + M * (j+1))
        if A[i, j] < 0:
            A[i, j] = 0
        print('%.3f' %A[i, j], end='10')
    print()
    

