##bibliotecas

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

plt.plot(ricker)
plt.xlabel("Frequência")
plt.ylabel("Tempo")
plt.grid()
plt.show()

##Reflectivy function
#Geologia section

d = np.array([2.6, 2.3, 2.9])
v = np.array([2.5, 6, 6.5]) 

if d == 2.6 and v == 2.5:
    print('Clay')
    
elif d == 2.3 and v == 6:
    print('Sandstone')

elif d == 2.9 and v == 6.5:
    print('Dolomite')
    
else:
    print("nada")
    
 
    
    