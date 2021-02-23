import numpy as np
import math
import matplotlib.pyplot as plt
#plt.switch_backend('Qt4Agg')

# read in and plot
rg = np.loadtxt("langevin/rg.txt", skiprows=2)
rg2 = np.loadtxt("dpd/rg.txt", skiprows=2)

fig, ax = plt.subplots() 

ax.plot(rg[:,0], rg[:,1], "r-", label="Rg, Langevin")
ax.plot(rg2[:,0], rg2[:,1], "b-", label="Rg, DPD")

plt.legend(loc="best", frameon=False)

ax.set_xlabel("time steps")
ax.set_ylabel("Rg")

plt.savefig("rg.png", dpi=200, bbox_inches="tight")

plt.show()
