# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Sumatoria de los n primeros números
#  Ciclo repetitivo: while
Numero = float(input("Ingrese el último Número a incluir en la sumatoria: "))

Sumatoria = 0
Contador = 1
while Contador <= 100:
    Sumatoria += Contador # Es equivalente a decir: Sumatoria = Sumatoria + Contador
    Contador += 1         # Es equivalente a decir: Contador  = Contador + 1

print("Sumatoria de los primeros: ", Numero, " numeros enteros: ", Sumatoria)
