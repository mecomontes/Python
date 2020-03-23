#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Biblioteca numpy
# Estructura de Datos:  Arreglos
# Creación del arreglo de manera explícita
# Operaciones entre arreglos
#
import numpy as np

# OPERACIONES ENTRE ARREGLOS

a = np.array([55, 21, 19, 11, 9])
b = np.array([2, 7, 4, 3, 5])
c= a + b
d= a-b
e= a*b
f= a/b
g= a**b
print ("\n  ARREGLOS ")
print(a)
print(b)
print ("\n  OPERACIONES ENTRE ARREGLOS ")
print("SUMA: ", c)
print("RESTA: ", d)
print("MULTIPLICACIÓN", e)
print("DIVISIÓN: ", f)
print("EXPONENCIACIÓN: ", g)


