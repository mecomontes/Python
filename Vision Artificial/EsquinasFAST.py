"""                                         Algoritmo FAST para la detección de esquinas


Hemos visto varios detectores de características y muchos de ellos son realmente buenos. Pero al mirar desde el punto de vista de la 
aplicación en tiempo real, no son lo suficientemente rápidos. Un mejor ejemplo sería SLAM (Simultaneous Localization and Mapping) 
robot móvil que tiene recursos computacionales limitados.

Como solución a esto, el algoritmo FAST (Features from Accelerated Segment Test) fue propuesto por Edward Rosten y Tom Drummond en su
 trabajo “Machine learning for speed corner detection” en 2006 (posteriormente revisado en 2010). Se presenta como un resumen básico 
 del algoritmo.
Detección de características con FAST

    Seleccione un píxel p en la imagen que debe ser identificado como un punto de interés o no. Que su intensidad sea I_p.
    Seleccione el valor umbral adecuado t.
    Considere un círculo de 16 píxeles alrededor del píxel bajo prueba.
    Ahora el pixel p es una esquina si existe un conjunto de n píxeles contiguos en el círculo (de 16 píxeles) que son todos más 
    brillantes que I_p + t, o todos más oscuros que I_p – t. n fue elegido para se 12.
     Se propuso una prueba de alta velocidad para excluir a un gran número de no esquinas. Esta prueba examina sólo los cuatro
     píxeles a 1,9,5 y 13 (Primeros 1 y 9 son probados si son demasiado brillantes u oscuros. Si es así, verifica 5 y 13). Si p es 
     una esquina, entonces al menos tres de ellas deben ser más brillantes que I_p + t o más oscuras que I_p – t. Si ninguno de estos 
     dos casos es el caso, entonces p no puede ser una esquina. El criterio de prueba de segmento completo se puede aplicar a los 
     candidatos aprobados examinando todos los píxeles del círculo. Este detector en sí mismo muestra un alto rendimiento, pero hay 
     varias debilidades:
         No rechaza tantos candidatos para n < 12.
        La elección de píxeles no es óptima porque su eficiencia depende del orden de las preguntas y la distribución de las 
        apariencias de las esquinas.
        Los resultados de las pruebas de alta velocidad se desechan.
        Se detectan múltiples características adyacentes entre sí.

Detector de características FAST en OpenCV

Se denomina como cualquier otro detector de características en OpenCV. Si lo desea, puede especificar el umbral, si se debe aplicar
 o no la supresión no máxima, el vecindario a utilizar, etc.

Para el vecindario, se definen tres banderas, cv2.FAST_FEATURE_DETECTOR_TYPE_5_8, cv2.FAST_FEATURE_DETECTOR_TYPE_7_12 y 
cv2.FAST_FEATURE_DETECTOR_TYPE_9_16. A continuación se muestra un código simple sobre cómo detectar y dibujar los puntos de la 
función FAST.
"""

import itertools
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('tablero.png',0)
# Iniciar objeto FAST con valores propuestos
fast = cv2.FastFeatureDetector_create()
# encontrar y dibujar los puntos clave
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img,kp,img)
cv2.imwrite('fast_tablero.png',img2)
# desactiva nonmaxSuppression
fast.setBool('nonmaxSuppression',0)
kp = fast.detect(img,None)