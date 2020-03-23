"""                                                 Emparejamiento de plantillas

 
Teoría

El emparejamiento de plantillas (o template matching en inglés) es un método para buscar y encontrar la ubicación de una imagen de 
plantilla en una imagen más grande. OpenCV viene con la función cv2.matchTemplate() para este propósito. Esta función, simplemente,
 desliza la imagen de la plantilla sobre la imagen de entrada (como en la convolución 2D) y en cada punto compara la plantilla con 
 la porción correspondiente de la imagen de entrada. En OpenCV están implementados varios métodos de comparación.  La función 
 devuelve una imagen en escala de grises, donde cada píxel indica cuánto coincide el entorno de ese píxel con la plantilla.

Si la imagen de entrada es de tamaño (WxH) y la imagen de la plantilla es de tamaño (wxh), la imagen de salida tendrá un tamaño de 
(W-w + 1, H-h + 1). Una vez que obtenga el resultado, puede usar la función cv2.minMaxLoc() para encontrar dónde está el valor 
máximo / mínimo. El valor máximo/ mínimo corresponde a la esquina superior izquierda del rectángulo con ancho w y alto h. Ese 
rectángulo será la región de la imagen de entrada que mejor coincide con la plantilla.

Nota:  Si está utilizando cv2.TM_SQDIFF como método de comparación, el valor mínimo dará la mejor coincidencia.
Emparejamiento de plantillas en OpenCV

A continuación se comparará el desempeño de diferentes métodos de emparejamiento de la función cv2.matchTemplate(), para encontrar 
la cara de un hombre entre los granos de café:

A continuación se muestra el código que hace esto:"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('cafe.jpeg',0)
img2 = img.copy()
template = cv2.imread('template.png',0)
w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)
    # Aplica el emparejamiento de plantillas
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # Si el método es TM_SQDIFF o TM_SQDIFF_NORMED, tomar el mínimo
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img,top_left, bottom_right, 255, 10)
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Resultado del emparejamiento'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Punto detectado'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()

"""En este caso se observa que los seis métodos dan resultados similares. Sin embargo, esto puede variar dependiendo de la imagen  
y la plantilla en particular. Nótese que en los cuatro primeros gráficos  a la izquierda el punto de máxima coincidencia es blanco 
(correspondiente con un máximo) mientras que, con los últimos dos métodos el punto de máxima coincidencia es negro (correspondiente
 con un mínimo)

Emparejamiento de plantillas con múltiples objetos

En la sección anterior, buscamos en la imagen la cara de un hombre, que aparece solo una vez en la imagen. Supongamos que está 
buscando un objeto que tiene múltiples ocurrencias, cv2.minMaxLoc() no le dará todas las ubicaciones. En ese caso, fijaremos un 
valor umbral por encima (o por debajo,dependiendo del método que usemos) del cual se asumirá que el objeto en la plantilla coincide 
con el objeto en la imagen. A continuación un ejemplo, en el que se muestra una captura de pantalla del famoso juego Mario. 
Utilizaremos el método explicado para encontrar todas las monedas."""

img_rgb = cv2.imread('mario.jpeg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('moneda.jpeg',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
umbral = 0.8
loc = np.where( res >= umbral)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv2.imwrite('res.png',img_rgb)