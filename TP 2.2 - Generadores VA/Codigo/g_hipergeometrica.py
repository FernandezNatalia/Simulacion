import numpy as np 
from matplotlib import pyplot as plt
from generator import nro_random
from graph_decoration import *
from math import factorial

def hipergeometrica(p, Nt, n):
    #Tamaño N, se toma una muestra de tamaño n
    x = n + 1
    while x > n:
        x = 0
        for i in range(n):
            r = nro_random()
            if r > p:
                s = 0
            else:
                s = 1
                x += 1
            p = (Nt * p - s) / (Nt - 1)
    return x

def generate_hipergeometrica(repetir, p, Nt, n):
    corrida = []
    for i in range(repetir): 
        x = hipergeometrica(p, Nt, n)     # Genero nro con dist. Hipergeometrica
        corrida.append( x )               # Secuencia de nros con dist. Hipergeometrica
    return corrida

def f_den_hipergeometrica(k, Nt, n, r):
    f = factorial(r) / (factorial(k) * factorial(r - k))
    f = f * (factorial(Nt - r) / (factorial(n - k) * factorial(Nt - r - (n - k))))
    f = f / (factorial(Nt) / (factorial(n) * factorial(Nt - n)))
    return f

def graph_hipergeometrica(corrida, p, Nt, n, r):
    fig1 = plt.figure("Distribucion Hipergeometrica")
    fig1.subplots_adjust(hspace=0.46, top = 0.78, bottom = 0.27, wspace=0.30, left=0.05, right=0.98)

    #======================== Diagrama de barras
    fig1.add_subplot(1,3,1)
    plt.hist(corrida, color = hiper_hist, bins = int(np.sqrt(len(corrida))), edgecolor = hiper_borde_hist,  linewidth=1)
    plt.xlabel('Valor de x')
    plt.ylabel('Frecuencia absoluta')
    poner_fondo_color()
    plt.grid(linestyle = '--')
    
    #======================== Funcion de probabilidad
    corrida.sort()
    f_den = []
    for x in corrida:
        f = f_den_hipergeometrica(x, Nt, n, r)
        f_den.append(f)

    fig1.add_subplot(1,3,2)
    plt.stem(corrida, f_den, use_line_collection = True, basefmt = 'None', linefmt = 'c')
    poner_fondo_color()
    plt.grid(linestyle = '--')
    plt.xlabel('Valor de x')
    plt.ylabel('f(x) - funcion de probabilidad')

    #======================== Funcion acumulada
    f_acum = []
    total = sum(f_den)
    f_acum.append(f_den[0] / total) 
    for i in range(len(corrida) - 1):
        f_acum.append(f_acum[i] + f_den[i + 1] / total) 
 
    fig1.add_subplot(1,3,3)
    for i in range(len(corrida) - 1):
        plt.hlines(y= f_acum[i], xmin= corrida[i], xmax= corrida[i + 1], color = 'b')
        if corrida[i] != corrida[i + 1]:
            plt.scatter([corrida[i]],[f_acum[i]], 20, color = 'c')
    poner_fondo_color()
    plt.hlines(y= 1, xmin=corrida[0], xmax= int(corrida[-1]), color = unf_puntos, linestyle = '--')
    plt.grid(linestyle = '--')
    plt.xlabel('Valor de x')
    plt.ylabel('Frecuencia acumulada')
    plt.show()