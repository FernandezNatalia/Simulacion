import numpy as np 
from matplotlib import pyplot as plt
from generator import nro_random
from graph_decoration import *
from f_binomial import *

def discreta_empirica(xs, frec_acum):
    r = nro_random() 
    for i in range(len(xs)):
        if(frec_acum[i] > r):
            return xs[i]

def calcula_frec_acum():
    # Elijo una distribucion cualquiera 
    # En este caso utilizamos la dist. Binomial
    nb = 20
    p = 0.4
    func = []
    probs = []
    xs = np.arange(0, nb)
   
    func  = [f_den_binomial(x, nb, p) for x in xs]
    probs = [f  / sum(func) for f in func]

    frec_acum = []
    frec_acum.append(probs[0])
    for i in range(1, len(xs)):
        acumulado = frec_acum[i - 1] + probs[i]
        frec_acum.append(acumulado)

    return xs, frec_acum

def generate_discreta_empirica(n):
    xs, frec_acum = calcula_frec_acum()
    corrida = []
    for i in range(n): 
        x = discreta_empirica(xs, frec_acum)   
        corrida.append( x )      
    return corrida

def graph_discreta_empirica(corrida, n):
    fig1 = plt.figure("Distribucion Discreta Empirica")
    fig1.subplots_adjust(hspace=0.46, top = 0.78, bottom = 0.27, wspace=0.30, left=0.05, right=0.98)

    #====================  Diagrama de barras
    fig1.add_subplot(1,3,1)
    plt.hist(corrida, color = de_hist, bins = int(np.sqrt(len(corrida))), edgecolor = de_borde_hist,  linewidth=1)
    plt.xlabel('Valor de x')
    plt.ylabel('Frecuencia absoluta')
    poner_fondo_color()
    plt.grid(linestyle = '--')

    #====================  Funcion de probabilidad
    corrida.sort()
    f_den = []
    nb, p = 20, 0.4
    for x in corrida:
        # Datos jarcodeados, cambiar cuando se cambie la dist.
        # Para la binomial utilizo esta f_den
        f = f_den_binomial(x, nb, p) 
        f_den.append(f)

    fig1.add_subplot(1,3,2)
    plt.stem(corrida, f_den, use_line_collection = True, basefmt = 'None', linefmt = de_punto)
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
        plt.hlines(y= f_acum[i], xmin= corrida[i], xmax= corrida[i + 1], color = de_hist)
        if corrida[i] != corrida[i + 1]:
            plt.scatter([corrida[i]],[f_acum[i]], 20, color=de_borde_hist)
    poner_fondo_color()
    plt.hlines(y= 1, xmin=corrida[0], xmax= int(corrida[-1]), color = unf_puntos, linestyle = '--')
    plt.grid(linestyle = '--')
    plt.xlabel('Valor de x')
    plt.ylabel('Frecuencia acumulada')
    plt.show()




