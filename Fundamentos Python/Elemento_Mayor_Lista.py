#!/usr/bin/env python
#-*- coding: utf-8 -*-

def Fun_Crea_Lista():

    import random

    # Crea una lista a partir de numeros aleatorios
    # Generar un numero aleatorio(7,10)
    # Generar una lista de números aleatorios de acuerdo al número generado en el punto anterior
    # Mostrar:
    # El numero aleatorio
    # La lista

    # Genera un numero aleatorio(10-15)
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
    print ""

    return Lista

# Función: Encuentra el elemento mayor de la lista

def Elemento_Mayor_Lista(Lista_Elementos):
    Elemento_Mayor=Lista_Elementos[0]
    # Recorre la lista
    for i in range(len(Lista_Elementos)):
        if Lista_Elementos[i]>Elemento_Mayor:
            Elemento_Mayor=Lista_Elementos[i]
    print ("El Elemento Mayor es: %d" % Elemento_Mayor)

# Función: Crea una lista a partir de numeros aleatorios
Lista = Fun_Crea_Lista()

# Función: Encuentra el elemento mayor de la lista
Elemento_Mayor_Lista(Lista)
