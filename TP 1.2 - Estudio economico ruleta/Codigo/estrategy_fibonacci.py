import random
import numpy as np 
import math
from matplotlib import pyplot as p
import scipy.stats as ss
from roullete import *

def secuencia_fibonacci(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a  

def estrategia_fibonacci(nro_secuencia, apuesta,capital,favs,nofavs, numero_secuencia0, pleno):
    if(tirar_ruleta(pleno)):
        capital = capital + secuencia_fibonacci(nro_secuencia) * 2
        if(nro_secuencia > numero_secuencia0 + 1):
            nro_secuencia = nro_secuencia - 2
        
        apuesta = secuencia_fibonacci(nro_secuencia)
        favs += 1  
    else:
        nro_secuencia = nro_secuencia + 1
        apuesta = secuencia_fibonacci(nro_secuencia)
        nofavs += 1

    return nro_secuencia, apuesta, capital, favs, nofavs