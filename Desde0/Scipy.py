"""Scipy es una biblioteca de código abierto de herramientas y algoritmos matemáticos que nació a
 partir de la colección original de Travis Oliphant y que consistía en módulos de extensión para Python.
 Scipy contiene módulos para optimización, álgebra lineal, integración, interpolación, funciones especiales,
 FFT, procesamiento de señales e imagen, resolución de EDOs y otras tareas relacionadas con la ciencia e 
 ingeniería. Está dirigida al mismo tipo de usuarios que los de aplicaciones como MATLAB, GNU Octave, y Scilab.

Esta librería esta organiza por subpaquetes donde cada 1 esta enfocado a un tema de cálculos específicos:

    Algebra lineal -> linalg
    Procesamiento de señales -> signal
    Funciones estadísticas -> stats
    Funciones especiales -> special
    Integración -> integrate
    Herramientas de interpolación -> interpolate
    Herramientas de optimización -> optimize
    Algortimos de transformada de Fourier -> fftpack –
    Entrada y salida de datos -> io
    Wrappers a la librería LAPACK -> lib.lapack
    Wrappers a la librería BLAS -> lib.blas
    Wrappers a librerías externas -> lib
    Matrices sparse -> sparse
    otras utilidades -> misc
    Vector Quantization / Kmeans -> cluster
    Ajuste a modelos con máxima entropía -> maxentropy"""

##  Ejemplo: calcular los mínimos con Scipy de la siguiente función en un intervalo:

import numpy as np # Importamos numpy como el alias np
import scipy as sp# Importamos scipy como el alias sp
from scipy.optimize import fminbound # Importamos fmindbound desde scipy.optimize&amp;nbsp;&amp;nbsp;&amp;nbsp; 
import matplotlib.pyplot as plt 
#definimos la funcion
def mi_funcion(x, a, b, c, d):
 y = -sp.cos(a*sp.pi*x/b) + c*x**d
 return y
# Definimos los coeficientes a, b, c, d
a = 2
b = 0.5
c = 0.05
d = 2
# Definimos el intervalo de busqueda del minimo
x1 = 0.2
x2 = 0.6
xt=sp.arange(0,1,.01)
yt = -np.cos(a*sp.pi*xt/b) + c*xt**d
# Calculamos del minimo local de la funcion entre x1 y x2 
x_minimo = fminbound(mi_funcion,x1,x2, args = (a,b,c,d))
ysol = mi_funcion(x_minimo, a, b, c, d)
# Presentamos la grafica y en pantalla el resultado
print (u'El minimo esta en x = %2.3f, y = %2.3f' %(x_minimo, ysol))
plt.plot(xt,yt)
plt.plot(x_minimo,ysol,'x')
plt.show()

 
#Ejemplo de ajuste de una función:

#Caso real: un supermercado tiene unas previsiones de venta de pescado durante las primeras 5 horas
#que está abierto al público y estas vienen determinadas por la siguiente función:

#El objetivo es mejorar las ventas a partir de los coeficientes desconocidos a, b, c  y d.

#A continuación, revolvemos este problema:

import numpy as np # Importamos numpy como el alias np
import scipy as sp# Importamos scipy como el alias sp
from scipy.optimize import curve_fit # Importamos curve_fit de scipy.optimize
import scipy as sp # Importamos scipy como el alias sp
import matplotlib.pyplot as plt # Importamos matplotlib.pyplot como el alias plt.
def mi_funcion(x, a, b, c, d):
  return a*sp.exp(-b*x**2/(2*d**2)) + c * x
# Añadimos ruido
x = sp.linspace(0, 5,40)
y = mi_funcion(x, 2.5, 1.3, 0.5,1)
def ruido(x,y,k):
  yn = y + k * sp.random.normal(size = len(x))
  return yn
# Ajustamos los datos experimentales a nuestra funcion y los almacenamos
coeficientes_optimizados, covarianza_estimada = curve_fit(mi_funcion, x, y)
# Mostramos los coeficientes calculados
print ("Coeficientes optimizados:", coeficientes_optimizados)
print ("Covarianza estimada:", covarianza_estimada)
# Creamos la figura
plt.figure()
# Dibujamos los datos ruido
plt.plot(x,y,'ro', label = 'Experimental')
# mantenemos la figura
#plt.hold(True)
results=mi_funcion(x,coeficientes_optimizados[0],coeficientes_optimizados[1],coeficientes_optimizados[2], coeficientes_optimizados[3])
plt.plot(x,results, label = 'Ajuste')
plt.legend()
plt.xlabel('Tiempo (h)')
plt.ylabel('Ventas del supermercado en pescado x100 ($)')
plt.show()

 
#Calculo de integrales:

#Ejemplo para el cálculo integral siguiente de 0 a infinito.

import scipy as sp
from scipy import integrate
def integral_1(limite_inferior, limite_superior, mostrar_resultados):
  # funcion e^(-x)
  exponencial_decreciente = lambda x: sp.exp(-x)
  # resultados por pantalla
  if mostrar_resultados == True:
    print (u'La integral entre %2.2f y %2.2f es '% (limite_inferior, limite_superior))
    print(integrate.quad(exponencial_decreciente,limite_inferior,limite_superior))
  # Los devuelvo
  return integrate.quad(exponencial_decreciente ,limite_inferior,limite_superior)
integral_1(limite_inferior = 0, limite_superior = sp.inf, mostrar_resultados = True)


#Solucion:

#La integral entre 0.00 y inf es
#(1.0000000000000002, 5.842606996763696e-11) el primer valor es el resultado y el segundo es el error

 

 
#Interpolación en Python:

#Ejemplo de interpolación a partir de unos datos experimentales con  interpolate.interp1d

import scipy as sp
from scipy import interpolate
import matplotlib.pyplot as plt
#array
x = sp.linspace(0,3,10)
# generamos datos experimentales de ejemplo)
y = sp.exp(-x/3.0)
# Interpol
interpolacion = interpolate.interp1d(x, y)
# array con mas puntos en el mismo intervalo
x2 = sp.linspace(0,3,1000)
# Evaluamos x2 en la interpolacion
y2 = interpolacion(x2)
plt.figure
plt.plot(x, y, 'ok')
plt.plot(x2, y2, '-c')
plt.legend(('Datos conocidos', 'Datos experimentales interpolados'))
plt.show()

#Calculo de las raíces en un polinomio en Python

import scipy as sp
import matplotlib.pyplot as plt
# Creamos un polinomio
polinomio = [4.3,9,.6,-1]# polinomio = 4.3 x^3 + 9 x^2 + 0.6 x - 1
# array
x = sp.arange(-4,2,.05)
#&amp;nbsp; Evaluamos el polinomio en x mediante polyval.
y = sp.polyval(polinomio,x)
# Calculamos las raices del polinomio 
raices = sp.roots(polinomio)
# Evaluamos el polinomio en las raices
s = sp.polyval(polinomio,raices)
# Las presentamos en pantalla
print ("Las raices son %2.2f, %2.2f, %2.2f. " % (raices[0], raices[1], raices[2]))
# Creamos la figura
plt.figure
# Dibujamos
plt.plot(x,y,'-', label = 'y(x)')
# Fibujamos en la figura anterior
#plt.hold('on')
# Dibujamos
plt.plot(raices.real,s.real,'ro', label = 'Raices')
# Etiquetas 
plt.xlabel('x')
plt.ylabel('y')
plt.title(u'Raices de un polinomio de x^3')
# Leyenda
plt.legend()
# Mostramos la figura en pantalla
plt.show()