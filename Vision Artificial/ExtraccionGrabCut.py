"""                             Extracción interactiva en primer plano utilizando el algoritmo GrabCut
 
Teoría

El algoritmo GrabCut fue diseñado por Carsten Rother, Vladimir Kolmogorov y Andrew Blake de Microsoft Research Cambridge, Reino U
nido. En su artículo, “GrabCut”: extracción interactiva en primer plano utilizando cortes iterativos de gráficos, se necesitaba un 
algoritmo para la extracción en primer plano con una mínima interacción del usuario, y el resultado fue GrabCut.

¿Cómo funciona desde el punto de vista del usuario? Inicialmente, el usuario dibuja un rectángulo alrededor de la región del primer
 plano (la región del primer plano debe estar completamente dentro del rectángulo). Luego, el algoritmo lo segmenta de forma 
 iterativa para obtener el mejor resultado.  Sin embargo, en algunos casos, la segmentación puede no estar bien. Por ejemplo,
 puede haberse marcado alguna región de primer plano como fondo y viceversa. En ese caso, el usuario debe hacer retoques finos. 
 Sólo debe dar algunos trazos en las imágenes donde hay algunos resultados defectuosos. Strokes básicamente dice “Oye, esta 
 región debe estar en primer plano, la marcó en segundo plano, corrígela en la siguiente iteración” o su opuesto en segundo 
 plano. Luego, en la siguiente iteración, obtienes mejores resultados.

Ver la imagen a continuación. El primer jugador y el fútbol están encerrados en un rectángulo azul. Luego se realizan algunos 
retoques finales con trazos blancos (que denotan el primer plano) y trazos negros (que denotan el fondo). Y obtenemos un buen 
resultado.

¿Pero, qué ha ocurrido por detrás?

    El usuario ingresa el rectángulo. Todo lo que esté fuera de este rectángulo se tomará como fondo seguro (es por eso que se 
    menciona antes que su rectángulo debe incluir todos los objetos). Todo dentro del rectángulo es desconocido. De forma similar, 
    cualquier entrada de usuario que especifique el primer plano y el fondo se considera de etiqueta dura, lo que significa que 
    no cambiará en el proceso.
    El algoritmo realiza un etiquetado inicial con los datos que proporcionamos. Etiqueta los píxeles de primer plano y de fondo 
    (o etiquetas duras)
    Ahora se usa un Modelo de Mezcla Gaussiana (MGM) para modelar el primer plano y el fondo.
    Según los datos que proporcionamos, GMM aprende y crea una nueva distribución de píxeles. Es decir, los píxeles desconocidos 
    están etiquetados como primer plano probable o fondo probable dependiendo de su relación con los otros píxeles con etiqueta 
    dura en términos de estadísticas de color (es como la agrupación en clúster).
    Un gráfico se construye a partir de esta distribución de píxeles. Los nodos en los gráficos son píxeles. Se agregan dos nodos
    adicionales, nodo Fuente y nodo Sumidero. Cada píxel de primer plano está conectado al nodo Fuente y cada píxel de fondo está 
    conectado al nodo Sumidero.
    Los pesos de los bordes que conectan los píxeles al nodo de origen / nodo final se definen por la probabilidad de que un píxel 
    sea de primer plano / fondo. Los pesos entre los píxeles están definidos por la información de borde o la similitud de píxeles. 
    Si hay una gran diferencia en el color del píxel, el borde entre ellos obtendrá un peso bajo.
    Luego, se usa un algoritmo mincut para segmentar el gráfico. Corta el gráfico en dos nodos de origen separadores y receptores 
    con una función de costo mínimo. La función de costo es la suma de todos los pesos de los bordes que se cortan. Después del 
    corte, todos los píxeles conectados al nodo Fuente se convierten en primer plano y los conectados al nodo Sumidero se 
    convierten en fondo.
    El proceso continúa hasta que la clasificación converge.

Este proceso se ilustra en la imagen de abajo (tomado de: http://www.cs.ru.ac.za/research/g02m1682/)

GrabCut en OpenCV

Ahora vamos a por el algoritmo de Grabcut con OpenCV. OpenCV tiene la función, cv2.grabCut() para esto. Primero veamos sus 
argumentos:

img : Imagen de entrada
mask: es una imagen de máscara donde especificamos qué áreas son fondo, primer plano o fondo probable / primer plano, etc. Se 
realiza mediante los siguientes indicadores, cv2.GC_BGD, cv2.GC_FGD, cv2.GC_PR_BGD, cv2.GC_PR_FGD, o simplemente pasando 0,1,2,3 
a la imagen.
rect: Son las coordenadas de un rectángulo que incluye el objeto de primer plano en el formato (x, y, w, h)
bdgModel, fgdModel – Estas son matrices utilizadas internamente por el algoritmo.
iterCount: número de iteraciones que debe ejecutar el algoritmo.
mode: debe ser cv2.GC_INIT_WITH_RECT o cv2.GC_INIT_WITH_MASK o combinado, que decide si estamos dibujando trazos de retoque 
rectangulares o finales.

Primero veamos con el modo rectangular. Cargamos la imagen, creamos una imagen de máscara similar. Creamos fgdModel y bgdModel. 
Le damos los parámetros rectangulares. Todo es sencillo. Deje que el algoritmo se ejecute durante 5 iteraciones. El modo debe 
ser cv2.GC_INIT_WITH_RECT ya que estamos usando un rectángulo. A continuación, ejecute el Grabcut. Modifica la imagen de la 
máscara. En la nueva imagen de máscara, los píxeles se marcarán con cuatro banderas que denotan fondo / primer plano como se 
especifica arriba. Así que modificamos la máscara de modo que todos los píxeles 0 y 2 se pongan a 0 (es decir, fondo) y todos 
los píxeles 1 y 3 se pongan a 1 (es decir, píxeles de primer plano). Ahora nuestra máscara final está lista. Simplemente 
multiplíquelo con la imagen de entrada para obtener la imagen segmentada."""
 

