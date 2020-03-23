#Ejemplo de una división por 0 donde se captura el error y el programa se ejecuta correctamente:

a=float(input('a = '))
b=float(input('b = '))

try:
  f=a/b;
  print('a/b = ',f)
except ZeroDivisionError:
  print (" No se puede dividir por 0")
except:
  print ("Oops! No era válido. Intente nuevamente...")

 

#Ejemplo con la cláusula finally:

def dividir(x, y):
  try:
    result = x / y
  except ZeroDivisionError:
    print ("¡division por cero!")
  else:
    print ("el resultado es", result)
  finally:
    print ("ejecutando la clausula finally")

dividir(a,b)
    
"""Excepciones en python

Tambien hay que tener en cuenta que aunque el programa sea sintácticamente correcto se pueden generar 
errores al ejecutarlo. Estos errores se llaman excepciones. Algunas de las excepciones más comunes son:

ZeroDivisionError: integer division or modulo by zero

Una división mal gestionada

NameError: name ‘pan’ is not defined

La variable pan no esta definida

TypeError: cannot concatenate ‘str’ and ‘int’ objects

No se pueden concatenar string con integer (caracteres con números enteros)

expected an indented block

Normalmente es un error del sangrado

 
Manejar excepciones con try en python

Con la excepciones try podemos capturar errores para que el código no de un error y se pare la ejecución. 
A continuación presentamos los códigos para capturar excepciones y algunos ejemplos:

    try:
    # código para controlar excepciones
    except IOError:
    # entra en caso de una excepción IOError
    except ZeroDivisionError:
    # entra en caso de una excepción ZeroDivisionError
    except:
    # entra en caso de una excepción que no corresponda a ninguno
    # de los except previos"""