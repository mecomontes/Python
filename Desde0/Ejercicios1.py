"""Ejercicio Python #01: Define una función llamada menorque() que nos devuelva en pantalla el número 
menor entre dos enteros. Define una salida de texto en caso de que .

Solución ejercicio #01:"""

def menorque(a, b):
    if a > b:
        print ("El menor es b")
    elif b > a:
        print ("El menor es a")
    else: 
        print ("Ambos son iguales")
menorque(1,2)

"""Ejercicio Python #02: Define una función llamada num_max() que nos devuelva en pantalla el número 
mayor entre 4 diferentes enteros. No definas ningún valor a imprimir en caso de que ambos números sean iguales.

Solución ejercicio #02:"""

def num_max (a, b, c):
    if a > b and a > c:
        print (a)
    elif b > a and b > c:
        print (b)
    elif c > a and c > b:
        print (c)
    else:
        print ("Son iguales")
num_max(1,2,3)

"""Ejercicio Python #03: Define una función llamada num_max_min() que nos devuelva en pantalla el número
 mayor y menor entre 3 diferentes enteros. En caso de que todos sean iguales imprime en pantalla un mensaje indicándolo.

Solución ejercicio #03:"""

def num_max_min(a, b, c):
    if a > b and a > c:
        print ("El mayor es", a, "y el menor", c) 
    elif b > a and b > c:
        print ("El mayor es", b, "y el menor", c)
    elif c > a and c > b:
        print ("El mayor es", c, "y el menor", b)
    else:
        print ("Son iguales")
num_max_min(4,2,1)

"""Ejercicio Python #04: Define una función que nos devuelva True si al darle una vocal mayúscula nos devuelva False,
 mientras que si es minúscula sea True.

Solución ejercicio #04:"""

def es_vocal (x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    elif x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return False
es_vocal('e')

"""Ejercicio Python #05: Haciendo uso de la función print consigue un resultado igual al siguiente:

Estoy escribiendo 
             Con espacio 
                      Entre líneas 
                              ¡Gracias al tabulador!

Solución ejercicio #05:"""

print("Estoy escribiendo \n\tCon espacio \n\t\t Entre líneas \n\t\t\t ¡Gracias al tabulador!")

"""Ejercicio Python #06: Define una función simple que no tenga parámetros y sólo imprima en pantalla un mensaje.

Solución ejercicio #06:"""

def sin_parametros():
    print ("¡No tengo parámetros!")
sin_parametros()

"""Ejercicio Python #07: Define una función que permita imprimir un mensaje en base a los valores tomados de 
una lista para comprobar si todos los de la lista son mayores o menores de edad.

Solución ejercicio #07: """

def mayor_menor_edad (lista):
    for i in lista:
        if i > 18:
            print ("Es mayor de edad")
        elif i == 18:
            print ("Apenas tiene la mayoría de edad")
        else:
            print ("Es menor de edad")
mayor_menor_edad([18,21,8,19,5,4,3,8,2,3])

"""Ejercicio Python #08: Define una función que permita multiplicar los números de una lista y sumar sus resultados.

Solución ejercicio #08: """

def multip (lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    print (multiplicacion)
multip([4,2,6])

"""Ejercicio Python #09: Imprime en pantalla la hora y fecha actual.

Solución ejercicio #09:"""

import datetime
now = datetime.datetime.now()
print ("La fecha y hora actual es : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

"""Ejercicio Python #10: Crea un código que solicite ingresar el nombre de un archivo con su extensión
 y devuelva la extensión de la misma. Por ejemplo: La extensión de programando-aprenderpython.py es “.py”.

Solución ejercicio #10:"""

nombrearchivo = input("Ingrese el nombre del archivo: ")
na_extns = nombrearchivo.split(".")
print ("La extensión del archivo es : " + repr(na_extns[-1]))