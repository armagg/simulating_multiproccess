
# coding: utf-8

# In[ ]:

from concurrent.futures import ProcessPoolExecutor
from .calculator import simulate
import numpy as np


def prepare_first_conditions():
            
    x = np.arange(-9,-6.5,0.5)
    y = np.append(x,np.arange(6.5,9,0.5))
    z = np.arange(20,25,0.5)
    args = []
    for x0 in x:
        for y0 in y:
            for z0 in z:
                for func_n in range(2):
                    args.append((x0,y0,z0,func_n, ))

    return args


if __name__ == "__main__":

    args = prepare_first_conditions()                        
    # values = [(1, 2, ) for i in range(100)]
    results = []
    with ProcessPoolExecutor(max_workers = 4) as executor:
        for arg in args:
            results.append(executor.submit(function, *arg))

        

       

# %%
