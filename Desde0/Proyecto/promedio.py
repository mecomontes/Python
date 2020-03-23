
"""Importar desde Subdirectorios

Una práctica muy común a la hora de desarrollar proyectos es la de crear subdirectorios en el directorio 
base con funciones, clases y/u objetos que vayan a ser necesarios en el desarrollo del proyecto. Para 
importar estos en el proyecto base, es necesario que en el directorio principal y en el subdirectorio 
estén presentes los respectivos archivos ‘__init__.py’. Teniendo esto en cuenta, el proceso de importación 
es similar al explicado antes:

Se tiene un programa que dado un numero de estudiantes, sus edades e indices académicos, calcula su promedio 
y lo imprime.

El proyecto está organizado de la siguiente forma:

    Proyecto /
     |-__init__.py
     |-promedios.py
     |-utiles /
         |-__init__.py
         |-funciones.py
         |-clases.py

Los archivos ‘__init__.py’ estarán en blanco. El archivo ‘promedios.py’ tendrá la siguiente estructura:"""

from utiles.clases import Estudiante # Se importa la clase 'Estudiante'
from utiles.funciones import proms # Se importa la función 'proms'
N = int(input("Ingrese la cantidad de estudiantes\n"))
grupo = [ Estudiante() for x in range(0,N) ]
promed = 0.0
promia = 0.0
for i in grupo:
  i.nombre = input("Ingrese el nombre del estudiante (min. 1 caracter)\n")
  i.edad = int(input("Ingrese la edad de %s\n" % i.nombre))
  i.indice = float(input("Ingrese el I.A de %s (entre 1 y 10)\n" % i.nombre))
PROMEDIOS = proms(grupo, N)
print("El promedio de las edades es: %s" % PROMEDIOS[0])
print("El promedio de los I.A. es: %s" % PROMEDIOS[1])

"""El archivo ‘clases.py’ será de la siguiente forma:

    class Estudiante():
      nombre   = ""
      edad   = 0
      indice   = 0.0

El archivo ‘funciones.py’ será de la siguiente forma:

    def proms(A, q):
      '''  Función:
        Calcula los promedios de las edades e indices  
        academicos y los almacena en un arreglo.
      '''
      pred = sum(i.edad for i in A)/q
      pria = sum(i.indice for i in A)/q
      S = [pred, pria]
      return S"""