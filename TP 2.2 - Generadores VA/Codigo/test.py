import numpy as np 
from matplotlib import pyplot as plt
from scipy.stats import chi2
from scipy.stats import norm
import math
from tabulate import tabulate

def test_chi_cuadrado(muestra_obs, muestra_esp):
    intervals = int(max(muestra_obs)) 
    len_interval = 1 #int(len(muestra_obs) / intervals)

    if min(muestra_obs) < 0:
        intervals = int(intervals * 1.9)
    #====================  Muestra observada
    cont = 1
    frec_obs = []
    k = 0
    for i in range(intervals):
        for m in muestra_obs:     
            if (k <= m) and (m < (k + len_interval)):
                cont += 1
        k += len_interval
        frec_obs.append(cont)
        cont = 1

    #====================  Muestra real
    cont = 1
    frec_esp = []
    k = 0
    for i in range(intervals):
        for m in muestra_esp:     
            if (k <= m) and (m < (k + len_interval)):
                cont += 1
        k += len_interval
        frec_esp.append(cont)
        cont = 1

    chi = 0
    for i in range(len(frec_obs)):
        chi += ((frec_obs[i] - frec_esp[i]) ** 2) / frec_esp[i]

    gl = intervals - 1
    ic = 0.95
    table = chi2.ppf(ic, gl)

    if(chi < table):
        #print('No hay evidencia estadística que permita rechazar la hipótesis nula H0:')
        param = f'[Val.Chi({round(chi, 2)}) < Val.table({round(table, 2)})]'
        paso = 'PASO'
    else:
        #print('Se rechaza la hipótesis nula H0:')
        param = f'[Val.Chi({round(chi, 2)}) > Val.table({round(table, 2)})]'
        paso = 'NO PASO'
    
    return param, paso
    
def realizar_test(corrida, esperada, selec):
    param, paso = test_chi_cuadrado(corrida, esperada)
    graph_table(param, paso, selec)

def graph_table(parame, pasos, nombre):
    test_arr_abaj = [['Distribucion'],
                    [''], 
                    [nombre]]

    test_arr_abaj[0].append('CHICUADRADO')
    test_arr_abaj[0].append('PASO EL TEST')
    test_arr_abaj[1].append('Valor: chicuadrado - Tabla')


    test_arr_abaj[2].append(parame)
    test_arr_abaj[2].append(pasos)

    print(tabulate(test_arr_abaj, headers='firstrow', tablefmt='fancy_grid', stralign='center', floatfmt='.0f'))
    print()

# def test_Kolmogorov_Smirnov(muestra):
#     #muestra = list(muestra0)
#     muestra.sort()
#     size = len(muestra)

#     #alfa = 1.358
#     #Dmaxi = round(alfa / (math.sqrt(size) + 0.12 + (0.11 / math.sqrt(size))),4)

#     Dmaxi  = round(0.895 / (math.sqrt(size) - 0.01 + 0.85 / math.sqrt(size)), 4)

#     #Calculo la frecuencia acumulada observada
#     frec_acum = []
#     divisor = sum(muestra)
#     frec_acum.append(muestra[0] / divisor)

#     for i in range(1, size):
#         frec_acum.append(frec_acum[i - 1] + muestra[i]/divisor)

#     D_mas = []
#     D_menos = []

#     for i in range(size):
#         D_mas.append(((i + 1) / size) - frec_acum[i])
#         D_menos.append(frec_acum[i] - (i / size))

#     D = round(max(max(D_mas), max(D_menos)),4)

#     if(D <= Dmaxi):
#         #Se acepta la hipotesis H0
#         return f'{D} <= {Dmaxi}', 'PASO' 
#     else:
#         #Se rechaza la hipotesis H0
#         return f'{D} > {Dmaxi}', 'NO PASO'
