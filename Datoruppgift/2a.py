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

R1 = 1.1
R2 = 1.1

tau_c = (-2.0 * La) / (c * (math.log(R1) + math.log(R2))) # La or L ??

N_inf = 0.01 * N_naught

V = La * math.pi * (D/2)**2 # La or L ??

P = N_inf / tau
B = (sigma * c) / V

dt = 0.1

V_a = math.pi * (4 * 10**(-3))**2 * 20 * 10**(-2)

def T_i(i):
    if (dt * i < 0):
        return 0
    else:
        return dt * i

def N(x):
    phi_ans = phi(T_i(x-1))
    N_ans = N(T_i(x-1))
    return N_ans + (P - B * N_ans * phi_ans - N_ans / tau) * dt

def phi(x):
    phi_ans = phi(T_i(x-1))
    N_ans = N(T_i(x-1))
    return phi_ans + (((B * V_a * N_ans)*(phi_ans + 1) - phi_ans) / tau_c) * dt

#time = range(0, 1)
#N_arr = []
#phi_arr = []

#for i in time:
    #N_arr.append(N(i))
    #phi_arr.append(phi(i))

print(N(1))

plt.plot(time, N_arr, 'r--', time, phi_arr, 'b')
plt.show()
