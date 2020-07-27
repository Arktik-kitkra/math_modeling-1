import math as m
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation


fig = plt.figure()
ax = fig.add_subplot(111)
dot, = plt.plot([], [], marker = 'o', color = 'r')

def dot_move(R, fi):
    x = R * (fi - np.sin(fi))
    y = R * (1 - np.cos(fi)) 
    
    return x, y

ax.set_xlim(-1, 51)
ax.set_ylim(-1, 9)

def animate(i):
    dot.set_data(dot_move(4, i))
    ax.set_title('Циклоида')

ani = animation.FuncAnimation(fig, animate, frames = np.linspace(0, 4 * np.pi, 1000), interval = 100)
cycl = dot_move(4, np.linspace(0, 4 * np.pi, 1000))
plt.plot(cycl[0], cycl[1])

ani.save('cycl.mp4')

ax.clear()
dot, = plt.plot([], [], marker = 'o', color = 'r')

def dot2_move(R, fi):
    x = R * np.cos(fi) ** 3
    y = R * np.sin(fi) ** 3
    
    return x, y

ax.set_xlim(-15, 15)
ax.set_ylim(-9, 9)

def animate2(i):
    dot.set_data(dot2_move(6, i))
    ax.set_title('Астроида')
    
ani = animation.FuncAnimation(fig, animate2, frames = np.linspace(0, 4 * np.pi, 1000), interval = 100)
astr = dot2_move(6, np.linspace(0, 2 * np.pi, 1000))
plt.plot(astr[0], astr[1])
ani.save('astr.mp4')