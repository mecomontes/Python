"""                                                         Teoría

La transformada de Fourier se utiliza para analizar las características de frecuencia de varios filtros. Para las imágenes, la 
transformada discreta de Fourier 2D (DFT, por sus siglas en inglés) se utiliza para encontrar el dominio de frecuencia. Para el 
cálculo de la DFT se utiliza un algoritmo rápido llamado Transformada Rápida de Fourier (o Fast Fourier Transform en inglés, 
abreviado como FFT). Los detalles al respecto se pueden encontrar en cualquier libro de texto de procesamiento de imágenes o 
procesamiento de señales.

Para una señal sinusoidal de la forma:

podemos decir que f es la frecuencia de la señal, y si su dominio de frecuencia es tomado, podemos ver un pico en f. Si la señal 
es muestreada para formar una señal discreta, obtenemos el mismo dominio de frecuencia, pero periódica en el rango [-pi, pi] o 
[0, 2pi] (o [0, N]  para N puntos de la DFT). Una imagen se puede considerar como una señal muestreada en dos direcciones. Así 
que tomar transformada de fourier en ambas direcciones X e Y da la representación de frecuencia de la imagen.

Más intuitivamente, para la señal sinusoidal, si la amplitud varía muy rápido en poco tiempo, se puede decir que es una señal de
 alta frecuencia. Si varía lentamente, es una señal de baja frecuencia. Se puede extender la misma idea a las imágenes. ¿Dónde
 varía drásticamente la amplitud en las imágenes? En los puntos extremos, o ruidos. Así podemos decir que los bordes y los ruidos 
 son contenidos de alta frecuencia en una imagen. Si no hay muchos cambios en la amplitud, se trata de una componente de baja 
 frecuencia.

Veamos entoces cómo encontrar el Transformador de Fourier.


                                                    Transformada de Fourier en Numpy

Primero veremos cómo encontrar Transformada de Fourier usando Numpy. Numpy tiene un paquete FFT para hacer esto. La función 
np. fft. fft2() nos proporciona la transformación de frecuencia, la cual será una matriz compleja. Su primer argumento es la 
imagen de entrada, que deberá estar en escala de grises. El segundo argumento es opcional y decide el tamaño de la matriz de 
salida. Si es mayor que el tamaño de la imagen de entrada, la imagen de entrada se rellena con ceros antes del cálculo de FFT. 
Si es inferior a la imagen de entrada, se recortará la imagen de entrada. Si no se pasa ningún argumento, el tamaño de la matriz 
de salida será igual al de la entrada.

Una vez obtenido el resultado, la componente de frecuencia cero (componente DC) estará en la esquina superior izquierda. Si 
quieres ponerlo en el centro, necesitas desplazar el resultado en N/2 en ambas direcciones. Esto se hace simplemente con la
 función np. fft. fftshift() (Es más fácil de analizar). Una vez que se encuentre la transformación de frecuencia, se puede
 encontrar el espectro de magnitudes."""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('nadal.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitudFFT = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Imagen de entrada'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitudFFT, cmap = 'gray')
plt.title('FFT'), plt.xticks([]), plt.yticks([])
plt.show()

"""En la imagen de la derecha se puede apreciar una región más blanca en el centro mostrando que el contenido de baja frecuencia 
es mayor.

Ya encontramos la transformación de frecuencia Ahora podemos hacer algunas operaciones en el dominio de la frecuencia, como el 
filtrado de paso alto y la reconstrucción de la imagen original, es decir, encontrar DFT inverso. Para eso, simplemente, se debe 
eliminar las bajas frecuencias utilizando una máscara formada por una ventana rectangular (en este caso utilizaremos una de tamaño
 60×60). A continuación, se aplica el desplazamiento inverso utilizando np.fft.ifftshift() para que el componente de DC vuelva a
 aparecer en la esquina superior izquierda. Luego se encuentra la FFT inversa utilizando la función np.ifft2(). El resultado, de
 nuevo, será un número complejo, del cual puedes tomar su valor absoluto."""

