from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np 
from tabulate import tabulate

scale   = 1
colors  = ['b', 'm', 'y', 'c', 'k', 'g']
nombres = ['Rand', 'RandU', 'Rand Python','Mixto', 'Random.ORG', 'Cuadrados medios']

def graph_reticulas(repeat, muestras):
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    for i in range(len(muestras)):
        x = []
        y = []
        z = []
        for j in range(0,repeat - 3,3):
            x.append(muestras[i][j])
            y.append(muestras[i][j + 1])
            z.append(muestras[i][j + 2])    
        ax1.scatter(x, y, z, c= colors[i], marker='o', s = 5)
    plt.title(nombres[i])
    plt.show()

def graph_reticulas_all(repeat, muestras):
    for i in range(len(muestras)):
        fig = plt.figure()
        ax1 = fig.add_subplot(111, projection='3d')
        x = []
        y = []
        z = []
        for j in range(0,repeat - 3,3):
            x.append(muestras[i][j])
            y.append(muestras[i][j + 1])
            z.append(muestras[i][j + 2])    
        ax1.scatter(x, y, z, c= colors[i], marker='o', s = 5)
        plt.title(nombres[i])
        plt.show()

def chi_line(fa_muestras, fo_acum_muestras, scatter, repeat, c = -1):
    #Lineal frec_o vs frec_real
    #plt.figure(figsize=(8, 8))
    plt.title('Observado vs Esperado')
    for i in range(len(fa_muestras)):
        co = colors[i]
        no = nombres[i]
        if(c == 5 ): 
            co = colors[c]
            no = nombres[c]
        if(scatter):
            plt.plot(fa_muestras[i], fo_acum_muestras[i], color = co, label = no)
        else:
            plt.scatter(fa_muestras[i], fo_acum_muestras[i], s = 15, color = co, label = no)
    
    plt.plot(fa_muestras[0], [i*repeat for i in fa_muestras[0]], color = 'r', label = 'frec esperada')
    plt.xlabel('Intervalo de clase')
    plt.ylabel('Frecuencia absoluta acumulada')
    plt.legend()
    #plt.show()

def chi_frec_abs_intervals(fa_muestras, fo_muestras, repeat, c= -1):
    # ======================= Frecuencias absolutas por intervalo
    #plt.figure(figsize=(8, 8))
    plt.title('Frecuencias absolutas por intervalo')

    for i in range(len(fa_muestras)):
        if (c == 5):
            plt.plot(fa_muestras[i], fo_muestras[i], color = colors[c], label = nombres[c])
        else:
            plt.plot(fa_muestras[i], fo_muestras[i], color = colors[i], label = nombres[i])

    plt.axhline(y = repeat / int(np.sqrt(repeat)), color = 'r', label = 'frec esperada')
    plt.xlabel('Intervalo de clase')
    plt.ylabel('Frecuencia absoluta')
    plt.legend()
    #plt.show()

def chi_graph(fas, fos, fos_acum, repeat, fig1, c = -1):
    if (c == -1):
        a,b = 1,2
    else:
        a,b = 3,4

    fig1.add_subplot(2, 2, a)
    chi_line(fas, fos_acum, True, repeat, c)
    
    fig1.add_subplot(2, 2, b)
    chi_frec_abs_intervals(fas, fos, repeat, c)

    
def chi_histogram(muestras, repeat):
    fig1 = plt.figure("Histogramas de diferentes generadores")
    fig1.subplots_adjust(hspace=0.46, wspace=0.29, top=0.94, left=0.06, right=0.97, bottom=0.07)

    for i in range(len(muestras)):
        fig1.add_subplot(2, 3, i + 1)

        plt.title(f'Ocurrencias por intervalo: Muestra {nombres[i]}')
        plt.hist(muestras[i], color = colors[i], bins=int(np.sqrt(repeat)), edgecolor = 'black',  linewidth=1)
        plt.xlabel('Intervalo de clase')
        plt.ylabel('Frecuencia absoluta')
    
    plt.show()

def chi_table(parame, pasos, muestras):
    test_arr_abaj = [['Generadores'],
                    [''], 
                    ['RAND'], 
                    ['RANDU '], 
                    ['RANDOM PYTHON'], 
                    ['GCL MIXTO'], 
                    ['RANDOM.ORG'],
                    ['CUADRADOS MEDIOS']]

    test_arr_abaj[0].append('CHICUADRADO')
    test_arr_abaj[0].append('PASO EL TEST')
    test_arr_abaj[1].append('Valor: chicuadrado - Tabla')

    for i in range (0,len(muestras)):
        test_arr_abaj[i+2].append(parame[i])
        test_arr_abaj[i+2].append(pasos[i])

    print(tabulate(test_arr_abaj, headers='firstrow', tablefmt='fancy_grid', stralign='center', floatfmt='.0f'))
    print()

def kolmo_smir_table(parame, pasos, muestras):
    test_ko_si = [['Generadores'],
                  [''], 
                  ['RAND'], 
                  ['RANDU '], 
                  ['RANDOM PYTHON'], 
                  ['GCL MIXTO'], 
                  ['RANDOM.ORG'],
                  ['CUADRADOS MEDIOS']]

    test_ko_si[0].append('Test Kolmogorov Smirnov')
    test_ko_si[0].append('PASO EL TEST')
    test_ko_si[1].append('Dcalc - Dtabla')
    for i in range (len(muestras)):
        test_ko_si[i+2].append(parame[i])
        test_ko_si[i+2].append(pasos[i])

    print(tabulate(test_ko_si, headers='firstrow', tablefmt='fancy_grid', stralign='center', floatfmt='.0f'))
    print()
    
def media_table(parame, pasos, muestras):
    test_arr_abaj = [['Generadores'],
                [''], 
                ['RAND'], 
                ['RANDU '], 
                ['RANDOM PYTHON'], 
                ['GCL MIXTO'], 
                ['RANDOM.ORG'],
                ['CUADRADOS MEDIOS']]

    test_arr_abaj[0].append('MEDIA')
    test_arr_abaj[0].append('PASO EL TEST')
    test_arr_abaj[1].append(f'Esperanza = {round(np.mean(muestras),4)}')

    for i in range (0,len(muestras)):
        test_arr_abaj[i+2].append(parame[i])
        test_arr_abaj[i+2].append(pasos[i])

    print(tabulate(test_arr_abaj, headers='firstrow', tablefmt='fancy_grid', stralign='center', floatfmt='.0f'))
    print()

def arriba_abajo_table(parame, pasos, muestras):
    test_arr_abaj = [['Generadores'],
                    [''], 
                    ['RAND'], 
                    ['RANDU '], 
                    ['RANDOM PYTHON'], 
                    ['GCL MIXTO'], 
                    ['RANDOM.ORG'],
                    ['CUADRADOS MEDIOS']]

    test_arr_abaj[0].append('Test ARRIBA Y ABAJO')
    test_arr_abaj[0].append('PASO EL TEST')
    test_arr_abaj[1].append('')
    for i in range (0,len(muestras)):
        test_arr_abaj[i+2].append(parame[i])
        test_arr_abaj[i+2].append(pasos[i])

    print(tabulate(test_arr_abaj, headers='firstrow', tablefmt='fancy_grid', stralign='center', floatfmt='.0f'))
    print()