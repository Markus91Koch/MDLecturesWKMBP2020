import numpy as np
import math
import matplotlib.pyplot as plt
#plt.switch_backend('Qt4Agg')

# read in Rg data
d0 = np.loadtxt("0/rg.txt", skiprows=2)
d1 = np.loadtxt("10/rg.txt", skiprows=2)
d2 = np.loadtxt("20/rg.txt", skiprows=2)
d3 = np.loadtxt("30/rg.txt", skiprows=2)
d6 = np.loadtxt("60/rg.txt", skiprows=2)
d10 = np.loadtxt("100/rg.txt", skiprows=2)

# concentrations
c = [0, 0.1, 0.2, 0.3, 0.6, 1.]

# radius of gyration values
rg = np.array([np.mean(d0[:,1]), np.mean(d1[:,1]), np.mean(d2[:,1]), np.mean(d3[:,1]), np.mean(d6[:,1]), np.mean(d10[:,1])])

# time to plot
fig, ax = plt.subplots()
ax.plot(c, rg/rg[0], color="xkcd:red", linestyle="-", marker="o")

# axis
plt.axis([-.1,1.1, 0., 1.1])

#plt.legend(loc="best", frameon=False)
ax.set_xlabel(r"$c_\mathrm{Co-Solvent}$")
ax.set_ylabel(r"$R_g$ [LJ units]")
plt.savefig("Rg_vs_concentration.png", dpi=300, bbox_inches="tight")
plt.show()
