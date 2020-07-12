import numpy as np 
from math import log, exp
from matplotlib import pyplot as plt
from generator import nro_random
from graph_decoration import *

def exponencial(alfa):
    r = nro_random()             # Genera nro pseudoaleatorio
    x = ti_exponencial(alfa, r)
    return x

def ti_exponencial(alfa, r):
    e = 1 / alfa                 # Esperanza
    x = - e * log( r )           # Transformada inversa
    return x

def generate_exponencial(alfa, n):
    corrida = []

    for i in range(n): 
        x = exponencial(alfa)   # Genero nro con dist. Exponencial
        corrida.append( x )     # Secuencia de nros con dist. Exponencial  

    return corrida

def graph_exponencial(corrida, alfa):
    fig1 = plt.figure("Distribucion exponencial")
    fig1.subplots_adjust(hspace=0.46, top = 0.78, bottom = 0.27, wspace=0.30, left=0.05, right=0.98)

    # =================== Histograma ===================
    fig1.add_subplot(1,3,1)
    plt.hist(corrida, color = exp_hist, bins = int(np.sqrt(len(corrida))), edgecolor = exp_borde_hist,  linewidth=1)
    plt.xlabel('Valor de x')
    plt.ylabel('Frecuencia absoluta')
    poner_fondo_color()

    # =================== Funcion de densidad
    corrida.sort()
    f_den = []
    for x in corrida:
        f = alfa * exp(- alfa * x)  # Funcion densidad exponencial
        f_den.append(f)

    fig1.add_subplot(1,3,2)
    plt.plot(corrida, f_den, color = exp_curva, label = 'f(x) Dist. Exponencial', linewidth=2.5)
    poner_fondo_color()
    plt.xlabel('Valor de x')
    plt.ylabel('f(x) - funcion de densidad')
    plt.legend()

    # =================== Frecuencia acumulada
    f_acum = []
    for x in corrida:
        r = 1 - exp( - alfa * x )  # F(x)
        f_acum.append(r)

    fig1.add_subplot(1,3,3)
    plt.plot(corrida, f_acum, color = exp_curva, label = 'F(x) Dist. Exponencial', linewidth=2.5)
    plt.hlines(y= 1, xmin=-0.3, xmax= int(corrida[-1]), color = exp_puntos, linestyle = '--')
    plt.xlabel('Valor de x')
    plt.ylabel('F(x) - Frecuencia acumulada')
    plt.legend(loc = 'best')
    poner_fondo_color()
    plt.show()



