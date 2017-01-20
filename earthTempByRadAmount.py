# -*- coding: utf-8 -

import numpy as np
import math
import matplotlib.pyplot as plt

f = np.linspace(0, 1, 100) # x-axel (f andel solstrålning som stannar kvar)

Fs = 1370 # Solstrålning från solen

A = 0.28 # Jordens Albedo

sigma = 5.670367*10**(-8)

y = []

nominator = Fs * (1 - A)

def denominator(fVal):
    return 4.0 * sigma * (1.0 - fVal / 2.0)

def temp(nom, denom):
    return (nom/denom)**(1.0/4.0)

for i in range(0, 100):
    y.append(temp(nominator, denominator(f[i])))

print (temp(nominator, denominator(0.77)))

plt.plot(f, y)
plt.show()
