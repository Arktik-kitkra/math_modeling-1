import math as m
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot([], [], color = 'b')
line2, = ax.plot([], [], color = 'r')

def move1(A, f, i):
    x = np.linspace(0, 6, 1000) 
    y = A * np.sin(f * (x - 0.01 * i)) 
    return x, y

def move2(A, f, i):
    x = np.linspace(0, 6, 1000) 
    y = A * np.sin(f * (x - 0.01 * i)) 
    return x, y

ax.set_xlim(0, 6)
ax.set_ylim(-6, 6)

def animate(i):
    line1.set_data(move1(4, 0.5, i))
    line2.set_data(move2(3, 1.5, i))
    ax.set_title('Синусоиды бегущие,\nсобрат статичных')
    return line1, line2

ani = animation.FuncAnimation(fig, animate, frames = 1500, interval = 10, blit = True)
ani.save('sinusoid.mp4')