# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Sumatoria de los n primeros números
#  Ciclo repetitivo: for
Numero = int(input("Ingrese el último Número a incluir en la sumatoria: "))

Sumatoria = 0

for Contador in range(1, (Numero+1)):
    Sumatoria += Contador  # Es equivalente a decir: Sumatoria = Sumatoria + Contador

print("Sumatoria de los primeros: ", Numero, " numeros enteros: ", Sumatoria)
