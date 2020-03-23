"""                                                 Tkinter – Label, Entry, método place y grid

Bienvenidos a la clase n° 4 de interfaces graficas de usuario con python y la libreria Tkinter, veremos que son los Label, los 
Entry y 2 métodos de posicionamiento de widgets como lo son place y grid.

Objetivo del 4º tutorial de Curso de Interfaz Gráfica con TKinter

Aprender sobre los Labels en Tkinter

Modificar labels en programas de ejemplo
¿Qué son los Label?

Son widgets de etiquetas que se utilizan para mostrar texto o imágenes. Por ejemplo:

La sintaxis para crear los label es la siguiente:

nombre_del_label = Label( contenedor, text=“ ”)

Llamamos a la clase Label(), le pasamos como parámetros el contenedor donde estará, y por último el texto que mostrará, entre 
comillas dobles.

El código de la ventana anterior es el siguiente"""

from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Yo soy un Label") #Creación del Label
mi_Label.pack()
raiz.mainloop()

"""El label está contenido dentro del Frame y le pasamos como texto “Yo soy un Label”.

Le cambiaremos el color de fondo a uno blanco, para ello nuevamente utilizamos el método config con el parámetro bg = “white”."""

from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Yo soy un Label") #Creación del Label
mi_Label.pack()
mi_Label.config(bg="white") #Cambiar color de fondo
raiz.mainloop()

"""Ejecutamos:

Para los label existen parámetros que podemos configurar dentro del método config entre ellos el tipo de fuente, el color del 
texto, el tamaño, el margen de relleno, entre otros

Cambiar el tipo de fuente necesita que le demos como valores el nombre de la fuente y el tamaño.

Sintaxis

font = (‘nombre_fuente’, tamaño)"""

from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Yo soy un Label") #Creación del Label
mi_Label.pack()
mi_Label.config(bg="white") #Cambiar color de fondo
mi_Label.config(font=('Arial', 44)) #Cambiar tipo y tamaño de fuente
raiz.mainloop()

"""Ejecutamos:

Para cambiar el color del texto empleamos como parámetros fg = “color”, fg de foreground."""

from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Yo soy un Label") #Creación del Label
mi_Label.pack()
mi_Label.config(bg="white") #Cambiar color de fondo
mi_Label.config(font=('Arial', 44)) #Cambiar tipo y tamaño de fuente
mi_Label.config(fg="red") #Cambiar color del texto
raiz.mainloop()

"""Ejecutamos:

Para que las letras no estén muy pegada al borde, le agregamos un margen de relleno o padding. El método config acepta dos
 parámetros el padx y el pady

padx: margen de relleno en el eje x, acepta valores en pixeles

pady: margen de relleno en el eje y, acepta valores en pixeles

En el código anterior:"""

from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Yo soy un Label") #Creación del Label
mi_Label.pack()
mi_Label.config(bg="white") #Cambiar color de fondo
mi_Label.config(font=('Arial', 44)) #Cambiar tipo y tamaño de fuente
mi_Label.config(fg="red") #Cambiar color del texto
mi_Label.config(padx=20, pady=20) #Agregar margen de relleno
raiz.mainloop()

"""Ejecutamos:

¿Qué son los Entry?

Son widgets de entrada, que un usuario puede emplear para introducir texto en nuestra interfaces gráfica, por ejemplo:

     

La sintaxis es la siguiente:

nombre_entry = Entry( contenedor )

Los Entry son útiles para mostrar información y pueden desactivarse para que el usuario no puede alterar su valor, además están 
limitados a solo una línea de entrada.

Llamamos a la clase Entry() y le pasamos el contenedor donde estará, en este caso el Frame. El código del programa anterior es:"""

from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Esto es un Entry") #Creación del Label
mi_Label.pack()
mi_Entry = Entry(mi_Frame) #Creación de Entry
mi_Entry.pack()
raiz.mainloop()

