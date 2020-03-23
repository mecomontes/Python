### MÚLTIPLOS

n=int(input('ingrese el número para entregar sus múltiplos: '))

for i in range(11):
    print(n, ' x ', i, '=', n*i)
    
### POTENCIAS DE DOS

n=int(input('ingrese el número para generar las potencias: '))

for i in range(n):
    potencia=2**i
    print(potencia, end=' ')
    
### SUMA ENTRE DOS NÚMEROS

a=int(input('ingrese el valor inferior a: '))
b=int(input('ingrese el valor inferior b: '))
suma=0
cont=a

while cont<b-1:
    cont=cont+1
    suma=suma+cont

print('la suma es ',suma)

### TABLA DE MULTIPLICAR

for i in range(1,10):
    for j in range(1,10):
        print(' ', i*j, end=' ')
    print()  

### DIVISORES DE UN NÚMERO
    
n=int(input('ingrese el número para hallarle los divisores: '))

for i in range(1,n):
    if n%i==0:
        print(i, end='  ')
    
### TIEMPO DE VIAJE
        
tramo=2
cont=0
tiempo=0

while tramo!=0:
    cont=cont+1
    promp='duración tramo ' + str(cont) + ': '
    tramo=int(input(promp))
    tiempo=tiempo+tramo

horas=int(tiempo/60)
minutos=tiempo%60

print('su tiempo total de viaje fue ', horas, ':', minutos)

### print('DIBUJEMOS CON ASTERÍSCOS')
print('\n 1. rectángulo \n 2. triángulo \n 3. hexágono')

tipo=int(input('ingrese el tipo de figura que desea aficar: '))

if tipo==1:
    a=int(input('ingrese el ancho del rectángulo: '))
    b=int(input('ingrese el alto del rectángulo: '))
    
    for i in range(b):
        for j in range(a):
            print('*',end=' ')
        print()
        
elif tipo==2:
    l=int(input('ingrese la longitud de los lados del triángulo: '))
    
    for i in range(l+1):
        for j in range(i):
            print('*',end=' ')
        print()
        
elif tipo==3:
    l=int(input('ingrese la longitud de los lados del hexágono: '))
    
    for i in range(l):
        for p in range(l-i):
            print(end=' ')
        for j in range(l+i):
            print('*',end=' ')
        print()
    
    for i in range(l-1):
        for p in range(i+2):
            print(end=' ')
        for j in range(2*l-i-2):
            print('*',end=' ')
        print()
else:
    print('opción inválida, inténtalo de nuevo')
    
### NÚMERO PI
    
n=int(input('ingrese el número de términos n: '))

suma=0

for i in range(n):
    suma=suma+(-1)**i/(2*i+1)

print('la aproximación del número pi es ', 4*suma)

### SUMA DE FRACCIONES

n=int(input('ingrese el número de términos n: '))

suma=0

print('\n potencia','       fracción', '       Suma')

for i in range(1,n+1):
    fraccion=1/(2*i)
    suma=suma+fraccion
    print(repr(i).center(11),repr(round(fraccion,6)).center(17),repr(round(suma,6)).center(11))   
    
### NÚMERO e
    
from math import factorial

n=int(input('ingrese el número de términos n: '))

suma=0

for i in range(n):
    suma=suma+1/factorial(i)

print('la aproximación del número e es ', suma)  

### SECUENCIA DE COLLATZ

n=int(input('ingrese el nÃºmero: '))

print(n,end=' ')

while n!=1:
    if n%2==0:
        n=int(n/2)
        print(n, end=' ')
    else:
        n=int(3*n+1)
        print(n, end=' ')
    
   