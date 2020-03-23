"""#guardar ficheros
#Puede ser \n (Unix) o \r\n (Windows). No obstante, en Python, cuando escribimos o leemos el carácter \n

r	Solo lectura. El fichero solo se puede leer. Es el modo por defecto si no se indica.
w	Solo escritura. En el fichero solo se puede escribir. Si ya existe el fichero, machaca su contenido.
a	Adición. En el fichero solo se puede escribir. Si ya existe el fichero, todo lo que se escriba se añadirá al final del mismo.
x	Como ‘w’ pero si existe el fichero lanza una excepción.
r+	Lectura y escritura. El fichero se puede leer y escribir.

 

Como te he indicado, todos estos modos abren el fichero en modo texto. Su versión correspondiente para abrir el fichero
en modo binario sería rb, wb, ab, xb, rb+.

Escribir un fichero de texto

Con todo lo anterior, si quisiéramos escribir un fichero de texto haríamos lo siguiente:"""

with open('mi_fichero', 'w') as f:
	f.write('Hola mundo\n')

"Escribir un fichero binario"

"Para escribir un fichero binario, simplemente añadimos el carácter b al parámetro modo y escribimos bytes:"

with open('mi_fichero', 'wb') as f:
    f.write(b'0x28')

"""Leyendo un fichero completo

Un objeto de tipo file también ofrece un método llamado read(). Este método leerá el fichero en su totalidad y lo devolverá como una cadena de texto. Usa este método con precaución ya que puede consumir mucha memoria si el fichero es demasiado grande. Yo lo usaría solo en caso de que el fichero fuera muy pequeño.
"""
with open('cloudbutton.py', 'r') as f:
    contenido = f.read()
    print(contenido)

"""¿Qué significa la palabra with al principio del bloque?

A la hora de gestionar y manipular recursos, como puede ser un fichero, hay ciertos patrones que se suelen repetir. Para estos casos, Python nos ayuda a abstraernos del código repetitivo introduciendo lo que se conocen como «Manejadores de contexto» a través de la sentencia with.

En el caso de los ficheros, with nos asegura de que el fichero se cerrará correctamente después de ejecutarse el código en el interior del bloque, incluso si ocurre alguna excepción.

De manera que el siguiente código:

    with open('hola.txt', 'r') as f:
        for linea in f:
            ...

sería equivalente a este

    f = open('hola.txt', 'r')
    try:
        for linea in f:
            ...
    finally:
        f.close()"""
		

