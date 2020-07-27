import math as m
import numpy as np
import matplotlib.pyplot as plt 

def cycloid(R, n):
    t = np.linspace(0, 4*m.pi, n)
    
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    
    plt.plot(x, y)
    plt.title("Циклоида")
    plt.grid()
    plt.legend()
    plt.show()

def astroid(R, n):
    t = np.linspace(0, 8*m.pi, n)
    
    x = R * np.cos(t)**3
    y = R * np.sin(t)**3
    
    plt.plot(x, y)
    plt.title("Астроида")
    plt.grid()
    plt.legend()
    plt.show()


cycloid(1.5, 1000)
astroid(12, 1000)