import random
import numpy as np 
import math
from matplotlib import pyplot as p
import scipy.stats as ss

def tirar_ruleta(pleno = 0):
    m = np.random.randint(0,37)

    if pleno != 0:
        return m == pleno
    else:      
        return m in valores_rojo
    
valores_rojo = [1,3,5,7,9,12,14,16,18,21,23,25,27,28,30,32,34,36]