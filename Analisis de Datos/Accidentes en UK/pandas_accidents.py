import pandas as pd
# Read the file 
data = pd.read_csv("Accidents7904.csv", low_memory=False)
# Output the number of rows 
print("Total rows: {0}".format(len(data)))
# See which headers are available
print(list(data))
# Accidents which happened on a Sunday
accidents_sunday = data[data.Day_of_Week == 1]
print("Accidents which happened on a Sunday: {0}".format( len(accidents_sunday)))
# Accidents which happened on a Sunday 
accidents_sunday = data[data.Day_of_Week == 1] 
print("Accidents which happened on a Sunday: {0}".format( len(accidents_sunday))) 
#Accidents which happened on a Sunday, &amp;gt; 20 



carsaccidents_sunday_twenty_cars = data[(data.Day_of_Week == 1) &amp;amp; (data.Number_of_Vehicles &amp;gt; 20)] 
print("Accidents which happened on a Sunday involving &amp;gt; 20 cars: {0}".format(&amp;nbsp;&amp;nbsp;&amp;nbsp; len(accidents_sunday_twenty_cars)))
# Accidents which happened on a Sunday, &amp;gt; 20 cars, in the rain 
accidents_sunday_twenty_cars_rain = data[(data.Day_of_Week == 1) &amp;amp; (data.Number_of_Vehicles &amp;gt; 20) &amp;amp;&amp;nbsp;(data.Weather_Conditions == 2)] 
print("Accidents which happened on a Sunday involving &amp;gt; 20 cars in the rain: {0}".format(&amp;nbsp;&amp;nbsp;&amp;nbsp; len(accidents_sunday_twenty_cars_rain)))
# Accidents in London on a Sunday 
london_data = data[data['Police_Force'] == 1 &amp;amp; (data.Day_of_Week == 1)] 
print("\nAccidents in London from 1979-2004 on a Sunday: {0}".format(len(london_data))) 
# Convert date to Pandas date/time 
london_data_2000 = london_data[ (pd.to_datetime(london_data['Date']) &amp;gt; pd.to_datetime('2000-01-01')) &amp;amp; (pd.to_datetime(london_data['Date']) &amp;lt; pd.to_datetime('2000-12-31')) ] 
print("Accidents in London in the year 2000 on a Sunday: {0}".format( len(london_data_2000)))
london_data_2000.rename(columns={'\xef\xbb\xbfAccident_Index': 'Accident_Index'}, inplace=True)
# Save to Excelwriter = pd.ExcelWriter(&amp;nbsp;&amp;nbsp;&amp;nbsp; 'London_Sundays_2000.xlsx', engine='xlsxwriter')london_data_2000.to_excel(writer, 'Sheet1')writer.save() 





