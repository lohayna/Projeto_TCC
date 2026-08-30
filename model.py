import numpy as np
import matplotlib.pyplot as plt

nz = 1000
nx = 1000
dz = 1.0
dx = 1.0

density = np.zeros((nz, nx))
velocity = np.zeros((nz, nx))

# Layer 1
density[0:200, :] = 2.6
velocity[0:200, :] = 2.5

# Layer 2
density[200:600, :] = 2.3
velocity[200:600, :] = 6.0

# Layer 3
density[600:1000, :] = 2.9
velocity[600:1000, :] = 6.5

# Anomalia lateral
velocity[220:280, 250:350] = 5.0

velocity.astype(np.float32).tofile("simple_velocity_model_1000x1000.bin")
# density.astype(np.float32).tofile("simple_density_model_1000x1000.bin")


velocity = np.fromfile("simple_velocity_model_1000x1000.bin",dtype=np.float32).reshape((nz, nx), order="C")
# density = np.fromfile("simple_density_model_1000x1000.bin",dtype=np.float32).reshape((nz, nx), order="C")

z = np.arange(nz) * dz
x = np.arange(nx) * dx

plt.figure(figsize=(10, 6))

plt.imshow(velocity, aspect="auto",extent=[x.min(), x.max(), z.max(), z.min()], cmap="jet")
plt.colorbar(label="Velocity [km/s]")
plt.xlabel("X [m]")
plt.ylabel("Depth [m]")
plt.title("Simple Geological Model")

plt.show()