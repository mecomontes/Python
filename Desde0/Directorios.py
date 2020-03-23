### para crear un directorio en Python con mkdir() sería como el que sigue:

import os
import errno
try:
    os.mkdir('dir1')
except OSError as e:
    if e.errno != errno.EEXIST:
       raise
	   
"""makedirs() es la función que nos permite crear directorios de forma recursiva en Python. 
Es como mkdir(), pero crea todos los directorios intermedios hasta el directorio hoja si no existen.

Pero a partir de la versión 3.2 de Python, a la función makedirs() se le puede pasar el parámetro 
exist_ok para que no se produzca ningún error en caso de que la carpeta ya exista:"""

import os
os.makedirs('dir1/dir2/dir3', exist_ok=True)

##La versión 3.4 de Python añadió el módulo pathlib. Gracias a este módulo, podemos crear directorios de 
##forma recursiva de manera similar a como lo hacemos con makedirs():

from pathlib import Path
path = Path('dir1/dir2/dir3/dir4')
path.mkdir(parents=True,exist_ok=True)

