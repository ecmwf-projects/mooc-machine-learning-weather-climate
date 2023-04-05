"""

     Copyright (c) Marc Bocquet <marc.bocquet@enpc.fr>
     "lyaspec.py"
     Original version: 10/12/2022
     Adaptation for the ECMWF MOOC: 11/12/2022

     Load and reformat Lyapunov spectrum

"""

import numpy as np

path = './lyapunov_spectrum/Post/'
def load(file_name):
    with open(path+file_name, encoding='utf8') as file:
        spectrum = file.readlines()
        spectrum = np.array([ spectrum[i].strip().split() for i in range(1,len(spectrum)) ]).T.astype(np.float32)
    return spectrum[0], spectrum[1]
