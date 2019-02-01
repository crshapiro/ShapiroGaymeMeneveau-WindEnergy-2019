import numpy as np
import matplotlib.pyplot as plt
import adm

def plot_sim(Ctp, gg, alpha, corrected, uncorrected, ax1, ax2, marker, markersize):
    ud_c = np.zeros(np.size(Ctp))
    ud_uc = np.zeros(np.size(Ctp))
    for i in range(0, np.size(Ctp)):
        s = '%dm-a%0.2f-Ctp%0.2f'%(gg, alpha, Ctp[i])
        ud_c[i] = corrected[s]
        ud_uc[i] = uncorrected[s]

    ax1.plot(Ctp, Ctp*(ud_uc - (1-ud_uc)*np.pi*Radius**2/576.0**2)**3, marker, MarkerSize=markersize, markerfacecolor='none')
    ax2.plot(Ctp, Ctp*(ud_c - (1-ud_c)*np.pi*Radius**2/576.0**2)**3, marker, MarkerSize=markersize, markerfacecolor='none')

# Parameters
Radius = 50
dx = 3
h = np.sqrt(2*dx**2 + (dx/4)**2) / Radius

# Create figures and axes
fig = plt.figure(figsize=(6.5,2.5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

# Plot the theory
Ctp = np.linspace(0, 4, 50)
ud0 = np.zeros(np.size(Ctp))
ud1 = np.zeros(np.size(Ctp))
ud2 = np.zeros(np.size(Ctp))
ud3 = np.zeros(np.size(Ctp))
ud4 = np.zeros(np.size(Ctp))

for i in range(0, np.size(Ctp)):
    ud0[i] = adm.calc_ud(0.75*h, Ctp[i])
    ud1[i] = adm.calc_ud(1.5*h, Ctp[i])
    ud2[i] = adm.calc_ud(3.0*h, Ctp[i])
    ud3[i] = adm.calc_ud(6.0*h, Ctp[i])
    ud4[i] = adm.calc_ud(12.0*h, Ctp[i])

ax1.plot(Ctp, Ctp*(4.0/(4.0+Ctp))**3,'k:')
ax1.plot(Ctp, Ctp*ud0**3,'c-')
ax1.plot(Ctp, Ctp*ud1**3,'r-')
ax1.plot(Ctp, Ctp*ud2**3,'b-')
ax1.plot(Ctp, Ctp*ud3**3,'g-')
ax1.plot(Ctp, Ctp*ud4**3,'m-')

# Plot axial momentum theory
ax2.plot(Ctp, Ctp*(4.0/(4.0+Ctp))**3,'k:')

# Plot simulations
uncorrected = adm.read_data('../data/uncorrected.dat')
corrected = adm.read_data('../data/corrected.dat')

Ctp = np.array([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2.0])
plot_sim(Ctp+0.05, 12, 0.75, corrected, uncorrected, ax1, ax2, 'bx', 5)
plot_sim(Ctp, 12, 1.50, corrected, uncorrected, ax1, ax2, 'gx', 5)
plot_sim(Ctp-0.05, 12, 3.00, corrected, uncorrected,  ax1, ax2, 'mx', 5)

plot_sim(Ctp+0.05, 6, 0.75, corrected, uncorrected, ax1, ax2, 'r+', 5)
plot_sim(Ctp, 6, 1.50, corrected, uncorrected, ax1, ax2, 'b+', 5)
plot_sim(Ctp-0.05, 6, 3.00, corrected, uncorrected,  ax1, ax2, 'g+', 5)
plot_sim(Ctp-0.10, 6, 6.00, corrected, uncorrected,  ax1, ax2, 'm+', 5)

Ctp = np.array([0.25, 0.75, 1.25, 1.75])
plot_sim(Ctp+0.05, 3, 0.75, corrected, uncorrected, ax1, ax2, 'cD', 4)
plot_sim(Ctp, 3, 1.50, corrected, uncorrected, ax1, ax2, 'rD', 4)
plot_sim(Ctp-0.05, 3, 3.00, corrected, uncorrected,  ax1, ax2, 'bD', 4)
plot_sim(Ctp-0.10, 3, 6.00, corrected, uncorrected,  ax1, ax2, 'gD', 4)

# Set labels, etc. and save
ax1.set_xlabel('$C_T\'$')
ax1.set_ylabel('$C_P$')
ax1.set_xlim([0,3])
ax1.set_ylim([0,1.0])

ax2.set_xlabel('$C_T\'$')
ax2.set_ylabel('$C_P$')
ax2.set_xlim([0,3])
ax2.set_ylim([0,1.0])

ax1.text(-0.25, -0.25, '(a)')
ax2.text(-0.25, -0.25, '(b)')
ax1.annotate('', xy=(1.75,0.9), xytext=(2.1, 0.4), arrowprops=dict(facecolor='black',width=1, headwidth=6, headlength=6))
ax1.text(1,0.3,r'Increasing $\Delta$')
plt.tight_layout()
plt.savefig('fig2.pdf')
