# Archivo de Datos

#!/usr/bin/python3
# -*- coding: utf-8 -*-

# A partir del archivo de datos entregado; construya un programa que muestre para cada estudiante:
#        a. Los datos del estudiante
#        b. El nombre completo del estudiante
#        c. La nota promedio de cada estudiante
try:
    # Abrir el archivo de datos: Debe existir
    # Metodo: readline() Lee una linea del archivo
    f = open("Datos_Notas.csv","r")
    print("Datos del Archivo")
    lineax = f.readline()
    print(lineax)
    lineas=f.readlines()
    print (lineas)

    # Para leer los datos de un archivo de valores con separadores, debe hacerlo linea por linea,
    # eliminar el salto de linea usando el metodo strip y luego
    # extraer los valores de la linea usando el metodo split
    # Este archivo tiene como separador de cada dato el caracter:  ; (punto y coma)

    print("")
    print("         LISTADO DE ESTUDIANTES")
    print("")

    for line in lineas:
         linea = line.strip().split(';')
         print(linea)
        # Toma cada uno de los datos del archivo
         Nombre = linea[0]
         Apellido = linea[1]
         Nota1= float(linea[2])
         Nota2= float(linea[3])
         Nota3= float(linea[4])
         Nota4= float(linea[5])
         # Obtiene el valor promedio
         Promedio = (Nota1 + Nota2 + Nota3 + Nota4) / 4


         # Salida por estudiante
         # Estas dos salidas son equivalentes
         print ('{0} {1} obtuvo promedio {2}'.format(Nombre, Apellido, Promedio))
         print("%s %s obtuvo un promedio de: %.2f \n" %(Nombre, Apellido, Promedio))


    # Cierra el archivo
    f.close()

except IOError:
 print("El archivo no fue encontrado")

