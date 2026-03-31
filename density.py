import matplotlib.pyplot as plt
import numpy as np

# eixo vertical (tempo)
#y = np.linspace(0, 10, 8)

# valores que controlam o tamanho dos "risquinhos"
#x_vals = np.array([0.2, -0.1, 0.3, -0.2, 0.15, -0.25, 0.2, -0.15])

#fig, ax = plt.subplots()

# linha vertical central
#ax.plot([0, 0], [y.min(), y.max()], color='black')

# desenhando os segmentos horizontais
#for yi, xi in zip(y, x_vals):
    #ax.plot([0, xi], [yi, yi], color='black')

# inverter eixo Y (tempo descendo)
#ax.invert_yaxis()

# remover eixos pra ficar igual ao desenho
#ax.axis('off')

#plt.show()

n = 100
den = np.zeros(n)
den[0:50] = 2.5
den[50:] = 5

print(den)