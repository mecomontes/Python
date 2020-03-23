# Archivo de datos - Ejemplo 3: Archivo con varias lineas
try:
    # Abrir el archivo de datos: Debe existir
    # Metodo: readline() Lee una linea del archivo
    f = open("input1.txt")
    linea1=f.readline()
    print (linea1)

    # Mostrar todas las lineas del archivo: for
    # Metodo: seek(byte) Mueve el puntero hacia el byte indicado
    f.seek(0)

    print("")
    print("Desde el for:")
    for i in range(3):
        Archivo=f.readline()
        print(Archivo)

    # Mostrar todas las lineas del archivo: while
    # Metodo: seek(byte) Mueve el puntero hacia el byte indicado
    f.seek(0)

    print("")
    print("Desde el while:")
    linea=f.readline()
    while linea!="":
        print linea
        linea=f.readline()

    # Metodo readlines() retorna una lista con cada linea del archivo de texto
    # Metodo: seek(byte) Mueve el puntero hacia el byte indicado
    f.seek(0)

    # Mostrar todas las lineas del archivo: readlines
    print("")
    print("Desde el for - readlines:")
    lineas=f.readlines()
    for i in lineas:
        print i

    # Mostrar todas las lineas del archivo: while
    # Metodo: seek(byte) Mueve el puntero hacia el byte indicado
    f.seek(0)

    print("")
    print("Desde el while True:")
    print("")

    while True:
        # Lee cada una de las lineas del archivo: readline
        linea = f.readline()
        if linea=="":
            break
        print(linea)

    # Cierra el archivo
    f.close()

    # except FileNotFoundError: No funciono
except IOError:
 print("El archivo no fue encontrado")

