"""                                                 Substracción de fondo de un vídeo


BackgroundSubtractorKNN

Fundamentos

La resta de fondo es uno de los pasos más importantes del preprocesamiento en muchas aplicaciones basadas en la visión. Por ejemplo,
 considere los casos como el contador de visitantes donde una cámara estática toma el número de visitantes que entran o salen de la
 habitación, o una cámara de tráfico que extrae información sobre los vehículos, etc. En todos estos casos, primero hay que extraer
 a la persona o vehículos solos. Técnicamente, es necesario extraer el primer plano móvil del fondo estático.

Si usted tiene una imagen de fondo solo, como la imagen de la habitación sin visitantes, la imagen de la carretera sin vehículos
 etc, es un trabajo fácil. Sólo resta la nueva imagen del fondo. Te quedas con los objetos en primer plano solo. Pero en la mayoría 
 de los casos, es posible que no tengas una imagen de este tipo, por lo que necesitamos extraer el fondo de cualquier imagen que 
 tengamos. Se vuelve más complicado cuando hay sombra de los vehículos. Puesto que la sombra también se está moviendo, una simple 
 sustracción marcará eso también como primer plano y complica las cosas.

Para ello se introdujeron varios algoritmos. OpenCV ha implementado tres algoritmos que son muy fáciles de usar.

Imagen original:

 
BackgroundSubtractorMOG2

Es un algoritmo de segmentación de fondo/primer plano basado en la mezcla gaussiana. Se basa en dos documentos de Z. Zivkovic,
”Modelo de mezcla gausiana adaptativa mejorada para la sustracción de fondo” en 2004 y “Efficient Adaptive Density Estimation per 
Image Pixel for the Task of Background Substraction” en 2006. Una característica importante de este algoritmo es que selecciona el 
número apropiado de distribución gaussiana para cada píxel. Proporciona una mejor adaptabilidad a la variación de escenas debido
 a cambios de iluminación, etc.

Tenemos que crear un objeto de substractor de fondo. Aquí tienes la opción de seleccionar si deseas que se detecte sombra o no. Si 
detectShadows = True (que es así por defecto), detecta y marca sombras, pero disminuye la velocidad. Las sombras se marcarán en 
color gris."""

 

import numpy as np
import cv2
cap = cv2.VideoCapture('toki.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
while(1):
  ret, frame = cap.read()
  fgmask = fgbg.apply(frame)
  cv2.imshow('frame',fgmask)
  k = cv2.waitKey(30) &amp;amp;amp; 0xff
  if k == 27:
    break
cap.release()
cv2.destroyAllWindows()

###    BackgroundSubtractorMOG2


cap = cv2.VideoCapture('toki.mp4')
fgbg = cv2.createBackgroundSubtractorKNN()
while(1):
  ret, frame = cap.read()
  fgmask = fgbg.apply(frame)
  cv2.imshow('frame',fgmask)
  k = cv2.waitKey(30) &amp;amp;amp;amp; 0xff
  if k == 27:
    break
cap.release()
cv2.destroyAllWindows()