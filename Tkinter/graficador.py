#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from math import *

root = tkinter.Tk()
root.wm_title("Graficador")
ta=root.geometry("1000x700")

style.use('dark_background')

fig = Figure()
ax1 = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)# barra de iconos
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

funciones={"sin":"np.sin","cos":"np.cos","tan":"np.tan","log":"np.log",
           "pi":"np.pi","sqrt":"np.sqrt","exp":"np.exp"}

def reemplazo(s):
    for i in funciones:
        if i in s:
            s=s.replace(i, funciones[i])
    return s

act_rango=False
ul_ran=""
ran=""
    
def animate(i):
    global act_rango
    global ul_ran
    if act_rango==True:
        try:
            lmin = float(ran[0]); lmax = float(ran[1])
            if lmin < lmax:
                x = np.arange(lmin, lmax, .01)#.01
                ul_ran = [lmin, lmax]
            else:
                act_rango = False
        except:
            messagebox.showwarning("Error","Introduzca los valores del rango de x, separado por coma.")
            act_rango=False
            ets.delete(0,len(ets.get()))
    else:
        if ul_ran!="":
            x =np.arange(ul_ran[0],ul_ran[1], .01)#.01
        else:
            x =np.arange(1, 10, .01)#.01
    try:
        #print(graph_data)
        solo=eval(graph_data)
        ax1.clear()
        ax1.plot(x, solo)
    except:
        ax1.plot()
    ax1.axhline(0, color="gray")
    ax1.axvline(0, color="gray")
    ani.event_source.stop() #DETIENE ANIMACIÓN

def represent():
    global graph_data
    global ran
    global act_rango
    texto_orig=et.get()
    if ets.get()!="":
        rann=ets.get()
        ran=rann.split(",")
        act_rango=True
    graph_data=reemplazo(texto_orig)
    ani.event_source.start() #INICIA/REANUDA ANIMACIÓN
    
ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()

et = tkinter.Entry(master=root,width=60)
et.config(bg="gray87", justify="left")

button = tkinter.Button(master=root, text="SET", bg="gray69", command=represent)
button.pack(side=tkinter.BOTTOM)
#label=tkinter.Label(master=root, text="RANGO DE X")
#label.place(x=855,y=600)
et.pack(side=tkinter.BOTTOM)
ets=tkinter.Entry(master=root,width=10)
ets.pack(side=tkinter.RIGHT)

tkinter.mainloop()

tkinter.mainloop()


