import numpy as np
import math
import matplotlib.pyplot as plt
#plt.switch_backend('Qt4Agg')

# read in and plot
data = np.loadtxt("langevin/z.txt", skiprows=2)
data2 = np.loadtxt("dpd/z.txt", skiprows=2)

fig, ax = plt.subplots() 

ax.plot(data[:,0], data[:,1], "r", label="z, Langevin")
ax.plot(data2[:,0], data2[:,1], "b", label="z, DPD")

plt.legend(loc="best", frameon=False)

ax.set_xlabel("time steps")
ax.set_ylabel("z")

plt.savefig("z.png", dpi=200, bbox_inches="tight")

plt.show()