img = cv2.imread('nadal.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(np.abs(fshift), cmap = 'gray')
plt.title('Filtro'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back,cmap = 'gray')
plt.title('Transformada inversa'), plt.xticks([]), plt.yticks([])
plt.show()

"""El resultado muestra que el Filtro Pasa Altos es una operación de detección de bordes. Esto es lo que hemos visto en el 
capítulo de Gradientes de imagen. Esto también muestra que la mayoría de los datos de imagen están presentes en la región de 
baja frecuencia del espectro. Hasta aquí hemos visto cómo encontrar DFT, IDFT, etc. en Numpy. Ahora veamos cómo hacerlo en OpenCV.

Aunque en este ejemplo no se observa mucho,  este procedimiento puede causar artefactos en la imagen final, conocidos como 
efectos de llamada (call effects en inglés). Estos efectos son causados por la ventana rectangular que utilizamos para enmascarar.
 El problema es causado al coveritr esta máscara a la forma seno. Por lo tanto, no es aconsejable utilizar ventanas rectangulares 
 para filtrar. En su lugar, la mejor opción es utilizar ventanas Gausianas.
 
 
                                                         Transformada de Fourier en OpenCV

OpenCV está provista con las funciones cv2.dft() y cv2.idft() para esto. Estas funciones devuelven el mismo resultado que las 
anteriores, pero con dos canales. El primer canal tendrá la parte real del resultado y el segundo canal tendrá la parte imaginaria
 del resultado. La imagen de entrada se debe convertir a np.float32 primero. Veamos un ejemplo de cómo hacerlo."""

img = cv2.imread('nadal.jpg',0)
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Imagen de entrada'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('FFT'), plt.xticks([]), plt.yticks([])
plt.show()

"""El resultado de este código es exactamente el mismo que utilizando la función de Numpy.
Nota:  También puede utilizar cv2.cartToPolar() que devuelve tanto la magnitud como la fase al mismo tiempo.
Entonces, ahora tenemos que hallar la DFT inversa. En la sesión anterior, creamos un Filtro Pasa Altos (FPA), esta vez veremos 
cómo eliminar los contenidos de alta frecuencia en la imagen, es decir, aplicamos un Filtro Pasa Bajos (FPB) a la imagen. El 
resultado de aplicar este tipo de filtro es una imagen desenfocada. Para esto, creamos una máscara primero con un valor alto (1) 
a bajas frecuencias, es decir, pasamos el contenido de baja fecuencia y 0 a la región altas frecuencia."""


img = cv2.imread('nadal.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)
# Crea la máscara primero, el centro del cuadrado vale 1, el resto son ceros
mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1
# Aplica la máscara y la DFT inversa
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Imagen de entrada'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('DFT'), plt.xticks([]), plt.yticks([])
plt.show()

"""Nota:  Como es habitual, las funciones de OpenCV cv2.dft() y cv2.idft() son más rápidas que las contrapartes de Numpy, pero 
las funciones de Numpy son más fáciles de usar.


                                                        Optimización del rendimiento de DFT

El rendimiento del cálculo DFT es mejor para algunos tamaños de matriz. Es más rápido cuando el tamaño de la matriz es potencia 
de dos. Las matrices cuyo tamaño es un producto de 2, 3 y 5 también se procesan de manera bastante eficiente. Por lo tanto, si 
le preocupa el rendimiento de su código, puede modificar el tamaño de la matriz a cualquier tamaño óptimo (rellenando con ceros) 
antes de encontrar la DFT. Para OpenCV, debe agregar ceros manualmente. Pero para Numpy, sólo necesitas especificar el nuevo 
tamaño del cálculo de FFT, y automáticamente este rellenará los ceros que falten por usted.

Entonces, ¿cómo encontramos este tamaño óptimo? OpenCV proporciona una función, cv2.getOptimalDFTSize() para esto. Es aplicable 
tanto a cv2.dft() como a np.fft.fft2(). Comprobemos su rendimiento usando el comando mágico de Python: % timeit."""
 

img = cv2.imread('nadal.jpg',0)
rows,cols = img.shape
print(rows,cols)

nrows = cv2.getOptimalDFTSize(rows)
ncols = cv2.getOptimalDFTSize(cols)
print(nrows, ncols)
"""<em>240 216</em>

Nótese que el tamaño (238, 212) se modifica a (240,216). Para aumentar el tamaño de la matriz rellenaremos con ceros los espacios 
nuevos. Esto puede hacerse creando una nueva matriz de ceros más grande (en este caso de dimensiones 240×216 )  y copiando los 
datos en ella, o utilizando cv2.copyMakeBorder().

nimg = np.zeros((nrows,ncols))
nimg[:rows,:cols] = img


right = ncols - cols
bottom = nrows - rows
bordertype = cv2.BORDER_CONSTANT #sólo para evitar la ruptura de línea en un archivo PDF
nimg = cv2.copyMakeBorder(img,0,bottom,0,right,bordertype, value = 0)

Ahora comparemos el rendimiento DFT de la función de Numpy con los dos tamños de matriz:"""

timeit_fft1 = np.fft.fft2(img)
#100 loops, best of 3: 3.64 ms per loop
timeit_fft2 = np.fft.fft2(img,[nrows,ncols])
#100 loops, best of 3: 2.18 ms per loop

#El resultado muestra una aceleración de ~1.5x. Ahora intentaremos lo mismo con las funciones de OpenCV.

timeit_dft1= cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)
#1000 loops, best of 3: 732 µs per loop
timeit_dft2= cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)
#1000 loops, best of 3: 324 µs per loop

