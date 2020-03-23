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
    print("")

    return Lista


# Funcion: Encuentra el valor promedio de la lista
def Promedio_Lista(Lista_Elementos):
    # Inicializa el acumulador
    Acumulador=0
    # Recorre la lista
    for i in range(len(Lista_Elementos)):
        Acumulador+=Lista_Elementos[i]

    Promedio= float(Acumulador/len(Lista_Elementos))
    print ("El Valor Promedio es: %.2f " %Promedio)

# Función: Crea una lista a partir de numeros aleatorios
Lista = Fun_Crea_Lista()

# Funcion: Encuentra el valor promedio de la lista
Promedio_Lista(Lista)
