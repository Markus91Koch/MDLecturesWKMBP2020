import numpy as np
import math
import matplotlib.pyplot as plt
#plt.switch_backend('Qt4Agg')

# read in and plot
data = np.loadtxt("brush_full_dens.txt", skiprows=4)
data1 = np.loadtxt("brush_dens.txt", skiprows=4)
data2 = np.loadtxt("end_dens.txt", skiprows=4)

A_wall = (2 * 7.875 * 2 * 9.09325)  # area of the grafting wall = Lx * Ly
binsize = data1[1,1] - data1[0,1]     # size of bins along z
N_samples = 10000. # number of measurements taken

norm = N_samples * binsize * A_wall # normalization constant for brush profile

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex = True) 

#ax1.plot(data[:,1], data[:,2]/norm, "r", label=r"$\rho(z)$")
ax1.plot(data1[:,1], data1[:,2]/norm, "xkcd:light green", label=r"$\rho(z)$")
ax2.plot(data2[:,1], data2[:,2]/np.sum(data2[:,2]), "b", label="P(z)")

ax1.set_ylabel(r"Brush profile")
ax2.set_ylabel("End monomer distribution")
ax2.set_xlabel("z")


plt.savefig("brush_profile.png", dpi=200, bbox_inches="tight")

plt.show()