"""También se muestra una aceleración, en este caso de  más  de 2x. También puede observar que las funciones de OpenCV son 
alrededor de 5 veces más rápidas que las funciones de Numpy. Esto también se puede comprobar para la FFT inversa (se deja como 
ejercicio al lector).
¿Por qué Laplaciano es un filtro de paso alto?

Una de las respuestas a esta interrogante se ecuentra en la Transformada de Fourier. Simplemente tome la transformada de Fourier 
del filtro Laplaciano para un tamaño mayor de FFT y analícelo:"""

from matplotlib import pyplot as plt
# filtro promedio simple sin parámetro de escala
mean_filter = np.ones((3,3))
# crea un filtro Gaussiano
x = cv2.getGaussianKernel(8,2)
gaussian = x*x.T
# Diferentes filtros de detección de bordes
# scharr en la dirección X
scharr = np.array([[-3, 0, 3],
                   [-10,0,10],
                   [-3, 0, 3]])
# sobel en la dirección X
sobel_x= np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])
# sobel en la dirección Y
sobel_y= np.array([[-1,-2,-1],
                   [0, 0, 0],
                   [1, 2, 1]])
# laplaciano
laplacian=np.array([[0, 1, 0],
                    [1,-4, 1],
                    [0, 1, 0]])
filters = [mean_filter, gaussian, laplacian, sobel_x, sobel_y, scharr]
filter_name = ['filtro_media', 'gaussiano','laplaciano', 'sobel_x', \
                'sobel_y', 'scharr_x']
fft_filters = [np.fft.fft2(x,[200,200]) for x in filters]
fft_shift = [np.fft.fftshift(y) for y in fft_filters]
mag_spectrum = [np.log(np.abs(z)+1) for z in fft_shift]
#
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(mag_spectrum [i],cmap = 'gray')
    plt.title(filter_name[i]), plt.xticks([]), plt.yticks([])
plt.show()

 
"""A partir de la imagen, se puede ver qué región de frecuencia bloquea cada núcleo y qué región pasa. A partir de esa 
información, podemos decir por qué cada núcleo es un FPB o un FPA."""