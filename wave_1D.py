#wave propagation 1D
##bibliotecas

import numpy as np
import matplotlib.pyplot as plt

#criar modelo



#criar geometria



#ricker

def f(t,fm):

 return (1-2*(np.pi*t*fm)**2)*np.exp(-(np.pi*t*fm)**2)

fm = 5
t = np.linspace(-1, 1, 1000)

ricker = f(t, fm)

#DIFERENÇAS FINITAS

def wave(x, t, v, A, L):
    