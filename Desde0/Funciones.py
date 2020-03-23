#Funciones: Una función no es un conjunto de líneas de código que realizan una tarea. Las funciones 
#se utilizan para dividir un código en tareas más sencillas, por partes, de esta manera el código 
#es más legible y fácil de entender. Las funciones empiezan por def nombre_funcion(parámetros): 

def iva():
  total=int( input('cuanto has gastado'))
  num=int( input('que tipo de producto has comprado 1)leche 2)pan 3)alcohol 4)otros'))
  if num==1:
    iv=6
  elif num==2:
    iv=8
  elif num==3:
    iv=14
  else:
    iv=9
  iva1=(total*iv/100)
  print('el impuesto de ese producto es:')
  print(iva1)
  return iva1
iva()
print("Programa terminado")

#Funciones con 2 argumentos:
#Esta función de 2 argumentos calcula la media:

def calcula_media(x, y):
  resultado = (x + y) / 2
  return resultado
a = 3
b = 5
media = calcula_media(a, b)
print("La media es:")
print(media)
print("Programa terminado")

 
#Funciones con argumento múltiples:
#Esta función calcula la media de todos los argumentos que quieras:

def calcula_media(*args):
  total = 0
  for i in args:
    total += i
    resultado = total / len(args)
  return resultado
a, b, c, d, e = 3, 5, 10, 15, 160
media = calcula_media(a, b, c, d, e)
print("La media es:")
print(media)
print("Programa terminado")

#Funcion recursiva
#Ya conocemos que las funciones pueden llamar a otras funciones, pero ¿que pasa si la función se
#llama a si misma? Pues lo que tenemos es una función recursiva. Ejemplo de función recursiva en Python:

def fun_fact(x):
 if x==1:
   return 1
 else:
   x=(x*fun_fact(x-1))
 return x
num=10
print('El factorial de ', num, 'es ',fun_fact(num))

#Compresión de listas e Iteradores
#Vamos a realizar algunos ejemplos con listas para mejorar su compresión y para que podáis 
#ver la flexibilidad del uso de las mismas. Ejemplo de listas e iteradores en python:

lista=[1,2,3,4,-2,5]
lista2=[num for num in lista if num>0]
print (lista)
print (lista2)

#Aquí podemos ver como también podemos hacer  for anidados o también if como hicimos en el artículo
#de Sentencias IF y los bucles WHILE y FOR

 
#Usando ‘iter’ y ‘next’
#En el siguiente ejemplo podemos ver el uso de iter y next de manera simple:

# definimos una lista
my_list = [4, 3, 8, 9]
# añadimos el iterador a la lista
my_iter = iter(my_list)  ###lista a iterar
# ahora podemos iterar con el commando next
print(next(my_iter ))## recorre la lista iterada

#   Decoradores en Python
#La función de un decorador en Python es añadir una funcionalidad nueva a una función. Ejemplo de
# un decorador haciendo una resta:

def decorador(funcion):
 def funcionDecorada(*args, **kwargs):
   print('Funcion ejecutada')
   funcion(*args,**kwargs) 
 return funcionDecorada 
 
def resta(n,m):
 print (n-m)
 
decorador(resta)(5,2) 

#Depurar (debug) en Anaconda – Spyder 
#La depuración del código de un programa tiene como objetivo encontrar los errores que pueda 
#tener al ejecutarlo, creando puntos de quiebre para detener la ejecución, examinando cada variable 
#en el momento que son utilizadas y cambiar sus valores mientras se detiene la ejecución del programa.

#Aquí te mostraremos paso a paso cómo usar el depurador de Python en la herramienta Spyder de Anaconda. 
#Depurando un programa sencillo con un bucle while.

#Paso 1: Para empezar utilizaremos este código de ejemplo:

contador = 0
acumulador = 0
while contador < 10:
    acumulador += contador
    contador+=1
    print(acumulador)