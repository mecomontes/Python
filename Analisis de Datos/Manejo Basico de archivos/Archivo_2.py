#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Archivo de datos - Ejemplo 2

# Abrir el archivo de datos: Debe existir
# Metodo: read() Lee todo el contenido de un archivo

f = open("Frases_Socrates.txt")
Archivo=f.read()
print(Archivo)

# Cierra l archivo
f.close



