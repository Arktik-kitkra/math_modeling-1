import math as m
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(111)
dot, = ax.plot([], [], color = 'r')
xdata, ydata =[], []

def dot_move(t):
    xdata.append(np.sin(t) * (m.e ** np.cos(t) - 2 * np.cos(4*t) + np.sin(t/12) ** 5))
    ydata.append(np.cos(t) * (m.e ** np.cos(t) - 2 * np.cos(4*t) + np.sin(t/12) ** 5))

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

def animate(i):
    dot_move(i)
    dot.set_data(xdata, ydata)
    ax.set_title('Бабочка')
    return dot
    
ani = animation.FuncAnimation(fig, animate, frames = np.linspace(0, 12 * np.pi, 1000), interval = 200)
ani.save('butterfly(no swim).mp4')

ax.clear()

dot, = ax.plot([], [], color = 'r')
xdata, ydata =[], []

def dot2_move(t):
    xdata.append(16 * np.sin(t) ** 3)
    ydata.append(13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t))

ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

def animate2(i):
    dot2_move(i)
    dot.set_data(xdata, ydata)
    ax.set_title('Сердешко')
    return dot
    
ani = animation.FuncAnimation(fig, animate2, frames = np.linspace(0, 2 * np.pi, 1000), interval = 200)
ani.save('double_hurt))).mp4')