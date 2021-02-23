import numpy as np
import math
import matplotlib.pyplot as plt
#plt.switch_backend('Qt4Agg')

# read in and plot
data = np.loadtxt("rho.txt", skiprows=4)
data2 = np.loadtxt("ends.txt", skiprows=4)

fig, ax = plt.subplots() 

ax.plot(data[:,0], data[:,2]/np.sum(data[:,2]), "r", label=r"$\rho(z)$")
ax.plot(data2[:,0], data2[:,2]/np.sum(data2[:,2]), "b", label="P(z)")

plt.legend(loc="best", frameon=False)

ax.set_xlabel("z")
ax.set_ylabel("Probability density")

plt.savefig("brush_profile.png", dpi=200, bbox_inches="tight")

plt.show()
