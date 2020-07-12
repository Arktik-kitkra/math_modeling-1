import math as m
import numpy as np
import matplotlib.pyplot as plt 

def func_trampoline(X_a, X_b, n, a, b):

    x = np.linspace(X_a, X_b, n)
    y = np.zeros(n)
    for i in range (0, n, 1):
        if x[i] < a:
            y[i] = a**2
        elif x[i] >= a and x[i] <= b:
            y[i] = x[i]**2
        else:
            y[i] = b**2
        
    plt.plot(x, y, label = "r = p/(1+ε*cosφ)")
    plt.title("Трамплин")
    plt.grid()
    plt.legend()
    plt.show()

#Подать на вход - концы рассматр. отрезка, кол-во точек, значение a и b
func_trampoline(-100, 100, 1000, -24, 57)