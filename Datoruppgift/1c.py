# -*- coding: utf-8 -

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

a1 = 2.271176
a2 = -9.700709 * 10**(-3)
a3 = 0.0110971
a4 = 4.622809 * 10**(-5)
a5 = 1.616105 * 10**(-5)
a6 = -8.285042 * 10**(-7)

R = 15
h = 2.5

lambda_wave = np.linspace(0.4, 0.7, 1000)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


def n(wavelen):
    return np.sqrt(a1 +
            a2*wavelen**2 +
            a3*wavelen**(-2) +
            a4*wavelen**(-4) +
            a5*wavelen**(-6) +
            a6*wavelen**(-8))

X, Y = np.meshgrid(lambda_wave, n(lambda_wave))

alfa = np.arcsin(h/R) - np.arcsin(h/(R*n(lambda_wave)))

f = h / np.sin(alfa)

Z = h / np.sin(alfa)

# plt.plot(n(lambda_wave), f)

ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, edgecolor=(0,0,0,0))

plt.show()
