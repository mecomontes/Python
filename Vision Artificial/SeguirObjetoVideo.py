"""                                             Meanshift y Camshift algoritmos



Aprenderemos sobre los algoritmos Meanshift y Camshift para encontrar y rastrear objetos en los videos.
Desplazamiento medio Meanshift y Camshift

La intuición detrás del cambio de medias es simple. Considere que tiene un conjunto de puntos. (Puede ser una distribución de 
píxeles como la retroproyección del histograma). Se te da una pequeña ventana (puede ser un círculo) y tienes que mover esa 
ventana al área de máxima densidad de píxeles (o número máximo de puntos). Se ilustra un vídeo simple:

El vídeo muestra en cuadrado azul con el nombre. Su centro original es llamado “C1_o”. Pero si encuentras el centroide de los 
puntos dentro de esa ventana, obtendrás el punto “C1_r” que es el verdadero centroide de la ventana. Seguramente no coinciden. 
Así que mueve tu ventana para que el círculo de la nueva ventana coincida con el centroide anterior. Vuelve a encontrar el nuevo 
centroide. Lo más probable es que no coincida. Así que muévelo otra vez, y continúa las iteraciones de tal manera que el centro 
de la ventana y su centroide caiga en la misma ubicación (o con un pequeño error deseado). Así que finalmente lo que se obtiene 
es una ventana con la máxima distribución de píxeles.

Así que normalmente pasamos la imagen del histograma retroproyectada y la ubicación inicial del objetivo. Cuando el objeto se 
mueve, obviamente el movimiento se refleja en la imagen retroproyectada del histograma. Como resultado, el algoritmo meanshift 
mueve nuestra ventana a la nueva ubicación con la máxima densidad.


                                                        Codigo Mediashift en OpenCV

Para usar meanshift en OpenCV, primero necesitamos configurar el objetivo, encontrar su histograma para que podamos retroproyectar
 el objetivo en cada fotograma para el cálculo del meanshift. También necesitamos proporcionar la ubicación inicial de la ventana. 
 Para el histograma, aquí sólo se considera el matiz. También, para evitar falsos valores debido a la poca luz, los valores de luz 
 baja se desechan usando la función cv2.inRange ()."""

import numpy as np
import cv2
cap = cv2.VideoCapture('mundi2.mp4')
# toma el primer fotograma del video
ret,frame = cap.read()
# Configuración de la ubicación inicial de la ventana
r,h,c,w = 120,40,190,40 # simply hardcoded the values
track_window = (c,r,w,h)
# establece el ROI para rastrear
roi = frame[r:r+h, c:c+w]
hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
# Configure el criterio de terminación, ya sea 10 iteración o mover por lo menos 1 pt.
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 50, 1 )

while(1):
  ret ,frame = cap.read()
  if ret == True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
    # Aplica meanshift para conseguir la nueva ubicación.
    ret, track_window = cv2.meanShift(dst, track_window, term_crit)
    # Dibújalo en la imagen
    x,y,w,h = track_window
    img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
    cv2.imshow('img2',img2)
    k = cv2.waitKey(60) & 0xff
    if k == 27:
      break
    else:
      cv2.imwrite(chr(k)+".jpg",img2)
  else:
    break
cv2.destroyAllWindows()
cap.release()

 
"""Camshift

¿Vio de cerca el último resultado? Hay un problema. Nuestra ventana siempre tiene el mismo tamaño cuando el jugador está más lejos 
o está muy cerca de la cámara. Eso no es bueno. Tenemos que adaptar el tamaño de la ventana con el tamaño y rotación del objetivo. 
Una vez más, la solución vino de “OpenCV Labs” y se llama CAMshift (Continuously Adaptive Meanshift) publicado por Gary Bradsky en 
su trabajo “Computer Vision Face Tracking for Use in a Perceptual User Interface” en 1988.

Aplica el cambio de significado primero. Una vez que mediashift converge, actualiza el tamaño de la ventana como, 
s = 2 x \(M_00 / 256 )^1/2. También calcula la orientación de la elipse que mejor se adapte a ella. De nuevo se aplica la
 mediashift con la nueva ventana de búsqueda a escala y la ubicación de la ventana anterior. El proceso continúa hasta que se 
 alcanza la precisión requerida.

                                            Desplazamiento de medios en la imagen estática
                                                            Código Camshift en OpenCV

Es casi igual a meanshift, pero devuelve un rectángulo girado (éste es nuestro resultado) y parámetros de caja (utilizados para 
pasar como ventana de búsqueda en la iteración siguiente). Vea el código abajo:"""

import numpy as np
import cv2
cap = cv2.VideoCapture('bola.flv')
# toma el 1º frame del video
ret,frame = cap.read()
# ajusta el tamño de la ventana
r,h,c,w = 250,90,400,125 
track_window = (c,r,w,h)
# ajusta el ROI para el rastreo
roi = frame[r:r+h, c:c+w]
hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
# Configure el criterio de terminación, ya sea 10 iteración o mover por lo menos 1 pt.
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

while(1):
  ret ,frame = cap.read()
  if ret == True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
    #aplica meanshift para conseguir la nueva ubicacion
    ret, track_window = cv2.CamShift(dst, track_window, term_crit)
    # dibuja en la imagen
    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    img2 = cv2.polylines(frame,[pts],True, 255,2)
    cv2.imshow('img2',img2)
    k = cv2.waitKey(60) & 0xff
    if k == 27:
      break
    else:
      cv2.imwrite(chr(k)+".jpg",img2)
  else:
    break
cv2.destroyAllWindows()
cap.release()