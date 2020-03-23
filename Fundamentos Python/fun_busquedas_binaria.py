import random

lista=[]
cantidad_elementos=random.randrange(2,28)

for i in range(cantidad_elementos):
    lista.append(random.randrange(4,200))

buscar=random.choice(lista)
inicio=0
encontrado=0
medio=cantidad_elementos/2

while inicio<=cantidad_elementos and encontrado==0:
    medio=int((inicio+cantidad_elementos)/2)
    if buscar==lista[medio]:
        print(f'el valor {buscar} esta en la posicion {medio}')
        encontrado=1
    elif buscar<lista[medio]:
        cantidad_elementos=medio-1
    else:
        inicio=medio+1    