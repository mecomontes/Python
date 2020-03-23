### CANTIDAD DE DÍGITOS

numero=input('ingrese el numero a evaluar: ')
digitos=len(numero)
print('el número ', numero, ' tiene ',digitos, ' dígitos')

### DÍGITO VERIFICADOR

numero=input('ingrese el el rol UTFSM a evaluar: ')
invertir=numero[::-1]
n=len(invertir)
cont=0
suma=0

for i in range(1,n+1):
        
    if i%7==0:
        cont=cont+1
    
    multi=i+1-6*cont
    suma=suma+multi*int(invertir[i-1])
    
verificador=11-suma%11
numero=numero+'-'+str(verificador)
print(numero)

#### ECUACION PRIMER GRADO

a=int(input('ingrese el valor de a: '))
b=int(input('ingrese el valor de b: '))

if a==0 and b!=0:
    print('no tiene solución')
elif a==0 and b==0:
    print('no hay solución única')
else:
    print('la solución es x = ',b/a)
    
### MEDIA ARMÓNICA

n=int(input('ingrese la cantidad de números a evaluar: '))
suma=0
for i in range(n):
     numero=int(input('ingerese el valor: '))
     suma=suma+1/numero

media=n/suma
print('la media armónica es ',media)


### NÚMERO PALÍNDROMO

numero=input('ingrese un número a evaluar: ')
invertir=numero[::-1]

if numero==invertir:
    print('el número es palíndromo')
else:
    print('el número NO es palíndromo')
    
### PALABRA PALÍNDROMA
    
palabra=input('ingrese un número a evaluar: ')
invertir=palabra[::-1]

if palabra==invertir:
    print('la palabra es palíndromo')
else:
    print('la palabra NO es palíndromo')
    
### PIEDRA, PAPEL O TIJERA

marcaA=0
marcaB=0
print('\n JUGUEMOS PIEDRA, PAPEL O TIJERA \n INGRESE SU OPCIÓN EN MAYÚSCULA \n PI: PIEDRA \n PA: PAPEL \n TI: TIJERA')

while marcaA<3 and marcaB<3:
    A=input('ingrese la opcion para A: ')
    B=input('ingrese la opcion para B: ')
    
    if A=='PI' and B=='TI':
        marcaA=marcaA+1
        print('GANA A   A: ',marcaA,'   B: ', marcaB)
    elif A=='TI' and B=='PA':
        marcaA=marcaA+1
        print('GANA A   A: ',marcaA,'   B: ', marcaB)
    elif A=='PA' and B=='PI':
        marcaA=marcaA+1
        print('GANA A   A: ',marcaA,'   B: ', marcaB)
    elif B=='PI' and A=='TI':
        marcaB=marcaB+1
        print('GANA B   A: ',marcaA,'   B: ', marcaB)
    elif B=='TI' and A=='PA':
        marcaB=marcaB+1
        print('GANA B   A: ',marcaA,'   B: ', marcaB)
    elif B=='PA' and A=='PI':
        marcaB=marcaB+1
        print('GANA B   A: ',marcaA,'   B: ', marcaB)
    elif A==B:
        print('EMPÁTE   A: ',marcaA,'   B: ', marcaB)
    else:
        print('Opción inválida')

if marcaA==3:
    print('el gaador absoluto es A')
elif marcaB==3:
    print('el gaador absoluto es B')

### NÚMEROS PRIMOS

n=int(input('ingrese el numero a evaluar: '))
cont=0

for i in range(n):
    if n%(i+1)==0:
        cont=cont+1

if cont==2:
    print('el numero es primo')
else:
    print('el numero es compuesto')

### INTERSECCIÓN DE CIRCUNFERENCIAS
    
print('ingrese el centro y radio de la circunferencia 1')
x1=int(input('X1 = '))
y1=int(input('Y1 = '))
r1=int(input('R1 = '))

print('ingrese el centro y radio de la circunferencia 2')
x2=int(input('X2 = '))
y2=int(input('Y2 = '))
r2=int(input('R2 = '))

Dcentros=((x1-x2)**2+(y1-y2)**2)**0.5
Dradios=r1+r2

if Dradios<Dcentros:
    print('las circunferencias no son secantes')
elif Dradios>Dcentros:
    print('las circunferencias son secantes')
elif Dradios==Dcentros:
    print('las circunferencias son tangentes')