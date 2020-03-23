### EXCLUYENDO MÚLTIPLOS DE 3 Y 7

n=int(input('ingrese el número n: '))

for i in range(n+1):
    
    if i%3!=0:
        if i%7!=0:
            print(i)
            
### SUMA DE NÚMEROS NATURALES
    
n=int(input('ingrese el número n: '))  

suma1=0

for i in range(n+1):
    suma1=suma1+i

suma2=n*(n+1)/2

if suma1==suma2:
    print('S1 es igual a S2 \n S1={0} \n S2={1}'.format(suma1,suma2))


### BUSCANDO EL MAYOR

n=int(input('ingrese la cantidad n: ')) 
mayor=0

for i in range(n): 
    promp='ingrese el número ' + str(i+1) + ':'
    número=int(input(promp))  
    
    if número>mayor:
        mayor=número

print('\n el número mayor es el ',mayor)

### PRODUCTOS ESPECIALES

print('\n QUE DESEAS CALCULAR?')
print('\n 1. FACTORIAL \n 2. POTENCIA FACTORIAL \n 3. COEFICIENTE BINOMIAL \n 4. NÚMERO STIRLING')

tipo=int(input('ingrese la opción deseada: ')) 

def factorialfun(n):
    factor1=1
    for i in range(n):
            factor1=factor1*(i+1)
    return factor1
    
def potenciafactorial(n):
    factor2=1
    
    for i in range(n):
        factor2=factor2*(n+i)
    return factor2

if tipo==1:
    n=int(input('ingrese el número n: '))
    
    if n==0:
        print('el factorial de 0 es 1')
    else:
        factor1=factorialfun(n)
        print('el factorial de ', n, ' es ',factor1)
        
elif tipo==2:
    n=int(input('ingrese el número n: '))
    factor2=potenciafactorial(n)
    print('la portencia factorial de ', n, ' es ',factor2)
    
elif tipo==3:
    
    n=int(input('ingrese el número n: '))
    k=int(input('ingrese el número k: '))
    
    coef=factorialfun(n)/(factorialfun(n-k)*factorialfun(k))
    
    print('el coeficiente binomial es ',coef)
        
elif tipo==4:
    n=int(input('ingrese el número n: '))
    k=int(input('ingrese el número k: '))
    
    suma=0
    
    for i in range(k):
        coef=factorialfun(k)/(factorialfun(k-i)*factorialfun(i))
        suma=suma+(-1)**i*coef*(k-i)**n
        
    print('el número de Stirling es ',suma/factorialfun(k))
    
else:
    print('opción inválida, inténtalo nevamente') 
    
### COMBINACIONES DE DADOS
    
n=int(input('ingrese el puntaje deseado: '))

if n==2:
    print('hay 1 cobinación posible para obtener el ',n)
elif n==3:
    print('hay 2 cobinación posible para obtener el ',n)
elif n==4:
    print('hay 3 cobinación posible para obtener el ',n)
elif n==5:
    print('hay 4 cobinación posible para obtener el ',n)
elif n==6:
    print('hay 5 cobinación posible para obtener el ',n)
elif n==7:
    print('hay 6 cobinación posible para obtener el ',n)
elif n==8:
    print('hay 5 cobinación posible para obtener el ',n)
elif n==9:
    print('hay 4 cobinación posible para obtener el ',n)
elif n==10:
    print('hay 3 cobinación posible para obtener el ',n)
elif n==11:
    print('hay 2 cobinación posible para obtener el ',n)
elif n==12:
    print('hay 1 cobinación posible para obtener el ',n)
else:
    print('hay 0 cobinación posible para obtener el ',n)
    
### HISTOGRAMA
    
n=1
contp=0
contn=0

while n!=0:
    n=int(input('ingrese un número: '))  
    if n>0:
        contp=contp+1
    elif n<0:
        contn=contn+1

print('\n positivos: ', end=' ')
for i in range(contp):
    print('*', end=' ')

print('\n negativos: ', end=' ')
for i in range(contn):
    print('*', end=' ')
    
### MÁS LARGA, MÁS CORTA
    
n=int(input('ingrese un número de palabras a comparar: ')) 
mayor=0
menor=10**10

for i in range(n):
    palabra=input('ingrese la palabra: ')
    if len(palabra)<menor:
        menor=len(palabra)
        menorp=palabra
    if len(palabra)>mayor:
        mayor=len(palabra)
        mayorp=palabra

print('la mayor palabar es '+ mayorp + ' con ', mayor, ' palabras')
print('la menor palabar es '+ menorp + ' con ', menor, ' palabras') 

### PUNTOS DEL DOMINÓ

suma=0

for i in range(7):
    for j in range(7-i):
        suma=suma+i+j
        
print('la cantidad de puntos en un dominó son ',suma, ' puntos')

### LANZAR DADOS

for i in range(6):
    for j in range(6):
        print(i+1,'   ',j+1)
    print('\n')