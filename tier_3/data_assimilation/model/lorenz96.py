"""

     Copyright (c) Marc Bocquet <marc.bocquet@enpc.fr>
     "lorenz96k.py"
     Original version: 21/11/2014-22/10/2019
     Adaptation for the ECMWF MOOC: 09/12/2022

"""


import numpy as np

# The model generating class
class l96():

    def __init__ (self, Nx, dt, F, **kwargs):
        super(l96, self).__init__(**kwargs)
        
        self.Nx = Nx
        self.F = F
        self.dt = dt
        self.tag = 'l96'

    
    def f(self, x):
        
        # Rolled tensors
        xp1 = np.roll(x, shift=1, axis=-1)
        xp2 = np.roll(xp1, shift=1, axis=-1)
        xm1 = np.roll(x, shift=-1, axis=-1)

        # Compute the bilinear terms
        p0 = xm1*xp1
        p1 = xp1*xp2

        # L96 increment
        dx = self.dt*(p0-p1-x+self.F)

        return dx

    # Fourth-order Runge-Kutta
    def __call__(self, q):
        
        k1 = self.f(q)
        k2 = self.f(q+k1/2)
        k3 = self.f(q+k2/2)
        k4 = self.f(q+k3)
        dq = k1/6+k2/3+k3/3+k4/6

        return dq
