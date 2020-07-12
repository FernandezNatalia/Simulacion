import numpy as np 
from matplotlib import pyplot as p
import math

def casos_favorables(lista, nro):
  casos_fav = 0
  for nro_random in lista:
    if nro == nro_random:
      casos_fav =  casos_fav + 1
  return casos_fav

def promedio(lista):
  return np.mean(lista)

def grafica_curva(X,Y,legenda,color):
  p.plot(X,Y,c=color, label = legenda, alpha=0.8)

def grafica_decorado(xlbl,ylbl,titulo):
  p.xlabel(xlbl) 
  p.ylabel(ylbl)
  p.title(titulo)
  p.legend(loc='best')
  

def agrandar():
  p.figure(figsize=(20, 8))

X = []
Y_graf1 = []
Y_graf2 = []
Y_graf3 = []
Y_graf4 = []
Y_graf5 = []

lista_nros_random = []
corridas = []
total_numeros = []

#============== VARIABLES DE ENTRADA ==============#
nro_max_tiradas = 2000
cant_nros_ruleta = 37
cant_corridas = 5
#==================================================#
nro_X = np.random.randint(cant_nros_ruleta)

for i in range(cant_corridas):

  lista_nros_random = []
  lista_fr_actuales = []
  lista_promedio_actuales = []
  lista_desvios_actuales = []
  lista_varianza_actuales = []

  for nro_tiradas in range(1,nro_max_tiradas + 1):

    nro_random = np.random.randint(0,cant_nros_ruleta)
    lista_nros_random.append(nro_random)

    #============== GRAFICO 1==============#
    frec_relativa = casos_favorables(lista_nros_random,nro_X) / nro_tiradas
    lista_fr_actuales.append(frec_relativa)

    #============== GRAFICO 2==============#
    lista_promedio_actuales.append(promedio(lista_nros_random))

    #============== GRAFICO 3==============#
    desvio_de_X = np.std(lista_nros_random)
    lista_desvios_actuales.append(desvio_de_X)

    #============== GRAFICO 4==============#
    varianza_de_X = np.var(lista_nros_random)
    lista_varianza_actuales.append(varianza_de_X)

    total_numeros.append(nro_random)

  corridas.append(lista_nros_random)

  Y_graf1.append(lista_fr_actuales)
  Y_graf2.append(lista_promedio_actuales)
  Y_graf3.append(lista_desvios_actuales)
  Y_graf4.append(lista_varianza_actuales)

# Listas a utilizar
fr_esperada = []
prom_esperado = []
desvio_esperado = []
varianza_esperada = []
fr_absoluta_esp = []

for i in range(nro_max_tiradas) :
  fr_esperada.append(np.mean([x[i] for x in Y_graf1]))
  prom_esperado.append(np.mean([x[i] for x in Y_graf2]))
  desvio_esperado.append(np.mean([x[i] for x in Y_graf3]))
  varianza_esperada.append(np.mean([x[i] for x in Y_graf4]))
  
fr_absoluta_esp = []

for i in range(cant_nros_ruleta):
  casos_fav = []
  for j in range(cant_corridas):
    casos_fav.append(casos_favorables(corridas[j],i))
  fr_absoluta_esp.append(promedio(casos_fav))

valor_prom_esperado = np.mean(corridas)
desvio = math.fabs(nro_X - valor_prom_esperado)
varianza = desvio * desvio
media_total = nro_max_tiradas/cant_nros_ruleta
xlabel = "n (numero de tiradas)"
colores = ["m","g","y","r","c"] * round(cant_corridas / 5)
X = np.arange(1,nro_max_tiradas + 1)

fig1 = p.figure("Graficas de una sola corrida")
fig1.subplots_adjust(hspace=0.46, wspace=0.29, left=0.09, right=0.95)

#================================GRAFICO 1====================================================#
fig1.add_subplot(2,2,1)
grafica_curva(X,Y_graf1[0],"frn (fr de X="+str(nro_X)+" con respecto a n)","m")
grafica_curva(X,fr_esperada,"fre (fr esperada de X="+str(nro_X),"c")
grafica_decorado(xlabel,"fr (frecuencia relativa)","Grafico 1")

