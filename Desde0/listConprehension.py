"""Qué son las list comprehensions

Básicamente son una forma de crear listas de una manera elegante simplificando el
 código al máximo. Como lo oyes, Python define una estructura que permite crear listas 
 de un modo un tanto especial. Te lo mostraré con un ejemplo:"""

numeros = [1, 2, 34, 86, 4, 5, 99, 890, 45]
pares = []
for num in numeros:
    if num % 2 == 0:
       pares.append(num)
print('numeros pares: ',pares)

"""El código anterior crea una lista de números pares a partir de una lista de números.
Para este tipo de situaciones es ideal el uso de las list comprehensions. El código 
anterior se puede modificar de la siguiente manera con la sintaxis de las list comprehensions:"""

pares = [num for num in numeros if num % 2 == 0]
print('numeros pares: ',pares)

"""Cómo se usan las list comprehensions

La estructura de las list comprehensions es la siguiente:

    [   expresion(i)   for i in list   if condición   ]

Es decir, entre corchetes definimos una expresión seguida de un bucle for al que opcionalmente
le pueden seguir otros bucles for y/o una condición.

❗️El resultado siempre es una lista.

El código anterior es similar al siguiente:

    nueva_lista = []
    for i in list:
        if condición:
            nueva_lista.append(expresion(i))

Ejemplos de uso de list comprehensions

A continuación te muestro diferentes formas de aplicar lo aprendido aunque ejemplos hay miles:"""

### Capitalizar las palabras de una lista

palabras = ['casa', 'perro', 'puerta', 'pizza']
cap = [palabra.title() for palabra in palabras]
print('Capitalizar palabras: ',cap)

### Calcular los cuadrados del 0 al 9

cuadrados = [num**2 for num in range(10)]
print('cuadrados: ',cuadrados)

###Calcular los cuadrados del 0 al 9 de los números pares

cuadrados_pares = [num**2 for num in range(10) if num % 2 == 0]
print('cuadrado de los pares: ',cuadrados_pares)

### Listar los ficheros python del directorio actual que comienzan por ‘f’

import os
ficheros_python = [f for f in os.listdir('.') if f.endswith('.py') and f.startswith('f')]
print('ficheros python: ',ficheros_python)

### Número, doble y cuadrado de los números del 0 al 9

num_doble_cuadrado = [(num, num*2, num**2) for num in range(10)]
print(f'numero {0}, doble {1}, cuadrado{2}',num_doble_cuadrado)

### Ejemplo de doble bucle for

saludos = ['hola', 'saludos', 'hi']
nombres = ['j2logo', 'antonio', 'vega']
frases = ['{} {}'.format(saludo.title(), nombre.title()) for saludo in saludos for nombre in nombres]
print('frases: ',frases)

