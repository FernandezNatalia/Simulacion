import numpy as np 
import math
from matplotlib import pyplot as plt
from generator import nro_random
from graph_decoration import *

def uniform(a, b):
    r = nro_random()     # Genera nro pseudoaleatorio
    x = a + (b - a) * r  # Transformada inversa
    return x

def generate_uniform(a, b, n):
    corrida = []
    for i in range(n):
        x = uniform(a,b)   # Genero nro con dist. Uniforme
        corrida.append(x)  # Secuencia de nros con dist. Uniforme   
    return corrida

def graph_uniform(corrida, a, b):
    fig1 = plt.figure("Distribucion Uniforme")
    fig1.subplots_adjust(hspace=0.46, top = 0.78, bottom = 0.27, wspace=0.30, left=0.05, right=0.98)

    #=================== Histograma ===================
    fig1.add_subplot(1,3,1)
    plt.title('Histograma')
    plt.hist(corrida, color = unf_hist, bins = b, edgecolor = unf_borde_hist,  linewidth=1)
    plt.xlabel('Valor de x')
    plt.ylabel('Frecuencia absoluta')
    poner_fondo_color()   
    #plt.show()

    # =================== Funcion de densidad =========
    f = 1 / (b - a)
    fig1.add_subplot(1,3,2)
    plt.title('Funcion de densidad')
    plt.plot(corrida, [f] * len(corrida), color = unf_borde_hist, label = 'Dist. Uniforme', linewidth=2.5)
    
    plt.vlines(x= a, ymin=0, ymax= f, color = unf_puntos, linestyle = '--')
    plt.vlines(x= b, ymin=0, ymax= f, color = unf_puntos, linestyle = '--')

    plt.grid(linestyle = '--')
    plt.xlabel('Valor de x')
    plt.ylabel('f(x) - funcion de densidad')
    plt.legend()
    poner_fondo_color()
    #plt.show()

    # =================== Frecuencia acumulada ========
    f_acum = []
    corrida.sort()
    for x in corrida:
        r = (x - a) / (b - a)  # F(x)
        f_acum.append(r)

    # ===== Tomo valores cualesquiera de ejemplo =====
    r0 = f_acum [ int(len(corrida) / 2) ]
    x0 = corrida[ int(len(corrida) / 2) ]

    fig1.add_subplot(1,3,3)
    plt.title('Frecuencia acumulada')
    plt.plot(corrida, f_acum, color = unf_borde_hist, label = 'F(x) Dist. Uniforme', linewidth=2.5)
    plt.hlines(y= r0, xmin=0, xmax= x0, color = unf_puntos, linestyle = '--')
    plt.vlines(x= x0, ymin=0, ymax= r0, color = unf_puntos, linestyle = '--')

    plt.yticks([0, 0.2, 0.4, r0, 0.6, 0.8, 1],[0, 0.2, 0.4, r'$r_{0}$', 0.6, 0.8, 1])
    plt.xticks([a, a + (b / 5), a + 2 * (b / 5), x0,  a + 3 * (b / 5), a + 4 * (b / 5), b] ,
              [a, a + (b / 5), a + 2 * (b / 5), r'$x_{0}$', a + 3 * (b / 5), a + 4 * (b / 5), b] )

    plt.grid(linestyle = '--')
    plt.xlabel('Valor de x')
    plt.ylabel('F(x) - Frecuencia acumulada')
    plt.legend()
    poner_fondo_color()
    plt.show()
    