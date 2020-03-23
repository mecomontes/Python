"""                                         Ejemplo de Graficar desde SQLite

basedatos-sqlite-aprenderpython

En este tutorial, vamos a mostrar cómo puede utilizar una consulta e iterarla a través de ella, para obtener datos que puede 
utilizar. En este ejemplo, vamos a generar un gráfico Matplotlib. Echa un vistazo a ese tutorial sobre cómo usar Matplotlib si 
aún no lo tienes claro.
Objetivo del 4° tutorial de Curso de SQLite

Poner en práctica nuestras habilidades con Matplotlib

Agregar una función que tome registros y cree gráficas con estos datos

Ahora añadimos la función a nuestro código para graficar, graf_data:

    def graf_data():
      c.execute('SELECT fecha, valor FROM tabla1')
      data = c.fetchall()
      dates = []
      values = []
      for row in data:
        dates.append(parser.parse(row[0]))
        values.append(row[1])
      plt.plot_date(dates,values,'-')
      plt.show()

 

En este ejemplo, estamos tomando la marca de la fecha y el valor de la tabla. A partir de ahí, estamos iterando la lista de fechas 
y valores. Después de eso, usamos Matplotlib para graficar los datos. Esto significa que probablemente necesitemos importar 
Matplotlib:

    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from dateutil import parser
    from matplotlib import style
    style.use('fivethirtyeight')

La gráfica de las fechas de mi base de datos es la siguiente:

basedatos-sqlite-aprenderpython
Parece un poco extraña aunque si vemos en la siguiente imagen los datos de las fechas podemos ver que es correcta:
basedatos-sqlite-aprenderpython

 

El código final seria:"""

import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')
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
  fecha = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
  palabraclave = 'AprenderPython'
  valor = random.randrange(0,10)
  c.execute("INSERT INTO tabla1 (unix, fecha, palabraclave, valor) VALUES (?, ?, ?, ?)",
      (unix, date, keyword, value))
  conn.commit()
  time.sleep(1)
def read_from_db():
  c.execute('SELECT * FROM tabla1 WHERE valor = 5')
  data = c.fetchall()
  print(data)
  for row in data:
    print(row)
  c.execute('SELECT * FROM tabla1 WHERE unix > 14525')
  data = c.fetchall()
  print(data)
  for row in data:
    print(row)
  c.execute('SELECT * FROM tabla1 WHERE unix >1522330328')
  data = c.fetchall()
  print(data)
  for row in data:
    print(row[0])
def graf_data():
  c.execute('SELECT fecha, valor FROM tabla1')
  data = c.fetchall()
  dates = []
  values = []
  for row in data:
    dates.append(parser.parse(row[0]))
    values.append(row[1])
  plt.plot_date(dates,values,'x-')
  plt.show()
graf_data()
c.close
conn.close()