"""                                                             Pirámides de imágenes

Se llama pirámide de imágenes a un conjunto de imágenes con diferentes resoluciones, todas obtenidas a partir de una misma imagen 
inicial. El término de pirámide viene del hecho de que la imagen inicial (en la base) se va reduciendo a medida que se reduce su 
resolución, como ilustra la siguiente imagen:

Este tipo de tratamiento sobre la imagen tiene múltiples aplicaciones, como por ejemplo, reducción de ruido, análisis de textura, 
reconocimiento de objetos, etc.

Existen dos tipos de pirámides de imagen. 1) Pirámide Gaussiana y 2) Pirámides Laplacianas

Los niveles superiores (de baja resolución) en una pirámide gaussiana se forman eliminando filas y columnas consecutivas en las 
imágenes de nivel inferior (de mayor resolución). Por lo tanto, cada píxel en el nivel superior está formado por la contribución 
de 5 píxeles en el nivel subyacente con pesos gaussianos. Al hacerlo, una imagen MxN se convierte en una imagen de (M/2)x(N/2). 
Así que el área se reduce a una cuarta parte del área original (se le llama una octava). El mismo patrón continúa a medida que 
avanzamos en la pirámide (es decir, la resolución disminuye). Del mismo modo, mientras se expande, el área aumenta cuatro veces 
al bajar cada nivel. Las pirámides gaussianas pueden hallarse usando las funciones cv2.pyrDown() y cv2.pyrUp(). La primera 
función se utiliza para ir de un nivel más bajo a uno más alto en la pirámide y la segunda, para lo contrario."""

#img = cv2.imread('piramide.jpg')

#mayor_res=cv2.pyrUp(baja_res)

"""Sin embargo, si bien con la función anterior se recupera el tamaño de la imagen original, no es posible recuperar la 
resolución original. Esto se debe a que al reducir la resolución se pierde información de la imagen, que luego es imposile de 
recuperar. En el ejemplo siguiente se ha utilizado la función cv2.pyrUp() para recuperar la imagen más grande de las anteriores, 
a partir de la más pequeña.
Las Pirámides Laplacianas se forman a partir de las Pirámides Gaussianas. No hay una función exclusiva para realizar esta 
operación. Las imágenes de la pirámide laplaciana son imágenes de contorno solamente, o sea que la mayoría de sus elementos 
son ceros. Las pirámides laplacianas se utilizan en la compresión de imágenes. Un nivel en la Pirámide Laplaciana está formado 
por la diferencia entre ese nivel en la Pirámide Gaussiana y la versión expandida de su nivel superior en la Pirámide Gaussiana. 
Los tres niveles de un nivel Laplaciano se verán como a continuación (el contraste de las imágenes se ha ajustado para 
visualizarlas mejor):
    
Mezcla de imágenes usando pirámides

Una aplicación de las pirámides de imágenes es en la mezcla de imágenes. Por ejemplo, cuando se desean juntar dos imágenes,
 es usual que la zona de unión no se vea muy bien debido a las discontinuidades entre las imágenes. En ese caso, la unión de 
 imágenes con pirámides ofrece una mezcla casi perfecta ya que elimina muchos datos en las imágenes, difuminando así la zona 
 de unión. Un ejemplo clásico de esto es la mezcla de dos frutas, como por ejemplo: Manzana y Naranja, dando lugar a la 
 “Manzaranja”. Vea el resultado a continuación:

 

Los pasos a seguir para obtener el resultado anterior son:

    Cargar ambas imágenes, de la manzana y la naranja
    Encuentrar las Pirámides Gaussianas para cada imagen (en este ejemplo particular, el número de niveles es 6)
    Obtenga las Pirámides Laplacianasa partir de las Gaussianas (por sustracción de imágenes de distitos niveles)
    Unir la mitad izquierda de la manzana y la mitad derecha de la naranja en cada nivel de la Pirámide Laplaciana
    Finalmente, a partir de esta pirámide de imágenes conjuntas, reconstruir la imagen original.

A continuación se muestra el código completo. Por simplicidad, cada paso se realiza por separado, lo que puede requerir más 
memoria."""

import cv2
import numpy as np
A = cv2.imread('manzana.jpeg')
B = cv2.imread('naranja.jpeg')
# Genera una Pirámide Gaussiana para A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)
# Genera una Pirámide Gaussiana para B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)
# Genera una Pirámide Laplaciana para A
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    height, width = gpA[i-1].shape[:2]
    GE1=cv2.resize(GE, (width,height)) 
    L = cv2.subtract(gpA[i-1],GE1)
    lpA.append(L)
# Genera una Pirámide Laplaciana para B
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    height, width = gpB[i-1].shape[:2]
    GE1=cv2.resize(GE, (width,height)) 
    L = cv2.subtract(gpB[i-1],GE1)
    lpB.append(L)
#Adiciona la mitad izquierda de la imagen A con la mitad derecha de la imagen B 
#para cada nivel
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:round(cols/2)], lb[:,round(cols/2):]))
    LS.append(ls)
# Reconstruye la imagen final
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    height, width = LS[i].shape[:2]
    ls_=cv2.resize(ls_, (width,height)) 
    ls_ = cv2.add(ls_, LS[i])
# Imagen final mezclando directamente las dos imágenes iniciales (sin utilizar pirámides) 
real = np.hstack((A[:,:round(cols/2)],B[:,round(cols/2):]))
#Muestra la imagen de la "Naranzana"
cv2.imshow('image',ls_)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Guarda ambas imágenes de "Naranzana", la obtenida utilizando mezcla directa y la obtenida 
#utilizando pirámides.
cv2.imwrite('Mezcla_piramides.jpg',ls_)
cv2.imwrite('Mezcla_directa.jpg',real)