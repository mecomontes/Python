

# Leer el archivo 'datos.csv' con reader() y 
# mostrar todos los registros, uno a uno:

import csv

with open('datos.csv') as csvarchivo:
    entrada = csv.reader(csvarchivo)
    for reg in entrada:
        print(reg)  # Cada línea se muestra como una lista de campos
        

# Leer el archivo 'datos.csv' con reader() y 
# realizar algunas operaciones básicas: 

csvarchivo = open('datos.csv')  # Abrir archivo csv
entrada = csv.reader(csvarchivo)  # Leer todos los registros
reg = next(entrada)  # Leer registro (lista)
print(reg)  # Mostrar registro
nombre, provincia, consumo = next(entrada)  # Leer campos
print(nombre, provincia, consumo)  # Mostrar campos
nombre, provincia, consumo = next(entrada)
print(nombre, provincia, consumo) 

# Crear listas para ordenarlas con la función sorted()

lista1 = ['ABCDEF', 'ABCEFGHIJ', 'ABC', 'ABCD']
lista2 = ['10', '30', '20', '4']

# Ordenar lista1 por la longitud de sus elementos:

lista1 = sorted(lista1, key=len)
print('lista1 ordenada por longitud de cadenas: \n', lista1)

# Ordenar lista1 por la longitud de sus elementos en orden inverso:

lista1 = sorted(lista1, key=len, reverse=True)
print('lista1 ordenada por longitud de cadenas inverso:\n', lista1)

# Ordenar lista2 por el valor numérico de sus elementos:

lista2 = sorted(lista2, key=int, reverse=False)
print('lista2 ordenada por valor numérico:\n', lista2)

# Declarar una lista con cuatro tuplas de dos campos cada una:

lista = [('cccc', 4444), ('d', 1), ('aa', 22), ('bbb', 333)]



import operator

# Ordenar lista por el segundo campo de cada tupla (índice 1):

listaord = sorted(lista, key=operator.itemgetter(1), reverse=False)
print('lista ordenada por campo2:', listaord)

# Ordenar lista por primer campo de cada tupla (índice 0), 
# orden inverso:

listaord = sorted(lista, key=operator.itemgetter(0), reverse=True)
print('lista ordenada inversa por campo1:', listaord)

# Ordenar alfabéticamente por el primer campo:

listaord = sorted(lista)
print('lista ordenada alfabéticamente:', listaord)

# Leer un archivo con reader() y mostrarlo ordenado por tercer
# campo con la función itemgetter() del módulo operator: 

csvarchivo = csv.reader(open('datos.csv'))
listaordenada = sorted(csvarchivo, 
                       key=operator.itemgetter(2), 
                       reverse=False)
print(listaordenada)

# Leer un archivo csv como lista de diccionarios con DictReader() y
# mostrar sólo datos de algunas columnas:

with open('datos.csv') as csvarchivo:
    entrada = csv.DictReader(csvarchivo)
    for reg in entrada:
        print(reg['provincia'], reg['consumo'])
        
        
# Mostrar lista de diccionarios a partir CSV y 
# consultar número de líneas (registros), dialecto y campos:

csvarchivo = open('datos.csv')
entrada = csv.DictReader(csvarchivo)
listadicc = list(entrada)  # Obtener lista de diccionarios
print('Lista:', listadicc)  # Mostrar lista de diccionarios
print('Líneas:', entrada.line_num)  # Obtener número de registros
print('Dialecto:', entrada.dialect)  # Obtener dialecto
print('Campos:', entrada.fieldnames)  # Obtener nombre de campos
del entrada, listadicc
csvarchivo.close()
del csvarchivo


# Obtener lista ordenada descendente por el campo 'consumo' 
# con la función itemgetter() del módulo operator.

csvarchivo = open('datos.csv')
entrada = csv.DictReader(csvarchivo)
listadicc = list(entrada)  # Obtener lista de diccionarios
listadiccord = sorted(listadicc, 
                      key=operator.itemgetter('consumo'), 
                      reverse=True)
for registro in listadiccord:
    print(registro)

del entrada, listadicc, listadiccord
csvarchivo.close()
del csvarchivo


# Leer con DictReader y escribir datos en otro csv si se 
# cumple condición.
# En el archivo 'salida.csv' se escribirán todos los datos 
# entrecomillaods con dobles comillas y separados entre sí
# con el carácter "|".

