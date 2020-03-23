"""                                     Detección de rostros, caras y ojos con Haar Cascad


Fundamentos

La detección de objetos mediante clasificadores en cascada basados en funciones de Haar es un método eficaz de detección de objetos
 propuesto por Paul Viola y Michael Jones en su documento,“Rapid Object Detection using a Boosted Cascade of Simple Features” en 
 2001. Se trata de un enfoque basado en el aprendizaje automático en el que la función en cascada se entrena a partir de muchas 
 imágenes positivas y negativas. Luego se utiliza para detectar objetos en otras imágenes.

Aquí trabajaremos con la detección de rostros o caras. Inicialmente, el algoritmo necesita muchas imágenes positivas (imágenes de 
caras) y negativas (imágenes sin caras) para entrenar al clasificador. Entonces necesitamos extraer rasgos de él. Para ello se 
utilizan las características de Haar mostradas en la imagen inferior. Son como nuestro núcleo convolucional. Cada característica 
es un valor individual obtenido restando la suma de píxeles bajo rectángulo blanco de la suma de píxeles bajo rectángulo negro.


                                                                Haarcascada1

Ahora se utilizan todos los tamaños y ubicaciones posibles de cada núcleo para calcular un montón de características. (¿Sólo 
imagínese cuánto cálculo necesita? Incluso una ventana de 24×24 resulta con más de 160000 características). Para cada cálculo de 
características, necesitamos encontrar la suma de píxeles bajo rectángulos blancos y negros. Para resolver esto, introdujeron las 
imágenes integrales. Simplifica el cálculo de la suma de píxeles, qué tan grande puede ser el número de píxeles, a una operación 
que involucra sólo cuatro píxeles. Bonito, ¿verdad? Hace que las cosas sean súper rápidas.

Pero entre todas estas características calculamos que la mayoría de ellas son irrelevantes. Por ejemplo, considere la imagen de 
abajo. La fila superior muestra dos buenas características. El primer rasgo seleccionado parece centrarse en la propiedad de que 
la región de los ojos es a menudo más oscura que la región de la nariz y las mejillas. La segunda característica seleccionada se 
basa en la propiedad de que los ojos son más oscuros que el puente de la nariz. Pero las mismas ventanas que se aplican en las 
mejillas o cualquier otro lugar es irrelevante. Entonces, ¿cómo seleccionamos las mejores características de las más de 16000000+ 
características? Lo consigue Adaboost.


                                                                Adaboosthaarcascada

Para ello, aplicamos todas y cada una de las características en todas las imágenes de entrenamiento. Para cada característica, 
encuentra el mejor umbral que clasificará los rostros en positivos y negativos. Pero obviamente, habrá errores o clasificaciones 
erróneas. Seleccionamos las características con una tasa de error mínima, lo que significa que son las características que mejor 
clasifican las imágenes faciales y no faciales. (El proceso no es tan simple como esto. Al principio, cada imagen tiene el mismo 
peso. Después de cada clasificación, aumenta el peso de las imágenes mal clasificadas. De nuevo se hace el mismo proceso. Se 
calculan nuevas tasas de error. También nuevos pesos. El proceso continúa hasta que se alcanza la precisión o la tasa de error 
requerida o se encuentra el número requerido de características).

El clasificador final es una suma ponderada de estos clasificadores débiles. Se llama débil porque solo no puede clasificar la 
imagen, pero junto con otros forma un fuerte clasificador. El papel dice que incluso 200 características proporcionan una detección 
con un 95% de precisión. Su configuración final tenía alrededor de 6000 características. (Imagine una reducción de 16000000+ 
características a 6000 características. Eso es una gran ganancia).

Así que ahora tomas una imagen. Tome cada ventana 24×24. Aplícale 6000 características… ¿No es un poco ineficiente y lleva mucho 
tiempo? Sí, lo es. Los autores tienen una buena solución para eso.

En una imagen, la mayor parte de la región de la imagen es una región no facial. Por lo tanto, es mejor tener un método simple para 
comprobar si una ventana no es una región facial. Si no lo es, deséchelo en un solo disparo. No lo proceses de nuevo. En su lugar, 
concéntrese en la región donde puede haber un rostro. De esta manera, podemos encontrar más tiempo para comprobar una posible 
región facial.

Para ello introdujeron el concepto de Cascade of Classifiers. En lugar de aplicar todas las 6000 características en una ventana, 
agrupe las características en diferentes etapas de clasificadores y aplíquelas una por una. (Normalmente, las primeras etapas
 contienen un número de características muy inferior). Si una ventana falla la primera etapa, deséchela. No tenemos en cuenta 
las características restantes. Si pasa, aplique la segunda etapa de las características y continúe el proceso. La ventana que 
pasa por todas las etapas es una zona de la cara.

El detector de autores tenía más de 6000 características con 38 etapas con 1,10,25,25,25 y 50 características en las primeras 
cinco etapas. (Dos características de la imagen anterior se obtienen como las dos mejores características de Adaboost). Según 
los autores, en promedio, se evalúan 10 de las 6000+ características por subventana.

Así que esta es una explicación intuitiva de cómo funciona la detección de cara Viola-Jones.
Detección de rostros o caras de Haar-cascade en OpenCV

OpenCV viene con un entrenador y un detector. Si quieres entrenar tu propio clasificador para cualquier objeto como coches,
 aviones, etc. puedes usar este de OpenCV.

Aquí nos ocuparemos de la detección. OpenCV ya contiene muchos clasificadores pre-entrenados para cara, ojos, sonrisa, etc. Esos 
archivos XML se almacenan en opencv/data/haarcascades/ folder. Vamos a crear un detector facial y ocular con OpenCV.

Primero necesitamos cargar los clasificadores XML requeridos. A continuación, cargue nuestra imagen de entrada (o vídeo) en modo
 escala de grises."""

import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('nadal.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

"""Ahora encontramos las caras en la imagen. Si se encuentran caras, devuelve las posiciones de las caras detectadas como Rect 
(x, y, w, h). Una vez que obtenemos estas ubicaciones, podemos crear un ROI para la cara y aplicar la detección de ojos en este 
ROI (ya que los ojos están siempre en la cara)."""

faces = face_cascade.detectMultiScale(gray, 1.35, 1)
for (x,y,w,h) in faces:
  img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,100,100),2)
  roi_gray = gray[y:y+h, x:x+w]
  roi_color = img[y:y+h, x:x+w]
  eyes = eye_cascade.detectMultiScale(roi_gray)
  for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(40,55,200),2)
cv2.imshow('img',img)
cv2.imwrite('img.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()