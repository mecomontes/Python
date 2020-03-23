#   pip3 install opencv-python
#   pip3 install opencv-contrib-python

"""                     Usando OpenCV con imágenes


                                Leer una imagen

Utiliza la función cv2.imread() para leer una imagen. La imagen debe estar en el directorio de trabajo o se ha 
de señalar una ruta absoluta a la imagen.

El segundo argumento es un indicador (o bandera) que especifica la forma en que se debe leer la imagen.

    cv2.IMREAD_COLOR: carga una imagen de color. Cualquier transparencia de la imagen será ignorada. Es el 
    indicador (o bandera) predeterminado.
    cv2.IMREAD_GRAYSCALE: carga la imagen en modo de escala de grises
    cv2.IMREAD_UNCHANGED: carga la imagen como sin alteraciones incluyendo el canal alfa

Nota
En lugar de estos tres indicadores (o banderas), simplemente puedes pasar números enteros, específicamente 
1, 0 o -1, respectivamente.


Mira el siguiente código:"""

import numpy as np 
import cv2 
# Load an color image in grayscale 
img = cv2.imread('58-aprenderpython.jpg',0)
cv2.imshow('image',img)

"""Advertencia
Incluso si la ruta de la imagen está mal, no lanzara ningún error, pero print img  dará como resultado None


                            Mostrar una imagen

Utiliza la función cv2.imshow() para mostrar una imagen en una ventana. La ventana se ajusta automáticamente 
al tamaño de la imagen.

El primer argumento es un nombre de ventana el cual es una cadena (tipo de dato string). El segundo 
argumento es nuestra imagen. Puedes crear tantas ventanas como desees, pero con nombres diferentes de ventana."""

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""cv2.waitKey () es una función de enlace con el teclado. Su argumento es tiempo en milisegundos. La función 
espera durante milisegundos especificados que suceda cualquier evento de teclado. Si presionas cualquier tecla 
en ese momento, el programa continúa. Si se pasa el valor 0, la esperad del evento es indefinida hasta que se 
presione una tecla. También se puede configurar para detectar pulsaciones de teclas específicas, por ejemplo, 
si se presiona la tecla a tecla, etc, lo cual veremos más adelante.

cv2.destroyAllWindows() Esta función destruye todas las ventanas que hemos creado. Si deseas destruir una ventana 
específica, utilice la función de cv2.destroyWindow () donde se pasa el nombre de la ventana a eliminar como argumento.

 
Nota
Hay un caso especial en que puedes crear una ventana y cargar la imagen posteriormente. En ese caso, puedes 
especificar si la ventana es redimensionable o no. Esto se realiza con la función cv2.namedWindow(). Por defecto, 
el indicador (o bandera) es cv2.WINDOW_AUTOSIZE. Pero si se especifica la que el indicador sea  cv2.WINDOW_NORMAL, 
puedes cambiar el tamaño de la ventana. Esto será útil cuando las dimensiones de la imagen sean muy grandes y 
se añada una barra de seguimiento (o un scroll).

 

Ve el siguiente código:"""

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""                                 Guarda una imagen

Utiliza la función cv2.imwrite () para guardar una imagen.

El primer argumento es el nombre del archivo y el segundo argumento es la imagen que deseas guardar.

cv2.imwrite('deepgris.png',img)

aprenderpython

Esto guardará la imagen en formato PNG en el directorio de trabajo.
Resumiendo todo

A continuación, el programa carga una imagen en escala de grises, la muestra, guarda la imagen si presionas 
‘s’ y termina su ejecución, o simplemente termina sin guardar si presionas la tecla ESC."""

import numpy as np
import cv2

img = cv2.imread('58-aprenderpython.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)

if k == 27: # wait for ESC key to exit
  cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
  cv2.imwrite('deepgray.jpg',img)
  cv2.destroyAllWindows()

 

"""Advertencia

Si está utilizando una máquina de 64 bits, tendrás que modificar la linea  k = cv2.waitKey (0) de la 
siguiente manera: k = cv2.waitKey (0) & 0xFF


                                       Usando de Matplotlib

Matplotlib es una biblioteca para gráficar en Python que te ofrece una amplia variedad de métodos para plotear. 
Los verás en los próximos artículos. Aquí, aprenderás a mostrar una imagen con Matplotlib. Puede ampliar las 
imágenes, guardarlas, etc utilizando Matplotlib."""

import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('58-aprenderpython.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()

"""      Véase también

Muchas opciones de ploteo están disponibles en Matplotlib. Consulta la documentación Matplotlib para obtener 
más detalles. Algunos, los veremos en el camino.

 

⚠ Advertencia

La imagen a color cargada por OpenCV está en modo BGR. Pero Matplotlib se muestra en modo RGB. Por lo tanto, 
las imágenes a color no se mostrarán correctamente en Matplotlib si se lee la imagen con OpenCV. Por favor 
revisa los ejercicios para más detalles."""
