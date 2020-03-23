#!/usr/bin/env python
#-*- coding: utf-8 -*-

def Fun_Crea_Lista():

    import random

    # Crea una lista a partir de numeros aleatorios

    # Generar un numero aleatorio(7-10)
    # Generar una lista de números aleatorios de acuerdo al número generado en el punto anterior

    # Mostrar:
    # El numero aleatorio
    # La lista

    # Genera un numero aleatorio(7,10)
    Numero_Aleatorio=int(random.randrange(7,10))

    # Crea la lista vacía
    Lista = []

    for i in range(Numero_Aleatorio):
        Numero_Aleatorio2=int(random.randrange(1,100))
        Lista.append(Numero_Aleatorio2)

    #Salida
    print("     Lista Creada     ")
    print("Numero de Elementos: %d" % Numero_Aleatorio)
    print(Lista)

    return Lista

# Programa 1 - ORDENAMIENTO POR INSERCION
# Ordenamiento en orden ascendente

def Fun_Insercion1(Lista_Elementos):

    # Ordenar la lista en orden ascendente
    # Clasificacion de la Lista

    for i in range(len(Lista_Elementos)):
         j=i
         Auxiliar=Lista_Elementos[i]
         while j > 0 and Auxiliar < Lista_Elementos[j-1]:
             Lista_Elementos[j] = Lista_Elementos[j-1]
             j= j-1

         Lista_Elementos[j]=Auxiliar
    print ("")
    print(" ORDENAMIENTO POR INSERCION (A)")
    print (Lista_Elementos)


# Función: Crea una lista a partir de numeros aleatorios
Lista = Fun_Crea_Lista()

# Función: Ordenamiento por Inserción (A)
Fun_Insercion1(Lista)