"""Podemos configurar el color de la barra del texto, la dirección, podemos desactivarlo, entre otros.
Efecto 	Parámetros
Cambiar color de la barra del texto 	insertbackground=”color”
Cambiar dirección del texto 	justify=RIGHT
Desactivar un entry 	state=DISABLED

Llamaremos al método config."""

from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Esto es un Entry") #Creación del Label
mi_Label.pack()
mi_Entry = Entry(mi_Frame) #Creación de Entry
mi_Entry.pack()
mi_Entry.config(insertbackground="red") #Cambiar color del texto
mi_Entry.config(justify=RIGHT)
raiz.mainloop()

"""Ejecutamos

Creamos otro entry y lo desactivamos"""

from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Esto es un Entry") #Creación del Label
mi_Label.pack()
mi_Entry = Entry(mi_Frame) #Creación de Entry
mi_Entry.pack()
mi_Entry.config(insertbackground="red") #Cambiar color del texto
mi_Entry.config(justify=RIGHT) #Dirección del texto
mi_Entry2 = Entry(mi_Frame)
mi_Entry2.pack()
mi_Entry2.config(state=DISABLE) #Desactivar un Entry
raiz.mainloop()

"""Ejecutamos el código:

Los entry son de mucha utilidad como veremos más adelante.
Método place y grid

Ya habíamos hablado del método pack para el empaquetamiento y posicionamiento de los widgets dentro de nuestra ventana raíz, los 
inconvenientes se presentan al querer tener dos elementos alineados uno al lado del otro ya que como hemos visto pack me los 
coloca uno debajo del otro. Para ello empleamos el método place que nos permite establecer posiciones relativa o absolutas a otra 
ventanas.

Este método necesita como parámetros los valores ‘x’ y ‘y’ en pixeles.

Sintaxis

objeto.place(x=’valor’, y=’valor’)

Por ejemplo para posicionar un Label y un Entry"""

from tkinter import *
raiz = Tk()
mi_Frame = Frame(raiz, width=500, heidht=250)
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Metodo place")
mi_Label.place(x=50, y=10)
mi_Entry = Entry(mi_Frame) #Creación de Entry
mi_Entry.place(x=150, y=10)
raiz.mainloop()

"""En el código anterior se le dio un tamaño al Frame, al usar el método place se le dio al Label una posición en x de 50 pixeles 
y en y una posición de 10 pixeles. Para el Entry se le dio en x 150 pixeles y en y 10 pixeles.

Pero este método también trae algunos inconvenientes, se debe calcular constantemente los pixeles para posicionar.

El método grid es uno de los más empleados y fáciles de utilizar a la hora de empaquetar y posicionar objetos. Ya que recibe como 
parámetros row y column, es decir filas y columnas, convirtiendo los widgets en una tabla bidimensional.

Por ejemplo:
	columna 0 	columna 1 	columna 2 	columna 3
fila 0 	(0,0) 	(0,1) 	(0,2) 	(0,3)
fila 1 	(1,0) 	(1,1) 	(1,2) 	(1,3)
fila 2 	(2,0) 	(2,1) 	(2,2) 	(2,3)
fila 3 	(3,0) 	(3,1) 	(3,2) 	(3,3)

La sintaxis en la siguiente:

objeto.grid(row= ‘valor’, column= ‘valor’)

En el código"""

from tkinter import *
raiz = Tk()
mi_Frame = Frame(raiz)
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Metodo grid")
mi_Label.grid(row=0, column=0)
mi_Entry = Entry(mi_Frame) 
mi_Entry.grid(row=0, column=1)
raiz.mainloop()

"""Posicionamos el Label en la fila 0, columna 0 y el Entry en misma fila, pero en la columna 1.

Ejecutamos:

Redimensionando la ventana

De esta manera los widgets se pueden posicionar correctamente de una manera más facil dentro del Frame y la ventana raíz.

¡Felicidades! Ya aprendimos que son los Label, Entry y dos metodos de posicionamiento nuevos  ? pasa a la siguiente lección del 
curso de Interfaz Gráfica con TKinter donde elaboraremos nuestra primer formulario simple con todos los elementos que hemos 
aprendido.:"""