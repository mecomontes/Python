"""                                 Suavizando Imágenes con OpenCV

En el proceso de alisado (smoothing en inglés) las imágenes son difuminadas. Una imagen se ve más nítida o más detallada si somos 
capaces de percibir todos los objetos y sus formas, correctamente, en ella. Mientras menos definidos son los bordes de las formas 
individuales dentro de la imagen, más difícil es distinguir una forma de otra. Esto es precisamente lo que hace el alisado, es 
decir, reducir el contenido de los bordes de las formas en la imagen, suavizando así la transición entre los distintos colores. 
Para este fin se utilizan  filtros de imágenes.


                                        Convolución 2D (Filtrado de imágenes)

Al igual que las señales unidimensionales, las imágenes también pueden ser filtradas con varios tipos de filtros, como por ejemplo, 
filtros pasa bajo (FPB), filtros pasa alto (FPA), filtros pasa banda, etc. Mientras que un FPB ayuda a eliminar el ruido en la 
imagen o a difuminar la imagen, un FPA ayuda a encontrar los bordes en una imagen. La función cv2.filter2D(), disponible en OpenCV, 
permite aplicar una convolución entre un kernel dado y una imagen. Un ejemplo de un kernel es un filtro para promediar, como el 
FPB de 5×5 que se muestra a continuación:
 
El filtrado de una imagen dada con el kernel anterior funciona de la manera siguiente: sobre cada pixel de la imagen se centra 
una ventana de 5×5. Los píxeles contenidos en esta ventana se suman y se dividen por 25, y el valor resultante es asignado al 
pixel. Esto equivale a calcular el promedio del valor de los píxeles que caen en la ventana de 5×5. La operación se repite sobre 
todos los píxeles de la imagen, dando lugar a la imagen filtrada. El siguiente código genera el kernel K y lo aplica a una imagen:"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('Candy.jpg')
#Crea el kernel
kernel = np.ones((5,5),np.float32)/25
#Filtra la imagen utilizando el kernel anterior
dst = cv2.filter2D(img,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Promediada')
plt.xticks([]), plt.yticks([])
plt.show()


"""                                     Difuminando imágenes (alisando o suavizando imágenes)


Como ya se ha mencionado, el difuminado de la imagen se consigue convolucionando la imagen con un kernel de filtro pasa bajo (FPB). 
Los FPB eliminan el contenido de alta frecuencia (ej: ruido y bordes) de la imagen, lo que resulta, en general, en imágenes con 
bordes más borrosos. No obstante, también hay filtros que eliminan el ruido con poco efecto sobre los bordes. Tres de los técnicas 
de difuminado más utlizadas, que vienen implementados en OpenCV son: el promediado, los filtros gaussianos y los filtros de mediana.
A continuación, se discutirán estos tres tipos de FPB.


                                                            Promedio
Este es justo el caso explicado más arriba, en el caso de los filtros personalizados. El promedio se realiza convolucionando la 
imagen con un filtro de caja normalizado. De este modo, este filtro toma el promedio de todos los píxeles bajo el área del kernel 
y reemplaza al elemento central por este promedio. Una manera alternativa de hacer esto es mediante las funciones cv2.blur() o 
cv2.boxFilter().  Al uilizar estas fucniones tenemos que especificar el ancho y la altura del kernel. Un filtro de caja normalizado
 3×3 se vería así:

Nota
Si no desea utilizar un filtro de caja normalizado, utilice cv2.boxFilter() y pase el argumento normalize = False a la función."""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('Candy.jpg')
blur = cv2.blur(img,(3,3))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Difuminada')
plt.xticks([]), plt.yticks([])
plt.show()


"""                                                     Filtro Gaussiano
En este enfoque, en lugar de un filtro de caja que consta de coeficientes iguales, se utiliza un núcleo gaussiano. Esto se hace con 
la función, cv2.GaussianBlur(). Como parámetros de entrada se tienen que pasar el ancho y la altura del kernel, que debe ser 
positivo y impar. Además hay que especificar la desviación estándar en las direcciones X e Y, sigmaX y sigmaY, respectivamente. 
Este tipo de filtrado es muy eficaz para eliminar el ruido gaussiano de la imagen.

Nota
Si sólo se especifica sigmaX, sigmaY se toma como igual a sigmaX. Si ambas se pasan como ceros, se calculan a partir del tamaño 
del núcleo.
El código anterior puede ser modificado para aplicar el filtro Gaussiano, sustituyendo blur por:

    blur = cv2.GaussianBlur(img,(5,5),0)

 
                                                        Filtro de Mediana
Este filtro calcula la mediana de todos los píxeles bajo la ventana del kernel y el píxel central se reemplaza con este valor 
mediano. Esto es muy efectivo para eliminar el ruido conocido como ruido de sal y pimienta. OpenCV dispone de la función 
cv2.medianBlur() para aplicar este tipo de filtro a una imagen. Al igual que en el filtro Gaussiano, el tamaño del kernel en el 
filtro de mediana tiene que ser un número entero impar positivo.
Un ejemplo del desempeño de este tipo de filtro se muestra a continuación. Sólo debes sustituir en el código anterior, blur por:

    median = cv2.medianBlur(img,5)""" 