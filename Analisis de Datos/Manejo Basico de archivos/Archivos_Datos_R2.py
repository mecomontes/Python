# Archivo de datos
# Abrir un archivo que no existe
# Manejar la Excepcion

try:
    archivo = open('Jovennes.txt')
    for linea in archivo:
        print linea
    archivo.close()
except IOError:
    print("Archivo no existe")

