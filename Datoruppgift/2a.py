# -*- coding: utf-8 -

import math
import numpy as np
import matplotlib.pyplot as plt

sigma = 2.8 * 10**(-23) # m^2
tau = 230.0 # µs
N_naught = 1.4 * 10**20 # cm^-3
D = 8.0 # mm
La = 20.0 # cm
c = 299792458.0 # m/s

R1 = 1.1
R2 = 1.1

tau_c = (-2.0 * La) / (c * (math.log(R1) + math.log(R2))) # La or L ??

N_inf = 0.01 * N_naught

V = La * math.pi * (D/2)**2 # La or L ??

P = N_inf / tau
B = (sigma * c) / V

dt = 0.01

def N(T_i):
    if (T_i == 0):
        return 0
    else:
        return N(T_i - 1) + (P - B * N(T_i - 1) * phi(T_i - 1) - N(T_i - 1) / tau) * dt

def phi(T_i):
    if (T_i == 0):
        return 0
    else:
        return phi(T_i - 1) + ((B * V * N(T_i - 1))*(phi(T_i - 1) + 1) - phi(T_i - 1) / tau_c) * dt

time_i = range(0, 12)

N_y_res = []
phi_y_res = []

for i in time_i:
    N_y_res.append(N(i))
    phi_y_res.append(phi(i))

plt.plot(time_i, N_y_res, 'r--', time_i, phi_y_res, 'b');
plt.show()
