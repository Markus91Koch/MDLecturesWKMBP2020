import numpy as np
import math
import matplotlib.pyplot as plt
#plt.switch_backend('Qt4Agg')  

# VELOCITY HISTOGRAM
fname1='v_hist.txt'
data1 = np.loadtxt(fname1, skiprows=4)
V = data1[:,1]
P = data1[:,2]

T = 1.5 # value set in simulation

# CALCULATE MAXW.-BOLTZM.-DISTR. IN 2 DIMENSIONS !!!
v = np.linspace(0.05, 9.95, 50);
m = 1.0 # mass
p = m / T * v * np.exp(-1.0 * (m * v**2)/(2 * T))

### PLOTS
csfont = {'size':20}
hfont = {'size':20}

plt.plot(V,P/np.sum(P),lw=2,color='b',label='MD histo.')
plt.plot(v,p/np.sum(p),lw=2,ls='--',color='r',label='MWB, T=%.4f'%T)

plt.rcParams.update({'font.size': 14})
plt.legend(frameon=False)
plt.xlabel('|v|',**csfont)
plt.ylabel('p(|v|)',**hfont)
plt.title('Abs. Velocity Distr.',**csfont)
plt.savefig("v_hist.png", bbox_inches="tight")
plt.show()
