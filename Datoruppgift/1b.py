# -*- coding: utf-8 -

import numpy as np
import math
import matplotlib.pyplot as plt

a1 = 2.271176
a2 = -9.700709 * 10**(-3) * 10**(-6)
a3 = 0.0110971 * 10**(-6)
a4 = 4.622809 * 10**(-5) * 10**(-6)
a5 = 1.616105 * 10**(-5) * 10**(-6)
a6 = -8.285042 * 10**(-7) * 10**(-6)

lambda_wave = np.linspace(400*10**(-9), 700*10**(-9), 1000)

############# debug
x = 400*10**(-9)

print("a1", a1)
print("a2", a2*x**(2))
print("a3", a3*x**(-2))
print("a4", a4*x**(-4))
print("a5", a5*x**(-6))
print("a6", a6*x**(-8))

print(math.sqrt(a1 + 
        a2*x**2 +
        a3*x**(-2) +
        a4*x**(-4) +
        a5*x**(-6) +
        a6*x**(-8)))
############ end of debug

def n(wavelen):
    return np.sqrt(a1 +
            a2*wavelen**2 +
            a3*wavelen**(-2) +
            a4*wavelen**(-4) +
            a5*wavelen**(-6) +
            a6*wavelen**(-8))

plt.plot(lambda_wave, n(lambda_wave))
#axes = plt.gca()
#axes.set_ylim([0, 3])
plt.show()
