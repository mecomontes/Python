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
    print("\n     Lista Creada     ")
    print("Numero de Elementos: %d" % Numero_Aleatorio)
    print(Lista)

    return Lista

# Programa 1 - ORDENAMIENTO POR INTERCAMBIO
# Ordenamiento en orden ascendente

def Fun_Busqueda_Binaria(Lista):
    buscar=12
    puntero=0
    Busqueda=0
    n=len(Lista)
    med=int(n/2)
    while puntero<=n and Busqueda==0:
        med=int((puntero+n)/2)
        if buscar==Lista[med]:
            print('el valor '+str(buscar)+' esta en la posicion '+str(med))
            Busqueda=1
        elif buscar<Lista[med]:
            n=med-1
        else:
            puntero=med+1  
    if Busqueda==0:
        print('el valor no esta en la lista')

# Función: Crea una lista a partir de numeros aleatorios
Lista = Fun_Crea_Lista()

# Función: Ordenamiento por Intercambio (A)
Fun_Busqueda_Binaria(Lista)
