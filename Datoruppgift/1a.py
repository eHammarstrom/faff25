# -*- coding: utf-8 -

import numpy as np
import matplotlib.pyplot as plt

h = np.linspace(-5.0, 5.0, 100) # 0.1 till 5cm höjd

R = 15.0 # 15cm

n2 = 1.5

def alfa(height):
    return np.arcsin(height/R) - np.arcsin(height/(R*n2))

def f_sin(height):
    return height / np.sin(alfa(height))

def f_tan(height):
    return height / np.tan(alfa(height))

plt.plot(h, f_sin(h), 'r--', h, f_tan(h), 'b')
axes = plt.gca()
axes.set_ylim([42.8, 45.5])

plt.annotate('Paraxialapproximation', xy=(0, 45), xytext=(0.5, 45.3),
            arrowprops=dict(facecolor='black', shrink=0.05),)

plt.show()
