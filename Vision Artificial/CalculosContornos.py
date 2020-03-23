"""                                                     Momentos

Los momentos de la imagen permiten calcular algunas de sus características, como el centro de masa del objeto, el área del
 objeto, etc.

La función cv2.moments() devuelve todos los momentos de la imagen. A continuación un ejemplo de como utilizar esta función:"""

import cv2
img = cv2.imread('test.jpg',0)
ret,thresh = cv2.threshold(img,127,255,0)
image,contours = cv2.findContours(thresh,1,2)
cnt = contours[0]
M = cv2.moments(cnt)
print(M)

"""M contiene la información de todos los momentos. Los distintos momentos son útiles para calcular diferentes parámetros de la 
imagen, como por ejemplo el centroide, que se determina a partir:"""

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])


"""                                                 Área de contorno

El área de contorno viene dada por la función cv2.contourArea() o por el momento M [‘m00’]."""

area = cv2.contourArea(cnt)


"""                                                 Perímetro de contorno

También llamado longitud de arco, se puede encontrar utilizando la función cv2.arcLength(). El segundo argumento especifica si 
la forma es un contorno cerrado (si se pasa como True) o simplemente una curva."""

perimetro = cv2.arcLength(cnt,True)


"""                                                 Aproximación de contorno

Aproxima una forma de contorno a otra forma con menos número de vértices, dependiendo de la precisión que se especifique. Es una 
implementación del algoritmo de Douglas-Peucker (veánse detalles en Wikipedia).

Para entender esto, supongamos que usted está tratando de encontrar un cuadrado en una imagen, pero debido a algunos problemas 
en la imagen, no obtuvo un cuadrado perfecto, sino una “mala forma” (como se muestra en la primera imagen a continuación). La 
función cv2.approxPolyDP permite aproximar esta forma a un cuadrado. El segundo argumento de esta función se denomina épsilon, 
que es la distancia máxima entre el contorno y el contorno aproximado. Es un parámetro de precisión y por lo tanto, una sabia 
selección de épsilon es necesaria para obtener la salida correcta."""

epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

"""Abajo, en la segunda imagen, la línea verde muestra la curva aproximada para epsilon = 10%. La tercera imagen muestra lo mismo 
para epsilon = 1% . El tercer argumento de cv2.approxPolyDP()  especifica si la curva es cerrada o no.


                                                        Envoltura convexa

La envoltura convexa es tiene un resultado similar a la aproximación de contorno. No obstante, aunque ambas pueden proporcionar 
los mismos resultados en algunos casos, en general, son dos técnicas distintas. La función cv2.convexHull() comprueba una curva 
de los defectos de convexidad y la corrige. En general, las curvas convexas son las curvas que siempre están abultadas, o al menos
 planas. Si la curva está abombada en el interior, se dice que tiene defectos de convexidad. Por ejemplo, compruebe la imagen de 
 la mano más abajo. La línea roja muestra la envoltura convexa de la mano. Las marcas de las flechas de doble cara muestran los 
 defectos de convexidad, que son las desviaciones máximas locales de la envoltura de los contornos.

La sintaxis para obtener la envoltura de contornos es la siguiente:

envoltura = cv2.convexHull(points[ hull[ clockwise[ returnPoints]]

Donde los argumentos de la función tiene los siguientes significados:

    points: son las coordenadas de los contornos que pasamos.
    hull: es la salida, que normalmente se evita.
    clockwise: Indicador de orientación. Si es verdadero, la envoltura convexa de salida estará orientada en sentido horario. De 
    lo contrario, estará orientada en sentido contrario a las agujas del reloj.
    ReturnPoints: Por defecto está fijado en True. Devuelve las coordenadas de los puntos de la envoltura. Si es Falso, devuelve 
    los índices de los puntos de contorno correspondientes a los puntos de la envoltura.
    


De manera que para obtener una imagen como la anterior es suficiente con escribir:"""

envoltura = cv2.convexHull(points[hull[clockwise[returnPoints]]])
envoltura = cv2.convexHull(cnt)

"""Nota 
Si se desean encontrar los defectos de convexidad, se necesita pasar returnPoints = False.
Revisando convexidad

Hay una función para comprobar si una curva es convexa o no, cv2.isContourConvex(). Sólo devuelve si es Verdadero o Falso."""

k = cv2.isContourConvex(cnt)


"""                                                         Rectángulo delimitador

Existen dos tipos de rectángulos delimitadores, rotado y sin rotar.
Rectángulo recto

Es un rectángulo recto, no considera la rotación del objeto. Así que el área del rectángulo delimitador no será mínima. Se encuentra por la función cv2.boundingRect().

Sea (x, y) la coordenada superior izquierda del rectángulo y  (w, h) su anchura y altura."""

x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


"""                                                                 Rectángulo rotado

En este caso el rectángulo delimitador se dibuja con el área mínima, por lo que considera la rotación también. La función 
utilizada es cv2.minAreaRect(). Devuelve una estructura Box2D que contiene los siguientes detalles: (esquina superior izquierda 
(x, y), (anchura, altura), ángulo de rotación). Pero para dibujar este rectángulo, necesitamos 4 esquinas del rectángulo, que se
 obtienen mediante la función cv2.boxPoints()."""

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
im = cv2.drawContours(im,[box],0,(0,0,255),2)

"""A continuación se muestran ambos rectángulos (rotado y sin rotar) sobre una imagen segmentada de una célula migratoria. Este
 tipo de análisis es muy útil para investigar las características del movimiento de estas células.
 

                                                    Círculo mínimo de inclusión

La función cv2.minEnclosingCircle() permite encontrar el círculo que cubre completamente el objeto con un área mínima."""

(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,255,0),2)


"""                                                     Ajustando a una elipse

La función cv2.fitEllipse() ajusta una elipse a un objeto. Devuelve la elipse inscrita en el rectángulo rotado."""

ellipse = cv2.fitEllipse(cnt)
im = cv2.ellipse(im,ellipse,(0,255,0),2)


"""                                                     Ajustando a una línea

Del mismo modo se puede ajustar una línea a un conjunto de puntos. A continuación un ejemplo de cómo trabaja la función 
cv2.fitLine():"""

rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
    