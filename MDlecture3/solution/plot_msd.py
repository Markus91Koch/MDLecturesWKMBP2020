import numpy as np
import math
import matplotlib.pyplot as plt
#plt.switch_backend('Qt4Agg')

# read in MSD and plot
data = np.loadtxt("2d_ideal/msd.txt", skiprows=2)
data2 = np.loadtxt("2d_lj/msd.txt", skiprows=2)
data3 = np.loadtxt("2d_chain/msd.txt", skiprows=2)

fig, ax = plt.subplots() 

ax.plot(data[:,0], data[:,4], "r", label="ideal gas")
ax.plot(data2[:,0], data2[:,4], "b", label="LJ gas")
ax.plot(data3[:,0], data3[:,4], "g", label="chain, N=40")

plt.legend(loc="best", frameon=False)

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("time steps")
ax.set_ylabel("MSD [LJ units]")

plt.savefig("MSD.png", dpi=200, bbox_inches="tight")

plt.show()
