import numpy as np 
import math
from matplotlib import pyplot as plt
from generator import nro_random
from graph_decoration import *
from math import exp, sqrt

def normal(mu, sigma):
    k = 12
    sum_r = 0
    for i in range(k):
        r = nro_random()
        sum_r += r

    x = sigma * ((12 / k ) ** 0.5) *  (sum_r - k / 2) + mu
    return x

def f_dens_normal(x, e, s):
    f = 1 / np.sqrt(2 * math.pi * s)
    f = f * exp((- 0.5) * ((x - e) / s) ** 2)
    return f
def generate_normal(e, s, n):
    corrida = []
    
    for i in range(n):
        x = normal(e, s)   # Genero nro con dist. Normal
        corrida.append(x)  # Secuencia de nros con dist. Normal  
    
    return corrida
def graph_normal(corrida, e, s):
    fig1 = plt.figure("Distribucion normal")
    fig1.subplots_adjust(hspace=0.46, top = 0.78, bottom = 0.27, wspace=0.30, left=0.05, right=0.98)

    # =================== Histograma
    fig1.add_subplot(1,3,1)
    plt.hist(corrida, bins = int(np.sqrt(len(corrida))), color = norm_hist,  edgecolor = norm_borde_hist,  linewidth=1)
    plt.xlabel('Valor de x')
    plt.ylabel('Frecuencia absoluta')

    # =================== Funcion de densidad
    corrida.sort()    
    f_den = []
    for x in corrida:
        f = f_dens_normal(x, e, s)
        f_den.append(f)

    fig1.add_subplot(1,3,2)
    plt.plot(corrida, f_den, color = norm_borde_hist, label = 'f(x) Dist. Normal', linewidth=2.5)
    plt.vlines(x= e, ymin = 0, ymax = f_dens_normal(e, e, s), color = norm_hist, linestyle = '--', label = f'μ = {e}')
    poner_fondo_color()
    plt.xlabel('Valor de x')
    plt.ylabel('f(x) - funcion de densidad')
    plt.legend()
    
    # =================== Funcion acumulada
    f_acum = []
    total = sum(f_den)
    f_acum.append(f_den[0] / total)     # Sumo los valores de f(x) - Es como hacer la integral.
    for i in range(len(corrida) - 1):
        f_acum.append(f_acum[i] + f_den[i + 1] / total) 
 
    fig1.add_subplot(1,3,3)
    plt.plot(corrida, f_acum, color = norm_borde_hist, label = 'F(x) Dist. Normal', linewidth=2.5)
    plt.xlabel('Valor de x')
    plt.ylabel('F(x) - Frecuencia acumulada')
    plt.legend(loc = 'best')
    plt.hlines(y= 1, xmin=corrida[0], xmax= int(corrida[-1]), color = norm_hist , linestyle = '--')
    poner_fondo_color()
    plt.xlim(corrida[0],corrida[-1])
    plt.show()





