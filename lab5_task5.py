import math as m
import numpy as np
import matplotlib.pyplot as plt 

def log_spir(a, b, X_a, X_b, n):
    fi = np.linspace(0, 8 * m.pi, n)

    x = np.zeros(n)
    y = np.zeros(n)
    for i in range (0, n, 1):
        x[i] = (m.e ** (b*fi[i])) * m.cos(fi[i]) * a
        y[i] = (m.e ** (b*fi[i])) * m.sin(fi[i]) * a 

    plt.plot(x, y, label = "r = a * e^(b*φ)")
    plt.grid()
    plt.title("Логарифмическая спираль")
    plt.legend()
    plt.show()
    
#Подать на вход - коэффициенты a и b, концы рассматр. отрезка, кол-во точек
log_spir(1, 0.15, -15, 15, 1000)
    
def arx_spir (k, X_a, X_b, n):
    fi = np.linspace(0, 8 * m.pi, n)

    x = np.zeros(n)
    y = np.zeros(n)
    for i in range (0, n, 1):
        x[i] = k * fi[i] * m.cos(fi[i])
        y[i] = k * fi[i] * m.sin(fi[i])

    plt.plot(x, y, label = "r = k*φ")
    plt.grid()
    plt.title("Архимедова спираль")
    plt.legend()
    plt.show()

#Подать на вход - коэффициент k, концы рассматр. отрезка, кол-во точек
arx_spir(1/(2*m.pi), -5, 5, 1000)
    
def rod_spir (a, X_a, X_b, n):
    fi = np.linspace(0.001, 8 * m.pi, n)

    x = np.zeros(n)
    y = np.zeros(n)
    for i in range (0, n, 1):
        x[i] = (a / m.sqrt(fi[i])) * m.cos(fi[i])
        y[i] = (a / m.sqrt(fi[i])) * m.sin(fi[i])

    plt.plot(x, y, label = "r = a/√φ")
    plt.grid()
    plt.title("Спираль 'Жезл'")
    plt.xlim(X_a, X_b)
    plt.legend()
    plt.show()

#Подать на вход - коэффициент ф, концы рассматр. отрезка, кол-во точек
rod_spir(5, -5, 5, 1000)
    
def rose_spir (k, X_a, X_b, n):
    if k >= 1:
        fi = np.linspace(0, 2*m.pi, n)
    else:
        fi = np.linspace(0, (2/k)*m.pi, n)
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range (0, n, 1):
        x[i] = m.sin(k*fi[i]) * m.cos(fi[i])
        y[i] = m.sin(k*fi[i]) * m.sin(fi[i])

    plt.plot(x, y, label = "r = sin(k*φ)")
    plt.grid()
    plt.title("Спираль 'Роза'")
    plt.xlim(X_a, X_b)
    plt.legend()
    plt.show()

#Подать на вход - коэффициент k, концы рассматр. отрезка, кол-во точек
rod_spir(0.1, -1, 1, 1000)
rod_spir(0.5, -1.3, 1.3, 1000)
rod_spir(1, -1, 1, 1000)
rod_spir(2, -1, 1, 1000)
rod_spir(3, -1, 1, 1000)
rod_spir(5, -1, 1, 1000)
rod_spir(6, -1, 1, 1000)
rod_spir(10, -1, 1, 1000)
    