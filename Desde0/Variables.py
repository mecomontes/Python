### DATOS CADENA

cadena1 = ('comillas simples')
print (cadena1)
cadena2 = ("comillas dobles")
print (cadena2)
n = "Aprender"
a = "Python"
n_a = n + " " + a
print (n_a)

### DATOS BOOLEANOS: Este es el tipo de variable que solo puede tener Verdadero o Falso. 
#Son valores muy usados en condiciones y bucles. Ejemplo de variable booleana:

aT = True
print ("El valor es Verdadero:", aT, ", el cual es de tipo", type(aT)), "\n"
aF = False
print ("El valor es Falso:", aF, ", el cual es de tipo", type(aF))

##  CONJUNTOS Son una colección de datos sin elementos que se repiten

pla = 'pastelito', 'jamon', 'papa', 'empanadilla', 'mango', 'quesito'
print (pla)

##  


## Listas: Son listas que almacenan vectores (arrays). Estas listas pueden tener diferentes 
#tipos de datos. Ejemplo de listas en Python:

b = ['2.36', 'elefante', 1010, 'rojo']
print (b)
l4 = b[0:3:2]
print(l4)

 
## Tuplas: Es una lista que no se puede modificar después de su creación, es inmodificable:

# Ejemplo simple
tupla = 19645, 59621, 'hola python!'
# Ejemplo tuplas anidadas
otra = tupla, (1, 5, 3, 6, 5)
# operación asignación de valores de una tupla en variables
x, y, z = tupla
print(tupla)
print(otra)
#ejemplo de tupla para una conexión con una base detos
print ("\nConectar a la base de datos MySql")
print ("==============================\n")
conexion_bd = "1546.540.07.18","accesoroot","1gh6","users",
print ("Conexion tipica:", conexion_bd)
print (conexion_bd)
conexion_c = conexion_bd, "3457","19",
print ("\nConexion con estos parametros:", conexion_c)
print (conexion_c)
print ("\n")
print ("Acceder a la IP de la base de datos:", conexion_c[0][0])
print ("Acceder al usuario de la base de datos:", conexion_c[0][1])
print ("Acceder a la clave de la base de datos:", conexion_c[0][2])
print ("Acceder al nombre de la base de datos:", conexion_c[0][3])
print ("Acceder al puerto :", conexion_c[1])
print ("Acceder al tiempo de espera de conexion:", conexion_c[2])

 
## Diccionarios: Define los datos uno a uno entre un campo y un valor, ejemplo:

datos_basicos = {"nombres":"Fran","apellidos":"Pardo Garcia","numero":"145548","fecha_nacimiento":"03111980",
                 "lugar_nacimiento":"Madrid, España","nacionalidad":"Portuguesa","estado_civil":"Casado"}

print ("\nDetalle del diccionario")
print ("=======================\n")
print ("\nClaves del diccionario:", datos_basicos.keys())
print ("\nValores del diccionario:", datos_basicos.values())
print ("\nElementos del diccionario:", datos_basicos.items())
# Ejemplo practico de los diccionarios
print ("\nInscripcion de Curso")
print ("====================")
print ("\nDatos de participante")
print ("---------------------")
print ("Cedula de identidad:", datos_basicos['numero'])
print ("Nombre completo: " + datos_basicos['nombres'] + " " + datos_basicos['apellidos'])

 
## Operadores aritméticos

#Suma +
g= 5+1 # g=6
#Resta –
g= 5-1 # g=4
#Negacion –
g= -5+1 # g=-4
#Multiplicacion *
g= 5*2 # g=10
#Exponente **
g= 5**2 # g=25
#Division /
g= 5/2 # g=2.5
#Division entera //
g= 5//2 # g=2
#Modulo: divide el operando de la izquierda por el operador del lado derecho y devuelve el resto.
g= 7 % 2 # g=1

## Operadores relacionales

""" Estos operadores comparan valores y dan como resultado un valor booleano (es decir un valor Verdadero o Falso):

==     ¿son iguales a y b?                     r = 5 == 3 # r es False

!=      ¿son distintos a y b?                  r = 5 != 3 # r es True

<       ¿es a menor que b?                   r = 5 < 3 # r es False

>      ¿es a mayor que b?                    r = 5 > 3 # r es True

<=    ¿es a menor o igual que b?      r = 5 <= 5 # r es True

>=    ¿es a mayor o igual que b?      r = 5 >= 3 # r es True"""


"""Operadores de asignaciones

Se utilizan para asignar el valor a una variable, parecido a “=”.

    = es el más simple y asignas a la variable izquierda el valor derecho
    += suma a la variable izquierda el valor derecho
    -= restas a la variable izquierda el valor derecho
    \*= multiplicas a la variable izquierda el valor derecho"""
    
num=5
num+=3
print(num)
num-=3
print(num)
num*=3
print(num)
num/=2
print(num)