# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 11:24:56 2018

@author: andre
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:30:41 2018

@author: andre
"""

import numpy as np

 ### calcular factorial

def funcion_factorial(n):
    if n<0:
        factorial=0
        
    elif n==0:
        factorial=1
        
    elif n>0:
        factorial = 1
        for i in range(1,n+1):
            factorial=factorial*i
            
    return factorial

### elevar a un número

def funcion_elevado(n,Radianes):    
    if n<0:
        elevado=0
        
    elif n==0:
        elevado=1
        
    elif n>0:
        elevado=1        
        for i in range(1,n+1):
            elevado = elevado*Radianes
            
    print(elevado)

def funcion_datos():
    Grados=float(input('Ingrese el ángulo en grados = '))
    N=int(input('ingrese el valor de n = '))
    Radianes=Grados*np.pi/180
    
    return Radianes,N

Radianes,N=funcion_datos()    

suma=0
for j in range(N):
    n=2*j+1   
    suma = suma + ((-1)**j)*funcion_elevado(n,Radianes)/funcion_factorial(n)
    
print('el resultado del seno es = ',suma)

exacto=np.sin(Radianes)
print('el valor real del seno es = ',exacto)