#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:02:55 2020

@author: akel
"""


from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def SIR(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

N = 1000
beta = 1  
D = 7.0 
gamma = 1.0 / D

S0, I0, R0 = 999, 1, 0  
t = np.linspace(0, 49, 10000) 
y0 = S0, I0, R0 

out = odeint(SIR, y0, t, args=(N, beta, gamma))

S, I, R = out.T

plt.plot(t,S,label='S')
plt.plot(t,I,label='I')
plt.plot(t,R,label='R')
plt.legend()


plt.show()

