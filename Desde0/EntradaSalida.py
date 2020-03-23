print ("\nSimulacion de Chat")
print ("=====================")
print ("\nChat ; De 18 a 45 anos")
print ("---------------------------\n")
print ('Menu: ')
nombre = input('Hola ¿cómo te llamás?: ')
print ('Pepe: Hola', nombre, ', encantado de saber tu nombre')
print ('Menu: ')
edad = input('¿cuantos anos tienes?: ')
print ('ok entonces tu tienes', edad, 'y yo tengo edad infinita porque soy un programa en python')
print ('Menu: ')
tiene_WebCam = input('¿Tienes camara? quiero verte, escribeme "si" o "no", ')

if tiene_WebCam in ('s', 'S', 'si', 'Si', 'SI'):
  print ("Pon la camara que tengo ganas de ver como eres")

print('En {0} programar es {1}'.format('AprednerPython.net','simple'))

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
    print(iva1)
    return iva1
print('el iva es:')
iva()
print("Programa terminado")

print (u'El minimo esta en x = %2.3f, y = %2.3f' %(3,2))