import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1,10,100)
f = np.sin(x)*np.exp(-x)
plt.figure()
plt.plot(x,f)
plt.show()