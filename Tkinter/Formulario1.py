"""                                                             Tkinter – Proyecto 1


Bienvenidos al curso de interface de graficas de usuario con python y la libreria Tkinter, crearemos un formulario simple con todo 
lo que hemos aprendido del curso.
Objetivo del 5º tutorial de Curso de Interfaz Gráfica con TKinter

Mezclar todo lo aprendido hasta ahora en nuestro curso

Crear un formulario básico

Por Ejemplo:

Para ello comenzamos a crear una ventana raíz, llamando a la clase Tk(), le daremos un tamaño con el método geometry de unos 
300×200 pixeles, le colocamos como título “Formulario Simple” y le cambiaremos el icono de la ventana."""

from tkinter import *
raiz = Tk()
raiz.geometry("300x200")
raiz.title("Formulario Simple")
raiz.mainloop()

"""Ejecutamos:

Ahora creamos un Frame y lo empaquetamos."""

from tkinter import *
raiz = Tk()
raiz.geometry("300x200")
raiz.title("Formulario Simple")
miFrame= Frame()
miFrame.pack()
raiz.mainloop()

"""Creamos nuestra primera fila la cual contendrá la palabra bienvenido, le daremos un tamaño, tipo de fuente y la posicionaremos 
en la fila 0, columna 0."""

from tkinter import *
raiz = Tk()
raiz.geometry("300x200")
raiz.title("Formulario Simple")
miFrame= Frame()
miFrame.pack()
bienvenido = Label(miFrame, text="BIENVENIDO")
bienvenido.grid(row=0, column=0)
bienvenido.config(font=('Arial', 16))
raiz.mainloop()

"""Para la segunda fila crearemos una etiqueta Label y un Entry y los posicionaremos uno al lado del otro. Al Label le agregamos 
un margen de relleno de 10 pixeles en ambas direcciones."""

from tkinter import *
raiz = Tk()
raiz.geometry("300x200")
raiz.title("Formulario Simple")
miFrame= Frame()
miFrame.pack()
bienvenido = Label(miFrame, text="BIENVENIDO")
bienvenido.grid(row=0, column=0)
bienvenido.config(font=('Arial', 16))
nombre_label= Label(miFrame, text="Cual es tu nombre:")
nombre_label.grid(row=1, column=0)
nombre_label.config(padx=10, pady=10)
cuadro_nombre=Entry(miFrame)
cuadro_nombre.grid(row=1, column=1)
raiz.mainloop()

"""Ejecutamos y observamos los que hemos realizado.

Repetimos el proceso y creamos dos Label y dos Entry más. Uno para el apellido y el otro para la dirección. Recuerda posicionarlos 
correctamente."""

from tkinter import *
raiz = Tk()
raiz.geometry("300x200")
raiz.title("Formulario Simple")
miFrame= Frame()
miFrame.pack()
bienvenido = Label(miFrame, text="BIENVENIDO")
bienvenido.grid(row=0, column=0)
bienvenido.config(font=('Arial', 16))
#-----Seccion de Nombre-----
nombre_label= Label(miFrame, text="Cual es tu nombre:")
nombre_label.grid(row=1, column=0)
nombre_label.config(padx=10, pady=10)
cuadro_nombre=Entry(miFrame)
cuadro_nombre.grid(row=1, column=1)
#-----Seccion de Apellido-----
apellido_label=Label(miFrame, text="Cual es tu apellido: ")
apellido_label.grid(row=2, column=0)
apellido_label.config(padx=10, pady=10)
cuadro_Apellido=Entry(miFrame)
cuadro_Apellido.grid(row=2, column=1)
#-----Seccion de Dirección-----
direccion=Label(miFrame, text="Dirección: ")
direccion.grid(row=3, column=0)
direccion.config(padx=10, pady=10)
cuadro_Direccion=Entry(miFrame)
cuadro_Direccion.grid(row=3, column=1)
raiz.mainloop()

"""Ejecutamos el código y observemos los resultados

De momento este formulario no posee ningún botón, selección de opciones, cuadro de texto pero a medida que avancemos el curso lo 
iremos mejorando.

¡Felicidades por llegar hasta aquí! Los formularios son una parte importante en los programas de desarrollo de escritorio ? pasa 
a la siguiente lección del curso de Interfaz Gráfica con TKinter donde crearemos una interfaz más avanzada:"""