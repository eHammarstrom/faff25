# -*- coding: utf-8 -

import numpy as np
import matplotlib.pyplot as plt

h = np.linspace(-5.0, 5.0, 100) # -5cm till 5cm med 100 punkters upplösning

R = 15.0 # 15cm krökningsradie

n2 = 1.5 # brytningsindex n2

def alfa(height): # vinkel alfa 3
    return np.arcsin(height/R) - np.arcsin(height/(R*n2))

def f_sin(height): # returnerar hypotenusans längd
    return height / np.sin(alfa(height))

plt.plot(h, f_sin(h), 'bo') # plot
axes = plt.gca()
axes.set_ylim([42.8, 45.5]) # fixerad y_axel

plt.annotate('', xy=(0, 45), xytext=(0.5, 45.3), # peka ut brytning i sfärisk yta
        arrowprops=dict(facecolor='black', shrink=0.05),)

plt.show()
