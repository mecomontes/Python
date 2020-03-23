"""                                                         Gradiente de Imágenes

El gradiente de una imagen mide cómo esta cambia en términos de color o intensidad. La magnitud del gradiente nos indica la 
rapidez con la que la imagen está cambiando, mientras que la dirección del gradiente nos indica la dirección en la que la 
imagen está cambiando más rápidamente. Matemáticamente, el gradiente se define por la derivadas parciales de una función dada 
(intensidad en el caso imágenes) a lo largo de las direcciones X e Y.  Los puntos donde la derivada es máxima (o mayor que cierto 
umbral) corresponden a cambios de intensidad grandes, normalmente asociados a los bordes de los objetos en la imagen. Por lo tanto, 
este operador resulta particularmente útil para encontrar los bordes de las formas dentro de una imagen. En OpenCV existen tres 
tipos de filtros de gradiente (o filtros pasa altos), estos son : Sobel, Scharr y Laplaciano. En este capítulo se verán cada uno 
de estos filtros.


                                                            Derivadas Sobel y Scharr

Los operadores Sobel y Scharr no son más que aproximaciones, más o menos precisas, para calcular el gradiente de una imagen. 
Ambos se definen a través de kernels cuadrados como los estudiados en los filtros pasa bajos. El operador Sobel aplica un 
alisamiento Gausssiano común y  estima las derivadas parciales a lo largo de X e Y. Utilizando los argumentos yorder y xorder, 
se puede especificar la dirección de las derivadas a tomar, vertical u horizontal, respectivamente. También se puede especificar 
el tamaño del kernel utilizando el argumento ksize. Cuando ksize = -1, se utiliza el kernel Scharr 3×3 que da mejores resultados 
que el kernel Sobel 3×3.


                                                            Derivadas Laplacianas

Este operador calcula el Laplaciano de la imagen, dado por la relación: donde cada derivada se determina utilizando el operador 
Sobel. Por ejemplo, si ksize = 1, el kernel que se utiliza para filtrar es:

Código

El código inferior muestra todos los operadores en un solo diagrama. Todos los kernels son de tamaño 3×3."""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cebra.jpeg')
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplaciano'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()

"""Nota
Note que mientras el filtro Sobel a lo largo de la dirección X no logra detectar la rayas horizontales, el filtro Sobel Y no puede 
detectar las rayas verticales. Por otro lado, las rayas diagonales son visibles utilizando cualquiera de los dos filtros dado que 
estas tienen las dos componentes, vertical y horizontal.

Un asunto importante!
Un punto importante a tener en cuenta es la profundidad de la imagen de salida. En el ejemplo anterior se ha utilizado cv2.CV_64F 
que muestra la imagen en la escala de grises. Si se quisera visualizar la imagen en blanco y negro entonces se debe sustituir, en 
el código anterior, cv2.CV_64F por cv2.CV_8U. Si hacemos este cambio, el resultado será el siguiente:
 
Si se comparan cuidadosamente estos resultados con los de más arriba se podrá notar que, en el caso de las imágenes en blanco y 
negro, algunos bordes han desaparecido. Esto es debido a que el gradiente de la transición de blanco a negro tiene valor positivo, 
mientras que la transición de negro a blanco tiene valor negativo. Luego, al utilizar cv2.CV_8U todas las transiciones negativas se 
hacen cero y por lo tanto no son detectadas por los filtros. Como resultado, algunos bordes de la imagen no son detectados.

Para evitar este problema y detectar ambos bordes, manteniendo la salida final en blanco y negro, la mejor opción es mantener el 
tipo de datos de salida en algunas formas superiores, como cv2.CV_16S, cv2.CV_64F etc; tomar su valor absoluto y luego convertirlo 
de nuevo a cv2.CV_8U. El código a continuación muestra este procedimiento para un filtro Sobel horizontal y las diferencias en los 
resultados."""

 
img = cv2.imread('whitebox.png',0)
# Utilizando cv2.CV_8U
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
#Utilizando cv2.CV_64F. Luego toma el valor absoluto y hace la conversión a cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)
plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
plt.show()