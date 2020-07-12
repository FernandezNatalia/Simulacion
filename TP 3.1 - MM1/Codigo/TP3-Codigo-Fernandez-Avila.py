import numpy as np
from math import log
import random
from operator import itemgetter
from matplotlib import pyplot as plt
import PyInquirer as inquirer
from os import system

def random_arribo():
    t_arribo = random.uniform(0,1)
    return - (1 / lamda_arribo) * log(t_arribo)

def random_partida():
    t_partida = random.uniform(0,1)
    return - (1 / lamda_partida) * log(t_partida)

def random_prioridad():
    paramet_poisson = 0.5
    return np.random.poisson(paramet_poisson)

def Inicializar():
    global Time
    global tProxArribo 
    global tProxPartida  
    global ProxEventoEsArribo
    global AreaQ    
    global AreaB    
    global AreaS  
    global NroClientesEnCola 
    global TimeUltimoEvento 
    global ServidorOcupado  
    global ListaArribos
    global ClientesDemorados 
    global NroCliCompDemora  
    global DemoraTotal  
    global NroClientesEnCola 
    global infinito     
    global NroClientesEnSistema
    global NroClientesDenegados
    global DemoraSistema

    Time                 = 0
    tProxArribo          = 0
    tProxPartida         = 0
    ProxEventoEsArribo   = True
    AreaQ                = 0
    AreaB                = 0
    AreaS                = 0
    NroClientesEnCola    = 0
    TimeUltimoEvento     = 0
    ServidorOcupado      = False
    ListaArribos         = []
    ClientesDemorados    = 0
    NroCliCompDemora     = 0
    DemoraTotal          = 0
    NroClientesEnCola    = 0
    infinito             = 999999999999999999999999
    NroClientesEnSistema = 0
    NroClientesDenegados = 0
    DemoraSistema        = 0
    tProxPartida         = infinito
    tProxArribo          = round(Time + random_arribo(), 4)
    
def DeterminarEvento():
    global Time
    global ProxEventoEsArribo

    if tProxArribo <= tProxPartida:
        Time = tProxArribo
        ProxEventoEsArribo = True
    else:
        Time = tProxPartida
        ProxEventoEsArribo = False

def ActualizarEstadisticos():
    global AreaQ
    global AreaB
    global AreaS
    global TimeUltimoEvento

    TDesdeUltimoEvento = round(Time - TimeUltimoEvento, 4)
    TimeUltimoEvento   = Time

    AreaQ += NroClientesEnCola    * TDesdeUltimoEvento
    AreaB += ServidorOcupado      * TDesdeUltimoEvento
    AreaS += NroClientesEnSistema * TDesdeUltimoEvento

    AreaQ = round(AreaQ,4)
    AreaB = round(AreaB,4)
    AreaS = round(AreaS,4)

def Arribo():
    global ListaArribos
    global NroCliCompDemora
    global ServidorOcupado
    global NroClientesEnCola
    global tProxPartida
    global tProxArribo
    global NroClientesEnSistema
    global DemoraSistema

    NroClientesEnSistema += 1
    tProxArribo = round(Time + random_arribo(),4)

    if ServidorOcupado:
        NroClientesEnCola += 1
        # Simulacion con prioridad
        if Prioridad: 
            prioridad = random_prioridad()
            ListaArribos.append([Time,prioridad])

            # Ordeno por prioridad y luego por tiempo
            ListaArribos = sorted(ListaArribos, key=itemgetter(0))
            ListaArribos = sorted(ListaArribos, key=itemgetter(1), reverse = True)  
        else:
            ListaArribos.append(Time)
        
    else:
        # Servidor desocupado, no hizo fila
        NroCliCompDemora  += 1
        ServidorOcupado    = True

        # Genera su propio evento partida
        tProxPartida       = round(Time + random_partida(),4)
        # 0 porque no hizo cola + el tiempo en atenderlo
        DemoraSistema       += (0 + (tProxPartida - Time))
    
