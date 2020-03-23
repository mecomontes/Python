"""                                                         Denoising de imagen

Teoría

En capítulos anteriores, hemos visto muchas técnicas de alisado de imágenes como el desenfoque gaussiano, el desenfoque medio, etc. 
y fueron buenas en cierta medida para eliminar pequeñas cantidades de ruido. En esas técnicas, tomamos un pequeño vecindario 
alrededor de un píxel e hicimos algunas operaciones como el promedio ponderado gaussiano, mediana de los valores etc para reemplazar 
el elemento central. En resumen, la eliminación del ruido en un píxel era local a su vecindario.

Hay una propiedad de ruido. El ruido se considera generalmente como una variable aleatoria con una media cero. Considere un píxel con 
ruidos, p = p_0 + n donde p_0 es el valor verdadero del píxel y n es el ruido en ese píxel. Puede tomar un gran número de los mismos 
píxeles (digamos N) de diferentes imágenes y calcular su promedio. Idealmente, debería obtener p = p_0 ya que la media del ruido es 
cero.

Usted mismo puede verificarlo mediante una sencilla configuración. Mantenga una cámara estática en un lugar determinado durante un 
par de segundos. Esto le dará un montón de fotogramas, o muchas imágenes de la misma escena. A continuación, escriba un código para 
encontrar el promedio de todos los fotogramas del vídeo (esto debería ser demasiado sencillo para usted ahora). Compare el resultado 
final y el primer cuadro. Se puede ver la reducción del ruido. Desafortunadamente, este sencillo método no es robusto a los 
movimientos de cámara y escena. También a menudo sólo hay una imagen ruidosa disponible.

Así que la idea es simple, necesitamos un conjunto de imágenes similares para promediar el ruido. Considere una ventana pequeña 
(digamos una ventana de 5×5) en la imagen. La probabilidad es grande de que el mismo parche pueda estar en otra parte de la imagen. 
A veces en un lugar pequeño a su alrededor. ¿Qué tal si usamos estos parches similares juntos y encontramos su promedio? Para esa
 ventana en particular, está bien.

La idea es que elegimos un pixel con ruido y tomamos una pequeña ventana alrededor de él, buscamos ventanas similares en la imagen, 
promediamos todas las ventanas y reemplazamos el píxel con el resultado que obtuvimos. Este método es la eliminación de medios no 
locales. Toma más tiempo en comparación con las técnicas de desenfoque que vimos antes, pero su resultado es muy bueno.

En el caso de las imágenes en color, la imagen se convierte al espacio de color CIELAB y luego se denotan por separado los 
componentes L y AB.


                                                                Denoising de imágenes en OpenCV

OpenCV proporciona cuatro variaciones de esta técnica.

    cv2.fastNlMeansDenoising () – funciona con una sola imagen en escala de grises
    cv2.fastNlMeansDenoisingColored () – funciona con una imagen en color.
    cv2.fastNlMeansDenoisingMulti () – funciona con la secuencia de imágenes capturadas en un corto periodo de tiempo (imágenes 
    en escala de grises)
    cv2.fastNlSignificaDenoisingColoredMulti () – igual que arriba, pero para imágenes en color.

Los argumentos comunes son:

    h: parámetro que determina la fuerza del filtro. Un valor h más alto elimina mejor el ruido, pero también elimina los detalles 
    de la imagen. (10 está bien)
    hForColorComponentes: igual que h, pero sólo para imágenes en color. (normalmente igual que h)
    templateWindowSize: debe ser impar. (recomendado 7)
    searchWindowSize: debe ser impar. (recomendado 21)

Demostraremos el punto 2. Dejamos el resto para que jueges tú un poco con estas funciones.
1. cv2. fastNlSignificaDenoisingColored ()

Como se mencionó anteriormente, se utiliza para eliminar el ruido de las imágenes en color. (El ruido se espera que sea gaussiano).
 Vea el ejemplo a continuación:"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('nadal.jpg')
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
plt.show()