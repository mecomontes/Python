# Archivo de datos

# Escribir datos al final de un archivo existente: el modo 'a' (append)

a = open('Prueba.txt', 'a')
a.write('\n')
a.write('Chao. ')
a.write('Saludos.')
a.close()
