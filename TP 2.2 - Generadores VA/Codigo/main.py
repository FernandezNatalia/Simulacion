from random import random
import numpy as np 
import math
from matplotlib import pyplot as plt
import PyInquirer as inquirer
from os import system
from a_uniform import *
from b_exponencial import *
from c_gamma import *
from d_normal import *
from e_pascal import *
from f_binomial import *
from g_hipergeometrica import *
from h_poisson import *
from i_discreta_empirica import *
from test import *

# ORDEN DE LAS DISTRIBUCIONES
# 1- Uniforme
# 2- Exponencial
# 3- Gamma
# 4- Normal
# 5- Pascal
# 6- Binomial
# 7- Hipergeometrica
# 8- Poisson
# 9- Empirica discreta

opciones = [
    {
         'type': 'list',
         'name': 'distribucion_seleccionada',
         'message': "Seleccione una distribucion",
         'choices': ['Uniforme', 
                     'Exponencial', 
                     'Gamma', 
                     'Normal', 
                     'Pascal', 
                     'Binomial', 
                     'Hipergeometrica', 
                     'Poisson', 
                     'Empirica discreta']
     }
 ]

# Cantidad de tiradas =====
n = 5000 
# =========================

while True:
    system("cls")
    print(chr(27)+"[1;33m") 
    print('---------------------------------------------')
    respuesta = inquirer.prompt(opciones)
    selec = respuesta['distribucion_seleccionada']

    print(chr(27)+"[;37m")
    system("cls")

    # 1- Distribucion Uniforme ===================================================
    if selec == 'Uniforme':
        a, b = 0, 20
        corrida = generate_uniform(a, b, n)
        esperada = list(np.random.uniform(a, b, n))

        # Test Chicuadrado
        realizar_test(corrida, esperada, selec)
        graph_uniform(corrida, a, b)

    # 2- Distribucion Exponencial =================================================
    if selec == 'Exponencial':
        alfa = 0.1
        corrida = generate_exponencial(alfa, n)

        # Test Chicuadrado
        realizar_test(corrida, corrida, selec)
        graph_exponencial(corrida, alfa)

    # 3- Distribucion Gamma =======================================================
    if selec == 'Gamma':
        # Distribucion
        alfa, k = 0.5, 2
        corrida = generate_gamma(alfa, k, n)
        graph_gamma(corrida, alfa, k)

        # Generador Python
        m = 100
        ks = [2] * m
        alfas    = [0.5] * m
        graph_n_gamma(alfas, ks, n)

        # Variando parametros
        alfas = [0.5, 0.8 , 1, 1, 1]
        ks    = [2, 2, 1, 2, 5]
        graph_n_gamma(alfas, ks, n)

    # 4- Distribucion Normal =======================================================
    if selec == 'Normal':
        #e, s= 0, 3
        e, s= 4.1, math.sqrt(1.82)
        corrida = generate_normal(e, s, n)
        esperada = np.random.normal(e, s, n)

        # Test Chicuadrado
        realizar_test(corrida, esperada, selec)
        graph_normal(corrida, e, s)

    # 5- Pascal ====================================================================
    if selec == 'Pascal':
        k, p = 5, 0.3
        corrida = generate_pascal(k, p, n)
        graph_pascal(corrida, k, p)
        #graph_pascal_esperada()

    # 6- Binomial ==================================================================
    if selec == 'Binomial':
        p = 0.4
        nb = 20

        corrida = generate_binomial(n, nb, p)
        esperada = np.random.binomial(nb, p, n)

        # Test Chicuadrado
        realizar_test(corrida, esperada, selec)
        graph_binomial(corrida, nb, p)

    # 7- Hipergeometrica ===========================================================
    if selec == 'Hipergeometrica':
        mues, Nt, r  = 100, 500, 50 #3, 25, 3
        p  = r / Nt
        corrida = generate_hipergeometrica(n, p, Nt, mues)
        graph_hipergeometrica(corrida, p, Nt, mues, r)

    # 8- Poisson ===================================================================
    if selec == 'Poisson':
        lamda = 0.4
        corrida = generate_poisson(n, lamda)
        esperada = np.random.poisson(lamda, n)

        # Test Chicuadrado
        realizar_test(corrida, esperada, selec)
        graph_poisson(corrida, lamda)

    # 9- Empirica discreta =========================================================
    if selec == 'Empirica discreta':
        p = 0.4
        nb = 20
        corrida = generate_discreta_empirica(n)
        esperada = np.random.binomial(nb, p, n)

        # Test Chicuadrado
        realizar_test(corrida, esperada, selec)
        graph_discreta_empirica(corrida, n)