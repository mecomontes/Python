"""Kivy con Python para el desarrollo de aplicaciones móviles


Bienvenido al tutorial de introducción a Kivy. Primero, ¿qué es Kivy? Kivy es un kit de desarrollo de aplicaciones multiplataforma 
que utiliza Python.

Esto significa que Kivy se ejecuta en iOS, Android, MacOS, Windows y Linux!

Con Kivy, también puede acceder a las API de los móviles, como la API de Android para manipular cosas como la cámara del teléfono,
 el sensor giroscópico, el GPS, el vibrador, etcétera.

Supongo que ya tienes algunas nociones de Python pero si eres nuevo en Python te recomendamos que pases por el Curso de aprender
 python – nivel principiante primero.

Para poder usar Kivy, también necesitarás PyGame y probablemente Cython en el futuro, aunque por ahora dejaremos eso fuera. PyGame 
es uno de los paquetes originales para crear juegos en Python. Hay un tutorial de PyGame aquí, si estas interesado en el desarrollo
 de juegos.

Para conseguir PyGame, y luego Kivy, vamos a usar pip. Mientras tengas una versión reciente de Python 2 o Python 3, ya tienes pip 
en tu sistema. Este tutorial se hace con Python 3, aunque deberías ser capaz de seguirlo junto con Python 2.

Abrir bash o cmd. exe, y hacer:

    pip install pygame
    pip install kivy

 

Una vez que Kivy se haya instalado con éxito, ¡estás listo para comenzar tu primer programa básico!

Kivy maneja muchos de los requisitos de backend por ti. Para cosas como dónde está el ratón, cómo debe reaccionar un botón al hacer
 clic o, incluso, cómo administrar varias pantallas, ¡Kivy te ayuda y protege!

Importamos Kivy App, seguida de un requisito para una versión Kivy. Esto no es necesario, pero es necesario si estás usando nuevas 
funciones de Kivy. Finalmente, extraemos la etiqueta de los paquetes UIX de Kivy."""

from kivy.app import App
kivy.require("1.8.0")
from kivy.uix.label import Label

"""Ahora creamos nuestra aplicación principal, llamada SimpleKivy. Estamos heredando de la clase App de Kivy. Nuestro método de 
construcción es un método esperado para Kivy. Dentro de nuestra construcción, sólo estamos devolviendo una simple Etiqueta, que 
está mostrando la típica aplicacion de empezar de “Hola Mundo”."""

class SimpleKivy(App):
    def build(self):
        return Label(text="Hello World!")

"""¿Confundido por “clase” o programación orientada a objetos? OOP ( programación orientada a objetos) es muy usado cuando se crean
 se crean cosas como GUIs interactivas (interfaces gráficas de usuario) o juegos.  Si está confundido acerca de OOP, consulta esta 
 intro a la programación orientado a objetos en Python."""

if __name__ == "__main__":
    SimpleKivy().run() 

#Ahora ejecutaremos el código. ¿Qué significa esto?

if __name__ == "__main__":
    SimpleKivy().run()

"""Deberías conseguir lo siguiente cuando ejecutes la aplicación:

Kivy ofrece documentación en su sitio web, pero Kivy también tiene extensos comentarios dentro del propio módulo de Python. Si
 quieres saber, por ejemplo, qué puedes hacer con esta “Etiqueta”, ¿por qué no la puedes ver en el módulo? Para hacer esto, ¿sabes 
 dónde buscar?

Los módulos de terceros son usualmente almacenados en el directorio /Lib/site-packages/ de tu instalación de Python. Sin embargo,
 si tienes problemas para encontrarlo, por lo general puedes conseguirlo haciendo algo como:

Eso le dará la ubicación de un módulo, que para mí es:

    C: \Python34\lib\site-packages\kivy\__init__. py

Eso es por lo menos donde está el __init__. py, pero estamos mayormente interesados en buscar en el directorio de Kivy.

Vemos que hemos importado la “Etiqueta” de kivy. uix. label, así que podemos asumir que encontraremos la Etiqueta dentro de 
kivy/uix/label. py.

Claro, ahí está. Ábrelo para editarlo, y mira todas esas opciones… y todos esos comentarios! Mucho más comentarios que código. Por 
lo tanto, si estás interesado en saber más sobre Kivy y sus aspectos, simplemente navega por tu instalación o consulta su 
documentación.

Hasta aquí la primera y sencilla parte de Kivy!"""