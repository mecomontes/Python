
"""                                                 Conceptos básicos de Brute-Force Matcher

Brute-Force matcher es simple. Toma el descriptor de una característica en el primer set y se empareja con todas las otras 
características en el segundo set usando un cálculo de distancia. Y el más cercano es devuelto.

Para BF matcher, primero tenemos que crear el objeto BFMatcher usando cv2.BFMatcher (). Se necesitan dos parametros opcionales. El 
primero es normType. Especifica la medición de distancia a utilizar. Por defecto, es cv2.NORM_L2. Es bueno para SIFT, SURF etc (cv2.
 NORM_L1 también está). Para descriptores binarios basados en cadenas de texto como ORB, BRIEF, BRISK etc.. Se debe utilizar 
cv2.NORM_HAMMING, que utiliza la distancia de Hamming como medida. Si ORB está usando VTA_K == 3 o 4, se debe usar
 cv2.NORM_HAMMING2.

El segundo parámetro es variable booleana, crossCheck que es false por defecto. Si es cierto, Matcher devuelve sólo aquellos 
partidos con valor (i, j) de tal manera que el descriptor i-ésimo del set A tenga el descriptor j-ésimo del set B como mejor 
partido y viceversa. Es decir, las dos características de ambos conjuntos deben coincidir entre sí. Proporciona un resultado 
consistente, y es una buena alternativa a la prueba de relación propuesta por D. Lowe en papel SIFT.

Una vez creado, dos métodos importantes son BFMatcher. match () y BFMatcher. knnMatcher (). El primero devuelve el mejor partido. 
El segundo método devuelve k las mejores coincidencias donde k es especificado por el usuario. Puede ser útil cuando necesitemos 
hacer un trabajo adicional sobre eso.

Como usamos cv2.drawKeypoints () para dibujar puntos clave, cv2.drawMatches () nos ayuda a dibujar los partidos. Apila dos imágenes
 horizontalmente y dibuja líneas de la primera imagen a la segunda, mostrando las mejores coincidencias. Hay también 
 cv2.drawMatchesKnn que sortea todos los mejores partidos de k. Si k=2, dibujará dos líneas de combate para cada punto clave. 
 Así que tenemos que pasar una máscara si queremos dibujarla selectivamente.

Veamos un ejemplo para cada uno de SURF y ORB (ambos usan diferentes medidas de distancia).
Combinación de fuerza bruta con descriptores ORB

Aquí, veremos un ejemplo sencillo de cómo hacer coincidir las características entre dos imágenes. En este caso, tengo una 
consultaImagen y una imagen de un ojo. Intentaremos encontrar la consulta Imagen en trainImage usando la coincidencia de 
características.

Estamos utilizando descriptores SIFT para combinar las características. Así que vamos a empezar con la carga de imágenes,
 encontrar descriptores, etc.

A continuación creamos un objeto BFMatcher con medición de distancias cv2.NORM_HAMMING (ya que estamos usando ORB) y se activa 
el crosscheck para obtener mejores resultados. Luego utilizamos el método Matcher.match () para obtener las mejores coincidencias 
en dos imágenes. Los clasificamos en orden ascendente de sus distancias para que los mejores partidos (con baja distancia) 
lleguen al frente. Luego sorteamos sólo las primeras 30 coincidencias (sólo por razones de visibilidad, puedes aumentarlo como 
quieras).

                                                                       
Combinación de fuerza bruta con descriptores ORB código python:"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
img1 = cv2.imread('ojo.jpg',0) # queryImage
img2 = cv2.imread('ojo4.jpg',0) # trainImage
#Iniciar detector SIFT
orb = cv2.ORB_create()
# Encuentra los puntos clave y descriptores con SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
# crea BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1,des2)
# Clasifícalos en el orden de su distancia.
matches = sorted(matches, key = lambda x:x.distance)
# Dibuja las primeras 30 coincidencias.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:30],None, flags=2)
plt.imshow(img3),plt.show()

"""Feature Matching

 
¿Qué es este objeto Matcher?

El resultado de matches=bf.match (des1, des2) es una lista de objetos DMatch. Este objeto DMatch tiene los atributos siguientes:

    DMatch.distance – Distancia entre descriptores. Cuanto más bajo, mejor.
    DMatch.trainIdx – Índice del descriptor en descriptores de trenes
    DMatch.queryIdx – Índice del descriptor en descriptores de consulta
    DMatch.imgIdx – Índice de la imagen del tren."""
