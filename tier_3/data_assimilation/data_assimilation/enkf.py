"""

     Copyright (c) Marc Bocquet <marc.bocquet@enpc.fr>
     "enkf.py"

     Original version: 03/03/2020-20/10/2020
     Adaptation for the ECMWF MOOC: 08/12/2022-11/12/2022

     Code originally used in the paper:
     M. Bocquet, A. Farchi, and Q. Malartic.
     Online learning of both state and dynamics using ensemble Kalman filters.
     Foundations of Data Science, 3:305-330, 2021
     https://www.aimsciences.org/article/doi/10.3934/fods.2020015

"""

import sys
sys.path.append('../model')

import numpy as np
import random, time
from lorenz96 import l96 
from lorenz96_cubic import l96cb
from enkf_call import call
from observation import checkerboard

# Key folders
dir = dict(output = "../Output")


"""
Define setup
"""

# State space dimension
Nx = 40

# Intégration time step and in between observation batches
dt = 0.05

# Define the model
model = l96(Nx=Nx, dt=dt, F=8)

# Ensemble size
Ne = 30

# Observation error standard deviation
sig_obs = 1.

# Dispersion of initial ensemble
sigx = 1.

# Model error standard deviation for the surrogate model
q = 0.1*dt
sig_q = np.sqrt(q)

# Inflation factor
infl = 1.00

# Observation operator
H = checkerboard(Nx)

# Load truth trajectory and generated observation database and associated dates
with open(dir['output']+'/xt.npy', 'rb') as file:
    xt = np.load(file)
with open(dir['output']+'/yp.npy', 'rb') as file:
    yp = np.load(file)
with open(dir['output']+'/dates.npy', 'rb') as file:
    dates = np.load(file)

# Length of the data assimilation run
Nt = xt.shape[0]

# which includes some burnin
Nts = 0


"""
Data assimilation run  
"""

models = (model, xt, H, yp, dates)
params = (Nx, dt, Nt, Nts, Ne, sig_obs, sigx, sig_q, infl)

print("> run")
rmse_mean, spread_mean, rmsei_mean, zeta_mean, wctime, prtime = call(models, params, dir)

print("> wctime(s)", wctime, " prtime(s)", prtime)
print("> rmse_mean", rmse_mean, "spread_mean", spread_mean, "rmsei_mean", rmsei_mean)
print("> zeta_mean", zeta_mean)
