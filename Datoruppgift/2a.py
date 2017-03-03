# -*- coding: utf-8 -

import math
import numpy as np
import matplotlib.pyplot as plt

sigma = 2.8 * 10**(-23) # m^2
tau = 230.0 * 10**(-6) # µs
N_naught = 1.4 * 10**20 * 10**(-6) # cm^-3 > m^-3
D = 8.0 * 10**(-3) # mm
La = 20.0 * 10**(-2) # cm
c = 299792458.0 # m/s

R1 = 1
R2 = 0.05

tau_c = (-2.0 * La) / (c * (math.log(R1) + math.log(R2))) # La or L ??

N_inf = 0.01 * N_naught

V = La * math.pi * (D/2)**2 # La or L ??

P = N_inf / tau
B = (sigma * c) / V

dt = 200 * 10**(-6)

V_a = math.pi * (4 * 10**(-3))**2 * 20 * 10**(-2)

def T_i(i):
    if (dt * i < 0):
        return 0
    else:
        return dt * i

def N(x):
    if x <= 0:
        return N_naught
    phi_ans = phi(T_i(x-1))
    N_ans = N(T_i(x-1))
    return N_ans + (P - B * N_ans * phi_ans - N_ans / tau) * dt

def phi(x):
    if x <= 0:
        return 0
    phi_ans = phi(T_i(x-1))
    N_ans = N(T_i(x-1))
    return phi_ans + (((B * V_a * N_ans)*(phi_ans + 1) - phi_ans) / tau_c) * dt

time = range(0, 20)
x_arr = []
N_arr = []
phi_arr = []

for i in time:
    x_arr.append(T_i(i))
    N_arr.append(N(i))
    phi_arr.append(phi(i))

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(x_arr, phi_arr)
axarr[0].set_title('PHI')
axarr[1].plot(x_arr, N_arr)
axarr[1].set_title('N')

plt.show()