"""
https://programacionpython80889555.wordpress.com/2019/06/04/creando-graficador-de-funciones-con-matplotlib-tkinter-y-numpy/?fbclid=IwAR1GoVAY3P6xigsx_BpeMS5sWRP2gbQCMuffDf47lFBtG0BgqbQMD6dVtIc


                                    CREANDO GRAFICADOR DE FUNCIONES CON “matplotlib”, “tkinter” Y “numpy”.


programacionpython80889555	algoritmos, calculo, GUI, matemáticas, matemáticas con python, matplotlib, numpy, programación en 
python, programacion, python, software, tech, tkinter	junio 4, 2019	8 Minutes	

Bienvenidos una vez más, a “El Programador Chapuzas”. Aquellos que sigan este blog, recordarán que hace un tiempo, estuvimos 
viendo el modo de integrar una gráfica creada con “matplotlib“, en una ventana creada con “tkinter“. Por su parte, en una 
ocasión posterior, vimos también el modo de actualizar una gráfica “matplotlib” en tiempo real, a medida que íbamos cambiando 
los datos de entrada. Bien, en la presente ocasión, vamos a combinar los que aprendimos en aquellas 2 ocasiones, para crear un 
programa consistente en una ventana que representará la gráfica correspondiente a la función que introduzcamos en una entrada 
que se mostrará debajo de la gráfica:

   
                                                Representación de”sin(x)” para un rango de -10 a 10.

Como es natural, lo primero que haremos será crear la ventana que integre nuestra gráfica (que crearemos con “matplotlib“) con los 
elementos que emplearemos para introducir la función a representan (y también el rango de “x”) así como el botón “SET” que 
mostrará la representación (elementos, estos, creados con “tkinter“). No obstante, antes de iniciar esta labor, importaremos los 
recursos necesarios de las librerías “tkinter” (para los widgets), “matplotlib” (para mostrar la gráfica) y “numpy” (para efectuar 
los cálculos sobre las series de datos):

Ya que vamos a crear una ventana “tkinter” que contenga la gráfica, el siguiente paso será crear dicha ventana (a la que con 
“wm_title“) le daremos el nombre de nuestra aplicación “Graficador“. A su vez, también especificaremos las dimensiones de la 
misma (que serán adecuadas para una buena visualización gráfica):

Aunque podemos usar el que viene por defecto, también podemos especificar el estilo visual que va atener nuestra gráfica (para 
ello empleamos el la función “style.use()“) a la que pasaremos el nombre del estilo deseado (“fivethirtyeight” en nuestro caso). 
Para ver el listado de estilos disponibles usaremos el método “style.available” como se muestra a continuación:

    
                                                 Estilos de gráfica, disponibles.

Una vez escogido el estilo de la gráfica, procederemos a crear el objeto que la representará, el cual insertaremos en el área de 
dibujo que crearemos a continuación:

Para ver como esta quedando la aplicación, vamos a introducir la función para visualización de gráficas, “plt.show()“:

Si ahora ejecutamos lo hecho, obtendremos el siguiente resultado:

Como se ve, hasta ahora ya tenemos creada la ventana, con el área en el que se va a dibujar nuestra gráfica. Como dijimos antes, 
nuestro programa va a representar la gráfica correspondiente a la función que nosotros le proporcionemos (y si queremos, también 
dentro del rango que pidamos). Por ello, tendremos que dotar a nuestra ventana de dos espacios en los que podamos introducir la 
función y el rango (que se especificará mediante dos valores separados por una coma). Dichos espacios los ubicaremos en la parte 
inferior de la ventana:

Como se ve, hemos añadido una entrada (“Entry“) para la función a representar y otra para el rango (que se ubicará en la parte 
inferior derecha), acompañada de la etiqueta (“Label“) “RANGO DE ‘X'”. A su vez, también hemos creado un botón (“Button“) “SET” 
con el que ordenaremos a nuestro programa que cree la gráfica a partir de los datos introducidos en la entrada. Una vez creados 
los elementos, pasaremos a ubicarlos en la ventana con el método “.pack()“:

Con ello, tendríamos creados (y ubicados) los elementos para la introducción de datos en el programa. Sin embargo, tal y como
 está ahora mismo, si introdujésemos una expresión en la entrada, y le diéramos al botón “SET” veríamos que no ocurre nada, y 
 es que nos falta crear las funciones encargadas de tomar los datos introducidos y plasmarlos en la correspondiente gráfica.

Como lo que queremos es crear una gráfica que se actualice con los datos introducidos en las entradas (si abrir ni generar 
ventanas adicionales) usaremos una función (a la que llamaremos “animate()“), la cual, es la que vamos a pasar como argumento 
del método “FuncAnimation()“, de modo que los cambios y operaciones que realice dicha función (“animate()“) son los que se 
plasmarán en el transcurso de la actualización (a intervalos regulares) que llevará a cabo FuncAnimation(). Para ver como 
funciona esto, como ejemplo, vamos a hacer que nuestra función de actualización “animate()” imprima un mensaje:

Y ejecutamos.

Así, vendría ser como un ciclo “while” con la diferencia de que aquí podemos alterar la actividad de la función durante su 
ejecución cíclica.

Otra función que vamos a necesitar (a la que llamaremos “represent()“), es aquella que tome los datos introducidos en las 
entradas (tanto de la destinada a la función a representar, así como la destinada al rango de “x“) proporcionando las variables 
necesarias para que la gráfica sea posteriormente dibujada por la función “anim()” (que completaremos más adelante):

   
                                                                    Función “represent()”.

Antes de continuar, hemos de tener en cuenta que a la hora de introducir una entrada, el usuario introduzca, para , por ejemplo, 
representar el coseno de “x“, “cos(x)“. El problema con esto se encuentra en que para hacer dicho calculo con “numpy“, habría que 
introducir “np.cos(x)“. De modo que para evitar dicho problema, tendremos que hacer que el programa, recibiendo como entrada 
“cos(x)” lo traduzca internamente como “np.cos(x)“. Para ello, haremos uso de una nueva función (de nombre “reemplazo()” 
mediante la que añadiremos “np.” a las funciones que lo requieran para ser calculadas por “numpy“. Para usar tal función, nos 
valdremos, igualmente, de un diccionario (“funciones{}“) en el que incluiremos las funciones y su correspondiente cadena de 
reemplazo. La cadena resultante de esta función “reemplazo()” es la que finalmente guardaremos en la variable “graph_data“, 
que emplearemos para dibujar la gráfica:

    
                                                    Función “reemplazo()” y diccionario “funciones{}”.

La otra entrada que va a tomar “represent()” es la correspondiente al rango de “X”. Dado que más adelante vamos a necesitar tomar 
los dos valores del rango por separado, separaremos (usando “split()” empleando la coma “,” como separador) dichos valores 
(“ran=rann.split(“,”)“). Puesto que vamos a dar la posibilidad de que el usuario no especifique ningún rango (ets.get()=””) 
estableceremos que dicha acción consistente en la separación se produzca solo si no se da tal condición (“if ets.get()!=””“).


                            Representación de “cos(x)” para un rango no especificado (que por defecto será de 1 a 10).

Finalmente, haremos que esta función se ejecute al pinchar en el botón “SET“, por ello añadiremos a dicho botón “command=repesent“:
    
Ya tenemos creada la función “represent()“, encargada de tomar y preparar los datos de las entradas. Ahora le toca el turno a la
función “animate()“, que dibujará la gráfica y que se irá actualizando a intervalos regulares durante la ejecución. Dentro de la 
cual, empezaremos por la parte dedicada al rango:

Para empezar, la función distinguirá el hecho de que el usuario haya especificado un rango para “x” (“act_rango=True“) o no 
(“act_rango=False“). En el primer caso, nuestro programa creará dos variables (“lmin” y “lmax“) que serán los limites mínimo y 
máximo del rango de “x“, los cuales, se corresponden con las posiciones 0 y 1 de la lista “ran” generada en la función 
“represent()” ya vista. A su vez, para evitar resultados erróneos que pudieran derivarse del hecho de que en la entrada se 
introdujese un primer valor más alto que el segundo, el establecimiento del rango, con el método “np.arange()” solo se produzca 
en el caso de que, efectivamente el valor de “lmin” sea menor que el de “lmax” (“if lmin<lmax:“). Una vez que se haya completado 
esta operación de establecimiento del rango crearemos una nueva variable (“ul_ran“) que almacenará el citado rango, por un motivo 
que veremos más adelante.

Otro posible error que podría darse es que el usuario introdujese un dato arbitrario que no tuviera nada que ver con el 
establecimiento de un rango (por ejemplo, una palabra cualquiera). Es por ello, que hemos hecho uso de la sentencia “try“, 
de modo, que si el programa no pudiera funcionar con los datos proporcionados, se produjese una excepción (“except“) consistente 
en la muestra de una ventana de error, que crearemos introduciendo “messagebox.showwarning(“Error”,”Entrada no válida”)“. En 
este caso se borrará la entrada (“ets.delete(0,len(ets.get()))“), una vez cerrada la ventana de error, estableciéndose, 
automáticamente el último rango, válido, introducido (almacenado en “ul_ran“).


                                Ante una entrada para el rango no válida, el programa mostrará un mensaje de error.

Lo visto, sería para el caso en el que se haya especificado rango, en caso contrario, este será de 1 a 1o, si se trata de una 
primera ejecución (en donde “ul_ran==””“) o será el correspondiente al último rango introducido (si “ul_ran!=””“):

A continuación, nuestra función “animate()” pasará a trazar la gráfica correspondiente a la expresión que queremos representar, la 
cual, quedó definida en “represent()” y almacenada en la variable “graph_data“:

Puesto, que, al introducir la función a representar, cabe el mismo peligro que veíamos en el caso del rango, de introducir una 
cadena, imposible de ser tratada (con “eval“), usaremos una sentencia “try“. De modo que si a expresión es apta, se almacenará 
en un variable “calculo_funcion“, para acto seguido, ser representada gráficamente con el método “.plot()” para el valor actual
 de cada uno de los que vaya tomando la variable “x” (“ax1.plot(x,calculo_funcion)“). Si la expresión no es apta (“except“), el
 programa no empleará “graph_data“. Simplemente representará los valores por defecto (si no se he hecho una representación
 correcta previamente) o dejará la última representación realizada con éxito.
Si se introduce una cadena no válida, el programa mantendrá la última gráfica representada con éxito.

Finalmente, para una mejor visibilidad, hemos marcado los ejes “x” e “y” con un tono de gris (“gray“) mediante los procedimientos 
“axhline()” y “axwline()” respectivamente:

Y con esto tendríamos creado nuestro graficador de funciones, que nos permitirá visualizar gráficas correspondientes a funciones
 sencillas combinando los recursos proporcionados por las librerías “tkinter“, “matplotlib” y “numpy“:

Tenéis el código fuente en el siguiente enlace:

https://github.com/antonioam82/graficador/blob/master/graficador.py
INCLUYENDO BARRA DE HERRAMIENTAS:

No obstante aún podemos hacer más, como por ejemplo, incluir la barra de herramientas de “matplotlib” (que nos permitirá hacer 
cosas tales como hacer zoom, mover la imagen o guardar la gráfica creada) en la parte inferior de nuestro graficador. Para ello,
 lo primero que haremos será importar “NavigationToolbar2Tk” para después crear el objeto con la variable “toolbar“, tal y como 
 se ve en la siguiente captura:

A su vez, para que la ejecución continuada no interfiera en el posible manejo de la barra de herramientas, necesitaremos que tras
 cada nueva actualización de la gráfica, se detenga la animación. Para los cual incluiremos el método “event_source.stop()” al 
 final de la función “animate()“:

Sin embargo, una vez detenida la animación, necesitamos que esta se reanude posteriormente, si queremos dibujar una nueva gráfica.
 Es por ello que incluiremos el método “event_source.start()” en la función “represent()” (que se activará con el botón “SET“):

Esta versión mejorada del programa, que incluye la barra de herramientas de “matplotlib“, puede verse en el siguiente enlace:

https://github.com/antonioam82/graficador/blob/master/graficador_con_toolbar.py

Saludos."""