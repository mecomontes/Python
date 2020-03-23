""""                                                    Actualizar y borrar en SQLite
SQLite-aprenderPython

Hasta este punto, en el curso de SQLite con Python, se le ha enseñado cómo crear una base de datos, una tabla, cómo insertar datos, 
cómo leerlos y como graficar desde SQLite. En este tutorial, vamos a hablar de cómo modificar los datos existentes y como 
borrarlos.
Objetivo del 5° tutorial de Curso de SQLite

Crear funciones que modifiquen y eliminen registros en nuestra base de datos
Actualizar y borrar en SQLite con Python

Es importante tener en cuenta que no se puede deshacer cuando se trata de SQL. Una vez que borras algo, o una vez que lo modificas 
no hay vuelta atrás. Tómese su tiempo, lea y relea sus consultas antes de hacerlas!

Primero, hagamos una actualización. Antes de eso, miraremos los datos existentes:"""

import sqlite3
conn = sqlite3.connect('tutorial5.db')
c = conn.cursor()
 
def actualizar_y_borrar():
  c.execute('SELECT * FROM tabla1')
  data = c.fetchall()
  [print(row) for row in data]
 
actualizar_y_borrar()

 

"""Por consola me sale:

(1452549219.0, ‘2016-01-11 13:53:39’, ‘Python’, 6.0)
(1522330321.0, ‘2018-03-29 15:32:01’, ‘AprenderPython’, 2.0)
(1522330322.0, ‘2018-03-29 15:32:02’, ‘AprenderPython’, 6.0)
(1522330323.0, ‘2018-03-29 15:32:03’, ‘AprenderPython’, 3.0)
(1522330324.0, ‘2018-03-29 15:32:04’, ‘AprenderPython’, 8.0)
(1522330325.0, ‘2018-03-29 15:32:05’, ‘AprenderPython’, 2.0)
(1522330326.0, ‘2018-03-29 15:32:06’, ‘AprenderPython’, 7.0)
(1522330327.0, ‘2018-03-29 15:32:07’, ‘AprenderPython’, 1.0)
(1522330328.0, ‘2018-03-29 15:32:08’, ‘AprenderPython’, 9.0)
(1522330329.0, ‘2018-03-29 15:32:09’, ‘AprenderPython’, 6.0)
(1522330330.0, ‘2018-03-29 15:32:10’, ‘AprenderPython’, 5.0)

 
Actualizar la base datos SQLite

Ahora podemos modificar la función actualizar_y_borrar y vamos a cambiar todos los valores menores de 5 por 2018:"""

import sqlite3
conn = sqlite3.connect('tutorial3.db')
c = conn.cursor()
def actualizar_y_borrar():
  c.execute('UPDATE tabla1 SET valor = 2018 WHERE valor < 5')
  conn.commit()
  c.execute('SELECT * FROM tabla1')
  data = c.fetchall()
  [print(row) for row in data]
actualizar_y_borrar()

"""Ahora me sale por consola:

(1452549219.0, ‘2016-01-11 13:53:39’, ‘Python’, 6.0)
(1522330321.0, ‘2018-03-29 15:32:01’, ‘AprenderPython’, 2018.0)
(1522330322.0, ‘2018-03-29 15:32:02’, ‘AprenderPython’, 6.0)
(1522330323.0, ‘2018-03-29 15:32:03’, ‘AprenderPython’, 2018.0)
(1522330324.0, ‘2018-03-29 15:32:04’, ‘AprenderPython’, 8.0)
(1522330325.0, ‘2018-03-29 15:32:05’, ‘AprenderPython’, 2018.0)
(1522330326.0, ‘2018-03-29 15:32:06’, ‘AprenderPython’, 7.0)
(1522330327.0, ‘2018-03-29 15:32:07’, ‘AprenderPython’, 2018.0)
(1522330328.0, ‘2018-03-29 15:32:08’, ‘AprenderPython’, 9.0)
(1522330329.0, ‘2018-03-29 15:32:09’, ‘AprenderPython’, 6.0)
(1522330330.0, ‘2018-03-29 15:32:10’, ‘AprenderPython’, 5.0)

 
Borrar en la base datos SQLite

Ahora ya solo nos falta saber borrar de nuestra base de datos. Vamos a borrar todos los valores que son iguales a 2018:"""

import sqlite3
conn = sqlite3.connect('tutorial3.db')
c = conn.cursor()
def actualizar_y_borrar():
  c.execute('DELETE FROM tabla1 WHERE valor = 2018')
  conn.commit()
  c.execute('SELECT * FROM tabla1')
  data = c.fetchall()
  [print(row) for row in data]
actualizar_y_borrar()

"""Tras borrar estos vaores por consola nos sale:

(1452549219.0, ‘2016-01-11 13:53:39’, ‘Python’, 6.0)
(1522330322.0, ‘2018-03-29 15:32:02’, ‘AprenderPython’, 6.0)
(1522330324.0, ‘2018-03-29 15:32:04’, ‘AprenderPython’, 8.0)
(1522330326.0, ‘2018-03-29 15:32:06’, ‘AprenderPython’, 7.0)
(1522330328.0, ‘2018-03-29 15:32:08’, ‘AprenderPython’, 9.0)
(1522330329.0, ‘2018-03-29 15:32:09’, ‘AprenderPython’, 6.0)
(1522330330.0, ‘2018-03-29 15:32:10’, ‘AprenderPython’, 5.0)"""