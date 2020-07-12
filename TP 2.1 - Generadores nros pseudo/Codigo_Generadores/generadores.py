from random import random
import numpy as np 
import math
import re

def NO_GCL_metodo_cuadrados(seed, repeat):
  metodo_cuadrados = []
  for i in range(repeat):
    value = str(seed ** 2).zfill(8)
    seed = int(value[2:6])
    metodo_cuadrados.append(seed / 10000)
  return metodo_cuadrados

def GCL(semilla, a, m, repeat, c = 0):
  x = []
  u = []
  x.append(semilla)

  for i in range(0, repeat):
    x.append((a * x[i] + c) % m)
    u.append(x[i + 1] / m)
  x.pop(0)
  return u

def GFisico(repeat):
  with open("ramdonORG.txt") as f:
      content = f.read()
      secuencia = content.split('\n')

  randonORG = []
  for s in secuencia:
      randonORG.append(float(s))

  return randonORG[:repeat]