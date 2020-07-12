import math as m
import numpy as np
import matplotlib.pyplot as plt 

#Функция построения кривых второго порядка(окружность, эллипс), заданных в неявном виде
def sec_ord_crv(name, X_a, X_b, n, a, b, R):
    if name == "Окружность":
        x = np.linspace(X_a, X_b, n)
        y = np.linspace(X_a, X_b, n)
        X, Y = np.meshgrid(x, y)
        fxy = X**2 + Y**2
        plt.contour(X, Y, fxy, levels = [R**2], label = "x^2 + y*2 = R^2")
        plt.title(name)
        plt.grid()
        plt.legend()
        plt.show()
    elif name == "Эллипс":
        x = np.linspace(X_a, X_b, n)
        y = np.linspace(X_a, X_b, n)
        X, Y = np.meshgrid(x, y)
        fxy = X**2 / a**2 + Y**2 / b**2
        plt.contour(X, Y, fxy, levels = [1], label = "x^2/a^2 + y*2/b^2 = 1")
        plt.title(name)
        plt.grid()
        plt.legend()
        plt.show()

#Подать на вход - имя кривой, концы рассматр. отрезка, кол-во точек,
#значение коэффициентов a,b для эллипса, радиуса для окружности
sec_ord_crv("Окружность", -5, 5, 1000, 3, 5, 4)
sec_ord_crv("Эллипс", -25, 25, 1000, 10, 5, 6)