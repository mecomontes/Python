"""Numpy para cargar un archivo de datos y lo mostramos

Cargamos los datos del archivo.txt en este caso el delimitador es la coma.

    archivoDatos=np.loadtxt('C:\ruta\archivoDatos.txt', delimiter = ',')

Arrays con Numpy

*los arrays son vectores en inglés

    ndarray.ndim –> Proporciona el número de dimensiones de nuestro array.
    ndarray.dtype –> Es un objeto que describe el tipo de elementos del array.
    ndarray.shape –> Devuelve la dimensión del array, es decir, una tupla de enteros indicando
    el tamaño del array en cada dimensión. Para una matriz de n filas y m columnas obtendremos (n,m).
    ndarray.data –> El buffer contiene los elementos actuales del array.
    ndarray.itemsize –> devuelve el tamaño del array en bytes.
    ndarray.size –> Es el número total de elementos del array."""

import numpy as np # Importamos numpy como el alias np
miArray = np.arange(10) # Creamos un array de 0 a 9 separados de uno en uno
print(type(miArray))
numdim= miArray.ndim
dim=miArray.shape
tam= miArray.size
byte=miArray.itemsize

 

"""identity(n,dtype) –>Devuelve la matriz identidad, es decir, uma matriz cuadrada nula excepto
 en su diagonal principal que es unitaria. n es el número de filas (y columnas) que tendrá la matriz 
 y dtype es el tipo de dato. Este argumento es opcional. Si no se establece, se toma por defecto como flotante.
ones(shape,dtype) –>Crea un array de 1 compuesto de shape elementos.
zeros(shape, dtype) –>Crea un array de 0 compuesto de “shape” elementos”.
linspace(start,stop,num,endpoint=True,retstep=False) –>Crea un array con valor inicial start, 
valor final stop y num elementos.
empty(shape, dtype) –>Crea un array de ceros compuesto de “shape” elementos” sin entradas.
meshgrid(x,y) –>Genera una malla a partir de dos los arrays x, y.
eye(N, M, k, dtype) –>Crea un array bidimensional con unos en la diagonal k y ceros en el resto. 
Es similar a identity. Todos los argumentos son opcionales. N es el número de filas, M el de columnas 
y k es el índice de la diagonal. Cuando k=0 nos referimos a la diagonal principal y por tanto eye es 
similar a identity.
arange([start,]stop[,step,],dtype=None) –>Crea un array con valores distanciados step entre el valor 
inicial star y el valor final stop. Si no se establece step python establecerá uno por defecto."""


import numpy as np # Importamos numpy como el alias np
g=np.zeros( (3,4) )
print(g)
k=np.linspace( 1, 4, 9 )
print(k)
X,Y=np.meshgrid([1,2,3],[7,9,34])
print(X)
print(Y)

##Matrices con Numpy
#Suma: se realiza elemento a elemento ya sea arrays o matrices. Ejemplo de suma y el producto por un escalar:

import numpy as np # Importamos numpy como el alias np
a = np.array([[8, 2], [8, 4]])
b=a+a
print(b)
c=a*b
print(c)

#Ejemplo de matrices y funciones con álgebra lineal como traspuestas, conjugado, inversa, cálculos de 
#determinantes ecuaciones lineales, autovalores ….

import numpy as np # Importamos numpy como el alias np
g=np.matrix( [[3,4,-9], [7,4,-5] ,[1,3,9]] )
print(g)
b=np.matrix( [[-9], [-5] ,[9]] )
print(b)
c=g*b
print(c)
bt=b.T #traspuestas
print(bt)
bh=b.H #traspuestas y conjudaga
print(bh)
gi=g.I #inversa
print(gi)
detgi=np.linalg.det(gi) #calculo del determinante
tragi=np.trace(gi) #calculo de la traza

#Producto matricial y producto elemento a elemento:

import numpy as np # Importamos numpy como el alias np
a = np.array([[8, 2], [8, 4]])
b=np.dot(a,a)
print(b)
c=a*a
print(c)
d=np.multiply(a, a)
print(d)

#Operaciones y Funciones con Numpy
#Producto vectorial y producto exterior:

import numpy as np # Importamos numpy como el alias np
a = np.array([[8, 1, 4]])
b= np.array([[3, 7, 4]])
c= np.cross(a, b) # Producto vectorial
print(c)
d=np.outer(a, b) # Producto exterior
print(d)

#Ejemplo de funciones trigonométricas y la transformada de Fourier:

import numpy as np # Importamos numpy como el alias np
x=np.linspace(0,1,100)
y=np.sin(x)
print (np.fft.fft(y))