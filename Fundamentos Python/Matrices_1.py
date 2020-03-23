#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np


# Creación de matriz de ceros
Numero_Filas = 4
Numero_Columnas = 5
# Matriz Ceros
Matriz_Ceros=np.empty(Numero_Filas*Numero_Columnas).reshape(Numero_Filas,Numero_Columnas)

# Matriz Unos
# Crear la matriz de unos como matriz vacía




# Matriz transpuesta
Matriz = np.arange(10,101,10).reshape(2,5)
print("\n MATRIZ ORIGINAL ")
print(Matriz)
# Crear la matriz traspuesta como una matriz vacía



# Matriz identidad
Matriz_Identidad=np.empty(Numero_Filas*Numero_Columnas).reshape(Numero_Filas,Numero_Columnas)

# Llenar la matriz de ceros
for i in range(Numero_Filas):
 for j in range(Numero_Columnas):
  Matriz_Ceros[i,j] = 0
# Salida
print("\n Matriz de Ceros: ", Matriz_Ceros)


# Llenar la matriz de unos


# Salida
#Mostrar la matriz de unos



# Llenar la matriz identidad
for i in range(Numero_Filas):
 for j in range(Numero_Columnas):
  if i==j:
     Matriz_Identidad[i,j] = 1
  else:
     Matriz_Identidad[i,j] = 0

# Salida
print("\n Matriz Identidad: ", Matriz_Identidad)


# Llenar la matriz traspuesta


# Salida
#Mostrar la matriz traspuesta
