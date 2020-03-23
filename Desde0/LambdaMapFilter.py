"""Con la palabra clave ‘lambda’ se pueden definir pequeñas funciones anónimas llamadas ‘Funciones lambda’. 
Las funciones lambda son diferentes de las funciones normales de Python, pero pueden ser utilizadas todas 
las veces que se requieran. Están restringidas a una sola expresión y no requieren la palabra clave ‘return’.
Ejemplos de función lambda:"""

f = lambda i : 5 * i
print(f(2))

#Las funciones lambda siempre devuelven algo y pueden contener condicionales en su cuerpo:

f = lambda x: x < 5
print(f(3))  # Devuelve 'True'
print(f(8))  # Devuelve 'False'

#Ejemplo 2:

suma = lambda x,y: x+y
resultado = suma(4,5)
print(resultado)

"""Función map

La función map está definida como map(función, iterable). Esta aplica la función a cada ítem en el iterable. 
Se puede usar map() con una función lambda:"""

lista = [2,4,8,10]
listaCuadrada = map(lambda x: x**2, lista)
print(listaCuadrada)

#Donde sea que se implemente una función lambda, es posible implementar una función normal. Una función lambda
#no es una declaración, es una expresión.

"""Función filter

filter(función, iterable) crea una lista nueva a partir de los elementos para los cuales ‘función’ devuelve ‘True’"""

lista = [1,2,3,4,5,6]
nuevaLista = filter(lambda x: x % 3 == 0, lista)
print(nuevaLista)

#Si se está utilizando Python 3, es necesario agregar una pequeña modificación, ya que ‘filter’ en python 3 
#devuelve un iterable.

lista = [1,2,3,4,5,6]
nuevaLista = list(filter(lambda x: x % 3 == 0, lista)) # 'list()' convierte el iterable
print(nuevaLista)                                      #  generado por 'filter' en una lista

#‘nuevaLista’ contendrá solo los elementos para los cuales ‘lambda x: x % 3 == 0’ devuelva ‘True’ ([3,6]).

"Ejemplo 2:"

lista = ["Alejandra","Juan","Maria","Alfonso"]
nuevaLista = list(filter(lambda x: x[0] == "A", lista))  # 'nuevaLista' tendrá solo los elementos de 'lista'
print(nuevaLista)                                        # que tengan como primer caracter la letra "A"

"Función reduce"

#reduce(función, iterable) aplica dos argumentos a los elementos en el iterable, de izquierda a derecha de forma acumulativa. 
#Ejemplo:

from functools import reduce  # Esto es necesario si se está usando Python 3
lista = [2,4,6,8]
a = reduce(lambda x,y: x-y, list)
print(a)

#En este caso, ya que la función siempre devuelve True, lo que hace es restar todos los números de la lista.