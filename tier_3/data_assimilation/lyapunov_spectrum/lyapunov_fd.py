"""

     Copyright (c) Marc Bocquet <marc.bocquet@enpc.fr>
     "lyapunov_fd.py"
     Original version: 30/10/2019
     Adaptation for the ECMWF MOOC: 20/12/2022

     Computation of Lyapunov spectrum using finite differences

"""

import sys
sys.path.append('../Model')

import time
import numpy as np
import scipy.linalg
from math import fabs, log
from lorenz96_cubic import l96cb
from lorenz96 import l96 

Nx = 40
dt = 0.05

F = 8.5
diffusion = 0.025
friction = 1.01
model = l96cb(Nx, dt, F, diffusion, friction)

# F = 8.
# model = l96(Nx, dt, F)


# Number of tangent perturbations
Np = 40

# Generating the initial state
x = 3 + np.random.randn(Nx)
print("> model spinup")
Niter = 1000
for niter in range(Niter):
    x += model(x)

# Generating the initial anomaly matrix
mu = 0.
sigma = 1
X = np.random.normal(mu, sigma, (Np, Nx))



tpr_beg = time.process_time()
twc_beg = time.perf_counter()

print("> tangent perturbations spinup")
eps = 1e-4
Niter = int(2e4)
for niter in range(Niter):
    E = x + eps*X
    x += model(x)
    E += model(E)
    X = (E-x)/eps
    X, R = np.linalg.qr(X.T, mode='complete')
    X = X.T


print("> main run")
L = np.zeros([Np])
Niter = int(1e6)
eps = 1e-4
for niter in range(Niter):
    E = x + eps*X
    x += model(x)
    E += model(E)
    X = (E-x)/eps
    X, R = np.linalg.qr(X.T, mode='reduced')
    X = X.T
    for p in range(Np):
        L[p] = (niter*L[p] + log(fabs(R[p,p])))/(niter+1)
    print(niter,"/", Niter,  L/dt)


tpr_end = time.process_time()
twc_end = time.perf_counter()

wctime = twc_end-twc_beg
prtime = tpr_end-tpr_beg
print("> wctime(s)", wctime, " prtime(s)", prtime)


lyapunov_file = open('Post/lyapunov_'+model.tag+'.dat', 'w')
lyapunov_file.write('tag '+model.tag+' Niter '+str(Niter)+'\n')
for p in range(Np):
    lyapunov_file.write(str(p+1)+' '+str(L[p]/dt)+'\n')
lyapunov_file.close()

