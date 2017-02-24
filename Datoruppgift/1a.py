# -*- coding: utf-8 -

import numpy as np

h = np.linspace(0.0, 5.0, 100) # 0 till 5cm höjd

R = 15.0 # 15cm

n2 = 1.5

def alfa(height):
    return np.arcsin(height/R) - np.arcsin(height/(R*n2))

def f(height):
    return height / np.sin(alfa(height))

print(f(h))
