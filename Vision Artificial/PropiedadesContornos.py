"""                                         Propiedades de los contornos

Es la razón entre el ancho y la altura del contorno del objeto."""


import cv2
x,y,w,h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h

"""                                                 Extensión

La extensión es la razón entre el área del contorno y el área del rectángulo delimitador."""

area = cv2.contourArea(cnt)
x,y,w,h = cv2.boundingRect(cnt)
rect_area = w*h
extension = float(area)/rect_area

"""                                                  Solidez

La solidez es la razón entre el área del contorno y el área de su envoltura convexa."""

area = cv2.contourArea(cnt)
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidez = float(area)/hull_area


"""                                                   Diámetro equivalente

Es el diámetro del círculo cuya área es igual que el área del contorno."""

area = cv2.contourArea(cnt)
equi_diametro = np.sqrt(4*area/np.pi)


"""                                                     Orientación

La orientación es el ángulo que forma el eje mayor de la elipse circunscrita  al objeto, con la dirección horizontal. El siguiente 
método también da las longitudes del Eje Mayor y del Eje Menor de dicha elipse."""

(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)


"""                                                 Máscara y número de píxeles

En algunos casos es muy útil crear una máscara del objeto de interés. Adicionalmente, puede resultar útil conocer los puntos que 
conforman el objeto. Ambas operaciones se pueden hacer de la siguiente manera:"""

mask = np.zeros(imgray.shape,np.uint8)
cv2.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
#pixelpoints = cv2.findNonZero(mask)

"""Ambos métodos mostrados conducen al mismo resultado. El primero utiliza funciones Numpy, mientras que el segundo utiliza la 
función OpenCV (última línea comentada). Auqnue los resultados de los dos métodos son iguales, existe una ligera diferencia entre 
ellos. Numpy da las coordenadas en formato (fila, columna), mientras que OpenCV da coordenadas en formato (x, y). Así que 
básicamente las respuestas serán intercambiadas. Tenga en cuenta que, row = x y column = y.

Valores mínimo y máximo y sus respectivas coordenadas

Estos valores pueden encontrarse utilizando una máscara de la imagen:"""

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imgray,mask = mask)

"""Color medio o Intensidad media

Aquí podemos encontrar el color medio de un objeto. O puede ser la intensidad media del objeto en modo de escala de grises. De 
nuevo usamos la misma máscara para hacerlo."""

mean_val = cv2.mean(im,mask = mask)

"""                                                      Puntos extremos

Los puntos extremos son cuatro y se corresponden con: el punto superior, el inferior, el derecho y el izquierdo de la imagen."""

izquierdo = tuple(cnt[cnt[:,:,0].argmin()][0])
derecho = tuple(cnt[cnt[:,:,0].argmax()][0])
superior = tuple(cnt[cnt[:,:,1].argmin()][0])
inferior = tuple(cnt[cnt[:,:,1].argmax()][0])


"""                                                      Defectos de convexidad

En entradas anteriores hemos visto el concepto de envoltura convexa. Cualquier desviación del objeto de esta envoltura puede 
considerarse como defecto de convexidad.

OpenCV viene con una función ya hecha para encontrar esto, cv2.convexityDefects(). A continuación un ejemplo de cómo llamar a 
esta función:"""

#Carga la imagen
img = cv2.imread('test.jpg',0)
#Determina los contornos
ret,thresh = cv2.threshold(img,120,255,0)
image,contours, hierarchy = cv2.findContours(thresh,1,2)
cnt = contours[0]
#Halla los defectos de convexidad
envoltura = cv2.convexHull(cnt,returnPoints = False)
defectos = cv2.convexityDefects(cnt,envoltura)

"""Nota 
Recuerde que debe pasar returnPoints = False,  cuando determine la envoltura convexa, a fin de encontrar defectos de convexidad.
La función cv2.convexityDefects() devuelve una matriz con los siguientes valores en sus filas: las coordenadas inicial y final de 
los puntos contiguos de mayor convexidad, el punto más alejado (“el defecto“) de lo que debería ser el contorno convexo sin 
defectos y, la distancia  hasta este punto. En el siguiente ejemplo se ilustra el significado de cada uno de estos puntos. Para 
ello dibujamos una línea (amarilla) que una los puntos de mayor convexidad, luego dibujamos un círculo (rojo) en el punto más 
lejano."""

   
#Carga la imagen
img = cv2.imread('estrella.png')
#Convierte la imagen a escala de grises
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
#Determina los contornos
image,contours, hierarchy = cv2.findContours(thresh,1,2)
cnt = contours[0]
#Determina los defectos de convexidad
envoltura = cv2.convexHull(cnt,returnPoints = False)
defectos = cv2.convexityDefects(cnt,envoltura)
#Dibuja la envoltura convexa y los defectos de convexidad
for k in range(defectos.shape[0]):
    i,f,l,d = defectos[k,0]
    inicio= tuple(cnt[i][0])
    fin= tuple(cnt[f][0])
    lejos = tuple(cnt[l][0])
    cv2.line(img,inicio,fin,[0,255,255],2)
    cv2.circle(img,lejos,5,[0,0,255],-1)
