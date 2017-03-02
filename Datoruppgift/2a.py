# -*- coding: utf-8 -

import math

sigma = 2.8 * 10**(-23) # m^2
tau = 230 # µs
N_naught = 1.4 * 10**20 # cm^-3
D = 8 # mm
La = 20 # cm

R1 = 0
R2 = 0

tau_c = (-2 * La) / c(math.log(R1) + math.log(R2)) # La or L ??

N_inf = 0.01 * N_naught

V = La * math.pi * (D/2)**2 # La or L ??

P = N_inf / tau
B = (sigma * c) / V
