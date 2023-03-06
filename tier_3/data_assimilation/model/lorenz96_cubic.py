"""

     Copyright (c) Marc Bocquet <marc.bocquet@enpc.fr>
     "lorenz96_cubic.py"
     Original version: 09/12/2022
     Adaptation for the ECMWF MOOC: 10/12/2022

     A novel Lorenz 96 model with a cubic correction.
     Integrated with an Runge Kutta 4th-order scheme.

"""

import numpy as np

# The model generating class
class l96cb():

    def __init__ (self, Nx, dt, F, diffusion, friction, **kwargs):
        super(l96cb, self).__init__(**kwargs)
        
        self.Nx = Nx
        self.F = F
        self.dt = dt
        self.diffusion = diffusion
        self.friction = friction
        self.tag = 'l96cb'
    
    def f(self, x):

        # Rolled tensors
        xp1 = np.roll(x, shift=1, axis=-1)
        xp2 = np.roll(xp1, shift=1, axis=-1)
        xp3 = np.roll(xp2, shift=1, axis=-1)
        xm1 = np.roll(x, shift=-1, axis=-1)
        xm2 = np.roll(xm1, shift=-1, axis=-1)
        
        # Compute the bilinear terms
        p0 = xp1*(xm1-xp2)
        p1 = self.diffusion*(xp2*x*(xm1-xp3)-xp1*xm1*(xm2-xp2))

        # L96 tendencies
        dx = self.dt*(p0+p1-self.friction*x+self.F)
        
        return dx

    # Fourth-order Runge-Kutta
    def __call__(self, q):
        
        k1 = self.f(q)
        k2 = self.f(q+k1/2)
        k3 = self.f(q+k2/2)
        k4 = self.f(q+k3)
        dq = k1/6+k2/3+k3/3+k4/6

        return dq


