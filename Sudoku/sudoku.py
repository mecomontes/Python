# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 21:43:47 2018

@author: Hp
"""

import numpy as np

def leer_sudoku (ruta_archivo):
    A = np.loadtxt(ruta_archivo, delimiter = ",")
    return A

def verificar_sudoku(solucion):
    lista=[]
    for i in range(9):
        for j in range(9):
            if solucion[i][j]<=9 and solucion[i][j]>=1: #verificar que solo contenga números entre 1 y 9
                lista.append(solucion[i][j])    ## creo una lista con cada una de las filas 
                
            else 
                return False

## C:/Users/Hp/Documents/sudoku.csv
ruta=str(input('Ingrese la ruta donde se encuentra el archivo: ')) ##Se pide la ruta donde se encuentra ubicado el archivo
B=leer_sudoku(ruta)
verificar_sudoku(B)

print(B)



