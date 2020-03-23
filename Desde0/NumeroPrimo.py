
numero= int(input("¿Qué número quieres saber si es primo? "))
valor= range(2,numero)
contador = 0

for n in valor:
  if numero % n == 0:
    contador +=1
    print("divisor:", n)

if contador > 0 :
  print("El número no es primo" )
else:
  print("El nÚmero es primo") 



def primo(num):
 if num < 2: #si es menor de 2 no es primo, devolverá Falso
   return False
 
 for i in range(2, num): #un ciclo desde el 2 hasta el num de entrada
   if num % i == 0: #si el resto da 0 no es primo, devuelve Falso
       return False
   return True #de lo contrario devuelve Verdadero

numero= int(input("¿Qué número quieres saber si es primo? "))
respuesta=primo(numero)
print(respuesta)