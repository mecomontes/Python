"""                                                             Tkinter – Ventanas


Bienvenidos a la clase n° 1 de interfaces graficas con python y su libreria Tkinter, veremos que es una ventana, como crearla y
 personalizarla.
Objetivo del 2º tutorial de Curso de Interfaz Gráfica con TKinter

Aprender a crear ventanas con TKinter

Aprender a personalizar ventanas
¿Qué es una ventana en Tkinter?

Una ventana es un área visual rectangular, la cual contendrá todos nuestros iconos, botones, cuadros de entrada de texto, entre 
otros. Existen dos tipos: las ventanas de aplicación, que inician y finalizan las aplicaciones gráficas, y las ventanas de dialogo,
 que permiten la comunicación simple con el usuario, ambas formando la interfaz de usuario.
¿Cómo importar el módulo Tkinter?

De la misma forma de llamar un módulo en python se utiliza el módulo Tkinter:

    from tkinter import * 

Con esta instrucción le decimos a python que emplearemos todo los componentes del módulo Tkinter.

    import tkinter as tk

Así le decimos a python de emplearemos el módulo tkinter y los llamaremos tk, cada vez que se utiliza algún elemento de Tkinter, 
debe estar precedido de tk.

Ejemplos:

    from tkinter import * 
    raiz = Tk()

    import tkinter as tk
    raiz = tk.Tk()

Creación de la primera ventana y métodos de personalización

La programación GUI es un arte, y como todo arte, necesitas un tablero de dibujo para capturar tus ideas. El tablero de dibujo 
que utilizará se llama ventana raíz. Nuestro primer objetivo es tener lista la ventana raíz.

La siguiente imagen muestra la ventana raíz que podemos crear:

Dibujar la ventana raíz es sencillo. Sólo necesita las siguientes tres líneas de código:

    from tkinter import *
    raiz = Tk()
    raiz.mainloop()

Guardamos el código con la extensión .py y lo ejecutamos. Este programa debería generar una ventana raíz en blanco, como se 
muestra en la imagen anterior. Esta ventana está equipada con la función de minimizar, maximizar, y cerrar botones, y un marco 
en blanco.

    La primera línea de código importamos el módulo tkinter, todos sus métodos y atributos
    La segunda línea creamos una clase llamada raíz del tipo Tk
    La tercera línea llamamos el método mainloop el cual es el que mantiene visible la ventana raíz. Si se elimina esta línea la 
    ventana no se mantendrá visible

Siempre el código debe terminar con el método mainloop.

Ahora, como personalizamos esta ventana, de igual forma como llamamos el método mainloop existen métodos que nos permiten cambiar 
el tamaño, el nombre a la ventana, el icono, el color de fondo, entre otros.

Para cambiar el nombre de la ventana solo debemos llamar el método title, el cual debemos pasarle como parámetro el nombre, le 
colocaremos, por ejemplo Primera Ventana

    from tkinter import *
    raiz = Tk()
    raiz.title("Primera Ventana") #Cambiar el nombre de la ventana
    raiz.mainloop()

El nombre debe ir entre comillas dobles, guardamos y ejecutamos el código:

Y observamos que, cambia el nombre de nuestra ventana.

Para cambiar el tamaño llamamos al método geometry el cual necesita que le demos un alto y ancho de nuestra ventana:

    from tkinter import * 
    raiz = Tk() 
    raiz.title("Primera Ventana") #Cambiar el nombre de la ventana 
    raiz.geometry("520x480") #Configurar tamaño
    raiz.mainloop() 

De igual forma debe estar entre comillas dobles y los valores deben estar en pixeles.

El icono que se muestra en la esquina superior izquierda se puede cambiar llamando el método iconbitmap, pasándole entre comillas 
doble el nombre de la imagen que debe estar con la extensión .ico y en el mismo lugar donde se tiene el programa. Por ejemplo se 
creo un icono con el nombre de form.ico.

    from tkinter import * 
    raiz = Tk() 
    raiz.title("Primera Ventana") #Cambiar el nombre de la ventana 
    raiz.geometry("520x480") #Configurar tamaño
    raiz.iconbitmap("form.ico") #Cambiar el icono
    raiz.mainloop() 

Ejecutamos:

 

Existe el método llamado config, el cual nos permite configurar múltiples aspectos de la ventana, y otros elementos. Para cambiar 
el color de fondo le pasamos como parámetros las letras bg seguidas de un igual y dentro de comillas dobles, el color en inglés o 
en formato hexadecimal. Las letras bg vienen de la palabra background.

¡Excelente! Con lo aprendido en este modulo podemos crear ventanas personalizadas para nuestras aplicaciones en python ? pasa a la 
siguiente lección del curso de Interfaz Gráfica con TKinter donde veremos los widgets, frames y el método pack():"""

from tkinter import * 
raiz = Tk() 
raiz.title("Primera Ventana") #Cambiar el nombre de la ventana 
raiz.geometry("520x480") #Configurar tamaño 
raiz.iconbitmap("icono.ico") #Cambiar el icono 
raiz.config(bg="gray") #Cambiar color de fondo
raiz.mainloop() 