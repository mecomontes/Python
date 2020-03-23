#!/usr/bin/env python
#-*- coding: utf-8 -*-

# PARCIAL Nº 3: ---> 15%(20%)
#       Ordenamiento: Selección: (25%)
#       Ordenamiento: Inserción: (25%)
#       Ordenamiento: Burbuja:   (25%)
#       Busqueda: Binaria:       (25%)
#       Bonificación: Quick Sort  (10%) sobre la nota obtenida en el Parcial 3 con respecto a los numerales: a, b, c, d.

import random

# DATOS DE TRABAJO
# Métodos de ordenamiento:
#                    Número de Elementos de la Lista
#                    La Lista

# Método de búsqueda:
#                   Número de Elementos de la Lista
#                   La Lista ordenada
#                   Elemento de Búsqueda

# Métodos de ordenamiento:
Numero_Elementos_Lista=random.randint(5,6)
# Creacion de la Lista de acuerdo al numero de elementos de la lista
Lista=[]

for i in range(Numero_Elementos_Lista):
    Numero_Lista=random.randint(0,100)
    Lista.append(Numero_Lista)

# Método de búsqueda:
Numero_Elementos_Lista2=random.randint(8,10)
# Creacion de la Lista de acuerdo al numero de elementos de la lista
Elemento_Busqueda=random.randint(0,100)

Lista2=[]

# for i in range(Numero_Elementos_Lista2):

# Creación de la Lista 2
while len(Lista2) < Numero_Elementos_Lista2:
    Numero_Lista=random.randint(0,100)
    if not Numero_Lista in Lista2:
            Lista2.append(Numero_Lista)

# Ordena la lista
Lista2.sort()
# Crea archivo con datos generados
try:
    Archivo = open('Datos_Parcial_3.txt','w')
    Linea1=str(Numero_Elementos_Lista)
    Linea2=str(Lista)
    Linea3=str(Numero_Elementos_Lista2)
    Linea4=str(Lista2)
    Linea5=str(Elemento_Busqueda)
    Archivo.write(Linea1)
    Archivo.write('\n')
    Archivo.write(Linea2)
    Archivo.write('\n')
    Archivo.write(Linea3)
    Archivo.write('\n')
    Archivo.write(Linea4)
    Archivo.write('\n')
    Archivo.write(Linea5)
    Archivo.write('\n')
    # Muestra el archivo
    print (Archivo)
    # Cierra el archivo
    Archivo.close()
except IOError:
    print("Archivo no existe")


print ("")
print(" \t      PARCIAL Nº 3")
print("\n MÉTODOS DE ORDENAMIENTO")
print ("Número de Elementos de la Lista: ",Numero_Elementos_Lista)
print ("Lista: ", Lista)
print("\n MÉTODO DE BÚSQUEDA")
print ("Número de Elementos de la Lista 2: ",Numero_Elementos_Lista2)
print ("Lista 2: ", Lista2)
print ("Elemento de Búsqueda: ",Elemento_Busqueda)





