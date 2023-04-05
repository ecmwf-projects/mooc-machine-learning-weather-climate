"""

     Copyright (c) Marc Bocquet <marc.bocquet@enpc.fr>
     "enkf_call.py"

     Original version: 03/03/2020-20/10/2020
     Adaptation for the ECMWF MOOC: 08/12/2022-20/12/2022

     Code originally used in the paper:
     M. Bocquet, A. Farchi, and Q. Malartic.
     Online learning of both state and dynamics using ensemble Kalman filters.
     Foundations of Data Science, 3:305-330, 2021
     https://www.aimsciences.org/article/doi/10.3934/fods.2020015

"""
import sys
sys.path.append('./data_assimilation')

import numpy as np
import scipy.interpolate
import random, time
import enkf_analysis as analysis

from tqdm.auto import tqdm

def call(models, params):

    model, xt, H, yp, dates = models
    Nx, Dt, Nt, Nts, Ne, sig_obs, sig_x, sig_q, infl = params
    Ny = H.Ny[0]
    
    print("> generate ensemble")
    x_prior = xt[0] + np.random.normal(0, sig_x, Nx)
    E = np.zeros((Ne, Nx))
    for i in range(Ne):
          E[i] = x_prior + np.random.normal(0, sig_x, Nx)

    # Record of the analysis 
    xa = np.empty((Nt,Nx), dtype=np.float32)
    
    # Record of the forecast
    xf = np.empty((Nt,Nx), dtype=np.float32)
    
    # Records for statistics
    spread = np.zeros(Nt)
    spread_mean =  0.
    rmse = np.zeros(Nt)
    rmse_mean = 0.
    rmsei = np.zeros(Nt)
    rmsei_mean = 0.
    zeta = np.zeros(Nt)
    zeta_mean = 0.

    """
    Data assimilation run
    """
    
    print("> data assimilation run")

    # Exception flag
    ef = True
    # Verbose?
    vb = False
    # Inflation relaxation
    ir = False

    # Hyperparameters for the hybrid EnKF-N
    beta = 1.
    nu = 100
    
    tpr_beg = time.process_time()
    twc_beg = time.perf_counter()
    
    with tqdm(total=Nt, desc='running EnKF') as progress:
        for t in range(Nt):

            # Get the obsevration vector at time t
            y = yp[t]

            if ir:
                inflx = 1.+(inflx-1)*0.9999

            if vb:
                print(' - step', t, ' rmse (%3.3f)'%rmse_mean, ' spreadx (%3.3f)'%spread_mean, \
                      ' rmsei (%3.3f)'%rmsei_mean,
                      ' infl (%3.3f)'%infl, 'beta (%3.3f)'%beta, 'nu', nu)

            try:
                xf[t] = E.mean(axis=0)
                analysis.Inflation(E, infl)
                xa[t], zeta[t], beta, nu = analysis.Analysis3(t, E, model, H, y, sig_obs, beta, nu)

            except:
                print('exception_raised')
                ef = False
                break

            if t>=Nts:

                # Compute instant rmse and spread
                rmse[t] = np.sqrt(np.mean((xa[t]-xt[t])**2))
                X = E - xa[t]
                spread[t] = np.linalg.norm(X)/np.sqrt(Ne*Nx)
                rmse_mean += (rmse[t]-rmse_mean)/(t-Nts+1)
                zeta_mean += (zeta[t]-zeta_mean)/(t-Nts+1)
                spread_mean += (spread[t]-spread_mean)/(t-Nts+1)

                # Compute score of the interpolation solution
                _x =  H.h[t%2]
                _x = np.append(_x, _x[0]+Nx)
                _y = np.append(y, y[0])
                f = scipy.interpolate.CubicSpline(_x, _y, bc_type='periodic')
                xi = f(np.array(range(Nx)))
                rmsei[t] = np.sqrt(np.mean((xi-xt[t])**2))
                rmsei_mean += (rmsei[t]-rmsei_mean)/(t-Nts+1)

            E += model(E)
            analysis.sqrt_core(E, sig_q)
            
            progress.set_postfix_str(
                'rmse={rmse:3.3f} spreadx={spreadx:3.3f} rmsei={rmsei:3.3f} infl={infl:3.3f} beta={beta:3.3f} nu={nu:3.3f}'.format(
                    rmse=rmse_mean,
                    spreadx=spread_mean,
                    rmsei=rmsei_mean,
                    infl=infl,
                    beta=beta,
                    nu=nu,
                ),
                refresh=False,
            )
            progress.update()
  

    tpr_end = time.process_time()
    twc_end = time.perf_counter()
 
    wctime = twc_end-twc_beg
    prtime = tpr_end-tpr_beg

    # # Save the analysis trajectory
    # with open(dir['output']/'xa.npy', 'wb') as file:
    #     np.save(file, xa)
    # # Save the forecast
    # with open(dir['output']/'xf.npy','wb') as file:
    #     np.save(file, xf)
        
    if ef:
        return xa, rmse_mean, spread_mean, rmsei_mean, zeta_mean, wctime, prtime
    else:
        nan =  float('inf')
        return xa, nan, nan, nan, wctime, prtime
