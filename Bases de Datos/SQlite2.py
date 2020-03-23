"""                                     Inserción dinámica en una base de datos con SQLite

Implementar dichos métodos en un programa

En este tutorial, vamos a ir cubriendo cómo insertar dinámicamente en la tabla de una base de datos, usando variables.

1º Vamos a importar algunas nuevo módulos:

    import time
    import datetime
    import random

Obtenemos los dos primeros módulos para poder crear las marcas de tiempo a usar, y luego usamos el módulo aleatorio para crear 
algunos valores a usar.

A continuación, haremos una nueva función, dynamic_data_entry:

    def dynamic_data_entry():
      unix = int(time.time())
      date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
      keyword = 'AprenderPython'
      value = random.randrange(0,10)
      c.execute("INSERT INTO tabla1 (unix, fecha, palabraclave, valor) VALUES (?, ?, ?, ?)",
            (unix, date, keyword, value))
    conn.commit()

En esta función, establecemos algunas variables, luego ejecutamos una consulta SQL ligeramente diferente. Tenga en cuenta que 
estamos utilizando ‘?’ para la entrada de variables. Con MySQL, estarías usando %s en su lugar. Al final, hacemos el commit. 
Ahora cambiamos el final del guión:

    #create_table()
    #data_entry()
    for i in range(10):
      dynamic_data_entry()
      time.sleep(1)
    c.close
    conn.close()

 

Comentamos create_table, que podríamos dejar si quisiéramos, pero ya no es necesario. También comentamos nuestra data_entry. Luego, 
usamos un bucle for para ejecutar dynamic_data_entry() diez veces. Esto nos da la hora actual, convertida en fecha y hora, y luego 
un valor aleatorio para la columna de valores.

Código completo hasta este punto:"""

import sqlite3
import time
import datetime
import random
conn = sqlite3.connect('tutorial3.db')
c = conn.cursor()
def create_table():
  c.execute("CREATE TABLE IF NOT EXISTS tabla1(unix REAL, fecha TEXT, palabraclave TEXT, valor REAL)")
def data_entry():
  c.execute("INSERT INTO tabla1 VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
  conn.commit()
  c.close()
  conn.close()
def dynamic_data_entry():
  unix = int(time.time())
  date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
  keyword = 'Python'
  value = random.randrange(0,10)
  c.execute("INSERT INTO tabla1 (unix, fecha, palabraclave, valor) VALUES (?, ?, ?, ?)",(unix, date, keyword, value))
  conn.commit()
for i in range(10):
  dynamic_data_entry()
  time.sleep(1)
c.close
conn.close()