"""                                             Transformaciones morfológicas

Las transformaciones morfológicas son algunas operaciones simples basadas en la forma de la imagen, que normalmente se aplican a 
imágenes binarias. Necesita dos entradas, una es nuestra imagen original, la segunda se llama elemento estructurante o núcleo 
(kernel) que decide la naturaleza de la operación. Dos operadores morfológicos básicos son Erosión y Dilatación. Luego, sus formas 
variantes como Apertura, Cierre, Gradiente, etc, también entran en juego. A continuación se verán algunas de estas transformaciones, 
apoyándonos en la siguiente imagen binaria:


                                                        Erosión

Similar a la convolución 2D, en el proceso de erosionado un kernel se desliza a través de la imagen. Un píxel de la imagen original 
(1 ó 0) sólo se considerará 1 si todos los píxeles que caen detro de la ventana del kernel son 1, de lo contrario se erosiona (se 
hace a cero). Por tanto, todos los píxeles cerca de los bordes de los objetos en la imagen serán descartados dependiendo del tamaño 
del kernel. Como consecuencia, el grosor o el tamaño de los objetos en primer plano disminuye o, en otras palabras, la región blanca 
disminuye en la imagen. Este procedimiento es útil para eliminar pequeños ruidos blancos, separar dos objetos conectados, etc. A 
continuación un ejemplo donde se utiliza un kernel de 7×7 formado por unos:"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('A.png',0)
kernel = np.ones((7,7),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)

 
"""                                                     Dilatación

El proceso de dilatación es justo lo opuesto a la erosión. Aquí, un elemento de píxel es ‘1’ si al menos un píxel de la imagen de 
los que caen dentro de la ventana del kernel es ‘1’. Por lo tanto, la dilatación aumenta el tamaño de los objetos de primer plano, 
es decir, la región blanca. Normalmente, en casos como la eliminación del ruido, la erosión es seguida de dilatación. La razón para 
esto es que aunque la erosión elimina los ruidos blancos también encoge los objetos. Por tanto, para recuperar el tamaño inicial, 
este se dilata. La transformación de dilatación también es útil para unir partes rotas de un objeto. A continuación un ejemplo de 
cómo la dilatación funciona:"""

dilatacion = cv2.dilate(img,kernel,iterations = 1)

#donde el kernel es el mismo que se ha utilizado en el ejemplo de Erosión.


"""                                                         Apertura
                                                         
La apertura es simplemente otro nombre para erosión seguida de dilatación. Como se explicó anteriormente, es útil para eliminar 
el ruido. En este caso se utiliza la función, cv2.morphologyEx(). Vea el ejemplo a continuación:"""

apertura = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)



"""                                                             Cierre

El Cierre es el opuesto de Apertura, es decir, dilatación seguida de erosión. Es útil para cerrar pequeños agujeros dentro de los 
objetos de primer plano, o pequeños puntos negros en el objeto. Vea un ejemplo a continuación:"""

cierre = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

  
"""                                                         Gradiente Morfológico

Es la diferencia entre la dilatación y la erosión de una imagen. El resultado se verá como el contorno del objeto."""

gradiente = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

 
"""Nota
En todos los ejemplos mostrados hemos creado manualmente elementos estructurantes (kernels) de forma rectangular 
(utilizando np.ones()). Sin embargo, en algunos casos, es necesario crear núcleos elípticos / circulares. Para este propósito, 
OpenCV tiene la función cv2.getStructuringElement()."""


plt.subplot(231),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(erosion),plt.title('Erosion')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(dilatacion),plt.title('Dilatacion')
plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(apertura),plt.title('Apertura')
plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(cierre),plt.title('Cierre')
plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(gradiente),plt.title('Gradiente')
plt.xticks([]), plt.yticks([])
plt.show()