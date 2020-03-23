#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Matrices especiales
import numpy as np
import math as mt

# Matriz de ceros
Matriz_Zeros=np.zeros((3,4))
print("\n MATRIZ DE CEROS ")
print(Matriz_Zeros)


# Matriz de unos
Matriz_Unos=np.ones((9,9))
print("\n       MATRIZ DE UNOS ")
print(Matriz_Unos)

# Matriz identidad: cuadrada
Matriz_Identidad=np.identity((5))
print("\n       MATRIZ IDENTIDAD  ")
print(Matriz_Identidad)

# Matriz vacía
Matriz_Vacia=np.empty((0))
print("\n       MATRIZ VACIA ")
print(Matriz_Vacia)

# Matriz transpuesta
Matriz = np.arange(10,101,10).reshape(2,5)
print("\n MATRIZ ORIGINAL ")
print(Matriz)
print("\n MATRIZ TRASPUESTA  ")
print(Matriz.transpose())

# Matriz con arange
Matriz_arange=np.arange(0,15,2)
print("\n       MATRIZ ARANGE ")
print(Matriz_arange)

# Matriz con linspace 1
Matriz_linspace=np.linspace(0,15,2)
print("\n       MATRIZ LINSPACE 1 ")
print(Matriz_linspace)

# Matriz con linspace 2
Matriz_linspace_2=np.linspace(0,2,9)
print("\n       MATRIZ LINSPACE 2 ")
print(Matriz_linspace_2)

# Matriz con linspace 3
Matriz_linspace_3=np.linspace(0,(2*mt.pi),10)
print("\n       MATRIZ LINSPACE 3 ")
print(Matriz_linspace_3)





