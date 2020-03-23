#### punto 1

import random as rd

n=2
i=0
valores=[]####crea la lista valores vacia para ingresar cuantos valores ean necesarios

while n!=0:
    #n=int(input('Ingrese un valor entero o 0 para finalizar: '))
    n=rd.randint(0,100)
    valores.append(n)###agrega valores n en la lista al final de ella
    
valores.remove(0)##3remueve el 0 de la lista
valores.sort()###organiza la lista en forma ascendente

print(valores)##imprime la lista

for i in range(len(valores)):####imprime cada valor de la lista en un renglon diferente
    print(valores[i])
    
valores.reverse()##ordena la lista en forma descendente
for i in range(len(valores)):
    print(valores[i])
    
print('el maximo es ',max(valores))##muestra el valor maximo de la lista
print('el minimo es ',min(valores))###muestra el valor minimo de la lista
sin_repetir=list(set(valores))## crea una nueva lista sin valores repetidos
print(sin_repetir,end='')
print()    
print(rd.choice(['cara','sello']))
print(rd.randrange(100))

#### punto 2
    
