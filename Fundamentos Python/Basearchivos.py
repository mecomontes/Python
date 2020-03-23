#### operacion con archivos txt

archivo = open('elementos.txt','r+') # abrir el archivo
elementos=archivo.read()
print(elementos)
archivo.close ### cerrar el archivo


#####################################################################################



# abre archivo (y cierra cuando termine lectura)
with open("elementos.txt") as fichero:
    # recorre línea a línea el archivo
    for linea in fichero:
        # muestra la última línea leída
        print(linea)
        
        
#####################################################################################
        
        
cadena1 = 'Datos'  # declara cadena1
cadena2 = 'Secretos'  # declara cadena2

# Abre archivo para escribir
archivo = open('datos1.txt','w')

# Escribe cadena1 añadiendo salto de línea 
archivo.write(cadena1 + '\n')

# Escribe cadena2 en archivo
archivo.write(cadena2) 

# cierra archivo
archivo.close

#####################################################################################


# Declara lista
lista = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']  

# Abre archivo en modo escritura
archivo = open('datos2.txt','w')

# Escribe toda la lista en el archivo
archivo.writelines(lista)  

# Cierra archivo
archivo.close 

#####################################################################################

# Abre archivo en modo lectura
archivo = open('datos2.txt','r')  

# Mueve puntero al quinto byte
archivo.seek(5)  

# lee los siguientes 5 bytes
cadena1 = archivo.read(6) 

# Muestra cadena
print('cadena 1: ',cadena1) 

# Muestra posición del puntero 
print(archivo.tell())

# Cierra archivo
archivo.close

#####################################################################################

# Importa módulo pickle
import pickle

# Declara lista
lista = ['Perl', 'Python', 'Ruby']

# Abre archivo binario para escribir   
archivo = open('lenguajes.dat', 'wb')

# Escribe lista en archivo
pickle.dump(lista, archivo)

# Cierra archivo
archivo.close

# Borra de memoria la lista
del lista  

# Abre archivo binario para leer
archivo = open('lenguajes.dat', 'rb')

# carga lista desde archivo
lista = pickle.load(archivo)

# Muestra lista  
print(lista)

# Cierra archivo
archivo.close 