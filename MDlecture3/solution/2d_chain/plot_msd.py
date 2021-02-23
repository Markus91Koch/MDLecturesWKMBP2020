import numpy as np
import math
import matplotlib.pyplot as plt
#plt.switch_backend('Qt4Agg')

# read in MSD and plot
data = np.loadtxt("msd.txt", skiprows=2)
fig, ax = plt.subplots() 
ax.plot(data[:,0], data[:,4], "r")

# compare to power law
x = np.arange(100, 500, step=100)
ax.plot(x, 0.00007* x**2, "b--")
ax.text(100, 50, r"$\sim t^2$", color="b", fontsize=24)

xx = np.arange(1000, 25000, step=100)
ax.plot(xx, 0.5*xx**(0.5), "g--")
ax.text(1000, 100, r"$\sim t^{1/2}$", color="g", fontsize=24)

xxx = np.arange(140000, 1200000, step=1000)
ax.plot(xxx, 0.002*xxx, "c--")
ax.text(70000, 800, r"$\sim t$", color="c", fontsize=24)

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("time steps")
ax.set_ylabel("MSD [LJ units]")

plt.savefig("MSD.png", dpi=200, bbox_inches="tight")

# simple moving average
def sma(array, period):
    ret = np.cumsum(array, dtype=float)
    ret[period:] = ret[period:] - ret[:-period]
    return ret[period - 1:] / period

# calulate and plot D(t)
delta_step = data[1,0] - data[0,0]
timestep = 0.005
dim = 2
D = 1 / (2*dim) * np.diff(data[:,4])/(delta_step*timestep)

fig2, ax2 = plt.subplots()
ax2.plot(data[1:,0], D, "r")
ax2.plot(sma(data[1:,0],1000), sma(D, 1000), "b")
ax2.set_xlabel("time")
ax2.set_ylabel("D(t)")

plt.savefig("D.png", dpi=200, bbox_inches="tight")

plt.show()
