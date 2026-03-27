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
t = np.linspace(-1, 1, 1000)

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
depth = [10, 50, 80, 100]   
#density = {"Clay": 2.6, "]Sandstone": 2.3, "Dolomite": 2.9}
density = [2.6, 2.3, 2.9, 2.3]
#velocity = {"Clay": 2.5, "Sandstone": 6, "Dolomite": 6.5}
velocity = [2.5, 6, 6.5, 6]

#print(density["Clay"])
#step(x, y, [fmt], *, data=None, where='pre', **kwargs)

plt.step(density, depth, where='pre')
plt.xlim(0, 10)   # eixo x vai de 2 até 10
plt.ylim(0, 200)
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
        R[i] = (density[i]*velocity[i] - density[i + 1]*velocity[i + 1]) / \
               (density[i + 1]*velocity[i + 1] + density[i]*velocity[i])
    return R
    
density = [2.6, 2.3, 2.9, 2.3]
velocity = [2.5, 6, 6.5, 6]
depth = [50, 80, 100]
Refletivitidade = R(density, velocity)
print(R(density, velocity))

plt.figure()
plt.hlines(y=depth, xmin=0, xmax=Refletivitidade, color='black')
plt.axhline()
plt.xlabel("velocity")
plt.ylabel("Depth")
plt.gca().invert_yaxis()
plt.grid()
plt.show() 
  