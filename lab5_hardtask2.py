import math as m
import numpy as np
import matplotlib.pyplot as plt 

def polar_ellips(n, p, ex):
    fi = np.linspace(0, 2 * m.pi, n)

    x = np.zeros(n)
    y = np.zeros(n)
    for i in range (0, n, 1):
        x[i] = (p * m.cos(fi[i])) / (1 + ex * m.cos(fi[i]))
        y[i] = (p * m.sin(fi[i])) / (1 + ex * m.cos(fi[i]))
        
    plt.plot(x, y, label = "r = p/(1+ε*cosφ)")
    plt.title("Эллипс")
    plt.grid()
    plt.legend()
    plt.show()

#Подать на вход - кол-во точек, значение фокального парам. и эксцентриситета
polar_ellips(1000, 10, 0.2)


    