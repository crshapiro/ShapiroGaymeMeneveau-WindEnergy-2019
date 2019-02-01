import numpy as np
import numpy.fft as fft
import scipy.optimize as opt
import matplotlib.pyplot as plt
plt.style.use('std-srf')

def indicator_function(delta, N):
    # Create grid
    N = 2*N
    L = 1 + 10*delta/np.sqrt(12)
    dxy = 2*L/N
    xy = np.linspace(-L+dxy/2, L-dxy/2, N)

    # Create mesh and radial direction
    X,Y = np.meshgrid(xy,xy)
    r = np.sqrt(X**2 + Y**2)

    # Unfiltered indicator function (noramlized to integrate to unity)
    H = np.zeros((N,N))
    H[r<1] = 1/np.pi
    H = H/np.sum(H*dxy**2)

    # Gaussian filter (normalized to integrate to unity)
    G = 6/(np.pi*delta**2)*np.exp(-6*r**2/delta**2)

    # Filtered indicator function doing convolution as multiplication in
    # spectral space
    I = fft.irfft2(fft.rfft2(H)*fft.rfft2(G)*dxy**2)

    # This is only really a function or r, so just return as a 1-D array
    # Notice the shift to the corners after doing the FFT
    r = xy[0:N//2]+L
    I = I[0,0:N//2]

    return r, I

def calc_ud(delta, Ctp):
    # Calculate the predicted disk-averaged velocity from filtered vortex
    # cylinder model
    N = 1024
    r, I = indicator_function(delta, N)
    dr = r[1]-r[0]
    Q = 1 + 0.25*Ctp*np.pi*np.sum(2*r*np.pi*I**2*dr)
    ud = 1/Q

    return ud

def read_data(file):
    # Read data from simulations
    d = dict()
    f = open(file,'r')
    for line in f:
        spl = line.split()
        d[spl[0]] = float(spl[1])
    f.close()
    return d
