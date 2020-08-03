import math as m
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
N = 1000
k = 0.3

fig = plt.figure()

def circ_build (x0, y0, R):
    x = np.zeros(N)
    y = np.zeros(N)
    
    alpha = np.linspace(0, 2 * np.pi, N)
    x = x0 + R * np.cos(alpha)
    y = y0 + R * np.sin(alpha)
    return x, y

anim_scr = []
t = np.linspace(0, 2 * np.e, N)
R = k * t
for i in range(0, N, 1):
    x, y = circ_build(0, 0, R[i])
    circle, = plt.plot(x, y, color = 'g')
    anim_scr.append([circle])

plt.xlim(-8, 8)
plt.ylim(0, 50)
plt.axis('equal')
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')

ani = animation.ArtistAnimation(fig, anim_scr, interval = 25) 
ani.save('circ.mp4')