#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Biblioteca numpy
# Estructura de Datos: Matrices - Arreglos
# Creación desde el arange (valor inicial, valor final, incremento)

import numpy as np

#
Matriz_A = np.arange(15).reshape(3,5)
print("\n MATRIZ A ")
print(Matriz_A)

# Atributo shape: (Dimensiones de la matriz: Numero de filas, Numero de columnas)
[Numero_Filas, Numero_Columnas] = Matriz_A.shape

print("\n    DIMENSIONES DE LA MATRIZ")
print("Número de filas: %d   Número de columnas:  %d \n" %(Numero_Filas, Numero_Columnas))

# Atributo ndim: (Dimensiones de la matriz: Bi-dimensional)
print("\n    DIMENSIONES DE LA MATRIZ")
print("Bi-dimensional: %d  \n" %(Matriz_A.ndim))

# Atributo size: (Número de elementos de la matriz)
print("\n   NÚMERO DE ELEMENTOS DE LA MATRIZ")
print("Número de Elementos: %d  \n" %(Matriz_A.size))