def Partida():
    global DemoraTotal
    global NroCliCompDemora 
    global NroClientesEnCola
    global NroClientesEnSistema
    global tProxPartida
    global ListaArribos
    global ServidorOcupado
    global DemoraSistema

    NroClientesEnSistema -= 1

    if NroClientesEnCola == 0:
        # Cola vacia
        ServidorOcupado = False
        tProxPartida    = infinito
    else:
        # Paso un cliente al servidor, fila - 1
        NroClientesEnCola -= 1
        if Prioridad:
            Demora             = Time - ListaArribos[0][0]
        else:
            Demora             = Time - ListaArribos[0]

        NroCliCompDemora    += 1
        tProxPartida         = round(Time + random_partida(),4)

        DemoraTotal         += round(Demora, 4)
        DemoraSistema       += (round(Demora, 4) + (tProxPartida - Time))
        
        ListaArribos.pop(0)

def DenegarServicio():
    global NroClientesDenegados
    global tProxArribo

    tProxArribo = round(Time + random_arribo(),4)
    NroClientesDenegados += 1

def input_medida_graficar():    
    opciones = [
        {
            'type': 'list',
            'name': 'medida_seleccionada',
            'message': "Seleccione una medida de rendimiento",
            'choices': ['Promedio de clientes en cola', 
                        'Numero de clientes en cola real', 
                        'Promedio de clientes en el sistema', 
                        'Promedio de tiempo en cola', 
                        'Promedio de tiempo en el sistema', 
                        'Utilizacion del servidor', 
                        'Probabilidad de n clientes en cola', 
                        'Denegacion de servicio'
                        ]
        }
    ]

    system("cls")
    print(chr(27)+"[1;33m") 
    print('---------------------------------------------')
    print('            ¿QUE DESEA GRAFICAR?             ')
    print('---------------------------------------------')
    print(chr(27)+"[;37m")
    respuesta = inquirer.prompt(opciones)
    selec = respuesta['medida_seleccionada']
    system("cls")
    
    return selec

def input_parametros():
    global lamda_arribo
    global lamda_partida
    global LimiteDenegacion
    global max_simulaciones
    global max_iteracion
    global Prioridad

    system("cls")
    # Parametros de entrada -----------
    print(chr(27)+"[1;33m") 
    print('    *  Ingrese los parametros de entrada.  *   ')
    print()
    print(chr(27)+"[;37m")
    lamda_arribo     = float(input('Lamda de arribo      : '))     
    lamda_partida    = float(input('Lamda de servicio    : '))
    LimiteDenegacion = int(input('Limite de denegacion : '))
    max_simulaciones = int(input('Cant. Simulaciones   : '))
    max_iteracion    = int(input('Cant. Iteraciones    : '))

    opciones = [
        {
            'type': 'list',
            'name': 'prioridad',
            'message': "¿Desea una disciplina de cola con prioridad?",
            'choices': ['Si', 'No']
        }
    ]

    respuesta = inquirer.prompt(opciones)
    selec = respuesta['prioridad']
    if selec == 'Si':
        Prioridad = True
    else:
        Prioridad = False

    system("cls")

    # # Parametros de entrada Default -----------
    # lamda_arribo     = 0.5 # 1.428571429
    # lamda_partida    = 1   # 1.5151515151
    # Prioridad        = False
    # LimiteDenegacion = 50
    # # ---------------------------------
    # max_simulaciones = 10
    # max_iteracion    = 20000
    # ---------------------------------
    # Se puede evaluar la cantidad de clientes que fueron denegados.
    # Tambien se puede evaluar la probabilidad
    # ---------------------------------


infinito             = 999999999999999999999999

# =====================================
# El programa tambien funciona para cuando existe una cola con prioridad.
# =====================================

