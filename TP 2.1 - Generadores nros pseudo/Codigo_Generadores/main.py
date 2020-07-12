from random import random
import numpy as np 
import math
from generadores import *
from graph_generadores import *
from tests import *
from graph_test import *
import statsmodels.api as sm
from os import system

# GENERADORES CONGRUENCIALES LINEALES (GCL)
# 1.RAND  - Generador por "Metodo congruencial multiplicativo"
# 2.RANDU - Generador por "Metodo congruencial mixto"

# GENERADORES NO CONGRUENCIALES
# 1.Generador por "Metodo de los cuadrados medios"
# 2.Generador por "Metodo de productos medios"
# 3.Generador por "Metodo de multiplicador constante"

# Consideraciones:
# m y c son primos relativos.
# a - 1 es divisible por todos los factores primos de m

system("cls")

print(chr(27)+"[1;33m") 
print('----------------------------------------------------------------')
print('             GENERACION DE NUMEROS PSEUDOALEATORIOS             ')
print('----------------------------------------------------------------')
print(chr(27)+"[;37m")

repeat= int(input('TOTAL de numeros a generar     : '))
semilla = int(input('Valor semilla GCL              : '))
seed = int(input('Valor semilla NOGCL (4 cifras) : '))


#====================== GENERADORES CONGRUENCIALES ====================== #
semilla = 7 #3
repeat = 6000

#====================== RAND =============================================#
a, m = 7**5, 2**31 - 1
rand = GCL(semilla, a, m, repeat)

#====================== RANDU ===========================================#
a, m = 2**16 + 3, 2**31 
randU = GCL(semilla, a, m, repeat)

#====================== PYTHON RANDOM ===================================#
random_py = [random() for i in range(repeat)] 

#====================== GCL MIXTO ======#
a, m, c = 106, 6075, 1283
mixto = GCL(semilla, a, m, repeat, c)

#====================== GENERADOR METODO DE LOS CUADRADOS MEDIOS ========#
seed = 9731 #6923
cuadrados = NO_GCL_metodo_cuadrados(seed, repeat)

#====================== GENERADOR FISICO DE RANDOM.ORG ==================#
randomORG = GFisico(repeat)

#====================== GRAFICOS DE MUESTRAS #===========================#
muestras = [rand, randU, random_py, mixto, randomORG, cuadrados]
#========================================================================#


#======================= Muestras todas juntas ==========================#
graph_muestra_scatter(muestras, repeat) #-Muestras todas juntas

#======================= Muestras individuales de c/generdaor ===========#
fig1 = plt.figure("Muestras de diferentes generadores")
fig1.subplots_adjust(hspace=0.46, wspace=0.29, top=0.94, left=0.06, right=0.97, bottom=0.07)
for i in range(len(muestras)):
    fig1.add_subplot(2, 3, i + 1)
    graph_only_muestra_scatter(i, muestras[i], repeat) #-Muestras separadas
plt.show()

#======================= TESTs ==========================================#
system("cls")
print(chr(27)+"[1;33m") 
print('----------------------------------------------------------------')
print('                TESTs DE NUMEROS PSEUDOALEATORIOS               ')
print('----------------------------------------------------------------')
print(chr(27)+"[;37m")
print()

graph_reticulas(repeat, muestras)       #-Reticulas 3D todas las muetras separadas
graph_reticulas_all(repeat, muestras)   #-Reticulas 3D todas las muetras juntas

#=================== TEST CHI-CUADRADO ===============#
cant = 5 # Numero de muestras a graficar en un mismo lugar
fas = list(np.zeros(cant))
fos = list(np.zeros(cant))
fos_acum = list(np.zeros(cant))
pasos = list(np.zeros(cant))
parame = [' '] * cant
for i in range(cant):
    # Prueba de chi-cuadrado a todas las muestras.
    fas[i], fos[i], fos_acum[i], parame[i], pasos[i] = test_chi_cuadrado(repeat, muestras[i])

# Prueba de chi-cuadrado de metodo de los cuadrados.
fa_cuadr, fo_cuadr, fo_acum_cuadr, param, pasoCuadr = test_chi_cuadrado(repeat, cuadrados)

#======================= GRAFICAS de los TEST =======================#

fig1 = plt.figure("Grafico del Test Chi-Cuadrado")
fig1.subplots_adjust(hspace=0.46, wspace=0.29, top=0.94, left=0.11, right=0.87, bottom=0.07)
chi_graph(fas, fos, fos_acum, repeat, fig1)
chi_graph([fa_cuadr], [fo_cuadr], [fo_acum_cuadr], repeat, fig1, 5)
plt.show()

# Tabla chicuadrado - Resultados
parame.append(param)
pasos.append(pasoCuadr)
chi_table(parame, pasos, muestras)

# Comparacion cantidad veces ocurrencia cada intervalo
chi_histogram(muestras, repeat)

#=================== TEST DE MEDIAS =================================#
pasos = list(np.zeros(len(muestras)))
valor_media = [' '] * len(muestras)
for i in range(len(muestras)):
    pasos[i], valor_media[i] = test_media(muestras[i], repeat)

media_table(valor_media, pasos, muestras)

#=================== TEST ARRIBA Y ABAJO ===========================#
pasos = [' '] * len(muestras)
parame = [' '] * len(muestras)
for i in range(len(muestras)):
    parame[i], pasos[i] = test_arriba_abajo(muestras[i])

arriba_abajo_table(parame, pasos, muestras)

#=================== TEST Kolmogorov Smirnov=======================#
pasos = [' '] * len(muestras)
parame = [' '] * len(muestras)
for i in range(len(muestras)):
    parame[i], pasos[i] = test_Kolmogorov_Smirnov(muestras[i])
kolmo_smir_table(parame, pasos, muestras)


