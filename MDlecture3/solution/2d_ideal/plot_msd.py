import numpy as np
import math
import matplotlib.pyplot as plt
#plt.switch_backend('Qt4Agg')

# read in MSD and plot
data = np.loadtxt("msd.txt", skiprows=2)
fig, ax = plt.subplots() 
ax.plot(data[:,0], data[:,4], "r")

# compare to power law
x = np.arange(1000, 10000, step=100)
ax.plot(x, 0.0002* x**2, "b--")
ax.text(1000, 4000, r"$\sim t^2$", color="b", fontsize=24)

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("time steps")
ax.set_ylabel("MSD [LJ units]")

plt.savefig("MSD.png", dpi=200, bbox_inches="tight")

# calulate and plot D(t)

delta_step = data[1,0] - data[0,0]
timestep = 0.005
dim = 2
D = 1 / (2*dim) * np.diff(data[:,4])/(delta_step*timestep)

fig2, ax2 = plt.subplots()
ax2.plot(data[1:,0], D, "r")
ax2.set_xscale('log')
ax2.set_xlabel("time")
ax2.set_ylabel("D(t)")

plt.savefig("D.png", dpi=200, bbox_inches="tight")

plt.show()
