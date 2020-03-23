# Archivo de datos
# Abrir un archivo
# Contar el numero de palabras hay en cada linea

archivo = open('Jovenes.txt')
for linea in archivo:
    print len(linea)
archivo.close()

# Si modificamos el programa para eliminar el salto de linea:
print("")
archivo = open('Jovenes.txt')
for linea in archivo:
    print len(linea.strip())
archivo.close()



