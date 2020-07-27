import math as m
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(111)
dot, = ax.plot([], [], color = 'r')
xdata, ydata = [], []


def move1(t, C, D):
    if t == 0:
        xdata.append(0.1)
        ydata.append(0.1)
    else:
        xdata.append(xdata[t-1] ** 2 - ydata[t-1] ** 2 + C)
        ydata.append(2 * xdata[t-1] * ydata[t-1] + D)

ax.set_xlim(-0.2, 0.4)
ax.set_ylim(0, 0.7)

def animate(i):
    move1(i, 0.3, 0.33)
    dot.set_data(xdata, ydata)
    ax.set_title('Фрактальное множество')
    return dot,

ani = animation.FuncAnimation(fig, animate, frames = 100, interval = 150)
ani.save('fractal.mp4')