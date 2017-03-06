# -*- coding: utf-8 -

import math
import numpy as np
import matplotlib.pyplot as plt

sigma = 2.8 * 10**(-23) # m^2
tau = 230.0 * 10**(-6) # µs
N_naught = 1.4 * 10**20 * 10**6 # cm^-3 > m^-3
D = 8.0 * 10**(-3) # mm
La = 20.0 * 10**(-2) # cm
L = 60 * 10**(-2) # cm
c = 299792458.0 # m/s

def R1(time):
    if (time > 1950000):
        return 1
    else:
        return 10**(-7)

R2 = 0.05

def tau_c(time):
    return (-2.0 * L) / (c * (math.log(R1(time)) + math.log(R2))) # La or L ??

N_inf = 0.01 * N_naught

V = L * math.pi * (D/2)**2 # La or L ??

P = N_inf / tau
B = (sigma * c) / V

dt = 1*10**(-10)

V_a = math.pi * (4 * 10**(-3))**2 * La

T = range(0, 2000000)

N_arr = []
phi_arr = []
Time_arr = []

N_arr.append(0)
phi_arr.append(0)
Time_arr.append(0)

k = 0
for t in T:
    if t != len(T) - 1:
        Time_arr.append(dt * k)
        N_arr.append(N_arr[k] + (P - B * N_arr[k] * phi_arr[k] - N_arr[k]/tau) * dt)
        phi_arr.append(phi_arr[k] + (B * V_a * N_arr[k] * (phi_arr[k] + 1.0) - phi_arr[k]/tau_c(t)) * dt)

    k = k + 1

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(Time_arr, phi_arr)
axarr[0].set_title('PHI')
axarr[1].plot(Time_arr, N_arr)
axarr[1].set_title('N')

plt.show()
