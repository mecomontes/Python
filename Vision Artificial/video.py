"""                         Captura de vídeo desde la cámara

A menudo, tenemos que capturar transmisiones en vivo con la cámara. OpenCV proporciona una interfaz muy
 simple para esto. Vamos a capturar un vídeo desde la cámara (estoy utilizando una webcam incorporada 
 de mi pc), convirtiendo en vídeo a escala de grises y mostrándolo. Es una tarea sencilla para empezar.

Para capturar un vídeo, es necesario crear un objeto VideoCapture. Su argumento puede ser el índice del 
dispositivo o el nombre de un archivo de vídeo. El índice del dispositivo es el número para especificar 
qué cámara se utilizará. Normalmente se conectará una cámara (como en mi caso). Así que simplemente paso 0 
(o -1). Puedes seleccionar una segunda cámara pasando 1 y así sucesivamente. Después de esto, puedes 
capturar el vídeo. Pero al final, no te olvide de liberar la captura."""

import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
  # Captura video cuadro a cuadro 
  ret, frame = cap.read()
  # Nuestras operaciones sobre los cuadros se hacen aqui
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # Muestra el cuadro resultante
  cv2.imshow('frame',gray)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break
# Cuando todo está listo, se libera la captura 
cap.release()
cv2.destroyAllWindows()

"""cap.read() devuelve un bool (verdadero / falso). Si el cuadro se lee correctamente, será verdadero (true). 
Por lo tanto, puedes comprobar el final del vídeo consultando este valor de retorno.

A veces, cap puede no haber inicializado la captura. En ese caso, este código mostrara error. Puede comprobar 
si se inicia o no con el método cap.isOpened(). Si es Verdad (true), excelente. De lo contrario ábrelo con cap.open().

También puede acceder a algunas de las características de este vídeo usando el método cap.get(PropID), donde 
PropID es un número del 0 al 18. Cada número indica una propiedad del video (si es aplicable a ese vídeo) y 
se puede detallar completamente aquí:  Property Identifier . Algunos de estos valores se pueden modificar 
mediante cap.set (propId, value). Valor es el nuevo valor que se desea.

Por ejemplo, puedo comprobar la anchura del marco y la altura por cap.get(3) and cap.get(4). Da como resultado 
por defecto 640×480. Pero si quieres modificarlo a 320×240.Sólo tienes que utilizar  ret = cap.set(3,320) y 
ret = cap.set(4,240)

 

Nota

Si obtienes un error, asegúrate de que la cámara esta funcionando correctamente con cualquier otra aplicación.


                        Reproducción de vídeo desde un archivo

Es lo mismo que capturar desde la Cámara, solo cambie el índice de la cámara con el nombre del archivo de vídeo. 
También, mientras que se visualice el cuadro, utiliza el tiempo apropiado para cv2.waitKey(). Si es demasiado 
corto, el video será muy rápido y si es demasiado alto, el video será lento (bueno, esta es una forma de mostrar 
vídeos en cámara lenta). 25 milisegundos estarán bien en casos normales."""

 

import numpy as np
import cv2
cap = cv2.VideoCapture('vtest.avi')
while(cap.isOpened()):
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('frame',gray)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()

 

"""Nota

Asegúrate de que las versiones adecuadas de ffmpeg o gstreamer estén instaladas. A veces, es un dolor 
de cabeza para trabajar con Capturas de Video, principalmente debido a una instalación incorrecta 
de ffmpeg / gstreamer.


                                         Guardando un video

Supongamos que queremos guardar un vídeo que hemos previamente capturado y procesado cuadro por cuadro. 
Para el caso de las imágenes, esto es muy simple, sólo necesitamos usar cv2.imwrite(). En el caso de los 
vídeos, sin embargo, se requeire un poco más de trabajo.

Para esto crearemos un objeto VideoWriter. Primero, debemos especificar el nombre que queremos dar al 
fichero (ej: output.avi). Luego tenemos que especificar el código FourCC (ver detalles más abajo), el 
número de cuadros por segundo (fps) y el tamaño de cuadro. El último argumento que debemos pasarle es 
la bandera isColor. Si es verdadero, el codificador espera cuadros a color, de lo contrario trabaja con 
escala de grises.

FourCC es un código de 4-bytes usado para especificar el códec del vídeo. Una lista de los diferentes 
códigos disponibles se puede encontrar en fourcc.org. Estos códigos son dependientes de la plataforma 
que estés utilizando, con lo cual, en dependencia del sistema operativo que estés usando puede que algunos
te funcionen y otros no. En el ejemplo que mostramos más abajo, que ha sido corrido sobre Windows 10,
hemos utilizado DIVX.

El código FourCC se puede pasar como cv2.VideoWriter_fourcc(‘M’, ‘J’, ‘P’, ‘G’) o cv2.VideoWriter_fourcc(*’MJPG) 
para el códec MJPG.

A continuación se muestra un código que captura vídeo de una cámara, invierte cada cuadro en la dirección 
vertical y lo guarda."""

import numpy as np
import cv2
cap = cv2.VideoCapture(0)
# Define el codec y crea el objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
       frame = cv2.flip(frame,0) #invierte el cuadro
       
       # escribe el cuadro invertido 
       out.write(frame)
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xFF == ord('q'):
           break
    else:
        break
#Libera todo si la tarea ha terminado
cap.release()
out.release()
cv2.destroyAllWindows()