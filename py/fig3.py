import numpy as np
import matplotlib.pyplot as plt
import adm

N = 50
delta = np.linspace(0.01,2,N)
Q = np.zeros(N)

for i in range(0, N):
    r, I = adm.indicator_function(delta[i],1024)
    dr = r[1]-r[0]
    Q[i] = 1-np.pi*np.sum(2*r*np.pi*I**2*dr)

fig = plt.figure(figsize=(4,2.5))
Ctp = 1.0
plt.plot(delta,1/(1+Ctp/4.0*Q),'r.',markersize=4)
plt.plot(delta, 1/(1 + Ctp/4.0*delta/np.sqrt(3*np.pi)),'r-')
Ctp = 1.5
plt.plot(delta,1/(1+Ctp/4.0*Q),'g.',markersize=4)
plt.plot(delta, 1/(1 + Ctp/4.0*delta/np.sqrt(3*np.pi)),'g-')
Ctp = 2
plt.plot(delta,1/(1+Ctp/4.0*Q),'b.',markersize=4)
plt.plot(delta, 1/(1 + Ctp/4.0*delta/np.sqrt(3*np.pi)),'b-')
plt.xlabel('$\Delta/R$')
plt.ylabel(r'$M$')
plt.xlim([0,2])
plt.ylim([0.75,1])
plt.gca().annotate('', xy=(1.0,0.8), xytext=(1.5,0.95), arrowprops=dict(facecolor='black',width=1, headwidth=6, headlength=6))
plt.text(0.425,0.825,r'Increasing $C_T^\prime$')
plt.tight_layout()
plt.savefig('fig3.pdf')