"""                                              Leyendo el Archivo

El primer archivo con el que trabajaremos es una compilación de todos los accidentes automovilísticos 
en Inglaterra durante el período entre 1979 – 2004, para extraer todos los accidentes suscitadas en 
Londres en el año 2000.


                                                        Excel

Comienza por descargar el archivo ZIP fuente desde este enlace http://data.gov.uk/dataset/road-accidents-safety-data , 
y extrae el contenido. Luego, intenta abrir Accidents7904.csv en Excel. Mejor no lo intentes. Si no posees memoria 
suficiente, esto podría colapsar tu pc. 


                                                    ¿Qué sucede?

Deberías ver un error “Archivo No Cargado Completamente” dado que Excel sólo maneja un millón de filas a la vez.

Probamos esto en LibreOffice también y recibimos un error similar –

    “Los datos no pudieron ser cargados completamente porque el número máximo de filas ha sido excedido.”

Para solventar esto podemos abrir un archivo en Pandas.


                                                        Pandas

En un nuevo directorio de proyecto, activa un entorno virtual, y luego instala Pandas:

 
$ pip install pandas==0.16.1

Ahora construyamos el script. Crea un archivo llamado pandas_accidents.py y agrega el siguiente código:

import pandas as pd
# Read the file
data = pd.read_csv("C:\\Users\\tux\\Desktop\\python\\Accidents7904.csv", low_memory=False)
# Output the number of rows
print("Total rows: {0}".format(len(data)))
# See which headers are available
print(list(data))

Aquí, importamos Pandas, leemos el archivo – este proceso podría llevar algo de tiempo, dependiendo en la 
cantidad de memoria que posea tu sistema – y la cantidad total de filas que tenga el archivo, así como los 
encabezados (ejemplo, los títulos de las filas).

Al iniciarlo deberías ver lo siguiente:

 

Total rows: 6224198[‘\xef\xbb\xbfAccident_Index’, ‘Location_Easting_OSGR’, ‘Location_Northing_OSGR’,  ‘Longitude’,
 ‘Latitude’, ‘Police_Force’, ‘Accident_Severity’, ‘Number_of_Vehicles’, ‘Number_of_Casualties’, ‘Date’, 
 ‘Day_of_Week’, ‘Time’, ‘Local_Authority_(District)’, ‘Local_Authority_(Highway)’, ‘1st_Road_Class’, 
 ‘1st_Road_Number’, ‘Road_Type’, ‘Speed_limit’, ‘Junction_Detail’, ‘Junction_Control’, ‘2nd_Road_Class’, 
 ‘2nd_Road_Number’, ‘Pedestrian_Crossing-Human_Control’, ‘Pedestrian_Crossing-Physical_Facilities’, 
 ‘Light_Conditions’, ‘Weather_Conditions’, ‘Road_Surface_Conditions’, ‘Special_Conditions_at_Site’, 
 ‘Carriageway_Hazards’, ‘Urban_or_Rural_Area’, ‘Did_Police_Officer_Attend_Scene_of_Accident’, 
 ‘LSOA_of_Accident_Location’]

¡Así que hay más de seis millones de filas! No es de extrañar que Excel se haya colapsado. Coloca tu atención 
sobre la lista de los encabezados, el primero en particular es:
‘\xef\xbb\xbfAccident_Index’,

Deberías poder leer Accident_Index. ¿Por qué aparece ese extra \xef\xbb\xbf al comienzo? Bueno el \x 
significa que el valor es hexadecimal, lo cual es una Marca de Orden de Bytes, que indica que el siguiente 
texto es Unicode.


                                ¿Por qué es relevante para nosotros?

No puedes asumir que los archivos que lees están limpios. Pueden contener símbolos adicionales, como este, 
que pueden alterar tus scripts

Este archivo está bien, excluyendo eso está limpio – pero en muchos archivos hay datos que falta, datos que 
están en diferentes formatos, etc… Así que cada vez que vayas a analizar un archivo, lo primero que debes 
hacer es limpiarlo. ¿Cuánto debo limpiarlo? Lo suficiente para que pueds llevar a cabo el análisis. Sigue 
el principio de KISS.

¿Qué clase de limpieza pueden requerir mis datos?

    Cambiar formato de fecha/hora. El mismo archivo puede tener distintos formatos de fecha, como el americano 
    (mm-dd-yy) o el europeo (dd-mm-yy). Estos deben ser transformados a un formato común.
    Eliminar cualquier valor vacío. Es posible que el archivo posea columnas y/o filas en blanco, y esto 
    destacará como NaN (Not a number) en Pandas. Pandas provee una forma simple para remover estas: la función 
    dropna() . Vimos un ejemplo de esto en la última entrada de nuestro blog.
    Eliminar cualquier valor que deseemos. Estos son valores que no tienen sentido (como la marca de orden de 
    bytes que vimos con anterioridad). A veces, es posible trabajar con ellos. Por ejemplo, podría haber un 
    conjunto de datos donde la edad fuera ingresada como un número de coma flotante (por error). La función 
    int() entonces podría usarse para asegurarse de que todas las edades se encuentren en un formato integro.

Cómo realizar el análisis de los datos

Para aquellos de ustedes que conozcan sobre SQL, pueden usar las afirmaciones SELECT, WHERE, AND/OR con distintas 
palabras claves para refinar su búsqueda. Podemos hacer lo mismo en Pandas, y de una forma más amigable para el 
programador.

Para comenzar, encontremos todos los accidentes que han sucedido un domingo. Observando los encabezados, hay un 
campo que dice Day_of_Weeks, el cual usaremos.

En el archivo ZIP que descargamos, hay un archivo llamado Road-Accident-Safety-Data-Guide-1979-2004.xls, el cual 
contiene información adicional sobre los códigos que usamos. Si lo abres, verás que el día Domingo tiene el código 1.

    # Accidents which happened on a Sunday
    accidents_sunday = data[data.Day_of_Week == 1]
    print("Accidents which happened on a Sunday: {0}".format(
     len(accidents_sunday)))

Es así de simple.

Aquí, nos enfocamos en el campo Day_of_Weeks y obtenemos de regreso un cuadro de datos con la condición que 
establecimos – day of week == 1.

Al ejecutar deberías ver lo siguiente:

Accidents which happened on a Sunday involving > 20 cars: 10

 

Como puedes ver hay 693.847 accidentes que sucedieron un domingo.

Hagamos que nuestra búsqueda sea más complicada: Encontremos los accidentes que sucedieron en días domingos 
y que involucraron el choque de más de 20 automóviles:

 

    #Accidents which happened on a Sunday, &amp;gt; 20 
    carsaccidents_sunday_twenty_cars = data[(data.Day_of_Week == 1) &amp;amp; (data.Number_of_Vehicles &amp;gt; 20)]
    print("Accidents which happened on a Sunday involving &amp;gt; 20 cars: {0}".format(len(accidents_sunday_twenty_cars)))
    

Ejecutamos el script. Ahora tenemos 10 accidentes:

Accidents which happened on a Sunday involving > 20 cars: 10

Agreguemos otra condición – el clima.

Abre el archivo Road-Accident-Safety-Data-Guide-1979-2004.xls, y ve a la hoja titulada Weather. Verás que código 
2 significa, “Raining with no heavy winds” (lloviendo sin vientos fuertes).

Agrégalo a tu búsqueda:

    # Accidents which happened on a Sunday, &amp;gt; 20 cars, in the rain
    accidents_sunday_twenty_cars_rain = data[
    &amp;nbsp;&amp;nbsp;&amp;nbsp; (data.Day_of_Week == 1) &amp;amp; (data.Number_of_Vehicles &amp;gt; 20) &amp;amp;
    &amp;nbsp;
    &amp;nbsp;&amp;nbsp;  (data.Weather_Conditions == 2)]
    print("Accidents which happened on a Sunday involving &amp;gt; 20 cars in the rain: {0}".format(&amp;nbsp;
    &amp;nbsp;&amp;nbsp; len(accidents_sunday_twenty_cars_rain)))

Así que hubo cuatro accidentes que sucedieron un domingo y que involucraron más de veinte automóviles mientras llovía:

Accidents which happened on a Sunday involving > 20 cars in the rain: 4

 

Podríamos seguir haciendo esto más y más complicado, tanto como lo necesitemos. Por ahora nos detendremos dado que 
nuestro principal interés es observar los accidentes ocurridos en Londres.

Si observas el Road-Accident-Safety-Data-Guide-1979-2004.xls de nuevo, verás que hay una hoja denominada 
Police Force. El código 1 dice: “Metropolitan Police”. Esto refiere a lo que comúnmente se conoce como 
Scotland Yard, y es la fuerza policíaca responsable de la mayor parte (aunque no de todo) de Londres. 
Para nuestro caso, es suficiente, y extraeremos esta información:

    # Accidents in London on a Sunday
    london_data = data[data['Police_Force'] == 1 &amp;amp; (data.Day_of_Week == 1)]
    print("\nAccidents in London from 1979-2004 on a Sunday: {0}".format(len(london_data)))

Ejecuta el script. Esto ha creado un nuevo cuadro de datos con los accidentes registrados por la 
“Policía Metropolitana” desde el año 1979 hasta el 2004 ocurridos en Domingo:

Accidents in London from 1979-2004 on a Sunday: 114624

¿Qué sucedería si quisieras crear un nuevo cuadro de datos que sólo registrase los accidentes del año 2000?

Lo primero que debemos hacer es convertir el formato de fecha a uno que Python pueda entender 
utilizando la función pd.to_datetime(). Esta toma la fecha en cualquier formato y la convierte a un 
formato que podamos entender (yyyy-mm-dd). Luego podemos crear otro cuadro de datos que sólo contenga 
los accidentes para el año 2000:

    # Convert date to Pandas date/time
    london_data_2000 = london_data[
     (pd.to_datetime(london_data['Date']) &amp;gt;
     pd.to_datetime('2000-01-01')) &amp;amp;
     (pd.to_datetime(london_data['Date']) &amp;lt;
     pd.to_datetime('2000-12-31'))
    ]
    print("Accidents in London in the year 2000 on a Sunday: {0}".format(
     len(london_data_2000)))

Cuando ejecutes el código deberías ver esto:

 London in the year 2000 on a Sunday: 3889

Así que, esto puede ser un poco confuso al principio. Normalmente, para filtrar un conjunto sólo haríamos 
uso de un bucle for con un condicional:

    for data in array:&amp;nbsp;&amp;nbsp;&amp;nbsp; if data &amp;gt; X and data &amp;lt; X:&amp;nbsp;
    &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; # do something

Sin embargo, no deberías definir tu propio bucle dado que muchas librerías de alto rendimiento, 
como Pandas, poseen funciones de ayuda. En este caso, el código de arriba hace bucles sobre todo los 
elementos y filtra los datos que se encuentran fuera del conjunto de fechas, y luego las regresa a los 
puntos de datos y se ejecuta donde se encuentra nuestro conjunto de fechas.

                                                ¡Continua la diversión!
                                                Conversión

Es probable que, mientras tú usas Pandas, todos en tu organización estén estancados con Excel. ¿Deseas compartir 
tus datos con aquellos que usan Excel?

Primero, necesitamos algo de limpieza. ¿Recuerdas la marca de orden de bytes que vimos antes? Eso causa 
problemas cuando se escriben los datos en un archivo de Excel – Pandas arroja UnicodeDecodeError. ¿Por qué? 
Porque el resto del texto está decodificado como ASCII, pero los valores hexadecimales no pueden ser 
representados en ASCII.

Podríamos escribir todo como un Unicode, pero recuerda, esta marca de orden de bytes es algo innecesario 
(para nosotros) que no queremos o necesitamos. Así que nos desharemos de ella renombrando el encabezado de la columna:

    london_data_2000.rename(&amp;nbsp;&amp;nbsp;&amp;nbsp; columns={'\xef\xbb\xbfAccident_Index': 'Accident_Index'}, 
    inplace=True)

Ahora podemos guardar los datos en Excel: Esta es la forma de renombrar una columna en Pandas: un poco complicada, 
para ser honesto. inplace = True es necesario porque queremos modificar la estructura existente, y no crear 
una copia, que es lo que Pandas hace por defecto.

    # Save to Excelwriter = pd.ExcelWriter(&amp;nbsp;&amp;nbsp;&amp;nbsp; 'London_Sundays_2000.xlsx',
    engine='xlsxwriter')london_data_2000.to_excel(writer, 'Sheet1')writer.save()

 

Asegúrate de instalar XlsxWriter en el terminal de tu pc antes de empezar:

    pip install XlsxWriter==0.7.3

Si todo funcionó bien, esto debió haber creado un archivo llamado London_Sundays_2000.xlsx, y luego debió 
guardar nuestros datos en la Hoja1. Abre este archivo usando Excel o LibreOffice, y confirma que los 
datos sean correctos.


                                                            Conclusión

Así que, ¿qué logramos? Bueno, abrimos un enorme archivo que Excel no podía abrir y usamos Pandas para:

    Abrir el archivo.
    Realizar búsquedas de tipo SQL en nuestros datos.
    Crear un nuevo archivo XLSX con un subconjunto de los datos originales.

Mantén en mente que, aunque este archivo pesa alrededor de 800MB, en la era del big data, aún es pequeño. 
¿Qué sucedería si quisieras abrir un archivo de 4GB? Incluso si posees una RAM de 8GB o más, podría ser 
imposible dado que la mayor parte de tu RAM está reservada para el Sistema Operativo y otros procesos 
del sistema. De hecho, mi pc se colgó varias veces la primera vez que leyó el archivo de 800MB. Si yo 
abriera un archivo de 4GB, mi pc saldría ardiendo.

Así que, ¿cómo procedemos?

El truco es no abrir el archivo completo a la primera. Eso lo estaremos viendo en la siguiente entrada del blog. 
Hasta ese momento, analiza tu propia data. Deja tus preguntas/comentarios abajo.

El código completo:
"""
