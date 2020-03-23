dic1 = {'Lorca':'Escritor', 'Goya':'Pintor'} # declara diccionario 
print(dic1) # {'Goya': 'Pintor', 'Lorca': 'Escritor'}
dic2 = dict((('mesa',5), ('silla',10))) # declara a partir de tupla
dic3 = dict(ALM=5, CAD=10) # declara a partir de cadenas simples 
dic4 = dict([(z, z**2) for z in (1, 2, 3)]) # declara a partir patrón
print(dic4)  # muestra {1: 1, 2: 4, 3: 9}
print(dic1['Lorca'])  # escritor, acceso a un valor por clave
print(dic1.get('Gala', 'no existe'))  # acceso a un valor por clave
if 'Lorca' in dic1: print('está')  # comprueba si existe una clave
print(dic1.items())  # obtiene una lista de tuplas clave:valor
print(dic1.keys())  # obtiene una lista de las claves
print(dic1.values())  # obtiene una lista de los valores
dic1['Lorca'] = 'Poeta'  # añade un nuevo par clave:valor
dic1['Amenabar'] = 'Cineasta'  # añade un nuevo par clave:valor
dic1.update({'Carreras' : 'Tenor'})  # añadir con update()
#del(dic1['Amenábar'])  # borra un par clave:valor 

print('1111111')
print(dic1.pop('Amenabar', 'no está'))  # borra par clave:valor
artistas = {'Lorca':'Escritor', 'Goya':'Pintor'} # diccionario
paises = ['Chile','España','Francia','Portugal'] # declara lista
capitales = ['Santiago','Madrid','París','Lisboa']  # declara lista
for c, v in artistas.items(): print(c,':',v)  # recorre diccionario
for i, c in enumerate(paises): print(i,':',c)  # recorre lista 
for p, c in zip(paises, capitales): print(c,' ',p) # recorre listas
for p in reversed(paises): print(p,)  # recorre en orden inverso
for c in sorted(paises): print(c,)  # recorre secuencia ordenada