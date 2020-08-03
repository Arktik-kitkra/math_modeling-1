import math as m
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
N = 1000
R = 4

fig = plt.figure()

def circ_build (x0, y0, R):
    x = np.zeros(N)
    y = np.zeros(N)
    
    alpha = np.linspace(0, 2 * np.pi, N)
    x = x0 + R * np.cos(alpha)
    y = y0 + R * np.sin(alpha)
    return x, y

fi = np.linspace(0, 6 * np.pi, N)
curve_x = R * (fi - np.sin(fi))
curve_y = R * (1 - np.cos(fi))
centre_x = R * fi

anim_scr = []
for i in range(0, N, 1):
    x, y = circ_build(centre_x[i], R, R)
    circle, = plt.plot(x, y, color = 'g')
    curve, = plt.plot(curve_x[:i+1], curve_y[:i+1], color = 'r')
    point, = plt.plot(curve_x[i], curve_y[i], color = 'k')
    anim_scr.append([circle, curve, point])

plt.axis('equal')
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')

ani = animation.ArtistAnimation(fig, anim_scr, interval = 25) 
ani.save('cycloid.mp4')