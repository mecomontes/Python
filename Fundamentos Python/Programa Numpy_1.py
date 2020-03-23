#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Biblioteca numpy
# Estructura de Datos: Matrices - Arreglos
# Creación de manera explicita

import numpy as np


# Arreglo unidimensional fila: 1 fila x 3 columnas
a=np.array([2,3,4])
print("Arreglo unidimensional fila: ")
print(a)

# Arreglo unidimensional columna: 3 filas x 1 columna
b=np.array([[7],[8],[9]])
print("\n Arreglo unidimensional columna: ")
print(b)

# Arreglo bidimensional (Matriz): 3 filas x 3 columnas
c=np.array([[2,5,1], [5,6,3], [8,9,2]])
print("\n Arreglo bidimensional (Matriz): ")
print(c)

# Atributo shape: (Dimensiones de la matriz: Numero de filas, Numero de columnas)
[Numero_Filas, Numero_Columnas] = c.shape

print("\n    ATRIBUTOS DEL ARREGLO UNIDIMENSIONAL FILA")

print("Numero de Columnas: ", a.shape)
print("Dimensión: ", a.ndim)
print("Número de Elementos: %d  \n" %(a.size))

print("\n    ATRIBUTOS DEL ARREGLO UNIDIMENSIONAL COLUMNA")
#print("Número de filas: %d   Número de columnas:  %d \n" %(Numero_Filas, Numero_Columnas))
print("Numero de Filas: ", b.shape)
print("Dimensión: ", b.ndim)
print("Número de Elementos: %d  \n" %(b.size))

print("\n    ATRIBUTOS DEL ARREGLO BIDIMENSIONAL")
print("Número de filas: %d   Número de columnas:  %d" %(Numero_Filas, Numero_Columnas))
print("Dimensión: ", c.ndim)
print("Número de Elementos: %d  \n" %(c.size))


# Obtener elementos de un arreglo bidimensional
a1 = np.array([[ 3.21, 5.33, 4.67, 6.41],
            [ 9.54, 0.30, 2.14, 6.57],
            [ 5.62, 0.54, 0.71, 2.56],
            [ 8.19, 2.12, 6.28, 8.76],
            [ 8.72, 1.47, 0.77, 8.78]])

print("\n    ARREGLO BIDIMENSIONAL")
print(a1)

print("\n    ELEMENTOS DEL ARREGLO BIDIMENSIONAL")
print(a1[1, 2])
print(a1[4, 3])
print(a1[-1, -1])
print(a1[0, -1])

# Secciones rectangulares del arreglo
print("\n    SECCIONES RECTANGULARES DEL ARREGLO BIDIMENSIONAL")
print(a1[2:3, 1:4])
print(a1[1:4, 0:4])
print(a1[1:3, 2])
print(a1[2, :])
print(a1[:, 3])

