"""Python es un lenguaje de gran utilidad para trabajar en numerosos campos. Entre ellos, el referente al análisis financiero y 
económico. Sin embargo, es común que cuando queremos trabajar en tales ámbitos, necesitemos contar con los datos actualizados que
 nos ofrecen organismos como la “OCDE” o el Banco Mundial. Para poder usar tal información, contamos en python, con una herramienta: 
     “pandas-datareader“, de la que vamos a hablar en la presente ocasión.

Lo que va a hacer “pandas-datareader” (el cual, deberemos instalar previamente) es conectar con la web (para lo que necesitaremos 
contar con conexión a internet) para importar los datos que pidamos. Aunque en nuestro ejemplo vamos a usar el servicio de “Yahoo! 
finance“, existen otras webs compatibles con esta herramienta, las cuales se pueden consultar en la documentación de 
“pandas-datareader“:"""
    
import pandas_datareader as pdr
import datetime

aapl=pdr.get_data_yahoo('AAPL',start=datetime.datetime(2006,10,1),end=datetime.datetime(2012,1,1))
print(aapl)
#print(aapl.head())
#print(aapl.tail())
#print(aapl.loc['2009'].head())
#print(aapl.loc['2007'].tail())
#print(aapl['close'][-10:])

import matplotlib.pyplot as plt
column=aapl['Adj Close']

column.plot(grid=True)
plt.show()


"""Como se ve en la imagen, hemos empezado importando “pandas-datareader” (para realizar la importación) y el módulo “datetime“, que 
usaremos para establecer la fecha de inicio (“start“) y la fecha final (“end“), de la serie temporal que queremos consultar de la 
compañía que quprint(aapl)eramos (“Apple” en nuestro caso, para lo que introduciremos su nombre de modo abreviado: “AAPL“). Para realizar la 
obtención de los datos deseados, con “Yahoo! finance“, emplearemos el método “.get_data_yahoo()“. Una vez importados los datos, los
 mostraremos en pantalla con la función “print“:

Obtenemos así el precio de las acciones: Su cotización máxima(‘High‘), mínima (‘Low‘), el volumen total de transacciones (‘Volume‘) y 
los datos referentes al ajuste de precio final (‘Adj Close‘) para cada uno de los días de la serie (‘Date‘). Información esta, que, 
tal y como se ve al final, se nos muestra en 1323 filas (de las que se han omitido las centrales) y 6 columnas.

Como se ve, aquí se nos muestra la información para el rango temporal, establecido con “datetime” y las variables “start” y “end“,
 que vimos antes. No obstante, también podemos mostrar, dentro de la información, ciertos sectores. Así, por ejemplo, si queremos 
 ver solo las primeras filas de la serie, podemos usar el método “.head()“:
     
     
                                             Aplicación del método “.head()” sobre “aapl”.


Con el método “.head()” se mostrarán solo las filas correspondiente a la primera semana de la serie.

Si, por contra, queremos ver solo, los datos de la última semana de la serie, haremos uso de “.tail()“:
Aplicación del método “.tail()” sobre “aapl”.
“.tail()” mostrará solo los datos más recientes del intervalo temporal elegido.

Lo que acabamos de hacer para la serie completa, lo podemos hacer, también, para un año concreto, dentro del rango establecido. 
Así, si quisiéramos ver los datos referentes a la primera semana de 2009, usaríamos el método “.loc[]” introduciendo entre los 
corchetes el año, y aplicando nuevamente el método “.head()” para ver sus primeros datos:
    
    
                                                    Datos correspondientes a a primera semana de 2009.

El mismo método emplearemos para ver los datos de la última semana (en esta ocasión de 2007), solo que aquí aplicaremos “.tail()” 
como ya vimos:
    
    
                                                Datos correspondientes a la última semana de 2007.

Este proceso de selección de información a visualizar que hemos hecho respecto a las filas, podemos hacerlo igualmente, respecto a 
las columnas. Así, si quisiéramos ver unicamente la columna de datos, relativa a los precios de cierre (columna “Close“) de la 
serie, centrándonos en sus últimos 10 valores:

Ejecutando este código, obtendremos, junto a las fechas correspondientes (dentro del rango temporal establecido)los valores de 
la columna “Close“, en este caso, de tal información, hemos seleccionado solo las últimas 10 filas (“[-10:]“):

A su vez, con los datos importados con “pandas-datareader” podemos hacer otras operaciones, ente ellas, visualizar dichos datos 
en una gráfica. Así, partiendo de este último ejemplo, podemos representar los datos del “precio de ajuste “Adj Close“, mediante 
una gráfica creada con “matplotlib” (que importaremos previamente):

Ejecutando el código, obtendremos la siguiente gráfica:
Evolución del precio de ajuste final, de “Apple” entre 2006 y enero de 2012.

Hasta aquí, hemos visto el modo de obtener los datos, correspondientes a un rango temporal. No obstante, es posible que queramos 
contar con los datos más recientes al momento de ejercitar nuestro script: Para ello, podemos hacerlo estableciendo la fecha actual
 en la variable “end“. Pero también podemos obtener el valor más reciente, omitiendo dicha variable:

Aquí, lo que va hacer nuestro código es importar los datos de “Google” (para lo que introduciremos el string “GOOGL“) desde 
octubre de 2009, para lo que introduciremos “start=datetime.datetime(2009,10,1)“, y la fecha más reciente (actual).

Ejecutado el código obtendremos, por una parte, las 0 últimas líneas de “Close“, y por otro, su correspondiente representación 
gráfica:

Y hasta aquí, este artículo acerca de la obtención de datos financieros, con “pandas-datareader“. En futuras entregas veremos el 
modo de realizar cálculos y operaciones con estos datos, para la obtención de la información necesaria para realizar análisis 
financieros."""