#Muestra la imagen final
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Guarda la imagen
cv2.imwrite('def_convexidad.png',img)


"""                                                 Prueba de polígono de puntos

Esta función encuentra la distancia más corta entre un punto de la imagen y su contorno. Esta distancia es negativa si el punto 
está fuera del contorno, positiva si está dentro y cero si está sobre el contorno.

Por ejemplo, podemos comprobar el punto (30,30) de la siguiente manera:"""

dist = cv2.pointPolygonTest(cnt,(30,30),True)

"""Aquí, el tercer argumento de la función es measureDist. Si es True, encuentra la distancia mínima explicada anteriormente. Si es 
Falso, entonces la función devuelve +1, -1 ó 0, indicando que el punto está dentro, fuera o sobre el contorno, respectivamente.

Nota 
Si no desea encontrar la distancia, asegúrese de que el tercer argumento es False, porque este es un proceso que consume mucho 
tiempo. De hecho, fijando el tercer argumento como False, la función corre de dos a tres veces más rápido.


                                                     Haciendo coincidir formas

Otra interesante función de OpenCV es cv2.matchShapes() que nos permite comparar dos formas, o dos contornos y devuelve una métrica
que muestra la similitud. Cuanto menor sea el resultado, más similares serán las imágenes comparadas. Se calcula sobre la base de 
los valores de los momentos invariantes de Hu."""


#Carga ambas imágenes que se desean comparar
img1 = cv2.imread('estrella.png',0)
img2 = cv2.imread('estrella2.png',0)
#Determina los contornos de ambas imágenes
ret, thresh = cv2.threshold(img1, 127, 255,0)
images,contours,hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours[0]
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
images,contours,hierarchy = cv2.findContours(thresh2,2,1)
cnt2 = contours[0]
#Calcula la similitud entre ambas imágenes y muestra el resultado
ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print(ret)

"""Más bajo se muestran los resultados obtenidos al comparar las siguientes imágenes:

Resultados de comparación:Imagen A con ella misma = 0.0
Imagen A con la imagen B = 0,001946
Imagen A con imagen C = 0.326911Note que incluso la rotación de la imagen no afecta mucho a esta comparación.

Nota 
Los Momentos de Hu son siete momentos invariantes a la traslación, la rotación y la escala. Estos valores se pueden encontrar 
utilizando la función cv2.HuMoments()."""


