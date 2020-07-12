import random
import numpy as np 
import math
from matplotlib import pyplot as p
import scipy.stats as ss
from ejecucion_estrategys import *

#def save(nombre):
    #p.savefig(f"{nombre}.jpg", bbox_inches='tight')

def graph_rondas(cant_jugadores, cant_jugadas, flujo_caja_total, capital0, capital_finito):
    #Ejecucion de varias rondas con varias corridas
    p.title(f'Flujo de caja en {cant_jugadores} rondas de {cant_jugadas} tiradas.')
    for i in range(cant_jugadores):
        X = np.arange(0, len(flujo_caja_total[i]))
        p.plot(X, flujo_caja_total[i])
        p.xlabel('Numero de tirada (n)')
        p.ylabel('Flujo de caja')

    if capital_finito:
        p.axhline(y = capital0, color = 'b', label = "Flujo de caja inicial")
        p.legend(loc = 'best')
    
    p.show()
def graph_diagrama_barras(cant_jugadores, frelativa_fav, cant_jugadas, frelativa_nofav):
    fig1 = p.figure("Diagramas de barra")
    fig1.subplots_adjust(hspace=0.46, wspace=0.29, left=0.09, right=0.95)

    #=========================== Grafico de barras exitos
    fig1.add_subplot(2,1,1)
    p.bar(range(cant_jugadores),frelativa_fav, color = "g")
    p.xticks(range(cant_jugadores),range(cant_jugadas))
    p.title("Frecuencia relativa de exitos por ronda")
    p.xlabel('Numero de ronda (N)')
    p.ylabel('Frec relativa de existos')

    #=========================== Grafico de barras fracasos
    fig1.add_subplot(2,1,2)
    p.bar(range(cant_jugadores),frelativa_nofav,color = "r")
    p.xticks(range(cant_jugadores),range(cant_jugadas))
    p.title("Frecuencia relativa de fracasos por ronda")
    p.xlabel('Numero de ronda (N)')
    p.ylabel('Frec relativa de fracasos')
    p.show()

def graph_exitos_vs_fracasos(cant_jugadas,cant_jugadores,frelativa_fav,frelativa_nofav):
    #=========================== Funcion de exitos y fracasos
    p.figure(figsize=(10, 10))
    p.title(f'Frecuencia relativa de éxitos y fracasos por ronda: {cant_jugadas} corridas')
    p.plot(np.arange(0,cant_jugadores),frelativa_nofav, color = 'r', label='Cantidad de fracasos')
    p.plot(np.arange(0,cant_jugadores),frelativa_fav, color = 'g', label='Cantidad de exitos')
    p.xlabel('Numero de ronda (N)')
    p.ylabel('Frec relativa de exitos(v) - fracasos(r)')
    p.axhline(y = 0.5, color = 'b')
    p.legend(loc = 'best')
    p.show()
    
def graph_estrategias_casos_extremos(estrategia):
    #=========================== Comportamiento de las estrategias en casos extremos.
    rango = 6
    bet0 = 100
    loss = []
    win = []

    X_rondas = np.arange(1, rango + 1)
    if estrategia == 'Estrategia Martingala':
        for i in range(1, rango + 1):
            loss.append(bet0 * ((2 ** i) - 1))
            win.append(bet0 * i)

    elif estrategia == 'Estrategia Fibonacci':
        sec_fibo = 11      
        loss_total = 0
        cont_win = 0
        for i in range(sec_fibo,rango + sec_fibo):
            loss_total = loss_total + secuencia_fibonacci(i)
            cont_win += 1

            win.append( secuencia_fibonacci(sec_fibo) * cont_win) 
            loss.append( loss_total)
    else:
        for i in range(1, rango + 1):
            win.append(bet0 * i)
            loss.append(bet0 * i)

    #=========================== Graficos
    p.figure(estrategia)#, figsize=(8, 8))    
    p.title('Casos extremos en n tiradas')
    p.plot(X_rondas, loss, color = 'r', label='Racha mala')
    p.plot(X_rondas, win, color = 'g', label='Racha buena')
    p.xlabel('Numero de tiradas (n)')
    p.ylabel('Catidad apostada acumulada en $')
    p.legend(loc='best')
    p.show()

def graph_martingala_dist_normal(estrategia):
    if estrategia == 'Estrategia Martingala':
        p.figure(figsize=(8, 8))
        n = 10
        p1 = 19/37
        for cant_jugadores in range(10,100,10):
            esperanza = round(1 - (p1*2)**n,2)
            sigma = round(np.sqrt((4 * p1)**n - (2 * p1)**(2*n)),2)

            esperanza = cant_jugadores * esperanza
            sigma = cant_jugadores * sigma

            X_normal = ss.norm(esperanza, sigma)  #-30.56,365.41)
            x_normal = np.arange(X_normal.ppf(0.001),X_normal.ppf(0.999))
            p.title('Distribucion de ganacias Martingala')
            p.plot(x_normal,X_normal.pdf(x_normal))#, label = f'NT = {cant_jugadores}')
          
        p.axvline(esperanza, color = 'y', label='Media')
        p.xlabel('Ganancia')
        p.show() 

def graph_pie(total_favs, total_no_favs):
    veces_ganadas_perdidas = [total_favs, total_no_favs]
    nombres = ["cant. veces con ganancia","cant. veces con perdida"]
    p.pie(veces_ganadas_perdidas, labels=nombres, autopct="%0.1f %%")
    p.title("Porcentaje cant. veces con ganancia VS perdida")
    p.show()
    
def graph_flujo_recuperar_apuesta(cant_jugadas, pleno = 0):
    favs = 0
    nofavs = 0
    recuperando_apuesta = []
    for i in range(1, cant_jugadas + 1):   
        if(tirar_ruleta(pleno)):
            favs += 1        
        else:
            nofavs += 1 
        #=========================== Lista para ver como es el flujo de recuperar el capital
        recuperando_apuesta.append(favs - nofavs)
    
    p.title('Recuperando la apuesta inicial')
    p.axhline(y = 0, color = 'b', label = 'Capital inicial')
    p.plot(np.arange(0,cant_jugadas), recuperando_apuesta,  color = 'm', lw = '2')
    p.xlabel('Numero de tiradas (n)')
    p.ylabel('Variaciones en el flujo de caja')
    p.show()