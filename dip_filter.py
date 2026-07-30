import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

nt = 1001 #cada traço possui nt amostras tempora
dt = 0.001 #o sismograma foi amostradado a cada 1 milissegundo
nr = 61 #numero de receptores
dr = 5 #espaçamento entre os receptores
vel = 250
angle_cut = 25

file = f"cmp_gather_{nt}x{nr}.bin"
data = np.fromfile(file, count = nt*nr, dtype = np.float32).reshape([nt,nr], order = "F")

data_fk = np.fft.fftshift(np.fft.fftn(data)) #fftn pra qualquer dimensao
frequency = np.fft.fftshift(np.fft.fftfreq(nt, dt))
wavenumber = np.fft.fftshift(np.fft.fftfreq(nr, dr))

K, F = np.meshgrid(wavenumber, frequency)
slope = np.tan(np.radians(angle_cut))
f_lim = np.abs(K) * slope * frequency.max()
mask = np.abs(F) > f_lim #<


mask = np.abs(F) > vel*np.abs(K)
mask_filt = gaussian_filter(mask.astype(float), sigma=5)

data_fk_filtered = data_fk * mask
data_filtered = np.real(np.fft.ifft2(np.fft.ifftshift(data_fk_filtered)))

# slope = np.tan(np.radians(angle_cut))


xloc = np.linspace(0, nr-1, 5, dtype = int)
xlab = np.linspace(0, nr-1, 5)*dr

tloc = np.linspace(0, nt-1, 11, dtype = int)
tlab = np.around(tloc*dt, decimals = 1)

scale = 0.9*np.std(data)

fig, ax = plt.subplots(ncols = 2, nrows = 2, figsize = (10, 8))

ax[0,0].imshow(data, aspect = "auto", cmap = "Greys", vmin = -scale, vmax = scale)
ax[0,0].set_yticks(tloc)
ax[0,0].set_yticklabels(tlab)
ax[0,0].set_xticks(xloc)
ax[0,0].set_xticklabels(xlab)
ax[0,0].set_title("Gather")
ax[0,0].set_xlabel("Offset [m]")
ax[0,0].set_ylabel("Two way time [s]")

ax[0,1].imshow(np.abs(data_fk), aspect = "auto", cmap = "jet", extent=[wavenumber.min(), wavenumber.max(), frequency.min(), frequency.max()])
ax[0,1].set_title("FK domain")
ax[0,1].set_ylim([-60, 60])
ax[0,1].set_xlabel(r"Wavenumber [m$^{-1}$]")
ax[0,1].set_ylabel("Frequency [Hz]")
ax[0,1].plot(np.zeros(nt), frequency, "--k")
ax[0,1].plot(wavenumber, np.zeros(nr), "--k")

# ax[0,1].plot(wavenumber, +slope, "--g")
# ax[0,1].plot(wavenumber, -slope, "--r")


ax[1,0].imshow(np.abs(data_fk_filtered), aspect = "auto", cmap = "jet", extent=[wavenumber.min(), wavenumber.max(), frequency.min(), frequency.max()])
ax[1,0].set_title("FK domain")
ax[1,0].set_ylim([-60, 60])
ax[1,0].set_xlabel(r"Wavenumber [m$^{-1}$]")
ax[1,0].set_ylabel("Frequency [Hz]")
ax[1,0].plot(np.zeros(nt), frequency, "--k")
ax[1,0].plot(wavenumber, np.zeros(nr), "--k")

# ax[1,0].plot(wavenumber, +slope, "--g")
# ax[1,0].plot(wavenumber, -slope, "--r")


ax[1,1].imshow(data_filtered, aspect = "auto", cmap = "Greys", vmin = -scale, vmax = scale)
ax[1,1].set_yticks(tloc)
ax[1,1].set_yticklabels(tlab)
ax[1,1].set_xticks(xloc)
ax[1,1].set_xticklabels(xlab)
ax[1,1].set_title("Gather")
ax[1,1].set_xlabel("Offset [m]")
ax[1,1].set_ylabel("Two way time [s]")
fig.tight_layout()
plt.show()