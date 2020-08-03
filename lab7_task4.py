import math as m
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
N = 1000
R = 8

fig = plt.figure()

def circ_build (x0, y0, R):
    x = np.zeros(N)
    y = np.zeros(N)
    
    alpha = np.linspace(0, 2 * np.pi, N)
    x = x0 + R * np.cos(alpha) / 4
    y = y0 + R * np.sin(alpha) / 4
    return x, y

fi = np.linspace(0, 2 * np.pi, N)
circ_x = R * np.cos(fi)
circ_y = R * np.sin(fi)

astr_x = R * np.cos(fi) * np.cos(fi) * np.cos(fi)
astr_y = R * np.sin(fi) * np.sin(fi) * np.sin(fi)


centr_x = R * np.cos(fi) * 3 / 4
centr_y = R * np.sin(fi) * 3 / 4

anim_scr = []
for i in range(0, N, 1):
    x, y = circ_build(centr_x[i], centr_y[i], R)
    big_circle, = plt.plot(circ_x, circ_y, color = 'b')
    circle, = plt.plot(x, y, color = 'g')
    point, = plt.plot(astr_x[i], astr_y[i], color = 'k')
    curve, = plt.plot(astr_x[:i+1], astr_y[:i+1], color = 'r')
    anim_scr.append([big_circle, circle, curve, point])

plt.axis('equal')
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')

ani = animation.ArtistAnimation(fig, anim_scr, interval = 50) 
ani.save('astroid.mp4')