import random
import numpy as np 
import math
from estrategy_fibonacci import *
from estrategy_martingale import *
from roullete import *

def ejecutar_estrategia(estrategia, capital0, cant_jugadores, cant_jugadas, numero_secuencia0, apuesta_inicial, restriccion, pleno = 0, capital_finito = True):   
    if restriccion:
        max_apuestas_casino = 1280
    else:
        max_apuestas_casino = math.inf
        
    casino_capital = 0
    frelativa_fav = []
    frelativa_nofav = []
    prom_ganancia = []
    prom_capital = []
    flujo_caja_total = []
    total_favs = 0
    total_no_favs = 0

    for j in range(cant_jugadores):
        corridas_por_ronda = []
        flujo_ronda = []
        nofavs = 0
        favs = 0
        nro_secuencia = numero_secuencia0
        apuesta = apuesta_inicial
        capital = capital0

        for i in range(cant_jugadas):
            if capital >= apuesta and apuesta <= max_apuestas_casino:
                capital = capital - apuesta
            
            elif capital - apuesta_inicial > 0:
            #=================== No me alcanza el capital para seguir apostando y apuesto el dinero que me sobra. 
            #=================== Razones:
            #=================== 1. Restriccion de maximo de mesa
            #=================== 2. No tengo capital para doblar la apuesta

                apuesta = apuesta_inicial
                nro_secuencia = numero_secuencia0

                capital = capital - apuesta

                if not capital_finito:
                    total_no_favs += 1
            else: 
            #=================== No queda mas dinero para apostar.
                capital = 0  
                flujo_ronda.extend(np.zeros((cant_jugadas-i,), dtype=int))
                total_no_favs += 1
                break

            #=================== Ejecucion de las estrategias
            if estrategia == 'Estrategia Martingala':
                apuesta, capital, favs, nofavs = estrategia_martingala(apuesta,capital, favs, nofavs, apuesta_inicial, pleno)
            
            elif estrategia == 'Estrategia Fibonacci':
                nro_secuencia, apuesta, capital, favs, nofavs = estrategia_fibonacci(nro_secuencia, apuesta,capital,favs,nofavs, numero_secuencia0, pleno)
            
            else:
                if(tirar_ruleta(pleno)):
                    capital = capital + apuesta_inicial * 2
                    favs += 1
                else:
                    nofavs += 1 

            #=================== Contando el flujo de caja por ronda
            flujo_ronda.append(capital)

        if capital != 0 :
            total_favs += 1
        
        casino_capital = casino_capital + (capital0 - capital)
        prom_ganancia.append(capital - capital0)
        prom_capital.append(capital)

        #=================== Contando la frecuencia relativa de cada ronda
        frelativa_fav.append(favs/cant_jugadas)
        frelativa_nofav.append(nofavs/cant_jugadas)

        #=================== Contando el flujo de caja total
        flujo_caja_total.append(flujo_ronda)
        corridas_por_ronda.append(np.arange(0,len(flujo_ronda)))

    print(f'Capital del casino: {casino_capital}')
    print(f'Promedio de ganancia total: {np.mean(prom_ganancia)}')
    print(f'Capital final: {np.mean(prom_capital)}')

    return flujo_caja_total, frelativa_fav, frelativa_nofav, total_favs, total_no_favs



