"""
                        REPRESENTACIÓN GRÁFICA DE DATOS EN PYTHON: GRÁFICAS CIRCULARES CON “matplotlib”.


programacionpython80889555	algoritmos, calculo, matemáticas, matplotlib, programación en python, programacion, python, software	
junio 25, 2019	2 Minutes	

Saludos, una semana más. Bienvenidos a vuestro sitio sobre programación en Python. En ocasiones anteriores hemos visto distintos 
modos de representar, gráficamente datos, con “matplotlib“. En esta ocasión vamos a dibujar una gráfica circular, perfecta para 
representar porcentajes.

Se trata de un ejercicio muy sencillo en el que, únicamente, vamos a necesitar importar la librería “matplotlib“, con el nombre 
“plt“:

Antes de crear nuestra gráfica, empezaremos definiendo los datos que queremos representar, empezando por las etiquetas de los 
elementos a representar (en forma de porciones de la gráfica). Como vamos a crear una gráfica dividida en 6 porciones, que llevarán 
por nombre, las 6 primeras letras del alfabeto, vamos incluir en una lista (a la que llamaremos “etiquetas“) dichos caracteres:

Dado que, en una gráfica de estas características, lo que representamos es el porcentaje que ocupa cada elemento, en un todo,
 pasaremos a establecer tales porcentajes, nuevamente, a través de una lista, a la que daremos el nombre de “porcentas“:

A fin de que nuestra gráfica sea visualmente expresiva, debemos asignar un color a cada una de las porciones de nuestra gráfica,
 otra vez, en una lista, de nombre “colores“:

Con esto, ya tenemos definidos los atributos necesarios, para cada una de las porciones de nuestra gráfica. A partir de aquí, 
lo que haremos será crear la gráfica en la que tales atributos se van a plasmar:

Para ello, emplearemos el método “.pie()” al que, en primer lugar, pasaremos como argumentos, los porcentajes de nuestros 
segmentos/porciones (“porcentas“), sus etiquetas “labels“) y los colores de cada uno (“colors“). Tras ello, incluiremos una 
serie de atributos que definirán ciertas cualidades geométricas de la gráfica: “startangle“. Que es la que determina el angulo 
con respecto al eje “x” desde el cual, se empieza a dibujar las porciones que componen la gráfica, “explode“. Que es una matriz 
que especifica la fracción del radio con la que se establece cada cuña, “radius“. Que determina el radio del la gráfica circular 
(la cual, si no se especifica será de 1 por defecto) y “autopct“. Consistente en una función o string para etiquetar cada porción 
con su valor numérico.

Finalmente, podemos darle un título a nuestra gráfica con la función “.title()“:

Hecho ello, podremos visualizar la gráfica (“plt.show()“) con los datos introducidos:


"""
#IMPORTAMOS "matplotlib".
import matplotlib.pyplot as plt 

#DEFINIMOS ETIQUETAS  
etiquetas = ['A', 'B', 'C', 'D', 'E', 'F'] #labels

#PORCENTAJE DE CADA PORCIÓN.
porcentas = [14,3,8,6,9,7]

#DEFIMIMOS COLORES
colores = ['#1abc9c', '#f1c40f', '#8e44ad', '#e74c3c', '#34495e', '#3498db'] #LabelColor

#DIBUJAMOS GRÁFICA.  
plt.pie(porcentas, labels = etiquetas, colors=colores,
        startangle=90, explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1),
        radius = 1.2, autopct = '%1.2f%%')

#TITULO
plt.title('Gráfica Circular')

#MOSTRAMOS GRÁFICA.
plt.show()