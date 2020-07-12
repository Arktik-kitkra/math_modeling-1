import math as m
import numpy as np
import matplotlib.pyplot as plt 

#Функция построения кривых второго порядка(парабола, гипербола)
#При этом гипербола задана неявно, в каноническом виде
def sec_ord_crv(name, X_a, X_b, n, a, b, c):
    if name == "Парабола":
        x = np.linspace(X_a, X_b, n)
        y = a * x**2 + b * x + c
        plt.plot(x,y, label = "a*x^2 + b*x + c")
        plt.title(name)
        plt.grid()
        plt.legend()
        plt.show()
    elif name == "Гипербола":
        x = np.linspace(X_a, X_b, n)
        y = np.linspace(X_a, X_b, n)
        X, Y = np.meshgrid(x, y)
        fxy = X**2 / a**2 - Y**2 / b**2
        plt.contour(X, Y, fxy, levels = [1], label = "x^2/a^2 - y^2/b^2 = 1")
        plt.title(name)
        plt.grid()
        plt.legend()
        plt.show()

#Подать на вход - имя кривой, концы рассматр. отрезка, кол-во точек,
#значение коэффициентов a,b,c для параболы, a,b для гиперболы
sec_ord_crv("Гипербола", -10, 10, 1000, 3, 5, -1)
sec_ord_crv("Парабола", -13, 26, 1000, 3, 5, -1)