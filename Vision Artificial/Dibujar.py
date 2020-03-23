"""                             Funciones para dibujar en OpenCV

Todas las funciones para dibujar, como las mencionadas anteriormente, tienen algunos argumentos comunes. 
A continuación se muestran algunos de ellos:

    img: La imagen donde se desea dibujar la forma geométrica
    color: Color de la forma. En el caso del espacio de colores BGR, debemos pasar los valores como una tupla, 
    ej: (255, 0, 0) para el azul. Por otra parte, para la escala de grises sólo se debe pasar un valor escalar.
    thickness: Grosor de la línea, círculo, etc. En el caso de figuras cerradas como el círculo, un valor de 
    thickness=-1 llenará el interior de la figura. El valor por defecto de este parámetro es =1.
    lineType: Tipo de línea, ya sea 8-conectada, suavizada, etc. Por defecto, es 8-conectada. Con cv2.LINE_AA 
    se obtiene una línea suavizada que luce genial para las curvas.


                                    Dibujando una línea

Para dibujar una línea, es necesario introducir las coordenadas iniciales y finales de la línea. En el siguiente 
ejemplo crearemos una imagen en negro y dibujaremos una línea horizontal verde a la altura media de la imagen."""

import numpy as np
import cv2
# Crea una imagen en negro
img = np.zeros((512,512,3), np.uint8)
# Dibuja una línea horizontal verde con un grosor de 4 px
img = cv2.line(img,(0,255),(511,255),(0,255,0),4)

"""                                 Dibujando un rectángulo

Para dibujar un rectángulo se necesitan especificar las coordenadas de la esquina superior izquierda y la 
esquina inferior derecha del rectángulo. El ejemplo a continuación, dibuja un rectángulo azul en la parte 
inferior de la imagen."""

img = cv2.rectangle(img,(210,360),(300,500),(255,0,0),3)

"""                                     Dibujando un círculo

Para dibujar un círculo debes indicar las coordenadas del centro y el valor del radio. A continuación se 
muestra cómo dibujar un círculo rojo, de radio igual a 100 px, insertado en el centro de la imagen."""

img = cv2.circle(img,(255,255), 100, (0,0,255), -1)

"""                                 Dibujando una elipse
Para dibujar una elipse se necesitan pasar varios argumentos; estos son: las coordenadas del centro (x,y), 
la longitud de su eje mayor y menor, y el ángulo de rotación de la elipse en sentido antihorario. startAngle 
y endAngle indican el arco inicial y final de la elipse, medidos en dirección horaria, respecto al eje mayor. 
Es decir, para dibujar la elipse completa debemos fijar startAngle=0 y endAngle=360. Para más detalles, por 
favor revisa la documentación de cv2.ellipse(). A continuación un ejemplo de media elipse dibujada en la 
parte centro-superior de la imagen."""

img = cv2.ellipse(img,(255,105),(100,50),0,0,180,255,-1)

"""                                         Dibujando un polígono

Para dibujar un polígono es necesario especificar las coordenadas de los vértices. Construye las coordenadas 
en un arreglo de dimensiones ROWSx1x2, donde ROWS es el número de vértices y debe ser de tipo int32. A 
continuación se muestra el código para dibujar un pequeño triángulo de color amarillo."""

pts = np.array([[180,120],[330,120],[255,140]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

"""Nota

    Si el tercer argumento en cv2.polylines es False, entonces se obtendrá una línea poligonal abierta.
    cv2.polylines se puede utilizar para dibujar varias líneas. Basta con crear una lista de todas las líneas 
    que se desean dibujar y pasarla a la función. Todas las líneas se dibujarán individualmente. Es una manera 
    mejor y más rápida de dibujar un grupo de líneas que llamar a cv2.line() para cada línea.

                                            Agregando texto a las imágenes

Para agregar un texto en las imágenes, es necesario especificar los siguientes atributos:

    Datos de texto que desea escribir.
    Coordenadas del sitio donde quiere colocar el texto en la imagen (es decir, la esquina inferior izquierda 
    donde comienza el texo).
    Tipo de fuente (Comprobar documentos cv2.putText () para las fuentes compatibles)
    Escala de fuentes (especifica el tamaño de la fuente)
    Otros como, color, grosor, lineType, etc. Para una mejor visualización, se recomienda lineType = cv2.LINE_AA.

En el ejemplo a continuación, escribiremos “DRAWING” en color blanco sobre la imagen con fondo negro."""

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'DRAWING',(40,90), font, 3,(255,255,255),2,cv2.LINE_AA)

"""                                     Resultado final de nuestros dibujos

Es hora de ver el resultado final de todos los dibujos que hemos ido haciendo a lo largo de esta entrada. 
Recuerda, de clases anteriores, que para mostrar una imagen debes utilizar las instrucciones siguientes:"""

# Mostrar la imagen
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()