"""                                                             Jerarquía

Como se ha señalado anteriormente, el objetivo principal de la función cv2.findContours() es detectar objetos en una imagen. 
Aunque muchas veces los objetos están en lugares diferentes, en algunos casos, algunas formas están anidadas dentro de otras 
formas. En este último escenario, se llama padres (parents) a los contornos más externos e hijos (children) a los contornos 
contenidos en los anteriores. De esta manera, los contornos de una imagen tienen cierta relación entre sí. Utilizando esta 
definición se puede especificar cómo los contornos están conectados entre sí, por ejemplo, especificando si un contorno es 
hijo de otro, o por el contrario su padre. Es precisamente la representación de esta relación a lo que se llama Jerarquía.

A continuación se muestra un ejemplo donde esta idea queda más clara:

En esta imagen hay algunas formas, numeradas de 0 a 5.  2 y 2a denotan los contornos externo e interno de la caja más externa,
 respectivamente.

Aquí, los contornos 0,1,2 son externos o ultraperiféricos. Podemos decir que están en jerarquía-0 o simplemente que están en el 
mismo nivel de jerarquía.

Luego viene el contorno-2a, que puede considerarse como un hijo del contorno-2 (o en sentido opuesto, el contorno-2 es el padre 
del contorno-2a). Estos definen la jerarquía-1.

Del mismo modo el contorno-3 es hijo de contorno-2 y pertenece a la siguiente jerarquía, 2.

Finalmente, los contornos 4 y 5 son los hijos del contorno-3a, y forman el último nivel de jerarquía, 3.

Debido a la manera en que están eumeradas las cajas, se podría estar tentado a pensar que el contorno-4 es el primer hijo del 
contorno-3a. Sin emabrgo, el contorno-5  también podría ser el primer hijo.

Con este ejemplo quedan claros conceptos tales como: mismo nivel de jerarquía, contorno externo, contorno hijo, contorno padre, 
primer hijo, etc. Ahora estamos listos para ver estos conceptos en OpenCV.


                                                    Representación de Jerarquías en OpenCV

Como se ha visto, cada contorno tiene su propia información sobre a qué jerarquía pertenece, quién es su hijo, quién es su padre, 
etc. OpenCV representa esta información como una matriz de cuatro valores: [Next, Previous, First_Child, Parent]. Esta matriz es 
la tercera salida de la función cv2.findContours().
Next (siguiente)

Next indica el siguiente contorno en el mismo nivel jerárquico. Por ejemplo, consideremos el contorno-0 de la imagen anterior. 
}¿Cuál es el siguiente contorno en su mismo nivel? Es el contorno-1. Por lo tanto Next = 1. De manera similar, para contorno-1, el
    siguiente es contorno-2. Por consiguiente Next = 2.

En el caso del contorno-2, como no hay siguiente contorno en el mismo nivel, Next = -1. Por otra parte, el contorno-4, está en 
el mismo nivel del contorno-5. Así que su siguiente contorno es contorno-5, luego Next = 5.
Previous (anterior)

Previous indica el contorno anterior en el mismo nivel jerárquico. Por ejemplo, el contorno anterior del contorno-1 es el 
contorno-0 en el mismo nivel. Del mismo modo para el contorno-2, es el contorno-1. Para el contorno-0, no hay anterior, así que 
Previous=-1.


                                                                First_Child (primer hijo)

First_Child denota el primer contorno hijo. Por ejemplo, para contorno-2, el hijo es contorno-2a. Así que First_Child tendrá el 
valor de índice correspondiente del contorno-2a. Por otro lado, el contorno-3a tiene dos hijos. Sin embargo, sólo se toma el
 primer hijo, que es el contorno-4. Así que First_Child = 4 para el contorno-3a. Por último, si no hay hijos, como en el caso 
 del contorno-4 o 5, First_Child=-1.


                                                                        Parent (padre)

Parent indica el índice del controno padre. Es justo lo opuesto de First_Child. Tanto para el contorno-4 como para el contorno-5, 
el contorno padre es el contorno-3a. Para contorno-3a, es contorno-3 y así sucesivamente. Si no hay contorno padre, como en el 
caso del contorno-0, Parent=-1.
Modos de recuperación de contorno:

Ahora que ya sabemos sobre el estilo de jerarquía utilizado en OpenCV, podemos entender los modos de recuperación de controno en 
OpenCV, con la ayuda de la misma imagen anteriormente utilizada. Veamos el significado de las banderas cv2.RETR_LIST,
 cv2.RETR_TREE, cv2.RETR_CCOMP y cv2.RETR_EXTERNAL.
 
 
                                                                         RETR_LIST

Esta es la más simple de las cuatro banderas (desde el punto de vista de la explicación). Simplemente, recupera todos los 
contornos, pero no crea ninguna relación padre-hijo. Los padres y los hijos son iguales bajo esta regla, y son sólo contornos. 
Es decir, todos ellos pertenecen al mismo nivel jerárquico.

Así que el 3er y 4to término en la matriz de jerarquía, correspondientes a First_Child y Parent, respectivamente, serán siempre -1.
 Obviamente, los términos Next y Previous tendrán sus valores correspondientes. 

A continuación se muestra el resultado obtenido al utilizar la bandera RETR_LIST. En cada fila están los detalles de la jerarquía
 del contorno correspondiente. Por ejemplo, la primera fila corresponde al contorno-0. El siguiente contorno es el contorno-1. 
 Así que Next = 1. No hay contorno anterior, así que Previous = -1. Los dos términos restantes, como se explicó anteriormente, 
 serán -1.

    print(hierarchy)

([[[ 1, -1, -1, -1],
   [ 2,  0, -1, -1],
   [ 3,  1, -1, -1],
   [ 4,  2, -1, -1],
   [ 5,  3, -1, -1],
   [ 6,  4, -1, -1],
   [ 7,  5, -1, -1],
   [-1,  6, -1, -1]]])

Esta es una buena opción, si no se está usando ninguna característica de jerarquía.
RETR_EXTERNAL

Si utiliza este indicador, sólo se devuelven indicadores externos extremos. Los contornos hijos no se tendrán en cuenta. Podemos decir, bajo esta ley, que sólo el mayor en cada familia es conservado. 

Por lo tanto, en nuestra imagen, sólo tendremos 3 contornos, corrspondientes al nivel de jerarquía 0. Es decir, sólo se tendrán en cuenta los contornos 0,1,2. A continuación se muestra el resultado de utilizar esta bandera a la imagen de prueba:

    print(hierarchy)

([[[ 1, -1, -1, -1],
   [ 2,  0, -1, -1],
   [-1,  1, -1, -1]]])

Este indicador es útil si se desea extraer sólo los contornos exteriores.


                                                                        RETR_CCOMP

Este indicador recupera todos los contornos y los organiza en una jerarquía de dos niveles. Es decir, los contornos externos del 
objeto (es decir, su frontera) se colocan en la jerarquía-1. Y los contornos de los agujeros dentro del objeto (si los hay) se 
colocan en la jerarquía-2.

Basta con considerar la imagen de un “gran cero blanco” sobre un fondo negro. El círculo exterior al cero pertenece a la primera 
jerarquía, y el círculo interno del cero pertenece a la segunda jerarquía.

Para qe quede más clara la idea, se utilizará la siguiente imagen, donde se ha etiquetado el orden de los contornos en color rojo 
y la jerarquía a la que pertenece, en color verde (1 o 2). El orden es el mismo que el orden en el que OpenCV detecta los 
contornos.

Por ejemplo, en la imagen se puede ver que el contorno-0 es de jerarquía-1, ya que tiene dos agujeros, los contornos 1 y 2, 
que por lo tanto son de jerarquía-2.  Bajo esta estructura, el contorno siguiente al contorno-0, en el mismo nivel de jerarquía, 
es el contorno-3, por tanto Next=3.  Por otro lado, Previous=-1, ya que no existe un contorno anterior. Finalmente, su primer 
hijo es contorno-1 en jerarquía-2. No tiene padre, porque está en jerarquía-1. Así que su matriz jerárquica sería [3, -1,1, -1].

El contorno-1, por otra parte, está en jerarquía-2. El siguiente en la misma jerarquía (bajo la paternidad del contorno-1) es 
contorno-2. No tiene contorno anterior ni hijos, pero el padre es contorno-0. Así que la matriz de jerarquía será [2, -1, -1,0].

Del mismo modo para el contorno-2 se tendrá: jerarquía-2, no contorno siguiente, contorno anterior el contorno-1, ningún hijo y 
contorno padre el contorno-0. Por tanto la matriz será [-1,1, -1,0].

Contorno-3: Siguiente en jerarquía-1 es contorno-5. Anterior es el contorno-0. El hijo es contorno-4 y ningún padre. Así que la 
matriz será [5,0,4, -1].

Contorno-4: Está en jerarquía-2 bajo contorno-3 y no tiene hermano. Así que no hay siguiente, no hay anterior, no hay hijo y el 
padre es el contorno-3. Así que la matriz de jerarquía para este contorno será [-1, -1, -1,3].

Aplicando este indicador a la imagen de arriba, el resultado que se obtiene es el siguiente:

    print(hierarchy)

([[[ 3, -1,  1, -1],
   [ 2, -1, -1,  0],
   [-1,  1, -1,  0],
   [ 5,  0,  4, -1],
   [-1, -1, -1,  3],
   [ 7,  3,  6, -1],
   [-1, -1, -1,  5],
   [ 8,  5, -1, -1],
   [-1,  7, -1, -1]]])


                                                                    RETR_TREE

Este indicador recupera todos los contornos y crea una lista completa de jerarquías familiares. Incluso cuenta, quién es el abuelo,
 padre, hijo, nieto,etc.

Por ejemplo,utilicemos la misma imagen anterior pero ahora indicando la jerarquía que devuelve la bandera  cv2.RETR_TREE. De nuevo,
 las letras rojas dan el número de contorno y las letras verdes dan el orden de la jerarquía.

Veamos algunos ejemplos:

contorno-0: Está en jerarquía-0. El siguiente contorno en la misma jerarquía es el contorno-7. No hay contornos anteriores. El 
hijo es el contorno-1  y no hay padre. Entonces la matriz de jerarquía es [7, -1,1, -1].

contorno-2: Está en jerarquía-1. No hay contornos en el mismo nivel. No anterior. El hijo es el contorno-2 y el padre es el 
contorno-0. Así que la matri para este contorno es [-1, -1,2,0].

Intenta obtener los restantes por tu cuenta y compara tus resultados con la respuesta correcta, que se muestra a continuación:

    print(hierarchy)"""