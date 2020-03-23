"""

                                                            Base de datos SQLite con Python

Las bases de datos ofrecen, un método superior de entrada y salida de datos de alto volumen sobre un archivo típico como puede ser 
un archivo de texto. SQLite es una versión “ligera” que funciona basada en la sintaxis SQL. SQL es un lenguaje de programación en 
sí mismo, pero es un lenguaje de base de datos muy popular. Muchos sitios web utilizan MySQL, por ejemplo.

SQLite es realmente extremadamente ligero. La configuración de una base de datos SQLite es casi instantánea, no hay ningún servidor
 que configurar, ningún usuario que definir y ningún permiso del que preocuparse. Por esta razón, a menudo se utiliza como una base 
 de datos de desarrollo y creación de prototipos. El principal problema con SQLite es que termina siendo como cualquier otro archivo
 plano, por lo que la entrada/salida de alto volumen, especialmente con consultas simultáneas, puede ser problemática y lenta. Cada 
 tabla probablemente necesita su propio archivo como si estuviera haciendo archivos planos, y en SQLite está todo en uno. SQLite 
 también va a almacenar sus datos en un búfer. Por último, en las ediciones no se requiere que se vuelva a guardar todo el archivo,
 tan sólo esa parte. Esto mejora significativamente el rendimiento. Muy bien, pues vamos con SQLite!
Creamos la base de datos SQLite con Python

1º Necesitamos establecer una conexión y un cursor. Esto es igual tanto con SQLite como con MySQL:

    import sqlite3
    conn = sqlite3.connect('tutorial3.db')
    c = conn.cursor()

Cuando ejecutemos el código, si la base de datos no existe, será creada. Si existe, no se sobrescribirá ni se volverá a crear. A 
continuación, definimos el cursor. Piensa en el cursor como el cursor de tu ratón, simplemente hace cosas como seleccionar, borrar, 
añadir, etc. La mayoría de la gente cuando piensa en una base de datos piensa en filas y columnas de datos, pero en realidad es 
como una mesa. Las tablas van en bases de datos, y los datos van en las tablas. Una base de datos sólo puede contener una sola 
tabla, o puede contener miles de tablas.


                                                    Creamos una tabla en la base de datos SQLite con Python

Creamos una tabla ahora:

    def create_table():
     c.execute("CREATE TABLE IF NOT EXISTS tabla1(unix REAL, fecha TEXT, palabraclave TEXT, valor REAL)")

 

Arriba, comenzamos con nuestra primera consulta SQL. SQL es un lenguaje propio. Esto significa que, cuando aprendas a usar SQL con 
Python, ya sabrá cómo crear consultas SQL, incluso si lo está haciendo en un otro lenguaje. Aunque no es necesario, generalmente se 
usa las mayúsculas para denotar comandos específicos de SQL, ya que una consulta SQL contiene tanto elementos SQL como elementos 
dinámicos que usted configura. Dado que las consultas SQL son cadenas, a veces puede ser difícil depurarlas sin algún tipo de 
diferenciación como ésta. Nota, SQLite no es ciego a las cajas, pero MySQL sí lo es. Python y la mayoría de los lenguajes de 
programación no están ciegos a la carcasa.

El código anterior crea una tabla, llamada tabla1, si no existe. Esta tabla contiene las siguientes filas: unix, fecha,
 palabraclave y valor. A cada columna se le asigna un tipo de datos. En nuestro caso, unix es un REAL, que es un número en coma
 flotante en Python, entonces tenemos algunas variables TEXT, y otro REAL. SQLite sólo tiene 5 tipos principales. MySQL tiene 
 muchos más. Puede que tengas curiosidad por saber por que todas las variables no son algo así como “texto” o por qué no usamos 
 “texto” para todo. La idea es que, si sabemos que serán sólo números enteros, entonces podemos asignar un tipo de datos que 
 ayudará a mantener el tamaño del archivo lo más comprimido posible, así como a mantener las operaciones de entrada/salida lo más 
 rápidas posibles. Hablando de entrada/salida, vamos a crear alguna entrada:

    def data_entry():
      c.execute("INSERT INTO tabla1 VALUES(1452549219,'2018-02-12 16:50:39','Python',6)")
      conn.commit()
      c.close()
      conn.close()
    create_table()
    data_entry()

 

Aquí, el cursor ejecuta una consulta SQL. Este es un INSERT INTO, y el nombre de la tabla sigue. Luego, insertamos una tupla de 
valores. Después de insertar usamos conn.commit(). Piensa en conn.commit() como si estuvieras guardando el documento. Recordar
 cómo funciona SQLite. Tienes una parte de archivo antes de confirmarlo. No es necesario confirmar después de cada INSERT. En su 
 lugar, usted confirma cuando termina con esa tarea de inserción específica. A continuación, cierre el cursor y la conexión cuando
 haya terminado totalmente. Si usted quiere hacer más inserciones en un momento, entonces no hay razón para cerrar la conexión. Si 
 en cambio está usando SQLite en una página de registro, por ejemplo, una vez que el usuario se ha registrado, no querrá dejar esa 
 conexión abierta desperdiciando memoria, por lo que querrá cerrarla.

Finalmente, en el código anterior, ejecutamos las funciones, creamos la tabla e introducimos una fila. Todo listo. ¿Cómo sabemos 
que está hecho? Podríamos ejecutar otra consulta SQL para solicitar algunos datos, pero es posible que desee ver visualmente su 
tabla de vez en cuando. Esto se puede hacer de varias maneras, pero prefiero y recomiendo: SQLite Browser

Código de nuestra base de datos SQLite con Python

Código completo hasta ahora:"""

import sqlite3
conn = sqlite3.connect('tutorial3.db')
c = conn.cursor()
def create_table():
  c.execute("CREATE TABLE IF NOT EXISTS tabla1(unix REAL, fecha TEXT, palabraclave TEXT, valor REAL)")
def data_entry():
  c.execute("INSERT INTO tabla1 VALUES(1452549219,'2018-02-12 16:50:39','Python',6)")
  conn.commit()
  c.close()
  conn.close()
create_table()
data_entry()

#Ahora con SQLite Browser podemos ver la base datos creada: