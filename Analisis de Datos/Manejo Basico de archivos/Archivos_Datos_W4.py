# Archivo de datos

# Escribir datos al final de un archivo existente: el modo 'a' (append)

# Manejar la Excepcion: NO ES NECESARIA

# En este caso, modo: a append; como en el caso del modo: w (write), el manejo de la excepcion no es valido por:
# Si el archivo no existe, lo crea
# Si el archivo existe, adiciona la informacion al final del archivo

try:
    a = open('Prueba2.txt', 'a')
    a.write('\n')
    a.write('Chao. ')
    a.write('Saludos.')
    a.close()
except IOError:
    print("Archivo no existe")
