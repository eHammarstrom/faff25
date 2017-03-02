# -*- coding: utf-8 -

import numpy as np
import math
import matplotlib.pyplot as plt

a1 = 2.271176
a2 = -9.700709 * 10**(-3)
a3 = 0.0110971
a4 = 4.622809 * 10**(-5)
a5 = 1.616105 * 10**(-5)
a6 = -8.285042 * 10**(-7)

R = 15
h = 2.5

lambda_wave = np.linspace(0.4, 0.7, 1000)

def n(wavelen):
    return np.sqrt(a1 +
            a2*wavelen**2 +
            a3*wavelen**(-2) +
            a4*wavelen**(-4) +
            a5*wavelen**(-6) +
            a6*wavelen**(-8))

alfa = np.arcsin(h/R) - np.arcsin(h/(R*n(lambda_wave)))

f = h / np.sin(alfa)

plt.plot(lambda_wave, f)
plt.show()
