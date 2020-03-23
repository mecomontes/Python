### EXPRESIONES

2 + 3      # Respuesta: tipo int, valor 5
4 / 0      # Respuesta: error de división por cero
5 + 3 * 2
'5' + '3' * 2
2 ** 10 == 1000 or 2 ** 7 == 100
int("cuarenta")
70/16 + 100/24
200 + 19%
3 < (1024 % 10) < 6
'six' + 'eight'
'six' * 'eight'
float(-int('5') + int('10'))
abs(len('ocho') - len('cinco'))
bool(14) or bool(-20)
float(str(int('5' * 4) / 3)[2])


### SALUDOS

nombre=input('ingrese su nombre: ')
print('hola, ' + nombre)

### CÍRCULO

radio=int(input('ingrese el radio del circulo= '))

import math

perimetro=2*math.pi*radio
area=math.pi*radio**2

print('perimetro = ',perimetro)
print('area = ',area)

### PROMEDIO

uno=int(input('ingrese la primera nota: '))
dos=int(input('ingrese la segunda nota: '))
tres=int(input('ingrese la tercera nota: '))
cuatro=int(input('ingrese la cuarta nota: '))

promedio=(uno+dos+tres+cuatro)/4

print('promedio = ',promedio)


### CONVERSIÓN

cm=int(input('ingrese la longitud en cm: '))
inch=cm/2.54
print('la longitud en pulgadas es: ', inch, 'in')


#### INVERTIR NÚMERO

numero=input('ingrese el numero que desea invertir: ')
invertir=numero[::-1]
print(invertir)


### PITÁGORAS

a=int(input('ingrese la longitud del cateto a = '))
b=int(input('ingrese la longitud del cateto b = '))
c=(a**2+b**2)**0.5
print('el largo de la hipotenusa es ',c)


### HORA

actual=int(input('ingrese la hora actual: '))
incremento=int(input('ingrese el numero de horas a incrementar: '))

futura=actual + incremento

print('la hora futura sera ', futura)

### PARTE DECIMAL Y ENTERA

numero=float(input('ingrese un numero decimal: '))
decimal=numero%1
entera=int(numero)
print('la parte decimal es ',decimal)
print('la parte entera es ',entera)

decimal1=abs(numero-int(numero))
print('la parte decimal por otro metodo es ', decimal1)


## NOTA FALTANTE

nota1=int(input('ingrese la nota 1: '))
nota2=int(input('ingrese la nota 2: '))
notalab=int(input('ingrese la nota del laboratorio: '))

Nc=(nota1+nota2)/2
Nl=notalab
nota3= 3*(3-0.3*Nl)/0.7-nota1-nota2

print('la nota 3 necesaria es ',nota3)

### TIEMPO COCIÓN DEL HUEVO

M=47
p=1.038
c=3.7
K=5.4e-3
Tw=100
Ty=70

T0=int(input('ingrese la temperatura inicial del huevo: '))
t=M**(2/3)*c*p**(1/3)/(K*math.pi**2*(4*math.pi/3)**(2/3))*math.log(0.76*(T0-Tw)/(Ty-Tw))

print('el tiempo de coción debe ser de ',T0, ' segundos')