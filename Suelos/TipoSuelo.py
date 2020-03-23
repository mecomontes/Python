# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 12:40:35 2018

@author: Diego Medina
"""

#datos de entrada
#este proyecto se compone de varios pasos para lograr el objetivo, 
#en el cual el primer paso sera realizar la grafica de profundidad vs velocidad
#el segundo paso sera calcular los vs30
#y el ultimo paso sera obtener la matriz para poder trabajar en la parte algoritmica 



#llamamos todas las bibliotecas que usaremos para el primer paso
import xlrd
import numpy as np
import matplotlib.pyplot as plt

# llamamos doc al archivo en formato excel donde se encuentran los datos de profundidad y velocidad
doc = xlrd.open_workbook("TipoSuelo.xlsx")
worksheet = doc.sheet_by_name("hoja1")

#llamamos d al numero de filas que tiene el archivo
c= worksheet.nrows
d= c-1

#llamamos e al numero de columnas que tiene el archivo
e= worksheet.ncols

# pasamos los datos del archivo de excel a una matriz la cual se llamamos M
M = np.zeros([d,e])


for i in range (0,d):
 for j in range (0,e):
        M[i,j] = worksheet.cell_value(i+1,j)




# creamos un codigo que nos grafique cada profundidad con su respectivo vs
data = np.array(M)
ncols = data.shape[1]
plt.figure(figsize=(4, 3))
for col in range(ncols//2): 
    plt.plot(data[:, 2*col + 1], -data[:, 2*col])
    plt.ylabel("profundidad (m)")
plt.xlabel("Velocidad (m/s)")
plt.legend()
plt.show()

#for col in range(ncols//2): 
    #plt.plot(data[:, 2*col + 1], -data[:, 2*col])
    #plt.ylabel("profundidad (m)")
    #plt.xlabel("Velocidad (m/s)")
    #plt.legend()
    #plt.show()
   
# paso 2, calcular vs30 de los suelos y clasicacion segun la norma
    
espesores=[]
velocidades=[]
suma=0

for cont in range(1, M.shape[0]):
    espesores.append((M[cont, 0] - M[cont - 1, 0]))
    velocidades.append(M[cont, 1])
    suma+=espesores[cont-1]/velocidades[cont-1]

Vs30=30/suma

print(f'\n Espesores = {espesores}')
print(f'\n Velocidades = {velocidades}')
print(f'\n Vs30 = {Vs30}')

