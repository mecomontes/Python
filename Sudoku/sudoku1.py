# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 21:43:47 2018

@author: Hp
"""

import numpy as np
import collections
import matplotlib.pylab as plt

def principal(ruta):
    A=leer_sudoku(ruta)
    B=verificar_sudoku(A)
    C=distribucion_digitos(A)
    histograma_digitos(C,ruta)
    
    return B,C,ruta


def leer_sudoku (ruta_archivo):##función para leer el archivo con el sudoku
    A = np.loadtxt(ruta_archivo, delimiter = ",",dtype=int)##cargar el archivo csv como una matriz
    return A##devuelve la matriz A (arreglo numérico)

def verificar_sudoku(solucion):## función para vericar si el sudoku está bueno o malo
    verificar1=0
    lista_fila=[]## se crea una lista vacía para almacenar las filas
    lista_columna=[]## se crea una lista vacía para almacenar las columnas
    
    for i in range(9): ## ciclo para leer cada fila
            for j in range(9):  ## ciclo para leer cada columna
                
                if solucion[i][j]<=9 and solucion[i][j]>=1: #verificar que solo contenga números entre 1 y 9
                    lista_fila.append(solucion[i][j])   ## se crea una lista que solo contiene los valores por cada fila
                    lista_columna.append(solucion[j][i])   ## se crea una lista que solo contiene los valores por cada columna
    
            lista_fila_unicos=list(set(lista_fila)) ## se crea una nueva lista con los valores de cada fila que no se repiten
            lista_columna_unicos=list(set(lista_columna)) ## se crea una nueva lista con los valores de cada columna que no se repiten
            
            if len(lista_fila_unicos)!=9 or len(lista_columna_unicos)!=9: ## si habian valores repetidos, la lista contiene menos de 9 elementos, por lo tanto, contenía valores repetidos
                verificar1=1
            
            lista_fila.clear()## se limpia la lista después de verificar que cumple para almacenar la siguiente fila
            lista_columna.clear()## se limpia la lista después de verificar que cumple para almacenar la siguiente columna
    
    lista_caja=[]  ## se crea una lista vacía para almacenar los subarreglos      
    for i in range(3):
        for j in range(3):
            Auxiliar=solucion[3*i:3*i+3,3*j:3*j+3]
            for p in range(3):
                for q in range(3):
                    lista_caja.append(Auxiliar[p][q])
            lista_caja_unicos=list(set(lista_caja))
           
            if len(lista_caja_unicos)!=9: ## si habian valores repetidos, la lista contiene menos de 9 elementos, por lo tanto, contenía valores repetidos
                verificar1=1
                
            lista_caja.clear()## se lipia la lista después de verificar que cumple para almacenar la siguiente submatriz
            
    if verificar1==0:
        verificar='True'
    else:
        verificar='False'
        
    return verificar

def distribucion_digitos(arreglo):
    lista=[]
    for i in range(9):
        for j in range(9):
            lista.append(arreglo[i][j])
    
    diccionario=dict(collections.Counter(lista))
            
    return diccionario

def histograma_digitos(Diccionario,Ruta):
    plt.hist(Diccionario)
    plt.show()


## C:\Users\Hp\Documents\sudoku.csv

ruta=str(input('Ingrese la ruta donde se encuentra el archivo: ')) ##Se pide la ruta donde se encuentra ubicado el archivo