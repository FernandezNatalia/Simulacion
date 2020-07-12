import numpy as np
from math import log, exp, factorial
from matplotlib import pyplot as plt
from generator import nro_random
from graph_decoration import *
from b_exponencial import *

# alfa e N ==> Erlang
# sino     ==> Gamma

def gamma(alfa, k):

    #alfa = int(esp / varz)
    #k = int((esp ** 2) / varz)
   
    producto = 1
    for i in range(k):
        r = nro_random()                # Genera nro pseudoaleatorio
        producto *= r
    # x = - (1 / alfa) * log(producto)  
    x = ti_exponencial(alfa, producto)  # Numero de Erlang con exponencial
    return x 

def generate_gamma(alfa, k, n):
    corrida = []
    for i in range(n):
        x = gamma(alfa, k)     # Genero nro con dist. Gamma
        corrida.append(x)      # Secuencia de nros con dist. Gamma    
    return corrida 

def f_dens_gamma(x, alfa, k):
    f = (alfa ** k) * (x ** (k - 1)) * exp(- alfa * x)
    f = f / factorial((k - 1))
    return f
    
def graph_gamma(corrida, alfa, k):
    fig1 = plt.figure("Distribucion gamma")
    fig1.subplots_adjust(hspace=0.46, top = 0.78, bottom = 0.27, wspace=0.30, left=0.05, right=0.98)

    # =================== Histograma
    fig1.add_subplot(1,3,1)
    plt.hist(corrida, color = gamma_hist, bins = int(np.sqrt(len(corrida))), edgecolor = norm_borde_hist,  linewidth=1)
    plt.xlabel('Valor de x')
    plt.ylabel('Frecuencia absoluta')
    poner_fondo_color()   

    # =================== Funcion de densidad
    f_den = []
    corrida.sort()
    for x in corrida:
        f = f_dens_gamma(x, alfa, k)
        f_den.append(f)

    fig1.add_subplot(1,3,2)
    plt.plot(corrida, f_den, color = gamma_hist, label = f'k = {k}, α = {alfa}', linewidth=2.5)
    poner_fondo_color()
    plt.xlabel('Valor de x')
    plt.ylabel('f(x) - funcion de densidad')
    plt.legend()

    # =================== Funcion acumulada
    f_acum = []
    total = sum(f_den)
    f_acum.append(f_den[0] / total)  # Sumo los valores de f(x) - Es como hacer la integral.
    for i in range(len(corrida) - 1):
        f_acum.append(f_acum[i] + f_den[i + 1] / total) 
 
    fig1.add_subplot(1,3,3)
    plt.plot(corrida, f_acum, color = gamma_hist, label = 'F(x) Dist. Gamma', linewidth=2.5)
    plt.xlabel('Valor de x')
    plt.ylabel('F(x) - Frecuencia acumulada')
    plt.legend(loc = 'best')
    plt.hlines(y= 1, xmin=- 0.3, xmax= int(corrida[-1]), color = exp_puntos, linestyle = '--')
    poner_fondo_color()
    plt.show()
def graph_n_gamma(alfas, ks, ns):
    # =================== Tiradas proporcionales al alfa
    n = []
    for i in alfas:
        n.append(int(i * ns))

    # =================== Genero varias corridas
    corridas =  []
    size = len(ks)
    for i in range(size):
        corrida = generate_gamma(alfas[i], ks[i], n[i])      
        corrida.sort()
        corridas.append(corrida)

    # =================== Funcion de densidad
    fs_den = []
    for i in range(size):
        f_den = []        
        for x in corridas[i]:
            f = f_dens_gamma(x, alfas[i], ks[i])
            f_den.append(f)

        fs_den.append(f_den)

    plt.title('Funcion de densidad Dist. Gamma')
    for i in range(len(corridas) - 1, -1, -1):
        if len(ks) == 5:
            colores = ['#9c5c5f', '#649481', '#5590a3', '#866791', '#8f8f69']
            plt.plot(corridas[i], fs_den[i], color = colores[i], label = f'k = {ks[i]}, α = {alfas[i]}')
            plt.legend()
        else:
            plt.plot(corridas[i], fs_den[i])       
    plt.xlim(0, 14)
    poner_fondo_color()
    plt.grid(linestyle = '--')
    plt.xlabel('Valor de x')
    plt.ylabel('f(x) - funcion de densidad')
    plt.show()




