from matplotlib import pyplot as plt
import numpy as np 

def graph_all_muestras(repeat):
    #Graficando todas las muestras
    #plt.figure(figsize=(8, 8))
    plt.title('Muestra de metodo Cuadrados Mixto')#s de distintos generadores')
    #plt.plot(np.arange(repeat),rand, color = 'b', label = 'Rand')
    #plt.plot(np.arange(repeat),randU, color = 'm', label = 'RandU')
    #plt.plot(np.arange(repeat),random_py, color = 'y', label = 'Rand Python')
    plt.plot(np.arange(repeat),cuadrados, color = 'g', label = 'Cuadrados medios')
    #plt.plot(np.arange(repeat),mixto, color = 'c', label = 'GCL mixto')

    plt.xlabel('Nro de repeticion')
    plt.ylabel('Valor de la muestra')
    plt.legend()
    plt.show()

scale = 1
colors = ['b', 'm', 'y', 'c', 'k', 'g']
nombres = ['Rand', 'RandU', 'Rand Python','Mixto', 'Random.ORG', 'Cuadrados medios']

def graph_muestra_scatter(muestras, repeat):
    #plt.figure(figsize=(8, 8))
    plt.title('Muestras de distintos generadores')
    for i in range(len(muestras)):
        plt.scatter(np.arange(repeat),muestras[i], color = colors[i],s = scale, label = nombres[i])
    plt.plot(np.arange(repeat), muestras[3], 'o', label=nombres[3], markersize=np.sqrt(0.2), c='c')
    
    plt.xlabel('Nro de repeticion')
    plt.ylabel('Valor de la muestra')
    #plt.legend()
    

    lgnd = plt.legend(loc="lower left", numpoints=1, fontsize=10)

    #change the marker size manually for both lines
    lgnd.legendHandles[0]._legmarker.set_markersize(6)
    plt.show()

def graph_only_muestra_scatter(i, muestra, repeat):
    plt.title(f'Muestra de {nombres[i]}')
    plt.scatter(np.arange(repeat),muestra, color = colors[i],s = scale )
    plt.xlabel('Nro de repeticion')
    plt.ylabel('Valor de la muestra')
