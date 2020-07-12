import numpy as np 
from matplotlib import pyplot as plt
from scipy.stats import chi2
from scipy.stats import norm
import math

def test_chi_cuadrado(repeat, muestra):
    # ======================= Divido el los intervalos en sqrt(n)
    intervals = int(np.sqrt(repeat))
    len_interval = 1 / intervals

    # ======================= Calculo la frecuencia relativa
    frec_acum = []
    frec_obs = list(np.zeros(intervals))

    # ======================= Calculo frecuencia acumulada esperada: absoluta por intervalo
    for i in range(0,intervals):
        frec_acum.append(len_interval * (i + 1))

    #Test chicuadrado
    for i in muestra:
        for j in range(intervals):
            if(i < frec_acum[j]):
                frec_obs[j] += 1
                break

    # ======================= Frec observada acumulada
    acum, frec_obs_acum = 0, []
    for i in frec_obs:
        acum = i + acum
        frec_obs_acum.append(acum)

    frec_esp = int(repeat / intervals)
    chi = 0
    for oi in frec_obs:
        chi += ((oi - frec_esp) ** 2) / frec_esp

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
    
    return frec_acum, frec_obs, frec_obs_acum, param, paso

def test_arriba_abajo(muestra):
    media = np.mean(muestra)
    landa = 0.05

    z_tabla = round(norm.ppf(landa/2),2)
    z_menor = z_tabla
    z_mayor = -z_tabla
    
    ns = []
    c0 = 1
    size = len(muestra)

    for m in range(size):
        if(muestra[m] > media):
            ns.append(0)
        elif (muestra[m] < media):
            ns.append(1)
    
        if((m != 0) and (ns[m] != ns[m - 1])):
            c0 += 1

    n0 = ns.count(1)
    n1 = ns.count(0)
    n = n0 + n1

    valor_esperado = 0.5 + (2 * n0 * n1) / n
    desviacion = np.sqrt((2 * n0 * n1 * (2 * n0 * n1 - n)) / ((n - 1) * (n ** 2)))
    z0 = (c0 - valor_esperado) / desviacion
    
    if(z0 > z_menor and z0 < z_mayor ):
        #print(f'No se puede rechazar la hipotesis {z_menor}< {round(z0,2)} < {z_mayor}')
        return f'Zmin({z_menor}) < Z0({round(z0,2)}) < Zmax({z_mayor})', 'PASO'
    elif (z0 < z_menor):
        return f'Zmin({z_menor}) < Z0({round(z0,2)})', 'NO PASO'
    else: 
        return f'Z0({round(z0,2)}) > Zmax({z_mayor})', 'NO PASO'
def test_Kolmogorov_Smirnov(muestra):
    #muestra = list(muestra0)
    muestra.sort()
    size = len(muestra)

    Dmaxi = round(1.358 / (math.sqrt(size) + 0.12 + (0.11 / math.sqrt(size))),4)

    # ======================= Calculo la frecuencia acumulada observada
    frec_acum = []
    # divisor = sum(muestra)
    frec_acum.append(muestra[0]) #/ divisor)

    for i in range(1, size):
        frec_acum.append(muestra[i])#frec_acum[i - 1] + muestra[i]/divisor)

    D_mas = []
    D_menos = []

    for i in range(size):
        D_mas.append(((i + 1) / size) - frec_acum[i])
        D_menos.append(frec_acum[i] - (i / size))

    D = round(max(max(D_mas), max(D_menos)),4)

    if(D <= Dmaxi):
        # ======================= Se acepta la hipotesis H0
        return f'{D} <= {Dmaxi}', 'PASO' 
    else:
        # ======================= Se rechaza la hipotesis H0
        return f'{D} > {Dmaxi}', 'NO PASO'

def test_media(muestra, repeat):

    media = round(np.mean(muestra),4)

    landa = 0.05
    z_tabla = round(norm.ppf(landa/2),2)
    limite_superior = round(0.5 + abs(z_tabla) * (1 / np.sqrt(12 * repeat)),4)
    limite_inferior = round(0.5 - abs(z_tabla) * (1 / np.sqrt(12 * repeat)),4)

    if media < limite_superior and media > limite_inferior :
        return 'PASO', f'li({limite_inferior}) <= {media} <= ls({limite_superior})'
    elif media > limite_superior:
        return 'NO PASO', f'{media} > ls({limite_superior})'
    else: 
        return 'NO PASO', f'li({limite_inferior}) > {media})'