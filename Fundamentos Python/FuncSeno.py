# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:30:41 2018

@author: andre
"""

import numpy as np

Grados=float(input('Ingrese el ángulo en grados = '))
N=int(input('ingrese el valor de n = '))
Radianes=Grados*np.pi/180 #numeral a
suma=0

for j in range(N):
    n=2*j+1
    
    ### calcular factorial

    if n<0:
        factorial=0
        
    elif n==0:
        factorial=1
        
    elif n>0:
        factorial = 1
        for i in range(1,n+1):
            factorial=factorial*i
    
    ### elevar a un número
    
    if n<0:
        elevado=0
        
    elif n==0:
        elevado=1
        
    elif n>0:
        elevado=1        
        for i in range(1,n+1):
            elevado = elevado*Radianes
    
    suma = suma + ((-1)**j)*elevado/factorial

    
print('el resultado del seno es = ',suma)

exacto=np.sin(Radianes)
print('el valor real del seno es = ',exacto)