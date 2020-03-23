"""La siguiente función toma dos parámetros y devuelve como resultado la suma de los mismos:

    def sum(x, y):
        return x + y

Si llamamos a la función con los valores x=2 e y=3, el resultado devuelto será 5.

    >>>sum(2, 3)
    5

Pero, ¿qué ocurre si posteriormente decidimos o nos damos cuenta de que necesitamos sumar un valor más?



La mejor solución, la más elegante y la más al estilo Python es hacer uso de *args en la definición de 
esta función. De este modo, podemos pasar tantos argumentos como queramos. Pero antes de esto, tenemos 
que reimplementar nuestra función sum:

    def sum(*args):
        value = 0
        for n in args:
            value += n
        return value

Con esta nueva implementación, podemos llamar a la función con cualquier número variable de valores:

    >>>sum()
    0
    >>>sum(2, 3)
    5
    >>>sum(2, 3, 4)
    9
    >>>sum(2, 3, 4, 6, 9, 21)
    45"""

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "x: {}, y: {}".format(self.x, self.y)

# Como vemos, en el método __init__ se indican dos parámetros: la coordenada x y la coordenada y 
#de un punto:

"""Punto(1, 2)
    x: 1, y: 2
	
El valor por defecto 0: Para indicar un parámetro de forma opcional se usa el operador ‘=‘. 
Veamos cómo quedaría:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

Ahora podemos invocar a la función del siguiente modo:

    >>>Punto()
    x: 0, y: 0
    >>>Punto(3)
    x: 3, y: 0
	
	"""
	
"""Bucle for en diccionarios

Un caso es especial de bucle for se da al recorrer los elementos de un diccionario. 
Dado que un diccionario está compuesto por pares clave/valor, las distintas formas de
iterar sobre ellos son:"""

valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for k in valores:
   print(valores[k])

### En este caso se recorren las claves del diccionario.

valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for v in valores.values():
    print(v)

###Aquí lo que se itera es sobre los valores de cada clave del diccionario.

valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for k, v in valores.items():
    print('k=', k, ', v=', v)

##En este último caso, iteramos a la vez sobre la clave y el valor de cada uno de los elementos del diccionario.