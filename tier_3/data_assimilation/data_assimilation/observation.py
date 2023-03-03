"""
     Copyright (c) Marc Bocquet <marc.bocquet@enpc.fr>
     "observation.py"
     Original version: 08/12/2022
     For the ECMWF MOOC: 19/12/2022

     Checkerboard and identity observation operator in the (Ot,Ox) space

"""

import numpy as np

class checkerboard():

    """
    Checkerboard observation operator
    """
    
    def __init__ (self, Nx, **kwargs):
        super(checkerboard, self).__init__(**kwargs)
        
        self.Ny = [
            (Nx+1)//2,
            Nx//2
        ]
        self.h = [
            np.array([2*i for i in range(self.Ny[0])]),
            np.array([2*i+1 for i in range(self.Ny[1])])
        ]

    def __call__(self, x, t):
        return x[..., self.h[t%2]]

class identity():

    """
    Identity observation operator
    """
    
    def __init__ (self, Nx, **kwargs):
        super(identity, self).__init__(**kwargs)
        
        self.Ny = [ Nx ]
        self.h = [ np.array([i for i in range(self.Ny[0])]) ]
        
    def __call__(self, x, t):
        return x
