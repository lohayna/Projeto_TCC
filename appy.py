##bibliotecas

import dataclasses
from plistlib import FMT_BINARY
import numpy as np
import matplotlib.pyplot as plt

##Input pulse(f amplitude da Ricker)
#ricker equation

def f(t,fm):

 return (1-2*(np.pi*t*fm)**2)*np.exp(-(np.pi*t*fm)**2)

fm = 5
t = np.linspace(-1, 1, 500)

ricker = f(t, fm)

##Reflectivy function
#Geologia section
depth = [0, 10, 80, 100, 200]   
#density = {"Clay": 2.6, "]Sandstone": 2.3, "Dolomite": 2.9}
density = [2.6, 2.3, 2.9, 2.3, 5]
#velocity = {"Clay": 2.5, "Sandstone": 6, "Dolomite": 6.5}
velocity = [2.5, 6, 6.5, 6, 5]

#Reflectivity Fuction

#n=500
#R = np.zeros(n)

def R(density, velocity):
    R = np.zeros(len(density) - 1)
    for i in range(len(density) - 1):
        Z1 = density[i] * velocity[i]
        Z2 = density[i+1] * velocity[i+1]
        R[i] = (Z2 - Z1) / (Z2 + Z1)
    return R
    
density = [2.6, 2.3, 2.9, 2.3, 5]
velocity = [2.5, 6, 6.5, 6, 5]
depth = [0, 10, 80, 100, 200]
Refletivitidade = R(density, velocity)
print(R(density, velocity))

# Convolution(refletivity * ricker)
#'full' → convolução completa
#same' → saída com mesmo tamanho do sinal 
#valid' → só onde há sobreposição completa

Conv = np.convolve(Refletivitidade, ricker, mode= "valid")
#depth_conv = np.linspace(min(depth), max(depth), len(Conv))

#plot of ricker

plt.subplot(1,5,1)
plt.plot(ricker, t, color="black")
#plt.xlabel("Amplitude")
#plt.ylabel("Tempo")
plt.title("Ricker")
plt.gca().invert_yaxis()
plt.grid()

#print(density["Clay"])
#step(x, y, [fmt], *, data=None, where='pre', **kwargs)

plt.subplot(1,5,2)
plt.step(density, depth, where='pre', color="black")
#plt.xlim(0, 20)   # eixo x vai de 2 até 10
#plt.ylim(0, 500)
#plt.xlabel("density")
#plt.ylabel("depth")
plt.title("Density")
plt.gca().invert_yaxis()
plt.grid()   

plt.subplot(1,5,3)    
plt.step(velocity, depth, where='pre', color="black")
#plt.xlim(0, 10)   # eixo x vai de 2 até 10
#plt.ylim(0, 200)
#plt.xlabel("velocity")
#plt.ylabel("Depth")
plt.title("Velocity")
plt.gca().invert_yaxis()
plt.grid() 

plt.subplot(1,5,4)

plt.plot([0, 0], [min(depth), max(depth)], color='black')

for depthi, Ri in zip(depth[1:], Refletivitidade):
    plt.plot([0, Ri], [depthi, depthi], color='black')

plt.gca().invert_yaxis()
plt.title("Reflectivity")
plt.grid()

plt.subplot(1,5,5)
plt.plot(Conv, color="black")
#plt.xlabel("Amplitude")
#plt.ylabel("Tempo")
plt.title("Seismic Trace")
plt.gca().invert_yaxis()
plt.grid()

plt.show()