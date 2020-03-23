"""                                                         Teoría

Este método fue propuesto por Michael J. Swain, Dana H. Ballard en su documento “Indexación a través de histogramas de color”.

Ahora bien, ¿qué es realmente un histograma de retroproyección? Se usa para la segmentación de imágenes o para encontrar objetos de
 interés en una imagen. En palabras simples, este método crea una imagen del mismo tamaño (pero en un solo canal) de la imagen de 
 entrada, donde cada píxel corresponde a la probabilidad de ese píxel de pertenecer a nuestro objeto. En palabras más simples, en 
 la imagen de salida, nuestro objeto de interés lucirá más blanco que el resto de la imagen. Los histograma de retroproyección se 
 utilizan con algoritmos de cambio de cámara, etc.

¿Cómo lo hacemos? Creamos un histograma de una imagen que contiene nuestro objeto de interés (en nuestro caso, el cielo azul; véase
 más abajo). El objeto debe llenar la imagen lo más posible para obtener mejores resultados. Es preferible utilizar un histograma
 de color antes que un histograma en escala de grises, porque el color del objeto es una mejor manera de definir el objeto que su
 intensidad de escala de grises. Luego “retro-proyectamos” este histograma sobre nuestra imagen de prueba donde necesitamos 
 encontrar el objeto, es decir, calculamos la probabilidad de cada píxel de pertenecer al cielo y lo mostramos. La salida 
 resultante en el umbral adecuado nos dará como resultado el cielo azul aislado del resto de objetos en la imagen.


                                                                        Algoritmo en Numpy

1. Primero debemos calcular el histograma de color tanto del objeto que necesitamos encontrar (llamémosle ‘M’) como de la imagen 
donde vamos a buscar (llamémosle ‘I’)."""

import cv2
import numpy as np
from matplotlib import pyplot as plt
#roi es el objeto o región de la imagen que queremos encontrar
roi = cv2.imread('azul.png')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
#<em>target</em> es la imagen en la que buscamos
target = cv2.imread('parlamento.jpeg')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
# Encuentra los histogramas usando calcHist. También pueden encontrarse con np.histogram2d
M = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
I = cv2.calcHist([hsvt],[0, 1], None, [180, 256], [0, 180, 0, 256] )

"""2. Encuentre la relación R = M/I. A continuación, vuelva a proyectar R, es decir, utilice R como paleta y cree una nueva imagen 
con cada píxel como su correspondiente probabilidad de ser la imagen target, es decir, B (x, y) = R [h (x, y), s (x, y)] donde h 
es el Matiz y s es la saturación del píxel en (x, y). Después de eso aplica la condición B (x, y) = min [B (x, y), 1]."""

R = np.divide(M,I)
h,s,v = cv2.split(hsvt)
B = R[h.ravel(),s.ravel()]
B = np.minimum(B,1)
B = B.reshape(hsvt.shape[:2])

"3. Ahora aplique una convolución con un disco circular, B = D*B, donde D es el kernel del disco."

disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(6,6))
cv2.filter2D(B,-1,disc,B)
B = np.uint8(B)
cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)

"""4. La ubicación de intensidad máxima nos da la ubicación del objeto. Teniendo en cuenta la región de la imagen que nos interesa, 
y fijando un valor de umbral adecuado obtenemos un buen resultado."""

ret,thresh = cv2.threshold(B,70,255,0)


"""                                                 Retroproyección en OpenCV

OpenCV proporciona una función incorporada cv2.calcBackProject(). Sus parámetros son casi los mismos que la función cv2.calcHist().
 Uno de sus parámetros es el histograma del objeto y tenemos que encontrarlo previamente. Además, el histograma del objeto debe 
 normalizarse antes de pasarse a la función backproject. La función devuelve la probabilidad de la imagen. Luego hacemos la 
 convolución de la imagen con un kernel de disco y aplicamos el umbral. A continuación un ejemplo de aplicación de este método y
 su resultado:"""

roi = cv2.imread('azul.png')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
target = cv2.imread('parlamento.jpeg')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
# calcula el histograma del objeto
roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
# normaliza el histograma y aplica la retroproyección
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)
# Ahora aplica la covolución con un disco
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(6,6))
cv2.filter2D(dst,-1,disc,dst)
# Aplica un umbral y convierte la imagen en blanco y negro
ret,thresh = cv2.threshold(dst,70,255,0)
thresh = cv2.merge((thresh,thresh,thresh))
res = cv2.bitwise_and(target,thresh)
res = np.vstack((target,thresh,res))
cv2.imwrite('res.jpg',res)