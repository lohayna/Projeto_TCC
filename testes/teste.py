import numpy as np
import matplotlib.pyplot as plt

nt = 1001
dt = 0.001
nr = 61
dr = 5
velocity_cut = 250

file = f"cmp_gather_{nt}x{nr}.bin"
data = np.fromfile(file, count=nt*nr, dtype=np.float32).reshape([nt, nr], order="F")

# --- zero-padding espacial para suavizar o eixo do wavenumber ---
nr_pad = 256  # aumente para mais suavidade (ex: 512)

def to_fk(d, nr_pad):
    return np.fft.fftshift(np.fft.fft2(d, s=(nt, nr_pad)))

data_fk = to_fk(data, nr_pad)
frequency = np.fft.fftshift(np.fft.fftfreq(nt, dt))
wavenumber = np.fft.fftshift(np.fft.fftfreq(nr_pad, dr))

# dip filtering (no domínio original, sem padding, pra não distorcer o dado)
data_fk_full = np.fft.fftshift(np.fft.fftn(data))
frequency_full = np.fft.fftshift(np.fft.fftfreq(nt, dt))
wavenumber_full = np.fft.fftshift(np.fft.fftfreq(nr, dr))
K, F = np.meshgrid(wavenumber_full, frequency_full)
mask = np.abs(K) > np.abs(F) / velocity_cut
data_fk_filtered = data_fk_full.copy()
data_fk_filtered[mask] = 0
data_filtrada = np.real(np.fft.ifft2(np.fft.ifftshift(data_fk_filtered)))

# FK do filtrado, também com padding pra visualização
data_fk_after = to_fk(data_filtrada, nr_pad)

def to_db(spec, floor_db=-50):
    amp = np.abs(spec)
    amp_db = 20 * np.log10(amp / (amp.max() + 1e-12) + 1e-12)
    return np.clip(amp_db, floor_db, 0)

fk_db_before = to_db(data_fk)
fk_db_after  = to_db(data_fk_after)

xloc = np.linspace(0, nr-1, 5, dtype=int)
xlab = np.linspace(0, nr-1, 5) * dr
tloc = np.linspace(0, nt-1, 11, dtype=int)
tlab = np.around(tloc * dt, decimals=1)

scale = 0.9 * np.std(data)
extent = [wavenumber.min(), wavenumber.max(), frequency.min(), frequency.max()]

f = np.linspace(-60, 60, 500)
k = f / velocity_cut

# faixa de zoom no eixo do wavenumber (onde a energia realmente está)
k_zoom = 0.15

fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(11, 9))

ax[0,0].imshow(data, aspect="auto", cmap="Greys", vmin=-scale, vmax=scale)
ax[0,0].set_yticks(tloc); ax[0,0].set_yticklabels(tlab)
ax[0,0].set_xticks(xloc); ax[0,0].set_xticklabels(xlab)
ax[0,0].set_title("Gather")
ax[0,0].set_xlabel("Offset [m]")
ax[0,0].set_ylabel("Two way time [s]")

im1 = ax[0,1].imshow(fk_db_before, aspect="auto", cmap="jet", extent=extent,
                      vmin=-50, vmax=0, origin="lower", interpolation="bilinear")
ax[0,1].set_title("FK domain (antes do filtro)")
ax[0,1].set_xlabel(r"Wavenumber [m$^{-1}$]")
ax[0,1].set_ylabel("Frequency [Hz]")
ax[0,1].axhline(0, color="k", ls="--", lw=1)
ax[0,1].axvline(0, color="k", ls="--", lw=1)
ax[0,1].plot(k, f, "--w", lw=2)
ax[0,1].plot(-k, f, "--w", lw=2)
ax[0,1].set_xlim([-k_zoom, k_zoom])
ax[0,1].set_ylim([-60, 60])
fig.colorbar(im1, ax=ax[0,1], label="dB")

im2 = ax[1,0].imshow(fk_db_after, aspect="auto", cmap="jet", extent=extent,
                      vmin=-50, vmax=0, origin="lower", interpolation="bilinear")
ax[1,0].set_title("FK domain (depois do filtro)")
ax[1,0].set_xlabel(r"Wavenumber [m$^{-1}$]")
ax[1,0].set_ylabel("Frequency [Hz]")
ax[1,0].axhline(0, color="k", ls="--", lw=1)
ax[1,0].axvline(0, color="k", ls="--", lw=1)
ax[1,0].plot(k, f, "--w", lw=2)
ax[1,0].plot(-k, f, "--w", lw=2)
ax[1,0].set_xlim([-k_zoom, k_zoom])
ax[1,0].set_ylim([-60, 60])
fig.colorbar(im2, ax=ax[1,0], label="dB")

ax[1,1].imshow(data_filtrada, aspect="auto", cmap="Greys", vmin=-scale, vmax=scale)
ax[1,1].set_yticks(tloc); ax[1,1].set_yticklabels(tlab)
ax[1,1].set_xticks(xloc); ax[1,1].set_xticklabels(xlab)
ax[1,1].set_title("Gather filtrado")
ax[1,1].set_xlabel("Offset [m]")
ax[1,1].set_ylabel("Two way time [s]")

fig.tight_layout()
plt.show()