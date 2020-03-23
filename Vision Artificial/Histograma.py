"""                                                             Teoría

En sentido general, un histograma es un gráfico que muestra la distribución de frecuencias de una variable dada. En el caso de la 
imágenes, el histograma da una idea general sobre la distribución de intensidades. Cuando hablamos de imágenes, un histograma es 
un gráfico con valores de píxeles (que, en general, oscilan entre 0 y 255 aunque no siempre) en el eje X y la cantidad 
correspondiente de píxeles en la imagen en el eje Y.

Es simplemente otra manera de entender la imagen. Al mirar el histograma de una imagen, se puede tener idea sobre el contraste, 
el brillo, la distribución de intensidad, etc. de esa imagen. Casi todas las herramientas de procesamiento de imágenes de hoy en 
día, proporcionan características en el histograma. A continuación se muestra una imagen del sitio web de Cambridge in Color.

En la figura se muestra la imagen y su histograma. (Recuerde, este histograma se dibuja para la imagen en escala de grises, no 
para la imagen en color). La región izquierda del histograma muestra la cantidad de píxeles más oscuros en la imagen y la región 
derecha muestra la cantidad de píxeles más brillantes. Del histograma puede verse que las regiones oscuras en la imagen son 
mayores que la regiones brillantes, pues hay más píxeles con valores cerca de 0 que píxeles cerca de su valor máximo (255). Por 
otra parte, la cantidad de medios tonos (valores de píxel en el rango medio, digamos alrededor de 127) son muy inferiores.


                                                        Generar un histograma

Ahora que ya tenemos una idea de qué es un histograma, podemos ver cómo generarlo. Tanto OpenCV como Numpy vienen con una función 
incorporada para esto. Pero antes de usar esas funciones, necesitamos comprender algunas terminologías relacionadas con los
 histogramas.

BINS: el histograma anterior muestra la cantidad de píxeles para cada valor de píxel, es decir, de 0 a 255. O sea que en el eje X
 hay 256 valores representados. Pero ¿qué pasa si no necesita encontrar la cantidad de píxeles para todos los valores de píxeles 
 por separado, sino el número de píxeles en un intervalo de valores de píxeles? por ejemplo, necesita encontrar la cantidad de 
 píxeles entre 0 y 15, luego 16 a 31, …, 240 a 255. Necesitará solo 16 valores para representar el histograma.

Entonces, lo que hace es simplemente dividir el histograma completo en 16 subintervalos y el valor de cada subintervalo es la suma
 de todos los recuentos de píxeles en él. Cada uno de estos subintervalos se denomina “BIN” (o columna en español). En el primer 
 caso, el número de BINS era 256 (una por cada píxel), mientras que en el segundo caso, es solo 16. BINS está representado por el 
 término histSize en OpenCV.

DIMS: es la cantidad de parámetros para los que recopilamos los datos. En este caso, recopilamos datos con respecto solo a una 
cosa, valor de intensidad. Por lo tanto aquí será 1.

RANGO: es el rango de valores de intensidad que se desea medir. Normalmente, es [0,256], es decir, todos los valores de intensidad.


                                                            Cálculo del histograma en OpenCV

La librería de OpenCV viene provista de una función para calcular histogramas, esta es: cv2.calcHist(). A continuación analizaremos
 esta función y sus parámetros:

cv2.calcHist (imágenes, canales, máscara, histSize, rangos [, hist [, acumular]])

Imágenes: es la imagen fuente del tipo uint8 o float32. debe darse entre corchetes, es decir, “[img]”.

canales: también se debe poner entre corchetes. Es el índice de canal para el que calculamos el histograma. Por ejemplo, si la 
entrada es una imagen en escala de grises, su valor es [0]. Para la imagen en color, puede pasar [0], [1] o [2] para calcular el 
histograma del canal azul, verde o rojo, respectivamente.

máscara: imagen de máscara. Para encontrar el histograma de la imagen completa, se indica “None”. Pero si desea encontrar un 
histograma de una región particular de la imagen, debe crear una imagen de máscara para eso y darle una máscara. (Más adelante se 
mostrará un ejemplo).

histSize: esto representa nuestro conteo de BINS. Necesita ponerse también entre corchetes. Para la escala completa, pasamos 
[256].

gamas: Este es el rango de valores que puede tomar cada pixel, normalmente es [0,256].

Comencemos, pues, con una imagen de muestra. Simplemente, cargaremos la imagen y encontraremos su hostograma."""
import cv2
img = cv2.imread('histograma.jpg',0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])

