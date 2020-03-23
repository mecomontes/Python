"""                             Detector de Esquina Shi-Tomasi y Buenas Características para Rastrear
 
Teoría

En el último capítulo, vimos el detector de esquinas Harris. Más tarde en 1994, J. Shi y C. Tomasi hicieron una pequeña modificación 
con Good Features to Track que muestra mejores resultados en comparación con Harris Corner Detector. La función de puntuación en 
Harris Corner Detector fue dada por:

En vez de esto, Shi-Tomasi propuso:

Código detector de Esquina Shi-Tomasi

OpenCV tiene una función, cv2.goodFeaturesToTrack (). Encuentra N esquinas más fuertes en la imagen por el método Shi-Tomasi (o 
Detección de esquinas Harris, si lo especifica). Como siempre, la imagen debe ser en escala de grises. A continuación, especifique 
el número de esquinas que desea encontrar. A continuación, especifique el nivel de calidad, que es un valor entre 0-1, que indica 
la calidad mínima de esquina por debajo de la cual se rechaza a todo el mundo. A continuación, proporcionamos la distancia euclidiana 
mínima entre las esquinas detectadas.

Con todas estas informaciones, la función encuentra esquinas en la imagen. Se rechazan todas las esquinas por debajo del nivel de
 calidad. A continuación, clasifica las esquinas restantes según la calidad en orden descendente. Entonces la función toma la primera
 esquina más fuerte, tira todas las esquinas cercanas en el rango de distancia mínima y devuelve N esquinas más fuertes.

En el siguiente ejemplo, trataremos de encontrar las 6 mejores esquinas:"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('tablero.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray,6,0.01,10)
corners = np.int0(corners)
for i in corners:
  x,y = i.ravel()
  cv2.circle(img,(x,y),3,255,-1)
plt.imshow(img),plt.show()