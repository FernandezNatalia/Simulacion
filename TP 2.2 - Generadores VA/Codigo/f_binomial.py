import numpy as np 
from matplotlib import pyplot as plt
from generator import nro_random
from graph_decoration import *
from math import factorial

def binomial(nb, p):
    # x = 0
    # for i in range(nb):
    #     r = nro_random()      # Genera nro pseudoaleatorio
    #     if r <= p:
    #         x += 1
    # return x

    # Por el metodo de la transf. inversa
    r = nro_random() 
    x = 0
    pr = (1 - p) ** nb
    F = pr
    while r >= F :
        pr *= ((p / (1 - p)) * (nb - x) / (x + 1))
        F  += pr
        x  += 1
    return x

def generate_binomial(n,nb, p):
    corrida = []

    for i in range(n): 
        x = binomial(nb, p)        # Genero nro con dist. Binomial
        corrida.append( x )        # Secuencia de nros con dist. Binomial

    return corrida

def f_den_binomial(x, nb, p):
    f = factorial(nb) / (factorial(x) * factorial(nb - x))
    f = f * (p ** x) * ((1 - p) ** (nb - x))
    return f


def f_acum_binomial(f_den, n):
    f_acum = []
    total = sum(f_den)
    f_acum.append(f_den[0] / total) 
    for i in range(n - 1):
        f_acum.append(f_acum[i] + f_den[i + 1] / total) 
    return f_acum
    
def graph_binomial(corrida, nb, p):
    fig1 = plt.figure("Distribucion Binomial")
    fig1.subplots_adjust(hspace=0.46, top = 0.78, bottom = 0.27, wspace=0.30, left=0.05, right=0.98)

    # =================== Diagrama de barras
    fig1.add_subplot(1,3,1)
    plt.hist(corrida,nb * 2, (0, nb - 1), color = bino_hist, edgecolor = bino_borde_hist,  linewidth=1)
    plt.xlabel('Valor de x')
    plt.ylabel('Frecuencia absoluta')
    poner_fondo_color()
    plt.grid(linestyle = '--')
    
    # =================== Funcion de probabilidad
    corrida.sort()
    f_den = []
    for x in corrida:
        f = f_den_binomial(x, nb, p)        
        f_den.append(f)

    fig1.add_subplot(1,3,2)
    for i in range(len(corrida)):
        plt.vlines(x = corrida[i], ymin=0, ymax= f_den[i], color = unf_puntos, linewidth= 1) #, linestyle = '--')
    
    for i in np.arange(min(corrida), max(corrida)):
        plt.scatter([i],[f_den_binomial(i, nb, p)], 20, color=bino_punto)

    poner_fondo_color()
    plt.grid(linestyle = '--')
    plt.xlabel('Valor de x')
    plt.ylabel('f(x) - funcion de probabilidad')

    # =================== Funcion acumulada
    f_acum = f_acum_binomial(f_den, len(corrida))
 
    fig1.add_subplot(1,3,3)
    for i in range(len(corrida) - 1):
        plt.hlines(y= f_acum[i], xmin= corrida[i], xmax= corrida[i + 1], color = bino_hist)
        if corrida[i] != corrida[i + 1]:
            plt.scatter([corrida[i]],[f_acum[i]], 20, color=bino_borde_hist)
    poner_fondo_color()
    plt.hlines(y= 1, xmin=corrida[0], xmax= int(corrida[-1]), color = bino_punto, linestyle = '--')
    plt.grid(linestyle = '--')
    plt.xlabel('Valor de x')
    plt.ylabel('Frecuencia acumulada')
    plt.show()

def densidad(corrida, nb, p):
    corrida.sort()
    f_den = []
    for x in corrida:
        f = f_den_binomial(x, nb, p)        
        f_den.append(f)
    return f_den