with open('datos.csv') as csvarchivo:
    entrada = csv.DictReader(csvarchivo)
    csvsalida = open('salida.csv', 'w', newline='')
    salida = csv.writer(csvsalida, delimiter='|', 
                        quotechar='"', 
                        quoting=csv.QUOTE_ALL)
    print('Escribiendo archivo "salida.csv"...')
    print('Dialecto:', entrada.dialect, '...')
    for reg in entrada:
        if reg['provincia'] != 'Huelva':
            salida.writerow([reg['nom'], 
                             reg['cons']])  # Escribir registro
  
    print('El proceso de escritura ha terminado.')

del entrada, salida, reg
csvsalida.close()
del csvsalida


# Escribir todas las tuplas de una lista con writerows()

datos = [('aaa', 111), ('bbb', 222), ('ccc', 333)]
csvsalida = open('salidat.csv', 'w', newline='')
salida = csv.writer(csvsalida)
salida.writerow(['campo1', 'campo2'])
salida.writerows(datos)
del salida
csvsalida.close()


# Leer archivo ignorando o no los espacios que existan después
# de los delimitadores de campos

# Si la propiedad skipinitialspace es True se ignorarán
# los espacios
# Si la propiedad strict es True se producirá un error si el 
# archivo csv no es válido 

# Leer archivos sin ignorar espacios

with open('archivo.csv') as csvarchivo:
    entrada = csv.reader(csvarchivo, 
                         skipinitialspace=False, 
                         strict=True)
    for reg in entrada:
        print(reg)

# Leer archivos ignorando espacios

with open('archivo.csv') as csvarchivo:
    entrada = csv.reader(csvarchivo, 
                         skipinitialspace=True, 
                         strict=True)
    for reg in entrada:
        print(reg)
        
        
try:
    salidacsv = open('campos.csv', 'w')
    campos = ['Campo1', 'Campo2']
    salida = csv.DictWriter(salidacsv, fieldnames=campos)
    salida.writeheader()
    for indice in range(6):
        salida.writerow({ 'Campo1':indice+1,
                          'Campo2':chr(ord('a') + indice)})
 
    print('Se ha creado el archivo "campos.csv"')

finally:
    salidacsv.close()
    
    
# Leer archivo csv con dialecto 'unix'

with open('salida.csv') as csvarchivo:
    entrada = csv.reader(csvarchivo, 
                         dialect='unix', 
                         delimiter='|')
    for reg in entrada:
        print(reg)
        
        
# Crear nuevo dialecto 'personal' y abrir archivo usándolo.

csv.register_dialect('personal', 
                     delimiter='|', 
                     quotechar='"', 
                     quoting=csv.QUOTE_ALL)
with open('salida.csv') as csvarchivo:
    entrada = csv.reader(csvarchivo, dialect='personal')
    for reg in entrada:
        print(reg)
        
        
#Listar dialectos disponibles

# Listar dialectos

print(csv.list_dialects())


# Obtener información del dialecto "personal"

dialecto = csv.get_dialect('personal')
print('delimiter', dialecto.delimiter)
print('skipinitialspace', dialecto.skipinitialspace)
print('doublequote', dialecto.doublequote)
print('quoting', dialecto.quoting)
print('quotechar', dialecto.quotechar)
print('lineterminator', dialecto.lineterminator)

##Suprimir dialecto

# Suprimir dialecto "personal"

csv.unregister_dialect('personal')
print(csv.list_dialects())  # Listar dialectos después

#####Deducir con Sniffer() el dialecto de un archivo csv

with open('salida.csv') as csvarchivo:
    dialecto = csv.Sniffer().sniff(csvarchivo.read(48))
    csvarchivo.seek(0)
    print("Dialecto:", dialecto)
    csvarchivo.seek(0)
    entrada = csv.reader(csvarchivo, dialecto)
    for reg in entrada:
        print(reg)

#Deducir con Sniffer() si un archivo tiene encabezado

# El archivo salida.csv no tiene encabezado

csvarchivo1 = open('salida.csv')
cabecera1 = csv.Sniffer().has_header(csvarchivo1.read(48))
print("\ncsvarchivo1 (salida.csv) cabecera:", cabecera1)
csvarchivo1.seek(0)
entrada = csv.reader(csvarchivo1, "unix")
for reg in entrada:
    print(reg)

csvarchivo1.close()

# El archivo salidat.csv sí tiene encabezado

csvarchivo2 = open('salidat.csv')
cabecera2 = csv.Sniffer().has_header(csvarchivo2.read(76))
print("\ncsvarchivo2 (salidat.csv) cabecera:", cabecera2)
csvarchivo2.seek(0)
entrada = csv.reader(csvarchivo2, "excel")
for reg in entrada:
    print(reg)

csvarchivo2.close()

#Mostrar/Establecer límite de tamaño de campo a analizar

# Para establecer un nuevo límite: field_size_limit(NuevoLímite)

print(csv.field_size_limit())  


