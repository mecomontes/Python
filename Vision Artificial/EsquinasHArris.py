"""                                                 Detección de esquinas Harris

 
Teoría

En el último capítulo, vimos que las esquinas son regiones de la imagen con grandes variaciones de intensidad en todas las 
direcciones. Un primer intento de encontrar estas esquinas fue hecho por Chris Harris y Mike Stephens en su documento A Combined 
Corner and Edge Detector en 1988, así que ahora se llama Harris Corner Detector. Llevó esta simple idea a una forma matemática.
 Básicamente encuentra la diferencia de intensidad para un desplazamiento de (u, v) en todas las direcciones. Esto se expresa a 
 continuación:


                                                     Detección de esquinas Harris

Por lo tanto, el resultado de Harris Corner Detection es una imagen en escala de grises. Lo haremos con una imagen sencilla.
Detector de esquinas Harris en OpenCV

OpenCV tiene la función cv2.cornerHarris () para este propósito. Sus argumentos son:

img – Imagen de entrada, debe ser en escala de grises y tipo float32.
blockSize – Es el tamaño del vecindario considerado para la detección de esquinas.
ksize – Parámetro de apertura del derivado Sobel utilizado.
k – Parámetro libre del detector Harris en la ecuación.

Vea el ejemplo a continuación:"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('tablero.jpg',0)
img = np.float32(img)
dst = cv2.cornerHarris(img,2,3,0.04)
dst = cv2.dilate(dst,None)
plt.subplot(2,1,1), plt.imshow(dst )
plt.title('Harris Corner Detection'), plt.xticks([]), plt.yticks([])
plt.subplot(2,1,2),plt.imshow(img,cmap = 'gray')


"""                                             Esquina con precisión de subpíxeles

A veces, es posible que necesite encontrar las esquinas con la máxima precisión. OpenCV viene con una función cv2.cornerSubPix ()
 que refina aún más las esquinas detectadas con precisión de subpíxeles. Abajo hay un ejemplo. Como siempre, tenemos que encontrar
 las esquinas de Harris primero. Luego pasamos los centroides de estas esquinas (Puede haber un manojo de pixeles en una esquina, 
 tomamos su centroide) para refinarlos. Las esquinas Harris están marcadas en píxeles rojos y las esquinas refinadas en píxeles 
 verdes. Para esta función, tenemos que definir los criterios para detener la iteración. Lo paramos después de que se haya 
 alcanzado un número específico de iteración o una cierta precisión, lo que ocurra primero. También tenemos que definir el tamaño 
 del barrido en el que se buscarían las esquinas.
"""
 
filename = 'tablero.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# encuentra Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)
# encuentra centroides
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 0.1)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
res = np.hstack((centroids,corners))
res = np.int0(res)
img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]
cv2.imwrite('subpixelharris.png',img)