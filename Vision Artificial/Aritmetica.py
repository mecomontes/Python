"""                         Operaciones Aritméticas en Imágenes OpcenCV con Python


                                        Suma de Imágenes

Puedes sumar dos imágenes usando la función de OpenCV, cv2.add() o simplemente por medio de una operación numpy, 
res = img1 + img2. Ambas imágenes deberían tener la misma profundidad y tipo, o la segunda puede ser un valor escalar.

 
Nota
Existe una diferencia entre la suma OpenCV y la suma Numpy. La suma OpenCV es una operación saturada mientras que la 
suma Numpy es una operación modular.

Por ejemplo, considera esta ejemplo:"""

import numpy as np
import cv2

x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x,y)) # 250+10 = 260 => 255
print(x+y) # 250+10 = 260 % 256 =4

"""Será más visible cuando añadas dos imágenes. La función de OpenCV proveerá un mejor resultado. Así que siempre 
procura adherirte a las funciones de OpenCV.


                                          Fusión de Imágenes

Esto también es suma de imágenes, pero con diferentes pesos lo cual da una sensación de mezcla o transparencia. 
Las imágenes son sumadas mediante esta ecuación:

Variando  alfa de 0 a infinito, puedes efectuar una transición suave entre una imagen y la otra.

Aquí tomo dos imágenes para fusionarlas. A la primera le doy un peso de 0.7 y a la segunda uno de 0.3. cv2.addWeighted() 
aplico la siguiente ecuación sobre la imagen.

Aquí  gamma es tomado como cero."""

cv2.startWindowThread()

img1 = cv2.imread('python_logo.png')
img2 = cv2.imread('pirata.png')
print('tamaño imagen   ',img1.shape)
print('tamaño imagen   ',img2.shape)
img3=img1[1000:1430,2000:2840,:]
print('tamaño imagen   ',img3.shape)
dst = cv2.addWeighted(img3,0.7,img2,0.3,0)
cv2.imshow('dst',dst)
cv2.imwrite('dst.png',dst)

cv2.waitKey(5000)
cv2.destroyAllWindows()


"""Fíjate en los resultados a continuación:

                                            openCV fusion imagen
                                            Operaciones Bitwise

Esto incluye bitwise Y, O, NO y operaciones XOR. Serán muy útiles para extraer cualquier parte de la imagen (así como veremos
en los capítulos siguientes), definir y trabajar con un ROI no rectangular, etc. Abajo veremos un ejemplo de cómo cambiar 
una particular ROI.

Quiero colocar el logo de OpenCV sobre una imagen. Si agrego dos imágenes, cambiará de color. Si lo mezclo, obtengo un efecto 
de transparencia. Pero quiero que sea opaco. Si fuera una región rectangular podría usar ROI. Pero el logo de aprednderPython 
no es una forma rectangular. Así que puedes hacerlo con operaciones bitwise como se muestra a continuación:"""

 

import cv2
# cargamos 2 imagenes
img1 = cv2.imread('dst.png')
img2 = cv2.imread('aprendepython.png')
# Yo quiero poner el logo en el corner izquierdo y por eso creo un ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
# Ahora creo una máscara de logotipo y hago su máscara inversa también
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 250, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
# Ahora pongo oscura el área de logotipo en ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
# Tome solamente la región del logotipo de la imagen del logotipo
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
# Ponga el logotipo en ROI y modifique la imagen principal
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.startWindowThread()

cv2.imshow('res',img1)
cv2.waitKey(1000)

cv2.destroyAllWindows()

cv2.startWindowThread()

cv2.imshow('res',roi )
cv2.waitKey(1000)

cv2.destroyAllWindows()

#Mira los resultados debajo. Para mejor comprensión, expón todas las imágenes intermedias expresadas en el código anterior, 
#especialmente img1_bg y img2_fg.