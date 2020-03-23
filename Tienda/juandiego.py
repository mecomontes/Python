import numpy as np

### Cargar, abrir y leer el archivo

f=open('tienda.csv') ### abrir el archivo con los datos
head=f.readline() ### leer la primer fila: el ancabezado
ls=f.readlines() #### LEer las demás lineas del archivo
f.close() ### Cerrar el archivo

### Convertir el archivo de texto a listas

nombre=list()### crer una lista con ceros donde voy a guardar los nombres
cantidad=list()### crer una lista con ceros donde voy a guardar los 
precio=list()### crer una lista con ceros donde voy a guardar los nombres

for l in ls:
    p = l.split(";") ### Cada que hay ; es un elemento nuevo
    Id = int(p[0])## lista con identificación
    nombre.append(p[1])## lista con el nombre
    cantidad.append(int(p[2]))## Lista con cantidades
    precio.append(int(p[3])) ### lista con el precio     
    
### cual es el producto mas costoso y el menos costoso
    
precio_mayor=0

for i in range(len(precio)):
    if precio[i]>precio_mayor:
        precio_mayor=precio[i]
        pos_mayor=i

print('el artículo más costoso es el',nombre[pos_mayor], f'con un costo de {precio_mayor} pesos')

precio_menor=precio_mayor

for i in range(len(precio)):
    if precio[i]<precio_menor:
        precio_menor=precio[i]
        pos_menor=i

print('el artículo más económico es el',nombre[pos_menor], f'con un costo de {precio_menor} pesos')

#### CAntidad de artículos disponibles en total en bodega

cant_total=0

for i in range(len(cantidad)):
    cant_total+=cantidad[i]
    
print(f'la cantidad total de artículos en bodega es {cant_total}')


#### costo toal de los artículos en bodega

costo_total=0

for i in range(len(precio)):
    costo_total+=cantidad[i]*precio[i]
    
print(f'el costo total de los artículos en bodega es de {costo_total} pesos')

### costo promedio de un artíkculo

costos=0

for i in range(len(precio)):
    costos+=precio[i]
    
promedio=costos/len(precio)

print(f'el precio promedio por articulo es de {promedio}')


### agregar un artículo nuevo

print('AGREGAR UN ARTIULO NUEVO')
Nom=input('ingrese el nombre del articulo nuevo: ')
nombre.append(Nom)
Can=int(input('ingrese la cantidad de este articulo: '))
cantidad.append(Can)
Pre=int(input('ingrese el precio del nuevoarticulo: '))
precio.append(Pre)

### borrrar un articulo de la lista

borrar=input('ingrese el articulo que desea eliminar: ')
nombre.remove(borrar)