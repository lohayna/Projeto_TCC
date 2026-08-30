import numpy as np
import matplotlib.pyplot as plt

nt, nr = 1000, 1000
dt = 0.001
dr = 1

velocity = np.fromfile("simple_velocity_model_1000x1000.bin",dtype=np.float32).reshape((nt, nr), order="C")

data_fk = np.fft.fftshift(np.fft.fftn(velocity))
frequency = np.fft.fftshift(np.fft.fftfreq(nt, dt))
wavenumber = np.fft.fftshift(np.fft.fftfreq(nr, dr))
fk_amplitude = np.abs(data_fk)
fk_log = np.log1p(fk_amplitude)

# plt.figure(figsize=(10, 6))

# plt.imshow(np.abs(data_fk),aspect="auto",extent=[wavenumber.min(),wavenumber.max(),frequency.min(),frequency.max()],cmap="jet")
# plt.xlabel(r"Wavenumber [m$^{-1}$]")
# plt.ylabel("Frequency [Hz]")
# plt.title("F-K Domain of the Geological Model")

# plt.show()

# xloc = np.linspace(0, nr-1, 5, dtype = int)
# xlab = np.linspace(0, nr-1, 5)*dr

# tloc = np.linspace(0, nt-1, 11, dtype = int)
# tlab = np.around(tloc*dt, decimals = 1)

# scale = 0.9*np.std(velocity)
z = np.arange(nt) * dt
x = np.arange(nr)* dr

fig, ax = plt.subplots(ncols = 2, nrows = 1, figsize = (12, 6))

ax[0].imshow(velocity, aspect="auto",extent=[x.min(), x.max(), z.max(), z.min()], cmap="jet")
# ax[0].set_yticks(tloc)
# ax[0].set_yticklabels(tlab)
# ax[0].set_xticks(xloc)
# ax[0].set_xticklabels(xlab)
ax[0].set_title("Simple Geological Model")
ax[0].set_xlabel("X [m]")
ax[0].set_ylabel("Depth [m]")

ax[1].imshow(np.abs(fk_log), aspect = "auto", cmap = "jet", extent=[wavenumber.min(), wavenumber.max(), frequency.min(), frequency.max()])
ax[1].set_title("FK domain")
ax[1].set_xlabel(r"Wavenumber [m$^{-1}$]")
ax[1].set_ylabel("Frequency [Hz]")
ax[1].plot(np.zeros(nt), frequency, "--k")
ax[1].plot(wavenumber, np.zeros(nr), "--k")

fig.tight_layout()
plt.show()