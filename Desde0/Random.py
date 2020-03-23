#funcionamiento de este módulo al generar 10 números escogidos aleatoriamente entre el 0 y el 100.

import random
for x in range(10): 
    print (random.randint(1,101))
    
#Funciones aleatorias y Ejemplos de números aleatorio en Python
#El módulo Random contiene algunas funciones que resultan ser muy útiles:

#   Randint: Si deseas usar un número entero elegido de forma aleatoria dentro de un rango de números 
#(del 1 al 10, por ejemplo), puedes usar la función llamada randint. Esta práctica función acepta dos 
#parámetros en su estructura: un número más bajo, y un número más alto.

import random
print (random.randint(10,30))

#El resultado en consola de este ejemplo, será un número aleatorio comprendido entre el 10 y el 30.

#Random: Si quieres un número mayor, puedes multiplicarlo. Por ejemplo, un número aleatorio entre 0 y 1000:

import random
print (random.random()*1000)

#Choice: Si utilizas la función choice generarás un valor aleatorio partiendo de una secuencia. 
#Esta función de selección es la mas usada si necesitamos elegir un elemento al azar de cualquier 
#lista en Python. Aquí tienes un ejemplo:

import random
color=random.choice( ['rojo', 'amarillo', 'verde'])
print(color)

#La salida que obtendrás en consola de este código, será la elección al azar de uno de estos colores.

#Shuffle: Con la función Shuffle, o barajar, vas a “barajar” o cambiar de posición aleatoriamente 
#los elementos de una lista cualquiera.

import random
s=list(range(15))
random.shuffle(s)
print(s)

#En la salida por consola verás los números del 0 al 15 en posiciones aleatorias, por ejemplo, quizá verás 
#al número 1 en la posición del número 13, entre otros. Pero te aseguro que difícilmente se te mostraran
# en su posición lógica o convencional.

#Randrange: Con Randrange vas a generar un elemento seleccionado aleatoriamente desde su comienzo partiendo
# de un rango (inicio, parada, paso).

#random.randrange(comienzo, parada, paso)

import random
print(random.randrange(0,50,2))

#La salida por consola será un número aleatorio desde 0 a 50 y con un paso de 2.

#Igualmente aquí te dejo abajo otro ejemplo de la función Randrage

import random
# Rango simple 0 <= r < 6
print (random.randrange(6)), (random.randrange(6))
# Rango más complejo 1 <= r < 7
print (random.randrange(1,7)), (random.randrange(1,7))
# Rango realmente complejo de números pares entre 2 y 36
print (random.randrange(2,37,2))
# Números impares del 1 al 35
print(random.randrange(1,36,2))

#Sample: La función sample () se usa para obtener una muestra de la secuencia (cadena, lista, tupla).
#Sintaxis
#random.sample (secuencia, longitud) La
#secuencia puede ser una cadena, lista o
#longitud de tupla. Especifique la longitud de la muestra que se obtendrá.

#Ejemplo:

import random
str1 = "L4wisdom.com"
list1= ['a','b','c','d','e','f','o','l']
print (random.sample(str1,4))
print (random.sample(str1, len(str1)))
print (random.sample(str1,4))
print (random.sample(str1, len(str1)))

#La función sample () devuelve la lista de muestras, independientemente de la entrada que se dé. 
#La función sample () se puede usar como mezcla, si la longitud es igual a len (secuencia).

#seed(): Cuando interese obtener varias veces la misma secuencia de números pseudoaleatoria se 
#puede utilizar la función seed() que fija mediante una “semilla” el mismo comienzo en cada secuencia, 
#permitiendo con ello obtener series con los mismos valores.

#A continuación, se muestra un ejemplo donde se realizan tres series de seis sorteos; y en cada serie 
#se obtienen los mismos regalos y en el mismo orden.

#La semilla en este caso se fija con un valor numérico (0 en este caso) pero también se puede utilizar
# una cadena o una unidad de tiempo obtenida con la función time() del módulo time; o incluso puede 
#expresarse con cualquier objeto “hashable” de Python.

import random
regalos = ['Hojas', 'Almohadas', 'iPhone', 'Cocina', 'Puerta',
'Tablet', 'Llavero', 'Zapatos', 'Automovil', 'Bolso']
for serie in range(3):
    print('\nserie:', serie + 1)
    random.seed(0)
for sorteo in range(6):
    regalo = regalos[random.randint(0, 9)]
    print('Sorteo', sorteo + 1, ':', regalo)