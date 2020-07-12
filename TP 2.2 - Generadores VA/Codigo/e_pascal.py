import numpy as np 
from math import log, exp, factorial
from matplotlib import pyplot as plt
from generator import nro_random
from graph_decoration import *

def pascal(k, p):       
    x = 0
    producto = 1
    for i in range(k):
        r = nro_random()                # Genera nro pseudoaleatorio
        producto *= r
    x = log(producto) / log(1 - p)      # T.Inv indirecta
    return int(x)                       # Redondeo al entero mas proximo

def generate_pascal(k, p, n):
    corrida = []
    for i in range(n): 
        x = pascal(k, p)        # Genero nro con dist. de Pascal
        corrida.append( x )     # Secuencia de nros con dist. de Pascal
    return corrida

def get_func_acumulada(f_den, corrida):
    # Funcion acumulada
    f_acum = []
    total = sum(f_den)
    f_acum.append(f_den[0] / total)     # Sumo los valores de f(x) - Es como hacer la integral.
    for i in range(len(corrida) - 1):
        f_acum.append(f_acum[i] + f_den[i + 1] / total) 

    return f_acum

def graph_pascal(corrida, k, p):
    fig1 = plt.figure("Distribucion de Pascal")
    fig1.subplots_adjust(hspace=0.46, top = 0.78, bottom = 0.27, wspace=0.30, left=0.05, right=0.98)

    # Diagrama de barras
    fig1.add_subplot(1,3,1)
    plt.hist(corrida,max(corrida) * 2, (0, max(corrida) - 1), color = pascal_hist, edgecolor = pascal_borde_hist,  linewidth=1)
    plt.xlabel('Valor de x')
    plt.ylabel('Frecuencia absoluta')
    poner_fondo_color()
    plt.grid(linestyle = '--')

    # Funcion de probabilidad
    f_den = []
    for x in corrida:
        f = factorial(k + x - 1) / (factorial(x) * factorial(k - 1))
        f = f * (p ** k) * ((1 - p) ** x)         # Funcion probabilidad pascal
        f_den.append(f)

    fig1.add_subplot(1,3,2)
    plt.stem(corrida, f_den, use_line_collection = True, basefmt= 'None', linefmt= pascal_hist)
    plt.xlabel('Valor de x')
    plt.ylabel('f(x) - funcion de densidad')
    poner_fondo_color()
    plt.grid(linestyle = '--')

    # Funcion acumulada
    corrida.sort()
    f_acum = get_func_acumulada(f_den, corrida)
 
    fig1.add_subplot(1,3,3)
    for i in range(len(corrida) - 1):
        plt.hlines(y= f_acum[i], xmin= corrida[i], xmax= corrida[i + 1], color = pascal_hist)
        if corrida[i] != corrida[i + 1]:
            plt.scatter([corrida[i]],[f_acum[i]], 20, color=unf_puntos)
    poner_fondo_color()
    plt.hlines(y= 1, xmin=corrida[0], xmax= int(corrida[-1]), color = exp_puntos, linestyle = '--')
    plt.grid(linestyle = '--')
    plt.xlabel('Valor de x')
    plt.ylabel('Frecuencia acumulada')
    plt.show()