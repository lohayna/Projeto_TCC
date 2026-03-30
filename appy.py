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
t = np.linspace(-1, 1, 100)

ricker = f(t, fm)

#plot of ricker

plt.plot(ricker, t)
plt.xlabel("Amplitude")
plt.ylabel("Tempo")
#plt.gca().invert_yaxis()
plt.grid()
plt.show()

##Reflectivy function
#Geologia section
depth = [10, 50, 80, 100, 200]   
#density = {"Clay": 2.6, "]Sandstone": 2.3, "Dolomite": 2.9}
density = [2.6, 2.3, 2.9, 2.3, 5]
#velocity = {"Clay": 2.5, "Sandstone": 6, "Dolomite": 6.5}
velocity = [2.5, 6, 6.5, 6, 5]

#print(density["Clay"])
#step(x, y, [fmt], *, data=None, where='pre', **kwargs)

plt.step(density, depth, where='pre')
plt.xlim(0, 20)   # eixo x vai de 2 até 10
plt.ylim(0, 500)
plt.xlabel("density")
plt.ylabel("depth")
plt.gca().invert_yaxis()
plt.grid()
plt.show()    
    
plt.step(velocity, depth, where='pre')
plt.xlim(0, 10)   # eixo x vai de 2 até 10
plt.ylim(0, 200)
plt.xlabel("velocity")
plt.ylabel("Depth")
plt.gca().invert_yaxis()
plt.grid()
plt.show() 

#Reflectivity Fuction

def R(density, velocity):
    R = np.zeros(len(density) - 1)
    for i in range(len(density) - 1):
        Z1 = density[i] * velocity[i]
        Z2 = density[i+1] * velocity[i+1]
        R[i] = (Z2 - Z1) / (Z2 + Z1)
    return R
    
density = [2.6, 2.3, 2.9, 2.3, 5]
velocity = [2.5, 6, 6.5, 6, 5]
depth = [50, 80, 100, 200]
Refletivitidade = R(density, velocity)
print(R(density, velocity))

fig, ax = plt.subplots()
ax.plot([0, 0], [min(depth), max(depth)], color='black')#linha vertical central
for depthi, Refletivitidadei in zip(depth, Refletivitidade):
    ax.plot([0, Refletivitidadei], [depthi, depthi], color='black')
ax.invert_yaxis()
#ax.axis('off')
plt.show()

# Convolution(refletivity * ricker)
#'full' → convolução completa
#same' → saída com mesmo tamanho do sinal 
#valid' → só onde há sobreposição completa

Conv = np.convolve(Refletivitidade, ricker, mode= "same")
depth_conv = np.linspace(min(depth), max(depth), len(Conv))

plt.plot(Conv, depth_conv)
plt.xlabel("Amplitude")
plt.ylabel("Tempo")
plt.gca().invert_yaxis()
plt.grid()
plt.show()