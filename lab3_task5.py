import math as m
import numpy as np
import constant_module as cm

N = int(input())
M = int(input())

A = np.zeros((N, M))

#Заполнение
for i in range (0, N, 1):
    for j in range (0, M, 1):
        A[i, j] = m.sin(N * (i+1) + M * (j+1))
        if A[i, j] < 0:
            A[i, j] = 0
        print('%.3f' %A[i, j], end=' ')
    print()

print()
print()
print()

#Изменение местами
for j in range (0, N, 1):
    change = A[1, j]
    A[1, j] = A[0, j]
    A[0, j] = change

for i in range (0, 2, 1):
    for j in range (0, M, 1):
        print('%.3f' %A[i, j], end=' ')
    print()