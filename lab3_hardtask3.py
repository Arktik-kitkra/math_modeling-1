import math as m
import numpy as np
import constant_module as cm

Y_sz = int(input())
X_sz = int(input())

arr = np.zeros((Y_sz, X_sz))

for i in range (0,Y_sz,1):
    for j in range (0,X_sz,1):
        arr[i,j] = int(input())
        
for i in range (0,Y_sz,1):
    for j in range (0,X_sz,1):
        print(arr[i,j], end=' ')
    print()

print
for j in range (0,X_sz,1):
    mx=0
    for i in range (0,Y_sz,1):
        if arr[i,j]>mx:
            mx = arr[i,j]
    print(mx, end=' ')
    