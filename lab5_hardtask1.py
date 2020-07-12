import math as m
import numpy as np
import matplotlib.pyplot as plt 

def lissajou_curv(b, B = 5, A = 1, delt = m.pi, a = 1):
    n = 1000
    t = np.linspace(0, 100, n)
    
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range (0, n, 1):
        x[i] = A * m.sin(a * t[i] * delt)
        y[i] = B * m.sin(b * t[i])
    
    plt.plot(x, y, label = "x = A * sin(a * t + δ) \ny = B * sin(b * t)")
    plt.grid()
    plt.title("Фигура Лиссажу")
    plt.legend()
    plt.show()

#Подать на вход - значение коэффициента b
lissajou_curv(0.5)