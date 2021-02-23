import numpy as np
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random
plt.switch_backend('Qt4Agg')
import os
#from scipy import stats

f_list = []
z_list = []

dir_list = list()
for root, dirs, files in os.walk(".", topdown=False):
    for name in dirs:
        if os.path.isfile(name+"/force.txt"):
            dir_list.append(os.path.join(root, name))


for z in dir_list:
    fname=z+'/force_ave.txt'
    data1 = np.genfromtxt(fname, skip_header=2, skip_footer=0)
    f = data1[3]
    f_list.append(np.mean(f))
    z_list.append(float(z[2:]))


zz = np.array(z_list)
ff = np.array(f_list)
inds = zz.argsort()
zsort = zz[inds]
fsort = ff[inds]

FE=np.trapz(fsort[5:], zsort[5:])
print("FE: ", FE)

fname1='../brush_profiles/brush_dens.txt'
data1 = np.loadtxt(fname1, skiprows=4)
z1 = data1[:,1]
g1 = data1[:,2]

fname2='../brush_profiles/end_dens.txt'
data2 = np.loadtxt(fname2, skiprows=4)
z2 = data2[:,1]
g2 = data2[:,2]


binsz = z1[1]-z1[0]
surface = (2*7.87500*2*9.09325)
N_obs = 10000
h = 40.0

norm = N_obs*surface*binsz
avg_z=0
norm_z=0

#for i in range(len(z1)):
#    avg_z += g1[i]*i*binsz
#    norm_z += g1[i]
#
#
#print "h: ", 8.0/3.0*avg_z/norm_z

x1=[0, 25]


fig, ax1 = plt.subplots()
t = np.arange(0.01, 10.0, 0.01)
ax1.plot(z1,g1/norm,lw=4.1,color='b',label='rho(z), brush')
ax1.plot(z2,g2/norm*10.0,lw=4.1,color='g',label='rho(z) x 10.0, ends')
ax1.legend(frameon=False, loc="upper left")
ax1.set_xlabel(r'$z$')
ax1.set_ylim((0,max(g1/norm)*1.25))
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel(r'$\rho(z)$', color='b')
ax1.tick_params('y', colors='b')
ax2 = ax1.twinx()
ax2.scatter(z_list, f_list, label='vertical force', lw=2.6, color="red")
ax2.plot(zsort[0:], fsort[0:], lw=1.2,linestyle="--", color="red")
ax2.set_ylabel(r'$f_z$', color='r')
ax2.set_ylim((0,max(f_list)*1.25))
ax2.tick_params('y', colors='r')
ax2.legend(frameon=False, loc="upper right")
ax1.set_xlim((0,25))
plt.rcParams.update({'font.size': 14})
fig.tight_layout()
plt.savefig("brush_force.png", dpi=200)
plt.show()

