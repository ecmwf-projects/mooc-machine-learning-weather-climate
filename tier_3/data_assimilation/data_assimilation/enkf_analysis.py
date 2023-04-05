"""

     Copyright (c) Marc Bocquet <marc.bocquet@enpc.fr>
     "enfk_analysis.py"
     Original version: 03/03/2020-22/07/2020
     Adaptation for the ECMWF MOOC: 08/12/2022-11/12/2022

     The key analysis routines.

     Code originally used in the paper:
     M. Bocquet, A. Farchi, and Q. Malartic.
     Online learning of both state and dynamics using ensemble Kalman filters.
     Foundations of Data Science, 3:305-330, 2021
     https://www.aimsciences.org/article/doi/10.3934/fods.2020015

     The hybrid adaptive inflation algorithm has been introduced in:
     P. N. Raanes, M. Bocquet, and A. Carrassi
     Adaptive covariance inflation in the ensemble Kalman filter by Gaussian scale mixtures.
     Q. J. R. Meteorol. Soc., 145:53-75, 2019.
     https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3386


"""

import numpy as np
from numpy import zeros, ones, dot, identity, sqrt, newaxis, diag, eye, sqrt
import random
import scipy.optimize
import sys

"""
Analysis 3
Hybrid scheme
See Raanes et al. QJRMS, 2019
"""

eps = 1.e-8

def J(zeta, delta, s, Ne, e, K, beta):
    sum = e*zeta+(Ne+1.)*np.log(Ne/zeta)-Ne
    for m in range(K):
        sum += pow(delta[m],2)/(1.+beta*pow(s[m],2)/zeta)
    return sum

def Analysis3(t, E, model, H, y, sig_obs, beta, nu):

    """
    Hybrid EnKF-N
    """

    # Get model dimension
    Nx = model.Nx
    Ny = y.shape[0]

    # Determine size of the ensemble
    Ne = E.shape[0] 

    # Parameter of the finite-size formalism
    e = 1.+1./Ne
    
    # Compute the mean of the ensemble
    xm = E.sum(axis=0)/Ne

    # Compute the innovation, normalised by the error
    delta = (y - H(xm, t))/sig_obs

    # Compute the state anomalies
    X = E - xm

    # Compute the observation anomalies normalised by the error
    Y = H(X, t)/sig_obs    

    # Compute the estimate in ensemble space
    
    # SVD of the normalised observation anomalies
    U, s, V = np.linalg.svd(Y, full_matrices=False)

    # Update beta parameter
    betar = (np.dot(delta,delta)-Ny)*(Ne-1)/np.dot(s,s)
    beta = (nu*beta+betar)/(nu+1)
    beta_star = (nu+1)/(nu-1)*beta
    nu += 1
    

    # Compute the normalised innovation vector in the mode space
    delta = dot(V,delta)

    # Compute the optimal zeta
    K = min(Ne, Ny)
    zeta = scipy.optimize.fminbound(J, eps, Ne-1, (delta, s, Ne, e, K, beta_star), 1e-8)

    # Update of the state vector in ensemble space
    _s = s/(s*s+zeta)
    S = diag(_s)
    wa = dot(U,dot(S,delta))
    xa = xm + dot(wa,X)

    # Compute the posterior ensemble
    T = dot(Y,Y.T)+zeta*(np.identity(Ne)-2*zeta/(Ne+1.)*dot(wa[newaxis].T,wa[newaxis]))
    # T = dot(Y,Y.T)+zeta*np.identity(N)
    U, s, V = np.linalg.svd(T, full_matrices=False)
    T = dot(U,dot(diag(sqrt((Ne-1.)/s)),U.T))
    Xa = dot(T,X)
    E[:] = Xa + xa

    return xa, zeta, beta, nu


"""
Inflation of the ensemble
"""
    
def Inflation(E, infl):

    # Determine size of the ensemble
    Ne = E.shape[0]

    # Compute the mean
    xm = E.sum(axis=0)/Ne

    # Rescale
    E[:Ne] = xm + infl*(E - xm)
    

"""
SQRT-CORE
"""

# Sqrt-Core
def sqrt_core(E, sig_q):
    # Determine size of the ensemble
    Ne = E.shape[0]
    # Compute the mean
    xm = E.sum(axis=0)/Ne
    # Anomalies
    X = E-xm
    # SVD of the anomalies
    U, s, V = np.linalg.svd(X, full_matrices=False)
    U = U[:,:Ne-1]
    V = V[:Ne-1]
    s = s[:Ne-1]
    T = scipy.linalg.sqrtm(np.diag(s*s)+(Ne-1)*sig_q*sig_q*V@V.T)
    E[:] = xm + np.dot(U, np.dot(T, V))
