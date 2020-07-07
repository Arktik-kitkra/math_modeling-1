import math as m
import numpy as np
import constant_module as cm

A = []
temp = ""

print("We're ready to start!")
for i in range (0,4,1):
    A.append(int(input()))

for i in range (0,4,1):
    print(A[i], end = ' ')
print("\nPlease, enter one more symbol and it's position in array")

symb = int(input())
pos = int(input())

for i in range(pos-1,4,1):
    temp = A[i]
    A[i] = symb
    symb = temp
A.append(symb)

print(A, "\nThat's it!")
