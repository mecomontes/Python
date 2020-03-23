"""                                                 La transformada de línea de Hough
Objetivo del 27º tutorial de Curso de Procesamiento de Imágenes y Visión Artificial

Entender el concepto de Transformada de Hough.

Prender cómo usarlo para detectar líneas en una imagen.

Estudiar las siguientes funciones: cv2.HoughLines(), cv2.HoughLinesP()

 
Teoría

La transformada de Hough es una técnica popular para detectar cualquier forma, siempre que se pueda representar esa forma 
matemáticamente. Este algoritmo puede detectar una forma determinada incluso si está rota o un poco distorsionada. Veamos cómo 
funciona para una línea.

Una línea se puede representar como y = mx + c o en forma paramétrica, como \rho = x \cos \theta + y \sin \theta donde \rho es la 
distancia perpendicular desde el origen a la recta, y \theta es el ángulo formado entre esta perpendicular a la recta y el eje 
horizontal, medido en sentido contrario a las agujas del reloj. Esta dirección varía según cómo represente el sistema de 
coordenadas. La que aquí se ha explicado es la representación que se usa en OpenCV (Vea la imagen debajo).

coordinate system

Por lo tanto, si la línea pasa por debajo del origen, tendrá un  \rho positivo y un ángulo menor que 180º. Si la línea va por 
encima del origen, el ángulo también se toma menor de 180º pero \rho se toma negativo. Cualquier línea vertical tendrá 0º y las 
líneas horizontales tendrán 90º.

Ahora veamos cómo funciona la Transformada de Hough para líneas. Cualquier línea se puede representar unívocamente con estos dos 
parámetros, (\rho, \theta). Primero debemos crear una matriz 2D o un acumulador (para mantener los valores de dos parámetros) y 
establecerlos en 0 inicialmente. Denotemos las filas como \rho y las columnas como \theta. El tamaño de la matriz dependerá de 
la precisión que necesite. Supongamos que quiere que la precisión de los ángulos sea de 1º grado, entonces necesitará 180 columnas.
 Para \rho , la distancia máxima posible es la longitud de la diagonal de la imagen. Así, por ejemplo, si tomamos una precisión 
 de 1 píxel, el número de filas podría ser igual a la longitud diagonal de la imagen.

Luego de aplicar el algoritmo, cada elemento de la matriz tendrá un valor igual a la suma de los puntos o píxeles que están 
posicionados en la línea representada por parámetros cuantificados (\rho, \theta). De este modo, el elemento (en la posición 
(\rho, \theta) en la matriz) con el valor más alto indicará la línea recta más representada en la imagen de entrada

Para entender esto mejor consideremos,  por ejemplo, una imagen de 100x100 con una línea horizontal en el medio. Para cada para 
par (x, y) de la imagen el algoritmo comprueba cuáles rectas, definidas en la matriz mediante (\rho, \theta), pasan por ese punto
 (x, y). Entonces, cada vez que un punto (x, y) pertence a una recta (\rho, \theta), el contador corrspondiente se incrementa en 
 1. Supongamos que empezamos cogiendo el punto (x=0, y=50). Muchas de las rectas con parámetros (\rho, \theta) pasarán por ese 
 punto y podrán sus respectivos acumuladores en 1. Sin embargo sólo la recta de parámetros \rho=50 y \theta=90º seguirá acumulando 
 por encima de 1. Es decir todos los puntos con coordenadas x=0,1,2… 100 e y=150, sumarán uno al contador de la celda \rho=50 y 
 \theta=90º

Por lo tanto, si ahora buscamos en la matriz, los valores máximos en el acumulador, obtendremos que es el valor correspondiente a 
la celda (50,90º). Esto nos dice hay una línea en esta imagen a una distancia 50 del origen y en un ángulo de 90 grados. En la 
animación siguiente se muestra claramente como funciona este algoritmo (Imagen cortesía: Amos Storkey).

Así es como funciona la transformación para líneas. Es simple y puede ser implementarlo usando Numpy. Sin embargo, como debe 
imaginar, este algoritmo ya está implementado en OpenCV. A continuación se muestra una imagen de la matriz acumulador. Los puntos
 brillantes en algunas ubicaciones denotan los parámetros (\rho, \theta) de posibles líneas en la imagen (tomado de Wikipedia).


                                                    Tranformada de Hough en OpenCV
                                                    
Todo lo explicado anteriormente está encapsulado en la función de OpenCV, cv2.HoughLines(). Simplemente devuelve una matriz de 
valores (\rho, \theta), donde\rho se mide en píxeles y\theta se mide en radianes. El primer parámetro, la imagen de entrada, debe 
ser una imagen binaria, por lo tanto, aplique el umbral o use la detección de bordes astutos antes de aplicar la transformada de 
Hough. Los parámetros segundo y tercero son las precisiones en \rho y \theta respectivamente. El cuarto argumento es el umbral, 
es decir, el acumulado mínimo que debe obtener para que se le considere como una línea. Recuerde, el número de votos (acumulados) 
dependerá del número de puntos en la línea. Por lo tanto, este número de votos representa la longitud mínima de línea que debe 
detectarse."""

import cv2
import numpy as np
img = cv2.imread('sudoku.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
lines = cv2.HoughLines(edges,1,np.pi/180,200)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imwrite('houghlines1.jpg',img)

 
"""                                                                 Transformada Probabilística de Hough

En la transformación de Hough, se puede ver que incluso para una línea con dos argumentos, se necesita mucha computación. La 
transformada probabilística de Hough es una optimización de la Transformada de Hough que vimos. No toma todos los puntos en 
consideración, en su lugar toma solo un subconjunto de puntos al azar y eso es suficiente para la detección de línea. Sólo se 
encesita disminuir el umbral. Vea la imagen a continuación que compara la Transformada de Hough y la Transformada Probabilística 
de Hough en un espacio amplio (tomado de la página de inicio de Franck Bettinger’s)

La implementación de OpenCV se basa en la detección robusta de líneas usando la Transformación probabilística progresiva de Hough, 
de Matas, J.,  Galambos, C. y Kittler, J.V .. La función utilizada es cv2.HoughLinesP(), la cual posee dos nuevos argumentos:

MinLineLength: longitud mínima de la línea. Los segmentos de línea más cortos que esto son rechazados.
maxLineGap: espacio máximo permitido entre los segmentos de línea para tratarlos como una sola línea.

Lo mejor es que devuelve directamente los dos puntos finales de las líneas. En el caso anterior, solo la función sólo devuelve 
los parámetros de las líneas, y uno tiene que encontrar todos los puntos. En este caso, todo es mucho más directo y simple."""

img = cv2.imread('sudoku.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imwrite('houghlines2.jpg',img)
