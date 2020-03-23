#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Biblioteca numpy
# Estructura de Datos: Matrices - Arreglos
# Creación desde el arange (valor inicial, valor final, incremento)
# Operaciones entre matrices

import numpy as np
import random as rd

#Filas= rd.randint(2,10)
Filas= 1
Columnas=rd.randint(2,10)

Matriz_1=np.zeros((Filas,Columnas))
Matriz_2=np.zeros((Filas,Columnas))

for i in range(Filas):
    for j in range(Columnas):
        Digito=rd.randint(0,99)
        Matriz_1[i,j]=Digito
        Digito=rd.randint(0,99)
        Matriz_2[i,j]=Digito

print ("\n  MATRIZ RESULTADO")
print("MATRIZ 1: \n",Matriz_1)
print("MATRIZ 2: \n", Matriz_2)


# OPERACIONES ENTRE MATRICES
Matriz_Suma = Matriz_1 + Matriz_2
print("\n MATRIZ SUMA ")
print(Matriz_Suma)

Matriz_C = Matriz_Suma*2
print("\n MATRIZ C ")
print(Matriz_C)
