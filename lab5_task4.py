import math as m
import numpy as np
import matplotlib.pyplot as plt 

def step_func():
    X_a = -3
    X_b = 3
    n = 1000
    x = np.linspace(X_a, X_b, n)
    y = np.zeros(n)
    for i in range (0, n, 1):
        y[i] = m.floor(x[i])   
    plt.plot(x, y, label = "y = N, x ∈ [N, N+1]")
    plt.grid()
    plt.title("Лесенка")
    plt.legend()
    plt.show()
    
step_func()
    