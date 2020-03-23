"""                                         Tkinter – Widgets, Frame y método pack()


Bienvenidos a la clase n° 3 de interfaces graficas de usuario con python y su libreria Tkinter, conoceremos que son los widgets, 
Frame y el método de posicionamiento pack().
Objetivo del 3º tutorial de Curso de Interfaz Gráfica con TKinter

Trabajar con los  widgets de TKinter

Crear Frames y utilizar el método pack()
¿Qué son los widgets en Tkinter?

Ya sabemos cómo realizar y personalizar nuestra ventana raíz, ahora debemos pensar que componentes deben aparecer en ella. En 
Tkinter, estos componentes se llaman widgets y existen 21 tipos principales:
    
Toplevel widget 	Label widget 	Button widget
Canvas widget 	Checkbutton widget 	Entry widget
Frame widget 	LabelFrame widget 	Listbox widget
Menu widget 	Menubutton widget 	Message widget
OptionMenu widget 	PanedWindow widget 	Radiobutton widget
Scale widget 	Scrollbar widget 	Spinbox widget
Text widget 	Bitmap Class widget 	Image Class widget

La mayoría se explicara a medida que avancemos en el curso
¿Qué es un frame?

Un Frame es un widget, que sirve como una especie de contenedor para los demás widgets, dentro de la ventana raíz. Para crear
 nuestro primer frame creamos una ventana raíz como lo hemos realizado anteriormente y antes del mainloop creamos un objetos 
 llamado mi_Frame y le asignamos la clase Frame(), pero no basta solo crearlo hay que empaquetarlo, es decir le decimos al frame 
 que debe estar dentro de la ventana raíz, para ello llamamos al método pack(), este frame no tiene un tamaño, color de fondo, 
 bordes, tipo de borde, entre otros."""

from tkinter import *
raiz = Tk()
mi_Frame = Frame() #Creación del Frame
mi_Frame.pack() #Empaquetamiento del Frame
raiz.mainloop()

"""Al ejecutar el anterior código observamos que hemos creado el frame sin ningún tipo de tamaño

Para personalizar el frame utilizamos el método config que empleamos anteriormente. Cambiaremos el tamaño, color de fondo, el 
tipo 
de borde, el grosor del borde, y el efecto que al pasar el cursor.
Efecto 	Sintaxis

Cambiar el tamaño 	mi_Frame.config(width=”400″, height=”200″)
Cambiar color de fondo 	mi_Frame.config(bg=”blue”)
Cambiar grosor del borde 	mi_Frame.config(bd=24)
Cambiar el tipo de borde 	mi_Frame.config(relief=”sunken”)
Cambiar el cursor 	mi_Frame.config(cursor=”heart”)

Para cambiar el tamaño le proporcionamos un alto y ancho en pixeles con width y height, con bd que viene de borderwidth, el 
tamaño del borde, relief el tipo de borde o relieve, cursor el tipo de forma que tendrá el cursor al pasar por encima del frame. 
Toda esta sintaxis y los tipos de parámetros que recibe el método config para diferentes widgets está más ampliada en la 
documentación de tkinter.

https://docs.python.org/3/library/tkinter.html

www.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf

http://effbot.org/tkinterbook/

Guardamos y ejecutamos el siguiente código"""

from tkinter import * 
raiz = Tk()
mi_Frame = Frame() #Creacion del Frame
mi_Frame.pack()  #Empaquetamiento del Frame
mi_Frame.config(bg="blue") #cambiar color de fondo 
mi_Frame.config(width="400", height="200") #cambiar tamaño
mi_Frame.config(bd=24) #cambiar el grosor del borde
mi_Frame.config(relief="sunken")   #cambiar el tipo de borde
mi_Frame.config(cursor="heart")    #cambiar el tipo de cursor 
raiz.mainloop()

"""Observamos que hemos creado efectivamente el frame con un color de fondo azul, un tamaño especifico, un grosor del borde, el 
tipo de borde, y al colocar el cursor encima del frame cambia a un corazón valor dado al parámetro cursor.
Método pack()

El método pack() es un tipo de posicionamiento para los widgets que ajusta todo los elementos acomodándolos entre sí, para luego 
hacer la ventana raíz tan grande para contener todos estos elementos. Por ejemplo en el código anterior al ejecutar vemos que la 
ventana raíz se ajusta al tamaño del frame.

Este método también tiene opciones de configuración como son fill, expand, side, entre otros. Para utilizarlos dentro del método 
pack, entre paréntesis colocamos los parámetros a configurar, por ejemplo.
Parámetros 	Valores
mi_Frame.pack(fill=”valor”) 	‘x’, ‘y’, ‘both’, ‘none’
mi_Frame.pack(expand=”valor”) 	0, 1, “True”, “False”
mi_Frame.pack(side=”valor”) 	‘left’, ‘right’, ‘top’, ‘bottom’

En el código:"""

from tkinter import * 
raiz = Tk()
mi_Frame=Frame()
mi_Frame.pack(fill="x") #Configurar el metodo pack()
mi_Frame.config(bg="blue")
mi_Frame.config(width="150", height="150")
raiz.mainloop()

"""Al redimensionar la ventana observamos que el tamaño del frame se aumenta en la dirección x

Con expand, le añade un espacio adicional a medida que se redimensiona la ventana raíz:"""

from tkinter import * 
raiz = Tk()
mi_Frame=Frame()
mi_Frame.pack(expand=1) #Configurar el metodo pack()
mi_Frame.config(bg="blue")
mi_Frame.config(width="150", height="150")
raiz.mainloop()

"También se puede emplear fill y expand ambas en el método pack()"

from tkinter import * 
raiz = Tk()
mi_Frame=Frame()
mi_Frame.pack(fill='x', expand=1) #Configurar el metodo pack()
mi_Frame.config(bg="blue")
mi_Frame.config(width="150", height="150")
raiz.mainloop()

"Con side, cambia la posición del widget dependiendo del valor dado:"

from tkinter import * 
raiz = Tk()
mi_Frame=Frame()
mi_Frame.pack(side='left') #Configurar el metodo pack()
mi_Frame.config(bg="blue")
mi_Frame.config(width="150", height="150")
raiz.mainloop()

"""Todos los widgets en Tkinter se deben de empaquetar, no solo existe el método pack, ya que este trae algunas desventajas al 
tener muchos elementos, está el método place() y grid() este último el más útil de todos como veremos más adelante.

En la proxima clase

¡Enhorabuena! Continua con nosotros para seguir aprendiendo sobre el desarrollo de aplicaciones de escritorio ? pasa a la 
siguiente lección del curso de Interfaz Gráfica con TKinter donde conoceremos que son los Label, los Entry, el método place() 
y grid():"""