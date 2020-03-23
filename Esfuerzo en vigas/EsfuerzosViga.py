# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 09:37:03 2018

@author: andre
"""

import numpy as np #importar la librería numérica de Python
import pylab as pl #Importar la librería para generar graficas

h=1 # Altura de la viga en metros
L=10 #Longitud de la viga en metros

def graficar(n,X,Y,S):
    pl.figure(n,dpi=100)
    pl.contourf(X,Y,S,cmap='nipy_spectral',alpha=0.85)
    pl.colorbar()
    pl.contour(X,Y,S,linewidths=2.5,colors='black')
    pl.xlabel('Longitud de la viga: L [m]')
    pl.ylabel('Altura de la viga: h [m]')
    if n==1:
        titulo='Distribución de esfuerzos Sxx/F'
    elif n==2:
        titulo='Distribución de esfuerzos Sxy/F'
    elif n==3:
        titulo='Distribución de esfuerzos Syy/F'
    
    pl.title(titulo)

x=np.linspace(0,L,1000)
y=np.linspace(-h/2,h/2,1000)
X,Y=pl.meshgrid(x,y)

Sxx=12*X*Y/h**3
graficar(1,X,Y,Sxx)

Sxy=3/2*h-6*Y**2/h**3
graficar(2,X,Y,Sxy)

Syy=0*X
graficar(3,X,Y,Syy)