"""hist es una matriz de 256×1, donde cada valor corresponde al número de píxeles en la imagen con valor 0, 1, 2…ó 255.
Cálculo del histograma con Numpy

Numpy también posee una función para calcular el histograma: np.histogram(). Prueba utilizar esta función en lugar de calcHist():"""

hist,bins = np.histogram(img.ravel(),256,[0,256])

"""En este caso, hist será exactamente igual lo devuelto por la función calcHist(). Sin emabrgo, los contenedores tendrán 257 elementos, porque Numpy calcula los contenedores como 0-0.99, 1-1.99, 2-2.99, etc. Por lo tanto, el rango final sería 255-255.99. Para representar eso, también se agrega 256 al final de los contenedores. Pero no necesitamos ese 256. Hasta 255 es suficiente.

Nota 
Numpy tiene otra función, np.bincount() que es mucho más rápida (alrededor de 10X) que np.histogram(). Por lo tanto para histogramas unidimensionales, puedes utilizar mejor esta función. No olvides establecer minlength = 256 en np.bincount. Por ejemplo, hist = np.bincount (img.ravel (), minlength = 256).

Nota 
La función de OpenCV es más rápida (alrededor de 40X) que np.histogram(). Así que mejor utilizar la función de OpenCV.
Cómo graficar histogramas

Hay dos maneras de hacer esto:

    Forma corta: utilizando las funciones de trazado Matplotlib
    Forma larga: utilizando las funciones de dibujo de OpenCV

1.Utilizando Matplotlib

Matplotlib viene con una función de trazado de histogramas: matplotlib.pyplot.hist(). Esta función encuentra directamente el 
histograma y lo traza. No es necesario uilizar primero la función calcHist() o np.histogram() para buscar el histograma. Vea el 
código a continuación:

    import cv2
    import numpy as np
    from matplotlib import pyplot as plt
    img = cv2.imread('parlamentoBP.jpg',0)
    plt.hist(img.ravel(),256,[0,256]); plt.show()

O también puede usar la representación normal de Matplotlib, lo cual sería bueno para el gráfico de BGR. Para esto, primero es
 necesario encontrar los datos del histograma. El código a continuación muestra un ejemplo de cómo hacer esto:"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('histograma.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

"""Del histograma anterior se puede deducir los colores rojos, verdes y azules están en áreas bien definidas de la imagen. Estos
 corresponden, obviamente, a los techos del Parlamento de Budapest (rojo), los árboles(verde) y el cielo (azul).
2. Utilizando OpenCV

Para dibujar un histograma como el anterior, utilizando la librería de OpenCV, hay que utilizar una de las siguientes funciones: 
    cv2.line() o cv2.polyline(). Para esto es necesario pasar las coordenadas X e Y, correspondientes a los valores de BINS y los
    valores del histograma, respectivamente.
    
                                                            
                                                            Cómo aplicar una máscara
                                                            
Hasta ahora hemos utilizado cv2.calcHist() para encontrar el histograma de la imagen completa. ¿Qué sucede si quisiéramos
 encontrar histogramas de algunas regiones de una imagen? Para esto, simplemente, debemos crear una imagen de máscara con un color 
 blanco en la región en la que desea buscar el histograma y, el resto de la imagen en negro. """

img = cv2.imread('histograma.jpg',0)
# crear máscara
mask = np.zeros(img.shape[:2], np.uint8)
mask[10:140, 100:200] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)
# Calcular el histohrama con máscara y sin máscara
# Fijar el tercer argumento como "mask"
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()