import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('messi.jpeg')
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (50,50,450,290)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
plt.imshow(img),plt.colorbar(),plt.show()

"""Vea el resultado a continuación:

Oops, el cabello de Messi se ha ido. ¿A quién le gusta Messi sin su cabello? Necesitamos traerlo de vuelta. Entonces haremos un 
retoque fino con 1 píxel (primer plano seguro). Al mismo tiempo, parte de la tierra ha llegado a la imagen que no queremos, y 
también algún logotipo. Necesitamos eliminarlos. Ahí damos un retoque de 0 píxeles (fondo seguro). Por lo tanto, modificamos 
nuestra máscara resultante en el caso anterior tal como lo dijimos ahora.

Lo que realmente hice fue que abrí la imagen de entrada en el Paint y agregué otra capa a la imagen. Usando la herramienta de 
pincel del Paint, marqué el primer plano perdido (cabello, zapatos, pelota, etc.) con fondo blanco y no deseado (como logotipo, 
suelo, etc.) con negro en esta nueva capa. Luego llené el fondo restante con gris. Después, cargué esa imagen de máscara en 
OpenCV, y edité la imagen de máscara original que obtuvimos con los valores correspondientes en la imagen de máscara recién 
añadida. Verifica el código a continuación:"""
 

# newmask es la máscara etiquetada manualmente
newmask = cv2.imread('newmask.png',0)
# donde sea que esté marcado en blanco (primer plano seguro), cambiar mask=1
# donde sea que esté marcado en negro (fondo seguro), cambiar mask=0
mask[newmask == 0] = 0
mask[newmask == 255] = 1
mask, bgdModel, fgdModel = cv2.grabCut(img,mask,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)
mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask[:,:,np.newaxis]
plt.imshow(img),plt.colorbar(),plt.show()

"""Vea el resultado a continuación:
Aquí, en lugar de inicializar en modo rect, puede pasar directamente al modo de máscara. Simplemente marque el área del 
rectángulo en la imagen de la máscara con 2-pixel o 3-pixel (fondo probable / primer plano). Luego marque nuestro sure_
foreground con 1 píxel como lo hicimos en el segundo ejemplo. A continuación, aplique directamente la función GrabCut con 
el modo de máscara."""