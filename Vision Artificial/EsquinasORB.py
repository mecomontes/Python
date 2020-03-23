"""                                         ORB (Oriented Fast y Rotativo BRIEF)

Teoría

Como entusiasta de OpenCV, lo más importante del ORB es que proviene de “OpenCV Labs”. Este algoritmo fue criado por Ethan Rublee, 
Vincent Rabaud, Kurt Konolige y Gary R. Bradski en su trabajo ORB: Una alternativa eficiente a SIFT o SURF en 2011. Como dice el 
título, es una buena alternativa al SIFT y al SURF en cuanto a los costes de cálculo, igualando el rendimiento y principalmente las 
patentes. Sí, SIFT y SURF están patentados y usted debe pagar por su uso. ¡Pero ORB no lo es!!

ORB es básicamente una fusión del detector de punto clave FAST y el descriptor BRIEF con muchas modificaciones para mejorar el 
rendimiento. Primero usa FAST para encontrar los puntos clave, luego aplica la medida de la esquina de Harris para encontrar los
 mejores N puntos entre ellos. También utiliza la pirámide para producir rasgos multifuncionales. Pero un problema es que FAST no 
 calcula la orientación. ¿Y qué pasa con la invariancia de rotación? A los autores se les ocurrió la siguiente modificación.

Calcula la intensidad ponderada del centroide del parche con la esquina localizada en el centro. La dirección del vector desde este 
punto de esquina al centroide da la orientación. Para mejorar la invariancia de rotación, los momentos se calculan con x y y que 
deben estar en una región circular de radio r, donde r es el tamaño del parche.

Ahora para descriptores, ORB usa descriptores BRIEF. Pero ya hemos visto que BRIEF funciona mal con la rotación. Por lo tanto, lo que
 ORB hace es “dirigir” según la orientación de los puntos clave. Para cualquier conjunto de características de n pruebas binarias en 
 la ubicación (x_i, y_i), defina una matriz 2 \ multiplicado por n, S que contenga las coordenadas de estos píxeles. Luego usando la 
 orientación del patch, \theta, se encuentra su matriz de rotación y gira la S para obtener la versión dirigida (rotada) S_\theta.

ORB discretize el ángulo a incrementos de 2 \Npi /30 (12 grados), y construye una tabla de búsqueda de patrones BRIEF precalculados. 
Mientras la orientación de los puntos clave \theta sea consistente en todas las vistas, se utilizará el conjunto correcto de puntos 
S_\theta para calcular su descriptor.

BRIEF tiene una propiedad importante de que cada característica bit tiene una gran varianza y una media cercana a 0,5. Pero una vez 
que se orienta en la dirección de los puntos clave, pierde esta propiedad y se distribuye mejor. La alta varianza hace que una 
característica sea más discriminatoria, ya que responde de forma diferente a las variables de entrada. Otra propiedad deseable es 
tener las pruebas no correlacionadas, ya que cada prueba contribuirá al resultado. Para resolver todo esto, ORB realiza una búsqueda 
codiciosa entre todas las pruebas binarias posibles para encontrar las que tienen alta varianza y significa cerca de 0.5, además 
de no estar correlacionadas. El resultado se llama rBRIEF.

Para la correspondencia de descriptores, se utiliza LSH multi-sonda que mejora el LSH tradicional. El artículo dice que ORB es 
mucho más rápido que SURF y que SIFT y ORB descriptor funciona mejor que SURF. ORB es una buena opción en dispositivos de baja 
potencia para costuras panorámicas, etc.
ORB en OpenCV

Como de costumbre, tenemos que crear un objeto ORB con la función, cv2.ORB () o utilizando la interfaz común feature2d. Tiene una
 serie de parámetros opcionales. Los más útiles son nFeatures que indican el número máximo de características a retener (por 
 defecto 500), scoreType que indica si la puntuación de Harris o FAST para clasificar las características (por defecto, la 
 puntuación de Harris) etc. Otro parámetro, WTA_K decide el número de puntos que producen cada elemento del descriptor BRIEF 
 orientado. Por defecto son dos, es decir, selecciona dos puntos a la vez. En ese caso, para la comparación se utiliza la distancia
 NORM_HAMMING. Si WTA_K es 3 o 4, lo que toma 3 o 4 puntos para producir el descriptor BRIEF, entonces la distancia de coincidencia 
 es definida por NORM_HAMMING2.

Abajo hay un código simple que muestra el uso de ORB."""
 

import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('ojo.jpg',0)
# Initiate STAR detector
orb = cv2.ORB_create()
# find the keypoints with ORB
kp = orb.detect(img,None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img,kp,img, flags=0)
plt.imshow(img2),plt.show()