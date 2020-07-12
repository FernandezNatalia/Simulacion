import numpy as np 
from matplotlib import pyplot as plt
from generator import nro_random
from graph_decoration import *
from math import exp, factorial

def poisson(lamda):
    x = 0
    b = exp(- lamda)
    producto = 1
    while producto >= b:
        r = nro_random()      # Genera nro pseudoaleatorio
        producto *= r

        if producto >= b:
            x += 1
        else:
            return x

    # ==================== Otro metodo ==================== 
    # r = nro_random()      # Genera nro pseudoaleatorio
    # x = 0
    # p = exp(- lamda)
    # F = p
    
    # while r >= F:
    #     p = (lamda * p) / (x + 1)
    #     F += p
    #     x += 1

    # return x


def generate_poisson(n, lamda):
    corrida = []

    for i in range(n): 
        x = poisson(lamda)        # Genero nro con dist. Poisson
        corrida.append( x )       # Secuencia de nros con dist. Poisson

    return corrida


def f_den_poisson(lamda, x):
    return ((lamda ** x) * exp(- lamda)) / factorial(x)

def graph_poisson(corrida, lamda):
    fig1 = plt.figure("Distribucion Poisson")
    fig1.subplots_adjust(hspace=0.46, top = 0.78, bottom = 0.27, wspace=0.30, left=0.05, right=0.98)

    #====================  Diagrama de barras
    fig1.add_subplot(1,3,1)
    plt.hist(corrida, color = poi_hist, bins = int(np.sqrt(len(corrida))), edgecolor = poi_borde_hist,  linewidth=1)
    plt.xlabel('Valor de x')
    plt.ylabel('Frecuencia absoluta')
    poner_fondo_color()
    plt.grid(linestyle = '--')

    #====================  Funcion de probabilidad
    corrida.sort()
    f_den = []
    for x in corrida:
        f = f_den_poisson(lamda, x)
        f_den.append(f)

    fig1.add_subplot(1,3,2)
    plt.stem(corrida, f_den, use_line_collection = True, basefmt = 'None', linefmt = poi_punto)
    poner_fondo_color()
    plt.grid(linestyle = '--')
    plt.xlabel('Valor de x')
    plt.ylabel('f(x) - funcion de probabilidad')

    #====================  Funcion acumulada
    f_acum = []
    total = sum(f_den)
    f_acum.append(f_den[0] / total) 
    for i in range(len(corrida) - 1):
        f_acum.append(f_acum[i] + f_den[i + 1] / total) 
 
    fig1.add_subplot(1,3,3)
    for i in range(len(corrida) - 1):
        plt.hlines(y= f_acum[i], xmin= corrida[i], xmax= corrida[i + 1], color = poi_hist)
        if corrida[i] != corrida[i + 1]:
            plt.scatter([corrida[i]],[f_acum[i]], 20, color = poi_borde_hist)
    poner_fondo_color()
    plt.hlines(y= 1, xmin=corrida[0], xmax= int(corrida[-1]), color = poi_punto, linestyle = '--')
    plt.grid(linestyle = '--')
    plt.xlabel('Valor de x')
    plt.ylabel('Frecuencia acumulada')
    plt.show()

