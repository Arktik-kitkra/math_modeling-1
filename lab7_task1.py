import math as m
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
N = 1000
R = 2

fig = plt.figure()

def circ_build (x0, y0, R):
    x = np.zeros(N)
    y = np.zeros(N)
    
    alpha = np.linspace(0, 2 * np.pi, N)
    x = x0 + R * np.cos(alpha)
    y = y0 + R * np.sin(alpha)
    return x, y

curve_x = np.linspace(-7, 7, N)
curve_y = curve_x * curve_x

anim_scr = []
for i in range(0, N, 1):
    x, y = circ_build(curve_x[i], curve_y[i], R)
    circle, = plt.plot(x, y, color = 'g')
    point, = plt.plot(curve_x[i], curve_y[i], color = 'g')
    parab, = plt.plot(curve_x, curve_y, color = 'r')
    anim_scr.append([circle, parab, point])

plt.xlim(-8, 8)
plt.ylim(0, 50)
plt.axis('equal')
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')

ani = animation.ArtistAnimation(fig, anim_scr, interval = 25) 
ani.save('curve.mp4')