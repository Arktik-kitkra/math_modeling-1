import math as m
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
N = 1000

fig = plt.figure()

def star_build():
    t = np.linspace(0, 4 * np.pi, N)
    x = 12 * np.cos(t) + 8 * np.cos(1.5 * t)
    y = 12 * np.sin(t) - 8 * np.sin(1.5 * t)
    return x, y

anim_scr = []
t = np.linspace(0, 4 * np.pi, N)
for i in range(0, N, 1):
    x, y = star_build()
    X = x * np.cos(t[i]) - y * np.sin(t[i])
    Y = y * np.cos(t[i]) + x * np.sin(t[i])
    star, = plt.plot(X, Y, color = 'r')
    anim_scr.append([star])
    
plt.axis('equal')
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')

ani = animation.ArtistAnimation(fig, anim_scr, interval = 50) 
ani.save('star.mp4')