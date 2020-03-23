# Archivo de datos - Ejemplo 1
# Crea archivo de datos: Archivo con varias lineas

# Abre el archivo, si no existe lo crea
Archivo = open('Archivo_Creado.txt', 'w')

# Muestra el archivo
print (Archivo)

# Crea la primera linea para el archivo
linea1 = "Estoy escribiendo la primera linea,\n"
# Graba la primera linea (primer registro) en el archivo
Archivo.write(linea1)

# Crea la segunda linea para el archivo
linea2 = "y aqui la segunda.\n"
# Graba la primera linea (primer registro) en el archivo
Archivo.write(linea2)

# Muestra el archivo
print (Archivo)

#Cierra el archivo
Archivo.close()
