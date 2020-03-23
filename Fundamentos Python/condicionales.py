### PAR O IMPAR

numero=int(input('ingrese un numero: '))
if numero%2==0:
    print('el numero es par')
else:
    print('el numero es impar')
        
    
#### AÑO BISIESTO
    
    year=int(input('ingrese el año: '))
    if (year-1582)/4==0:
        print('el año es bisieto')
    else:
        print('el año no es bisieto')
        
### DIVISIÓN EXACTA?
        
N1=int(input('ingrese el numerador: '))
N2=int(input('ingrese el denominador: '))
division=N1/N2

if N1%N2==0:
    print('la division es exacta')
else:
    print('la division no es exacta')
    
### PALABRA MÁS LARGA
    
palabra1=len(input('ingrese la primer palabra: '))
palabra2=len(input('ingrese la segunda palabra: '))

if palabra1<palabra2:
    print('la segunda palabra es mas larga que la primera por ',palabra2-palabra1,' palabras')
elif palabra1>palabra2:
    print('la primera palabra es mas larga que la segunda por ',palabra1-palabra2,' palabras')
else:
    print('la segunda palabra es igual a la primera ')

### DETERMINAR MAYOR
    
n1=int(input('ingrese el primer numero: '))  
n2=int(input('ingrese el segundo numero: '))  
n3=int(input('ingrese el tercero numero: '))  
n4=int(input('ingrese el cuarto numero: '))    

mayor=0
if n1>mayor:
    mayor=n1
elif n2>mayor:
    mayor=n2
elif n3>mayor:
    mayor=n3
elif n4>mayor:
    mayor=n4

### NÚMERO, LETRA O SÍMBOLO
    
caracter=input('ingrese el caracter a evaluar: ')

if caracter in '0123456789':
    print('el caracter ingresado es el numero ' + caracter)

elif caracter in 'abcdefghijklmnopqrstuvwxyz':
    print('el caracter es la letra '+ caracter + ' en minuscula')

elif caracter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print("EL CARACTER ES LA LETRA " + caracter + " en MAYUSCULA")
else:
    print("no es ni numero ni letra, es el simbolo " + caracter)
    

## CALCULADORA
    
n1=int(input('ingrese el primer numero: '))  
op=input('ingrese el operador: ')  
n2=int(input('ingrese el segundo numero: ')) 

if op=='+':
    print('el resultado es: ',n1+n2)
elif op=='-':
    print('el resultado es: ',n1-n2)
elif op=='*':
    print('el resultado es: ',n1*n2)
elif op=='/':
    print('el resultado es: ',n1/n2)    
    
## DETERMINAR EDAD
    
from time import localtime
t = localtime()
dia=t.tm_mday
mes=t.tm_mon
año=t.tm_year

añon=int(input('ingrese el año de nacimiento: '))
mesn=int(input('ingrese el mes de nacimiento: '))
dian=int(input('ingrese el dia de nacimiento: '))

edad=año-añon

if mesn>mes:
    edad=edad-1
elif mesn==mes and dian>dia:
    edad=edad-1
    
print('su edad es ', edad, ' años')


### SET DE TENIS

marcadores=int(input('ingrese la cantidad de marcadores a verificar: '))
cont=1

while cont<=marcadores:
    cont=cont+1
    m=int(input('ingrese numero de juegos ganados por A:' ))
    n=int(input('ingrese numero de juegos ganados por B:' ))
    
    if m>7 or n>7:
        print('marcador invalido')
    elif m<6 and n<6:
        print('el juego aun notermina')
    elif m==7 and (n==5 or n==6):
        print('el ganador del set es el jugador A')
    elif n==7 and (m==5 or m==6):
        print('el ganador del set es el jugador B')
    elif n==6 and m<5:
        print('el ganador del set es el jugador B')
    elif m==6 and n<5:
        print('el ganador del set es el jugador A')
    else:
         print('marcador invalido')
         
### TIPO DE TRIÁNGULO

a=int(input('ingrese la medida del lado a: ')) 
b=int(input('ingrese la medida del lado b: ')) 
c=int(input('ingrese la medida del lado c: '))  

if a+b>c and a+c>b and b+c>a:
    if a==b or a==c or b==c:
        print('el triángulo es isosceles')
    elif a==b and b==c and a==c:
        print('el triángulo es equilátero')
    else:
        print('el triángulo es escaleno')
else:
    print('no es un triángulo válido')       

### ÍNDICE DE MASA CORPORAL
    
masa=int(input('ingrese su masa corporal en Kg: '))
talla=int(input('ingrese su talla en metros: '))
edad=int(input('ingrese su edad en años: '))

IMC=masa/talla**2

if IMC<22 and edad<45:
    print('su riesgo de sufrir enfermedades coronarias es bajo')
elif IMC<22 and edad>=45:
    print('su riesgo de sufrir enfermedades coronarias es medio')
elif IMC>=22 and edad<45:
    print('su riesgo de sufrir enfermedades coronarias es medio')
if IMC>=22 and edad>=45:
    print('su riesgo de sufrir enfermedades coronarias es alto')