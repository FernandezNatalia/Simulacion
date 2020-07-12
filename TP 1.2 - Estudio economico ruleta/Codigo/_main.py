from estrategy_fibonacci import *
import numpy as np
import math
import PyInquirer as inquirer
from os import system

system("cls")
opciones = [
    {
        'type': 'list',
        'name': 'color_apostado',
        'message': "¿A qué color apostás?",
        'choices': ['Rojo', 'Negro']
    }
]

opciones_estrategia = [
    {
        'type': 'list',
        'name': 'tipo_estrategia',
        'message': "¿Qué tipo de estrategia elegís?",
        'choices': ['Estrategia Martingala', 'Estrategia Fibonacci', 'Jugar sin estrategia']
    },
]

opciones_tipo_apuesta = [
    {
        'type': 'list',
        'name': 'tipo_apuesta',
        'message': "¿Qué tipo de apuesta haces?",
        'choices': ['Por color', 'Por paridad', 'Por numero']
    },
]
opciones_paridad = [
    {
        'type': 'list',
        'name': 'tipo_par',
        'message': "¿Apostás a número par o impar?",
        'choices': ['Par', 'Impar']
    },
]

opciones_infinito = [
    {
        'type': 'list',
        'name': 'tipo_capital',
        'message': "¿Apostás con capital finito o infinito?",
        'choices': ['Finito', 'Infinito']
    },
]

opciones_restriccion = [
    {
        'type': 'list',
        'name': 'tipo_restriccion',
        'message': "¿Desea tener una restriccion maxima de mesa?",
        'choices': ['Si', 'No']
    },
]

opciones_vista = [
    {
        'type': 'list',
        'name': 'tipo_vista',
        'message': "¿Que desea hacer?",
        'choices': ['Analisis del comportamiento de las estrategias', '¡Jugar a la ruleta!']
    },
]

while True:
    tipo_apuesta      = ''
    pleno             = 0
    bet               = 0
    numero_secuencia0 = 0

    print(chr(27)+"[1;33m") 
    print('---------------------------------------------')
    print('    ¡Bienvenido al juego de la ruleta!')
    print('---------------------------------------------')
    print(chr(27)+"[;37m")
    print('              MENU PRINCIPAL ')
    print('---------------------------------------------')

    respuesta       = inquirer.prompt(opciones_vista)
    tipo_vista      = respuesta['tipo_vista']    
    system("cls")
    respuesta       = inquirer.prompt(opciones_estrategia)
    tipo_estrategia = respuesta['tipo_estrategia']   
    estrategia      = tipo_estrategia
    system("cls")
    almost_infinity = 9999999999

    if tipo_vista == '¡Jugar a la ruleta!': 

        respuesta    = inquirer.prompt(opciones_tipo_apuesta)
        tipo_apuesta = respuesta['tipo_apuesta']

        if tipo_apuesta == 'Por color': 
            respuesta      = inquirer.prompt(opciones)
            color_apostado = respuesta['color_apostado']
                
        if tipo_apuesta == 'Por paridad': 
            respuesta = inquirer.prompt(opciones_paridad)
            tipo_par  = respuesta['tipo_par'] 
        
        if tipo_apuesta == 'Por numero': 
            pleno = int(input('Ingrese a que número va a apostar       : '))          

        respuesta        = inquirer.prompt(opciones_restriccion)
        tipo_restriccion = respuesta['tipo_restriccion']  

        if tipo_restriccion == 'Si':
            restriccion = True
        else:
            restriccion = False

        respuesta_infinito = inquirer.prompt(opciones_infinito)
        tipo_capital       = respuesta_infinito['tipo_capital']

        if tipo_capital == 'Finito':
            capital0       = int(input('Ingrese cual es su capital inicial      : '))
            capital_finito = True
        else:
            capital0       = almost_infinity
            capital_finito = False
        
        if tipo_estrategia == 'Estrategia Fibonacci':
            print('Numeros de Fibonacci:     [1 – 2 – 3 – 5 – 8 – 13 – 21 – 34 – 55 – 89 – 144 – 233 – 377 – 610 - ...]')
            print('Posicion de la secuencia: [1 – 2 – 3 – 4 – 5 – 6 –  7 –  8 –  9 –  10 – 11 –  12 –  13 –  14 - ...]')
            numero_secuencia0 = int(input('Ingrese la "posicion de la secuencia" para su apuesta: '))
            bet = secuencia_fibonacci(numero_secuencia0)      
        else:                               
            bet = int(input('Ingrese el valor de la apuesta inicial  : '))
                            
        cant_jugadores = int(input('Ingrese la cantidad de rondas           : '))
        cant_jugadas =   int(input('Ingrese la cantidad de tiradas por ronda: '))


        flujo_caja_total, fr_fav, fr_no_fav, total_win, total_loss = ejecutar_estrategia(estrategia, 
                                                                                        capital0, 
                                                                                        cant_jugadores, 
                                                                                        cant_jugadas, 
                                                                                        numero_secuencia0,
                                                                                        bet,
                                                                                        restriccion,
                                                                                        pleno,
                                                                                        capital_finito)

        #=========================== Graficos
        graph_rondas(cant_jugadores, cant_jugadas, flujo_caja_total, capital0, capital_finito)
        graph_diagrama_barras(cant_jugadores, fr_fav, cant_jugadas, fr_no_fav)
        graph_exitos_vs_fracasos(cant_jugadas,cant_jugadores,fr_fav,fr_no_fav)
        graph_pie(total_win, total_loss)

    else: 
        if estrategia != 'Jugar sin estrategia':
            #=========================== Comportamiento de las estrategias
            graph_estrategias_casos_extremos(estrategia)

        if estrategia == 'Estrategia Martingala':
            graph_martingala_dist_normal(estrategia)
        
        if estrategia == 'Jugar sin estrategia':
            #=========================== Prob. cercana al 50 porciento
            graph_flujo_recuperar_apuesta(2000)
            #=========================== Pleno
            graph_flujo_recuperar_apuesta(2000, 6)

    system("cls")

