"""¿Qué es un contorno?

Un contorno es una curva que une todos los puntos continuos en una imagen (a lo largo de los bordes), que tienen el mismo color o 
intensidad. Los contornos son una herramienta útil para el análisis de formas y para la detección y reconocimiento de objetos. 
Algunas consideraciones generales a tener en cuenta son:

    Para una mayor precisión lo mejor es utilizar imágenes binarias. Así que antes de encontrar los contornos, es recomendable 
    aplicar cierto umbral o utilizar el algoritmo de Canny  para la detección de bordes.
    La función findContours modifica la imagen de origen. Por lo tanto, si desea conservar la imagen original incluso después de
    encontrar contornos, esta se debe almacenar en una variable distinta.
    En OpenCV, encontrar contornos es como encontrar objetos blancos de fondo negro. Así que recuerde, el objeto a ser encontrado 
    debe ser blanco y el fondo debe ser negro.

Veamos cómo encontrar contornos de una imagen binaria:"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
im = cv2.imread('whitebox.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
imagen, contornos = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
plt.subplot(221),plt.imshow(im),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(imgray),plt.title('escala de gris')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(thresh),plt.title('Threshold')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(imagen),plt.title('Promediada')
plt.xticks([]), plt.yticks([])
plt.show()

"""Véase que hay tres argumentos en la función cv2.findContours(), el primero es la imagen fuente, el segundo es el modo de 
recuperación de contorno, y el tercero es el método de aproximación de contorno. Del mismo modo, la función posee tres variables 
de salida: imagen, contornos y jerarquía. Contornos es una lista de Python de todos los contornos de la imagen. Cada contorno 
individual es una matriz Numpy de coordenadas (x, y) de los puntos de los bordes del objeto.
🗒Nota 
Más adelante se dicutirán en detalle, los argumentos segundo y tercero, y sobre la jerarquía. Hasta entonces, los valores dados 
a ellos en el ejemplo del código funcionarán bien para todas las imágenes.
¿Cómo dibujar contornos?

Para dibujar los contornos se utiliza la función cv2.drawContours. Esta función también se puede utilizar para dibujar cualquier 
forma siempre que se conozcan sus contornos. El primer argumento de la función es la imagen fuente, el segundo argumento son los 
contornos, que deben ser pasados como una lista de Python; el tercer argumento es el índice de los contornos (útil para dibujar 
contornos individuales; para dibujar todos los contornos fijar este parámetro en -1), y los restantes argumentos son color, grosor, 
etc.

Para dibujar todos los contornos en una imagen:"""

img = cv2.drawContours(img, contornos, -1, (0,255,0), 3)

#Para dibujar, dígamos, el cuarto contorno:

img = cv2.drawContours(img, contornos, 3, (0,255,0), 3)

#Sin embargo, la mayoría de las veces el método siguiente resulta mucho más útil.

cnt = contornos[4]
img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)

"""Nota 
Aunque los dos métodos anteriores conducen exactamente al mismo resultado, más adelante se verá que el segundo resulta mucho más 
útil.
Método de aproximación de contornos

Este es el tercer argumento en la función cv2.findContours. Veamos su significado.

Más arriba hemos dicho que los contornos son los límites de una forma con la misma intensidad. La variable contornos almacena las 
coordenadas (x, y) de los bordes de una forma. ¿Pero almacena todas las coordenadas? Esto se precisamente lo que se especifica 
mediante este método de aproximación de contorno.

Si se pasa cv2.CHAIN_APPROX_NONE, todos los puntos de los bordes se almacenan. ¿Pero realmente necesitamos todos los puntos? Por 
ejemplo, supongamos que encontramos el contorno de una línea recta. ¿Necesitamos todos los puntos de la recta para representar esa 
línea? No, sólo necesitamos dos puntos a los extremos de esa línea. Esto es lo que hace cv2.CHAIN_APPROX_SIMPLE. Es decor, elimina 
todos los puntos redundantes y comprime el contorno, ahorrando memoria.

Debajo se muestra una imagen de un rectángulo que ilustra esta técnica. Basta con dibujar un círculo en todas las coordenadas de la
 matriz de contorno (en color azul). La primera imagen muestra los puntos que se obtienen con cv2.CHAIN_APPROX_NONE (734 puntos) y 
 la segunda imagen muestra los obtenidos con cv2.CHAIN_APPROX_SIMPLE (sólo 4 puntos). ¡Obsérvese, cuánta memoria se ahorra!"""

