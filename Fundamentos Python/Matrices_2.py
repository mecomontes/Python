#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Creación de una Matriz, de manera aleatoria
# Hacer un programa que llene la matriz de manera aleatoria
# Encontrar:
# El valor mayor
# El valor menor
# El valor promedio

# Generar aleatoriamente:
# El numero de filas que tiene la matriz
# El numero de columnas que tiene la matriz
# Los valores de la matriz

# Mostrar:
# La matriz
# El valor mayor
# El valor menor
# El valor promedio


import numpy as np
import random as rd


Filas=rd.randint(2,10)
Columnas=rd.randint(2,10)

Matriz=np.zeros((Filas,Columnas))

for i in range(Filas):
    for j in range(Columnas):
        Digito=rd.randint(0,99)
        Matriz[i,j]=Digito
        
print ("\n  MATRIZ RESULTADO")
print(Matriz)