#================================GRAFICO 2====================================================#
fig1.add_subplot(2,2,2)
grafica_curva(X,Y_graf2[0],"vpn (valor promedio de las tiradas con respecto a n)","m")
grafica_curva(X,prom_esperado,"vpe (valor promedio esperado)","c")
grafica_decorado(xlabel,"vp (valor promedio de las tiradas)","Grafico 2")
#================================GRAFICO 3====================================================#
fig1.add_subplot(2,2,3)
grafica_curva(X,Y_graf3[0],"vd (valor del desvio del numero X)","m")
grafica_curva(X,desvio_esperado,"vde (valor del desvio esperado)","c")
grafica_decorado(xlabel,"vd (valor de desvio)","Grafico 3")
#================================GRAFICO 4====================================================#
fig1.add_subplot(2,2,4)
grafica_curva(X,Y_graf4[0],"vvn (valor de la varianza del numero X)","m")
grafica_curva(X,varianza_esperada,"vve (valor de la varianza esperada)","c")
grafica_decorado(xlabel,"vv (valor de la varianza)","Grafico 4")
p.show()
#=============================================================================================#
fig1 = p.figure("Graficas de varias sola corrida")
fig1.subplots_adjust(hspace=0.46, wspace=0.29, left=0.09, right=0.95)
#================================GRAFICO 5 - VARIAS CORRIDAS PARA LA FRECUENCIA===============#
fig1.add_subplot(1,2,1)
for i in range(cant_corridas):
  grafica_curva(X,Y_graf1[i],"Corrida numero "+str(i+1),colores[i])

p.plot(X,fr_esperada,c="b", label = "fre (fr esperada de X="+str(nro_X)+")", linewidth=2.5)
grafica_decorado(xlabel,"fr (frecuencia relativa)","Grafico de varias corridas")

#================================GRAFICO 6 - VARIAS CORRIDAS PARA LA MEDIA====================#
fig1.add_subplot(1,2,2)
for i in range(cant_corridas):
  grafica_curva(X,Y_graf2[i],"Corrida numero "+str(i+1),colores[i])

p.plot(X,prom_esperado,c="b", label = "vpe (valor promedio esperado)", linewidth=2.5)
grafica_decorado(xlabel,"vp (valor promedio de las tiradas)","Grafico de varias corridas")
p.show()
#=============================================================================================#
fig1 = p.figure("Diagramas de barra")
fig1.subplots_adjust(hspace=0.46, wspace=0.29, left=0.09, right=0.95)
#================================DIAGRAMAS DE BARRA===========================================#
#Una sola corrida
fig1.add_subplot(2,2,1)
p.hist(corridas[0],cant_nros_ruleta*2,(0,cant_nros_ruleta),color="c")
grafica_decorado("r (numeros de la ruleta)","fa (frecuencia absoluta)","Diagrama de frecuencias de una sola corrida")

#=======================DIAGRAMAS DE BARRA CON VARIAS CORRIDAS===============================#
fig1.add_subplot(2,1,2)
p.hist(corridas,(cant_nros_ruleta*2),(0,cant_nros_ruleta - 1),color=colores, alpha=0.8)
p.plot(range(cant_nros_ruleta),fr_absoluta_esp,c="b", label = "vpe (valor promedio esperado)", linewidth=2.5)

legendas = []
legendas.append("vpe (valor promedio esperado)")
legendas = legendas + [f"Corrida nro {i}" for i in range(1,6)]
p.legend(legendas)

p.xlabel("r (numeros de la ruleta)")
p.ylabel("fa (frecuencia absoluta)")
p.title("Diagrama de frecuencias de ("+str(cant_corridas)+" corridas)")

#==================DIAGRAMAS DE BARRA DE MEDIA DE TODAS LAS CORRIDAS========================#
fig1.add_subplot(2,2,2)
p.hist(total_numeros,cant_nros_ruleta*2,(0,cant_nros_ruleta),color="m")
p.title("Diagrama de frecuencias de la media de todas las corridas")

p.xlabel("r (numeros de la ruleta)")
p.ylabel("fam (frecuencia absoluta media)")
p.show()

