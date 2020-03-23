##    Sentencias If

#Se usa para tomar desiciones donde se evalua una expression que da como resultado un 
#boolenao (verdadero o falso). Una vez evaluada la expresión se ejecuta el código. Ejemplo:

num= int(input('escribe un numero'))
 
if num<0:
    print(' numero negativo') 
elif num==0:
    print('el numero es 0') 
elif num>0:
    print('el numero es positivo')


f=3
h=2
if (f==h):
    print('los numeros son iguales')
else:
    print('los numeros NO son iguales') 
 
if (f<h):
    print('el numero h es MAYOR que el f')
else:
    print('el numero h NO es MAYOR que el f')
 
if (f>=h):
    print('el numero f es MAYOR o IGUAL que el h')
else:
    print('el numero f NO es MAYOR NI IGUAL que el h')
    

#   Operadores de Lógicos

#  Son los operadores para trabajar con números booleanos:

#  and        ¿se cumple a y b?               r = True and False # r es False

#  or           ¿se cumple a o b?              r = True or False # r es True

#  not         No a                                      r = not True # r es False
    

###           WHILE

#Este ciclo nos permite llevar a cabo múltiples iteraciones analizando una expresión 
#lógica que puede tener un valor verdadero o falso.


# Bucles While controlado por conteo:

print('While controlado por conteo')
print('===============================')
print('Sumador numero hasta 10')
sum=0
num=1
while (sum<=10):
    sum=num+sum
    num=num+1
    print('La suma es ' +str(sum))

 
# While controlado por Evento:

print('While controlado con Evento')
print('===============================')
print('Calcular promedio')
promedio=0.1
total=0
contar=0
print('Escribe el valor (-1 para salir):')
grado=int(input())

while grado !=-1:
    total=total+grado
    contar= contar + 1
    print('Escribe el valor (-1 para salir):')
    grado=int(input())
    
promedio=total/contar
print('El promedio es ' +str(promedio))

 
#  Usando sentencias Break

#Estas sentencias se usan cuando queremos para un ciclo (break) o cuando queremos que un 
#ciclo continue aunque no se haya terminado.

#Ejemplo break:

print('While con sentencia break')
print('===============================')
print('Sumador numero hasta 20')
sum=0
num=0

while (sum<=30):
   sum=num+sum
   num=num+1
   print('El num es ' +str(num))
   if num > 4:
       break
   
print('La suma es ' +str(sum) + ' y no ha llegado a 30 por el break')

#  Usando sentencias Continue

#Ejemplo continue:

print('While con sentencia continue')
print('===============================')
vari=10

while (vari>0):
    vari=vari-1
    if vari== 4:
        print('entra en el continue y la vari es ' +str(vari))
        continue
    print('La vari es ' +str(vari))

 
#   Tipo de bucles for

#Normalmente estos bucles iteran sobre una progresión numérica aunque en Python podemos iterar 
#no solo una progresión numérica sino también una secuencia como una lista o una cadena de texto.

#Bucles for con listas:

#ejemplo 1:

print('for con listas')
print('===============================')
nombre_list=['paco','manu','alonso']
for nombre in nombre_list:
    print('Su nombre es: ', nombre, ' el numero de letras son:', len(nombre))

#ejemplo 2:

a=[1, 2, 3, 4 ,5]
for i in a:
    print('el bucle va por el numero: ',i, 'y la longitud de la lista es: ',len(a))

 
#Bucles for con Tuplas

print('for con tuplas')
print('===============================')
tupla_list=['paco','48989642','madrid','encargado']
for tupla in tupla_list:
    print(tupla)