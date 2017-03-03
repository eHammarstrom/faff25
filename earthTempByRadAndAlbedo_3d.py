# -*- coding: utf-8 -

import numpy as np
import math
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

A = np.linspace(0, 0.60, 100) # x-axel (A andel Albedo på planet)
f = np.linspace(0, 1, 100) # y-axel (f andel solstrålning som stannar kvar)

X, Y = np.meshgrid(A, f)

Fs = 1370 # Strålning från solen

sigma = 5.670367*10**(-8) # Stefan-Boltzmann

def nominator(aVal):
    return Fs * (1 - aVal)

def denominator(fVal):
    return 4.0 * sigma * (1.0 - fVal / 2.0)

def temp(nom, denom):
    return (nom/denom)**(1.0/4.0)

Z = temp(nominator(X), denominator(Y)) # Applies function on meshgrid (2cool4me)

# ax.set_zticks(np.arange(Z.min(), Z.max(), 15))
ax.set_zticks(np.arange(Z.min() - 287, Z.max() - 287, 15))
# ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, vmin=247, vmax=327)
ax.plot_surface(X, Y, Z - 287, cmap=cm.coolwarm, vmin=-40, vmax=40)

ax.set_xlabel('Albedo (andel)')
ax.set_ylabel('Absorption av långvågig strålning i atmosfär (andel)')
ax.set_zlabel('Temperaturskillnad i Celsius')

plt.show()