input_parametros()
while True:
    opcion = input_medida_graficar()

    list_t_prom_en_cola         = []
    list_prom_nro_cli_cola      = []
    list_utilizac_servidor      = []
    list_tiempos                = []
    list_nro_cli_cola           = []
    list_t_prom_en_sistema      = []
    list_prom_nro_cli_sist      = []
    list_nro_cli_cola           = []
    list_nro_cli_denegados      = []
    list_prom_nro_cli_denegados = []
    barras_prom_nro_cli_cola    = []
    barras_prom_cli_denegados   = []

    #============================= VARIAS SIMULACIONES
    for j in range(max_simulaciones):
        prom_nro_cli_cola      = []
        t_prom_en_cola         = []
        utilizac_servidor      = []
        tiempos                = []
        nro_cli_cola           = []
        t_prom_en_sistema      = []
        prom_nro_cli_sist      = []
        nro_cli_denegados      = []
        prom_nro_cli_denegados = []

        #========================  UNA SIMULACION
        Inicializar()
        for i in range(1, max_iteracion):
            DeterminarEvento()
            ActualizarEstadisticos()

            if ProxEventoEsArribo:
                if (ServidorOcupado + NroClientesEnCola) < LimiteDenegacion:
                    Arribo()
                else:
                    DenegarServicio()
            else:
                Partida()   

            nro_cli_cola      .append(NroClientesEnCola)
            tiempos           .append(Time)
            t_prom_en_cola    .append(round(DemoraTotal   / NroCliCompDemora,4))
            prom_nro_cli_cola .append(round(AreaQ         / Time, 4))
            utilizac_servidor .append(round(AreaB         / Time, 4))
            t_prom_en_sistema .append(round(DemoraSistema / NroCliCompDemora, 4))
            prom_nro_cli_sist .append(round(AreaS         / Time, 4))
            nro_cli_denegados .append(NroClientesDenegados)

            prom_nro_cli_denegados.append(NroClientesDenegados / (NroCliCompDemora + NroClientesDenegados))
            

        if j == 0:
            print('------------ Medidas de desempeño ------')
            print(f'd(n)  = SUM(Di) / n           = {round(DemoraTotal  / NroCliCompDemora,4)}')           # Tiempo promedio en cola
            print(f'q(n)  = integral(Q(t)) / T(n) = {round(AreaQ        / Time, 4)}')                      # Nro promedio de clientes en cola
            print(f'mu(n) = integral(B(t)  / T(n) = {round(AreaB        / Time, 4)}')                      # Utilizacion del servidor
            print()
            print(f'Demora en el sistema          = {round(DemoraSistema/ NroCliCompDemora,4)}') # Tiempo promedio en el sistema
            print(f'Nro clientes en el sistema    = {round(AreaS        / Time, 4)}')
            print()
            print(f'Prom nro clientes denegados   = {NroClientesDenegados / (NroCliCompDemora + NroClientesDenegados)}')
            print(f'Nro clientes denegados        = {NroClientesDenegados}')
            print(f'Nro clientes fueron atendidos = {NroCliCompDemora}')
            cli_denegados = NroClientesDenegados / (NroCliCompDemora + NroClientesDenegados)


        # Listas de medidas de desempeño
        list_prom_nro_cli_cola.append(prom_nro_cli_cola)
        list_t_prom_en_cola   .append(t_prom_en_cola)
        list_utilizac_servidor.append(utilizac_servidor)
        list_tiempos          .append(tiempos)
        list_t_prom_en_sistema.append(t_prom_en_sistema)
        list_prom_nro_cli_sist.append(prom_nro_cli_sist)
        list_nro_cli_cola     .append(nro_cli_cola)

        list_nro_cli_denegados.append(nro_cli_denegados)
        list_prom_nro_cli_denegados.append(prom_nro_cli_denegados)

        #========================  Listas para el diagrama de barras
        barras_nro_cli_cola = []
        barras_cli_denegados = []

        for i in range(9):#max(nro_cli_cola)):
            barras_nro_cli_cola.append(nro_cli_cola.count(i) / len(nro_cli_cola))
        barras_prom_nro_cli_cola.append(barras_nro_cli_cola)

    #========================  Promedio de las medidas de desempeño
    prom_list_prom_nro_cli_cola   = []
    prom_list_t_prom_en_cola      = []
    prom_list_utilizac_servidor   = []
    prom_list_t_prom_en_sistema   = []
    prom_list_prom_nro_cli_sist   = []
    prom_barras_prom_nro_cli_cola = []
    prom_barras_prom_cli_denegados = []

    for i in range(max_iteracion - 1) :
        prom_list_prom_nro_cli_cola  .append(np.mean([x[i] for x in list_prom_nro_cli_cola]))
        prom_list_t_prom_en_cola     .append(np.mean([x[i] for x in list_t_prom_en_cola   ]))
        prom_list_utilizac_servidor  .append(np.mean([x[i] for x in list_utilizac_servidor]))
        prom_list_t_prom_en_sistema  .append(np.mean([x[i] for x in list_t_prom_en_sistema]))
        prom_list_prom_nro_cli_sist  .append(np.mean([x[i] for x in list_prom_nro_cli_sist]))

    for i in range(9) :
        prom_barras_prom_nro_cli_cola.append(np.mean([x[i] for x in barras_prom_nro_cli_cola]))

    def poner_fondo_color():
        ax = plt.gca()
        ax.set_facecolor('#f5f5f5')


    #====================================================================================================
    # TODAS LAS GRAFICAS ================================================================================
    #====================================================================================================

    #=======================GRAFICOS PROMEDIO CLIENTES EN COLA ============================
    if opcion == 'Promedio de clientes en cola':
        valor_calculadora = 0.5
        for i in range(max_simulaciones):
            plt.plot(list_tiempos[i], list_prom_nro_cli_cola[i], c = '#c6a664', alpha = 0.8)

        # plt.axhline(y = valor_calculadora, color = '#1766e2', label = "Valor calculadora online", linewidth=3)
        #plt.plot([0, 10000], [0, 10000], color = '#1766e2', label = "Valor calculadora online", linewidth=3)
        plt.plot(list_tiempos[i], prom_list_prom_nro_cli_cola, label = 'Promedio del promedio', c = '#b32428', linewidth=3)
        #plt.xlim(0,10000)
        plt.title ('Promedio de clientes en cola q(n)')
        plt.xlabel('Tiempo')
        plt.ylabel('Promedio de clientes en cola q(n)')
        plt.legend()
        poner_fondo_color()
        plt.show()

    #=============================== Clientes en cola reales. SCATTER ====================================
    if opcion == 'Numero de clientes en cola real':

        for i in range(max_simulaciones):
            plt.scatter(list_tiempos[i], list_nro_cli_cola[i], s = 5, alpha=0.3, c='#c03997')

        plt.title('Numero de clientes en cola N(t)')
        plt.xlabel('Tiempo (t)')
        plt.ylabel('Numero de clientes en cola N(t)')
        plt.legend()
        poner_fondo_color()
        plt.show()

        #=============================== Clientes en cola reales. LINEAS =====================================

        for i in range(max_simulaciones):
            plt.plot(list_tiempos[i], list_nro_cli_cola[i], c='#49b07d')
        #plt.plot(list_tiempos[i], prom_list_prom_nro_cli_cola, label = 'Promedio del promedio', c = 'k')
        plt.title('Numero de clientes en cola N(t)')
        plt.xlabel('Tiempo (t)')
        plt.ylabel('Numero de clientes en cola N(t)')
        plt.show()

    #=============================== PROM CLIENTES EN EL SISTEMA ==========================================
    if opcion == 'Promedio de clientes en el sistema':

        plt.hist(list_nro_cli_cola[0], color = '#ffd900', bins = 15, edgecolor = '#ffd900',  linewidth=1)
        plt.xlabel('Numero de clientes en el sistema')
        plt.ylabel('Frecuencia absoluta de Ns(t)')
        poner_fondo_color()
        plt.grid(linestyle = '--')
        plt.show()

        for i in range(max_simulaciones):
            plt.plot(list_tiempos[i], list_prom_nro_cli_sist[i], c = '#c6d8a5')
        plt.plot(list_tiempos[i], prom_list_prom_nro_cli_sist, label = 'Promedio del promedio', c = '#0071bc')
        plt.title('Promedio de clientes en el sistema')
        plt.xlabel('Tiempo (t)')
        plt.ylabel('Numero de clientes en cola Ns(t)')
        plt.legend()
        poner_fondo_color()
        plt.show()

    #================================ PROM TIEMPO EN LA COLA =============================================================
    if opcion == 'Promedio de tiempo en cola': 

        for i in range(max_simulaciones):
            plt.plot(list_tiempos[i], list_t_prom_en_cola[i], c='#ff7203', alpha = 0.5)
            plt.plot(list_tiempos[i], list_t_prom_en_sistema[i], c='#e63244', alpha = 0.5) #T.Sistema

        plt.plot(list_tiempos[i], prom_list_t_prom_en_cola, label = 'Promedio del promedio Wq', c = '#641c34', linewidth = 2)
        plt.plot(list_tiempos[i], prom_list_t_prom_en_sistema, label = 'Promedio del promedio Ws', c = '#641c34',linewidth = 2) #T.sistema
        plt.title('Promedio de demora en cola (Wq) / sistema (Ws)')
        poner_fondo_color()
        plt.grid(linestyle = '--')
        plt.legend()
        plt.show()

    #=============================== PROM TIEMPO EN EL SISTEMA ==========================================
    if opcion == 'Promedio de tiempo en el sistema':

        for i in range(max_simulaciones):
            plt.plot(list_tiempos[i], list_t_prom_en_sistema[i])
        plt.plot(list_tiempos[i], prom_list_t_prom_en_sistema, label = 'Promedio del promedio', c = 'k')
        plt.title('Promedio de tiempo en el sistema')
        plt.legend()
        plt.show()

    #=============================== PROM UTILIZACION SERVIDOR ==========================================
    if opcion == 'Utilizacion del servidor':

        for i in range(max_simulaciones):
            plt.plot(list_tiempos[i], list_utilizac_servidor[i], c= '#03baff', alpha = 0.5)
        
        plt.title('Promedio de utilizacion del servidor p')
        plt.plot(list_tiempos[i], prom_list_utilizac_servidor, label = 'Promedio del promedio', c = '#032cff', linewidth = 2)
        poner_fondo_color()
        plt.grid(linestyle = '--')
        plt.xlabel('Tiempo (t)')
        plt.ylabel('Promedio de utilizacion del servidor (p)')
        plt.legend()
        plt.show()


        mu = AreaB / Time
        veces_mu = [mu, 1 - mu]
        nombres = ["Porcentaje que se utilizó el servidor","Porcentaje que no se utilizó el servidor"]
        plt.pie(veces_mu, labels=nombres, autopct="%0.1f %%")
        plt.title("Porcentaje factor de utilizacion del servidor")
        plt.show()
        #=============================== UTILIZACIÓN DEL SERVIDOR scatter ====================================
        for i in range(max_simulaciones):
            list_utilizac_servidor[i].sort()
            list_prom_nro_cli_sist[i].sort()
            #plt.plot(list_utilizac_servidor[i], list_prom_nro_cli_sist[i])
            plt.scatter(list_utilizac_servidor[i], list_prom_nro_cli_sist[i], s = 10, alpha=0.5, c= '#baff03')

        poner_fondo_color()
        plt.grid(linestyle = '--')
        plt.xlabel('Promedio utilizacion del servidor (p)')
        plt.ylabel('Promedio nro de clientes en cola (Nq)')
        plt.show()

    #==================== PROB. n CLIENTS EN COLA (UTILIZACIÓN DEL SERVIDOR) ======================
    if opcion == 'Probabilidad de n clientes en cola':

        x = np.arange(len(prom_barras_prom_nro_cli_cola))
        y = prom_barras_prom_nro_cli_cola

        plt.stem(x, y, use_line_collection = True, basefmt = 'None', linefmt = 'm')
        plt.grid(linestyle = '--')
        poner_fondo_color()
        plt.xlim(-0.1, 9)
        #plt.ylim(0,1)
        plt.xlabel('Cllientes en cola')
        plt.ylabel('Probabilidad de n clientes en cola')
        plt.show()

    #================================ DENEGACION DE SERVICIO ========================================
    # Hacer tender la denegacion a un nro muy alto de corridas.

    if opcion == 'Denegacion de servicio':
    #================================ Clintes denegados en promedio
        for i in range(max_simulaciones):
            plt.plot(list_tiempos[i], list_prom_nro_cli_denegados[i])
        plt.xlabel('Tiempo (t)')
        plt.ylabel('Promedio clientes denegados.')
        poner_fondo_color()
        plt.grid(linestyle = '--')
        plt.show()

        #================================ Clintes denegados reales
        for i in range(max_simulaciones):
            plt.plot(list_tiempos[i], list_nro_cli_denegados[i])
        plt.xlabel('Tiempo (t)')
        plt.ylabel('Clientes denegados.')
        poner_fondo_color()
        plt.grid(linestyle = '--')
        plt.show()


        # x = np.arange(len(prom_barras_prom_cli_denegados))
        # y = prom_barras_prom_cli_denegados

        # plt.stem(x, y, use_line_collection = True, basefmt = 'None', linefmt = 'm')
        # plt.grid(linestyle = '--')
        # poner_fondo_color()
        # #plt.xlim(-0.1, 9)
        # #plt.ylim(0,1)
        # plt.xlabel('Cllientes denegados')
        # plt.ylabel('Probabilidad de n clientes denegados')
        # plt.show()


        # plt.hist(list_nro_cli_denegados[0], color = '#fdd900', bins = 10, edgecolor = '#fdd900',  linewidth=1)
        # plt.show()
    #=============================================================================================


