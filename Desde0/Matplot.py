"""Matplotlib es una librería para generar gráficas a partir de datos contenidos en listas, vectores, 
en el lenguaje de programación Python y en su extensión matemática NumPy.


Lo primero que debemos hacer es importarla con esta línea:

    import matplotlib.pyplot as plt

Hay diferentes formas de plotear con Matplotlib:

figure(num, figsize, dpi, facecolor, edgecolor, frameon)

    num = numeración de la figura, si num = None, las figuras se numeran automáticamente.
    figsize = w, h tuplas en pulgadas. Tamaño de la figura
    dpi = Resolución de la imagen en puntos por pulgada.
    facecolor = Color del rectángulo de la figura.
    edgecolor = Color del perímetro de la figura.
    frameon = Si es falso, elimina el marco de la figura.

Para crear mas figuras en una misma ventana podemos utilizar el siguiente comando:

subplot(numRows, numCols, plotNum)

    numRows = Número de filas
    numCols = Número de columnas
    plotNum = Número de gráfica

plot(x, y, linestyle, linewidth, marker) –> Permite incluir varias gráficas en una única figura.

    x = Abcisas.
    y = Ordenadas. Tanto x como y pueden ser abcisas tuplas, listas o arrays, pero ambas deben tener el mismo tamaño.
    linestyle = color y tipo de dibujar la gráfica. Por ejemplo ‘k- -‘
    linewidth = ancho de línea.
    marker = Marcador."""

import matplotlib.pyplot as plt
import numpy as np # Importamos numpy como el alias np
a = np.linspace(0,20,50)
b= np.sin(a)
plt.plot(a, b, 'k--', linewidth = 2) 
plt.show()

 
"""Tipos o trazados de líneas communes en Matplotlib:

‘ – ‘ línea sólida

‘ -. ‘ línea con puntos y rayas

‘ – -‘ línea a rayas

‘ : ‘ línea punteada
Colores comunes en Matplolib

‘c’ Cián

‘b’ Azul

‘g’ Verde

‘y’ Amarillo

‘k’ Negro

‘w’ Blanco

‘r’ Rojo

‘m’ Magenta
Ejemplo con tipos de líneas, colores, marcadores, leyenda, textos en los ejes, malla…

Ejemplo donde se aplican diferentes tipos de líneas, colores, marcadores, leyenda, textos en los ejes, 
malla y se guarda la figura en Matplolib:"""

import matplotlib.pyplot as plt
import numpy as np # Importamos numpy como el alias np
a = np.linspace(0,20,50)
b= np.sin(a)
c=plt.plot(a, b, 'c-3', linewidth = 2)
c=plt.plot(a+0.2, b-1, 'r-o', linewidth = 2)
plt.xlabel("Tiempo (s)", fontsize = 20)
plt.ylabel(r"$y (\mu m)$", fontsize = 24, color = 'blue')
plt.text(5, 7, "Más texto", fontsize = 12)
plt.title("velocidad (m/s)", fontsize = 20)
plt.legend( ('Etiqueta1', 'Etiqueta2', 'Etiqueta3'), loc = 'upper left')
plt.grid(True)
plt.savefig('figura3.png', dpi = 300) #guarda la gráfica con 300dpi (puntos por pulgada)
plt.show()

 
### Ejemplo de subplot en Matplolib:

import matplotlib.pyplot as plt
import numpy as np # Importamos numpy como el alias np
a = np.linspace(0,20,50)
b= np.sin(a)
plt.figure()
# plot 1
plt.subplot(2,2,1)
plt.plot(a, b,'r')
# Segunda grafica
plt.subplot(2,2,2)
plt.plot(a+2, b*25,'g')
# Tercera grafica
plt.subplot(2,2,3)
plt.plot(b, a,'b')
# Cuarta grafica
plt.subplot(2,2,4)
plt.plot(a, b,'k')
# Mostramos en pantalla
plt.show()

#Ejemplo de gráfica en dos dimensiones en Matplolib:

import numpy as np
import matplotlib.pyplot as plt
plt.figure()
x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)
X, Y = np.meshgrid(x, y)
# Definimos cos (x^3 + y^2)
fxy = np.cos(X**3+Y**2)
plt.imshow(fxy);
plt.colorbar();
plt.show()

 

 
#Ejemplo de una gráfica de 3 dimensiones en Matplolib:

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, .3)
Y = np.arange(-4, 4, .3)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='jet')
plt.show()