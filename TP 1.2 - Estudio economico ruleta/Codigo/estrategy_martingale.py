import random
import numpy as np 
import math
from matplotlib import pyplot as p
import scipy.stats as ss
from roullete import *

def estrategia_martingala(apuesta,capital,favs,nofavs, apuesta_inicial, pleno):
    if(tirar_ruleta(pleno)):
        capital = capital + apuesta * 2
        apuesta = apuesta_inicial
        favs += 1
    else:
        apuesta = apuesta * 2
        nofavs += 1 
    return apuesta, capital, favs, nofavs


    