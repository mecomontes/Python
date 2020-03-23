"""                                 Cambiando Espacios de Color

 
Objetivo del 8º tutorial de Curso de Procesamiento de Imágenes y Visión Artificial

En este tutorial, aprenderás como convertir imágenes de un espacio de color a otro, como RGB Gris, RGB  HSV, etc.

Adicionalmente a ello, crearemos una aplicación que extrae un objeto de color en un video.

Aprenderás las funciones siguientes: cvtColor(), cv2.inRange() etc.
Cambiando el Espacio de Color OpenCV con Python

Existen más de 150 métodos de conversión de espacio de color en OpenCV. Pero sólo nos detendremos en dos que son
los mayormente usados, RGB <-> Gris, RGB <-> HSV.

Para conversión de color, usamos la función

cv2.cvtColor(input_image, flag) donde flag determina el tipo de conversión.

Para la conversión de RGB -> Gris usamos los indicadores cv2.COLOR_BGR2GRAY. De forma similar para RGB -> HSV. 
Usamos el indicador cv2.COLOR_BGR2HSV. Para obtener otros indicadores, sólo ejecuta los siguientes comandos en tu t
erminal Python:

import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

Nota
Para HSV, el rango de tonos es [0,179], el rango de saturación es [0,255] y el rango de valor es [0,255]. Los distintos 
programas usan distintas escalas. Así que si estás comparando los valores de OpenCV con ellos, necesitas normalizar 
estos rangos.


                                        Seguimiento de Objetos

Ahora sabemos cómo convertir una imagen RGB a HSV, podemos usar esto para extraer un objeto de color. En HSV es más 
fácil representar un color que en RGB. En nuestra aplicación, trataremos de extraer un objeto de color azul. Así que 
aquí está el método:

    Toma cada fotograma del video
    Conviértelo de RGB a HSV
    Limitamos la imagen en HSV a un rango de color azul
    Ahora extraemos el objeto azul únicamente, podemos hacer lo que nos plazca en esa imagen.

Debajo está el código comentado en detalle:

import cv2
import numpy as np
image = cv2.imread('nadal.jpg')
#cap = cv2.VideoCapture(0)
while(1):
  # Take each frame
  #_, frame = cap.read()
  # Convert BGR to HSV
  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  # define range of blue color in HSV
  lower_verde = np.array([25,50,50])
  upper_verde = np.array([67,255,255])
  lower_rosa1 = np.array([125,50,50])
  upper_rosa1 = np.array([167,255,255])
  # Threshold the HSV image to get only blue colors
  mask = cv2.inRange(hsv, lower_verde, upper_verde)
  mask1 = cv2.inRange(hsv, lower_rosa1, upper_rosa1)
  # Bitwise-AND mask and original image
  bola = cv2.bitwise_and(image,image, mask= mask)
  camiseta = cv2.bitwise_and(image,image, mask= mask1)
  
  cv2.startWindowThread()

  cv2.imshow('frame',image)
  cv2.imshow('mask',mask)
  cv2.imshow('Bola',bola)
  cv2.imshow('Camiseta',camiseta)
  k = cv2.waitKey(5) 
  # si pulsa q se rompe el ciclo
  if k == ord("q"):
    break
    cv2.destroyAllWindows()
  cv2.destroyAllWindows()
cv2.destroyAllWindows()  """


import cv2
import numpy as np
image = cv2.imread('imagen_share.png')
#cap = cv2.VideoCapture(0)
while(1):
  # Take each frame
  #_, frame = cap.read()
  # Convert BGR to HSV
  # define range of blue color in HSV
  lower_rojo = np.array([0,0,50])
  upper_rojo = np.array([0,0,255])
  # Threshold the HSV image to get only blue colors
  mask = cv2.inRange(image, lower_rojo, upper_rojo)

  rojo = cv2.bitwise_and(image,image, mask= mask)
  
  cv2.startWindowThread()

  cv2.imshow('frame',image)
  cv2.imshow('cuadrado',rojo)
  k = cv2.waitKey(5) 
  # si pulsa q se rompe el ciclo
  if k == ord("q"):
    break
    cv2.destroyAllWindows()
  cv2.destroyAllWindows()
cv2.destroyAllWindows()  

"""Nota
Hay algo de ruido en esta imagen. Veremos cómo removerlo en capítulos posteriores.

Nota
Este es el método más simple para rastrear un objeto. Una vez que aprendas las funciones de contorno, podrás hacer 
muchas cosas como conseguir el centro de este objeto y usarlo para rastrearlo, dibujar diagramas sólo moviendo tu 
mano en frente de la camera y muchas otras cosas divertidas.

¿Cómo encontrar valores HSV para seguir o rastrear?

Esta es una pregunta común que encontramos en stackoverflow.com. Es muy simple y puedes usar la misma función, 
cv2.cvtColor(). En lugar de pasar una imagen, sólo pasas los valores RGB que deseas. Por ejemplo, para encontrar 
el valor HSV para el verde, intenta seguir los siguientes comandos en la terminal Python:

    green = np.uint8([[[0,255,0 ]]])
    hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
    print hsv_green

 

Ahora toma [H-10, 100,100] y [H+10, 255, 255] como los límites más bajo y superior de forma respectiva. A parte de este 
método, puedes usar cualquier herramienta de edición de imagen como GIMP o cualquier convertidor online para encontrar 
estos valores, pero no olvides ajustar los rangos HSV.

 
Recursos Adicionales
Ejercicios

Intenta encontrar una forma de extraer más de un objeto de color, por ejemplo: extrae objetos rojos, azules y amarillos 
de forma simultánea."""