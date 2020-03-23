"""                                 Operaciones Básicas en Imágenes en OpcenCV con Python

Casi todas las operaciones en esta sección están principalmente relacionadas con Numpy más que a OpenCV. 
Conocer bien Numpy es un requerimiento para escribir un código mejor optimizado con OpenCV. Si no conoces 
Numpy te recomendamos esta introducción a Numpy.

(Mostraremos los ejemplos en la terminal Python dado que la mayor parte de ellos corresponden a líneas únicas de código)

 
                                    Accediendo y Modificando los valores de píxeles

Primero carguemos una imagen a color:"""

import cv2
import numpy as np
img = cv2.imread('trump.jpg')

"""Puedes acceder al valor de un pixel por medio de las coordenadas de su fila y su columna. Para imágenes RGB, 
regresan una gama de valores entre Azul, Verde y Rojo. Para las imágenes en escala de grises, sólo la intensidad 
correspondiente es regresada."""

px = img[100,100]
print(px)
# accessing only blue pixel
blue = img[100,100,0]
print(blue)

"Puedes modificar los valores de pixel de la misma forma."

img[100,100] = [255,255,255]
print(img[100,100])

 
"""Advertencia
Numpy es una biblioteca optimizada para cálculos rápidos. Así que simplemente acceder a cada valor de pixel 
y modificarlo podría resultar muy lento y no es recomendado.

Nota
El método mencionado anteriormente es usado normalmente para seleccionar una región, por ejemplo, las 
primeras 5 filas y las últimas 3 columnas de este modo. Para acceder a los píxeles de forma individual, 
los métodos de Numpy array.item() y  array.itemset() son considerados mejores. Pero siempre regresa un escalar. 
Así que si deseas acceder a los valores R,G,B necesitas llamar array.item() de forma separada para todos.


Un mejor método para acceder al pixel y editarlo:"""

# accessing RED value
img.item(10,10,2)
# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

"""                                 Accediendo a las Propiedades de Imagen

Las propiedades de imagen incluyen número de filas, columnas y canales, tipo de data de imagen, 
número de píxeles, etc.

Se accede a la forma de la imagen por medio de img.shape. Este regresa una tupla de números de filas, 
columnas y canales (si la imagen es a color):"""

print(img.shape)

 
"""Nota
Si la imagen es a escala de grises, la tupla regresada contiene únicamente el número de filas y columnas. 
Así que es un buen método para verificar si la imagen cargada está a escala de grises o es una imagen a color.


Se accede al número total de píxeles por medio de img.size:"""

#print(img.size)

"El tipo de datos (datatype) de la imagen se obtiene por medio de img.dtype:"

#print(img.dtype)

 
"""Nota
img.dtype es muy importante al momento de la depuración porque un gran número de errores en el código 
OpenCV-Python son causados por tipos de datos inválidos.

 
                                Dividiendo y Combinando Canales de Imagen

Los canales R,G,B de una imagen pueden dividirse en sus planos individuales cuando sea necesario. Luego, 
puede combinarse nuevamente dichos canales para nuevamente formar una imagen:"""

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

#O

b = img[:,:,0]

"""Supongamos que quieres hacer que todos los píxeles rojos valgan cero, no necesitas dividirlos todos 
de esta forma y colocarlos igual a cero. Puedes simplemente usar indexación Numpy la cual es más rápida."""

img[:,:,2] = 0

 
"""  Advertencia
cv2.split() es una operación costosa (en términos de tiempo), así que sólo utilízala si es necesario. 
La indexación Numpy es mucho más eficiente y debería usarse siempre que sea posible.

Haciendo Bordes para la Imagen (Padding)

Si deseas crear un borde alrededor de una imagen, algo como un marco, puedes usar la función 
cv2.copyMakeBorder(). Pero tiene más aplicaciones para la operación de circonvolución, zero padding, 
etc. Esta función toma los siguientes argumentos:

    src – introducir imagen
    top, bottom, left, right – ancho de borde en número de píxeles en correspondencia con las direcciones.
    borderType – Marca que define el tipo de borde a añadir. Puede ser de los siguientes tipos:
        BORDER_CONSTANT – Añade un borde de color constante. El valor debería ser provisto como el siguiente argumento.
        BORDER_REFLECT – El border será el reflejo de sus elementos, como este: fedcba|abcdefgh|hgfedcb
        BORDER_REFLECT_101 or cv2.BORDER_DEFAULT – Igual que arriba, pero con un pequeño cambio, como este: 
            gfedcb|abcdefgh|gfedcba
        BORDER_REPLICATE – El último elemento es replicado alrededor, así: aaaaaa|abcdefgh|hhhhhhh
        BORDER_WRAP – No puedo explicarlo, luciría así: cdefgh|abcdefgh|abcdefg

 

    valor – El color del borde si el tipo de borde es cv2.BORDER_CONSTANT

Más abajo hay una muestra del código demostrando todos estos tipos de borde para su mejor entendimiento:"""

from matplotlib import pyplot as plt

BLUE = [255,0,0]
img1 = cv2.imread('opencv.jpg')
replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()

#Fíjate en el resultado debajo. (La imagen se expone usando matplotlib. Así que los planos del ROJO y el 
#AZUL están intercambiados):