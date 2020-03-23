
"""                                                        La transformada de círculo de Hough

Objetivo del 28º tutorial de Curso de Procesamiento de Imágenes y Visión Artificial

Aprender a usar Transformada de Hough para encontrar círculos en una imagen.

Entender la función cv2.HoughCircles()

 
Teoría

Un círculo se representa matemáticamente como (x-x_{center})^2 + (y - y_{center})^2 = r^2 donde (x_{center},y_{center}) es el centro 
del círculo, y r es el radio del círculo. A partir de la ecuación, podemos ver que tenemos 3 parámetros, por lo que necesitamos un 
acumulador 3D para la transformada de Hough, que sería altamente ineficaz. Así que OpenCV usa un método más complicado, el Método
 Hough Gradient, que utiliza la información de degradado de los bordes.

La función que usamos aquí es cv2.HoughCircles(). Tiene muchos argumentos que están bien explicados en la documentación. Veamos un 
ejemplo directamente:"""

 

import cv2
import numpy as np
img = cv2.imread('monedas.jpg',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,3,30,
                            param1=80,param2=20,minRadius=10,maxRadius=40)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # Dibuja la circusnferencia del círculo
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # dibuja el centro del círculo
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
cv2.imshow('círculos detectados',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()