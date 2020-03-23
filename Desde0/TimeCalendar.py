"""Un programa en Python puede manejar la fecha y la hora de varias maneras. La conversión entre formatos 
de fecha es una tarea común para las computadoras. Los módulos de tiempo y calendario de Python ayudan a 
conocer fechas y horas de una forma muy sencilla.


Darle formato a fechas y horas.
¿Qué es Tick?

Los intervalos de tiempo son números de punto flotante en unidades de segundos. Instantes particulares en el
tiempo se expresan en segundos.
Módulos para Fechas, Calendarios y Hora actual en Python

Hay un popular módulo de tiempo disponible en Python que proporciona funciones para trabajar con tiempos y 
fechas. La función time.time() devuelve la hora actual del sistema en ticks desde las 12:00 am del 1 de enero 
de 1970.
Ejemplo en python"""

import time
ticks = time.time()
print ("Número de tick desde 12:00am, Enero 1, 1970:", ticks)

"""La salida por consola sera un número bastante grande

La aritmética de fechas es fácil de hacer con los ticks. Sin embargo, las fechas anteriores a la época no pueden
 representarse de esta forma. Las fechas en un futuro lejano tampoco pueden ser representadas de esta manera 
 – el punto límite es en algún momento del 2038 para UNIX y Windows.

¿Qué es TimeTuple?

Muchas de las funciones de tiempo con Python manejan el tiempo como una tupla de 9 números, como se muestra a continuación.
Index	Campo	Valor
0	4 digitos para el año	2008
1	mes	de 1 a 12
2	día	de 1 a 31
3	hora	de 0 a 23
4	minuto	de 0 a 59
5	segundos	de 0 a 60
6	días de la semana	de 0 a 6 (o lunes)
7	días del año	de 1 a 366
8	horario de verano	-1, 0, 1, -1

La tupla anterior es equivalente a la estructura struct_time. Esta estructura tiene los siguientes atributos:
Index	Atributos	Valores
0	tm_year	2009
1	tm_mon	de 1 a 12
2	tm_mday	de 1 a 31
3	tm_hour	de 0 a 23
4	tm_min	de 0 a 59
5	tm_sec	de 0 a 60
6	tm_wday	de 0 a 6 (o lunes)
7	tm_yday	de 1 a 366
8	tm_isdst	-1, 0, 1, -1

 
Cómo obtener la hora actual en python

Para convertir un instante de tiempo de un segundo desde el valor de punto flotante de la época en un tiempo
doble, pase el valor de punto flotante a una función (por ejemplo, time.time()). De esta manera obtenemos 
la fecha y hora a partir de los valores de la tabla anterior."""

import time
localtime = time.localtime(time.time())
print ("Actual hora local :", localtime)

#La salida por consola en mi caso es:

#Actual hora local : time.struct_time(tm_year=2018, tm_mon=3, tm_mday=22, tm_hour=14, tm_min=9, tm_sec=45, 
#                        tm_wday=3, tm_yday=81, tm_isdst=0)

 
#Cómo cambiar el formato de la hora y la fecha

#Para cambiar el formato en cualquier momento según sus necesidades, hay un método sencillo para obtener 
#la hora en formato legible es asctime()

import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Actual hora local :", localtime)

#La salida por consola es:

#Actual hora local : Thu Mar 22 14:17:41 2018

 
#Obtener el calendario para un mes

#El módulo de calendario ofrece una amplia gama de métodos para jugar con calendarios anuales y mensuales. 
#Aquí imprimimos un calendario para un mes dado ( Febrero 2018)

import calendar
cal = calendar.month(2018, 2)
print ("Aquí está el calendario:", cal)

 
"""El módulo de tiempo time

Hay un popular módulo de tiempo (time) disponible en Python que proporciona funciones para trabajar con 
tiempos y para convertir entre estos. Aquí está la lista de todos los métodos disponibles:
	lista de funciones
1	time.altzone
2	time.asctime([tupletime])
3	time.clock()
4	time.ctime([secs])
5	time.gmtime([secs])
6	time.localtime([secs])
7	time.mktime(tupletime)
8	time.sleep(secs)
8	time.strftime(fmt[,tupletime])
9	time.strptime(str,fmt=’%a %b %d %H:%M:%S %Y’)
10	time.time( )
11	time.tzset()
time.altzone

Este método nos permite devolver el desplazamiento de la zona horaria DST en segundos al oeste UTC si esta ha
sido definida previamente.

Si bien se trata de un método bastante bueno, puede generar un error en el caso de que la zona horaria DST 
esté al este de UTC.

Para usar time.altzone en Python tenemos que usar la siguiente sintaxis:

time.altzone

Veamos un pequeño ejemplo a la hora de usar este método:"""

#!/usr/bin/python
import time
print ("time.altzone %d " % time.altzone)

##Y ahora, si corremos nuestro programa obtendremos algo así.

#time.altzone() 12600

#Los números son el resultado de segundos de la zona horaria.
#time.asctime([tupletime])

#Este método se encarga de convertir una tupla (struct_time) representada por una hora devuelta como gmtime() 
#o localtime() y convertirlo en una cadena de caracteres con un formulario del tipo “Mon Jul 30 15:16:04 1997”.

#Para hacer uso de este método tendremos que usar la siguiente sintaxis:

#time.asctime([t])

#t será considerada como la variable del tiempo de donde obtendremos los datos, sea esta gmtime() o localtime().

#Un pequeño ejemplo del uso de este método es el siguiente:

#!/usr/bin/python
import time
t = time.localtime() # Establecemos nuestra tupla, la cual será obtenida por localtime.
print ("time.asctime(t): %s " % time.asctime(t))

#Y si corremos nuestro programa obtedremos el siguiente resultado:

#time.asctime(): Mon Jul 30 15:16:04 1997

#time.clock

#El método clock nos devuelve el tiempo que posee el procesador como un dato float expresado en segundos.

#El método clock nos devuelve el tiempo del procesador como un dato float expresado en segundos si nos e
#ncontramos en Unix.

#En Windows, esta función nos dará los segundos desde que se realizó la primera llamada a la función como un 
#número flotante basándose en la función QueryPerfomanceCounter de Win32.

#Veamos un ejemplo:

import time
def procedure():
    time.sleep(1)
# Proceso de impresión con time.clock
    t0 = time.clock()
    
procedure()
print (time.clock(), "segundos del proceso time")
# Proceso de impresión en Windows
t0 = time.time()
procedure()
print (time.time() - t0, "seconds wall time")

#Con lo cual obtendremos por consola el siguiente resultado:

#475.51913208470336 segundos del proceso time

"""Toma en cuenta que no todos los sistemas son capaces de mostrar un correcto sistema del tiempo. En algunos 
sistemas, incluyendo Windows, el reloj solo mostrará el tiempo desde que se inició el programa.
time.ctime([secs])

Este método nos permite convertir el tiempo que expresamos en segundos desde la época a una cadena que representa
 el tiempo local.

En dicho caso de que no le demos los datos de los segundos o equivalen a none, nuestro método toma los
 datos regresados por la time().

Esta función es igual a asctime(localtime(secs)), pero mucho más práctica.

Para usar este método debemos usar la siguiente sintaxis:

time.ctime([sec])

Toma en cuenta que sec es la cantidad de segundos que vamos a convertir en una cadena. Veamos un ejemplo:"""

import time
print ("time.ctime() : %s" % time.ctime())

#Y ahora esto nos daría el siguiente resultado:

#time.ctime() : Tue Mar 27 12:54:32 2018

#time.gmtime([secs])

#El método gmtime() nos convierte el tiempo expresado en segundos de una época a una struct_time en UTC en el cual 
#el indicador DST es igual a cero siempre.

#En dicho caso de que no se le de un valor a secs se tomará la hora actual devuelta por time().

#Veamos un ejemplo:

# -*- coding: utf-8 -*-
#import time
#print ("time.gmtime() : %s" % time.gmtime())

#Y ahora obtenemos un resultado del tipo:

#time.gmtime() : (2009, 2, 17, 17, 3, 38, 1, 48, 0)

#time.localtime([secs])

#El método localtime() es muy parecido a gmtime(), pero en este no obtenemos los segundos de la hora local.

#En el caso de que no se especifíquen los segundos a utilizar o el valor sea igual a none, se devuelve el 
#tiempo actual devuelto por el método time(). El indicador DST se fija en 1 una vez sea aplicado el tiempo dado.

#Veamos un ejemplo de localtime().

#import time
#print ("time.localtime() : %s" % time.localtime())

""" obtenemos un resultado parecido:

time.localtime() : (2009, 2, 17, 17, 3, 38, 1, 48, 0)

time.mktime(tupletime)

Este método es algo completamente inverso a la función localtime(). Con esto obtendremos un número tipo float 
que tiene compatibilidad con time().

Para mktime haremos uso de un argumento en forma de struct_time o full9-tuple.

En dicho caso de que los datos que le brindemos a nuestro método no sean representables obtendremos un error
del tipo OverflowError o ValueError.

Observemos un ejemplo del uso de time.mktime:"""

import time
t = (2018, 3, 28, 17, 3, 38, 1, 48, 0) # Damos un valor a la tupla con una fecha
secs = time.mktime( t ) #Definimos nuestro método
print ("time.mktime(t) : %f" % secs) # Imprimimos el método en segundos
# Convertimos nuevamente nuestro código a una cadena de texto
print ("asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs)))

#Y obtenemos este resultado:

#time.mktime(t) : 1234915418.000000
#asctime(localtime(secs)): Tue Feb 17 17:03:38 2009

"""time.sleep(secs)

El método sleep() nos permite suspender la ejecución durante el número de segundos que han sido obtenidos.

El argumento que le brindamos al método puede ser un número float, de esta forma podemos obtener un resultado 
mucho más preciso.

Es importante que tomes en cuenta que con este método el tiempo de suspensión puede ser menor al solicitado.

Este es un ejemplo del uso de este método:"""

import time
print ("Inicio : %s" % time.ctime())
time.sleep( 1 )
print ("Final : %s" % time.ctime())

#El resultado es el siguiente:
 
#Inicio : Wed Mar 28 12:30:13 2018 # Fecha inicial.
#Final : Wed Mar 28 12:30:23 2018 # Fecha al terminar de ejecutarse el método.

"""time.strftime(fmt[,tupletime])

El método strftime convierte una tupla o struct_time representando un tiempo como devuelto por gmtime() o 
localtime() a una cadena con un formato específico de argumentos.

En el caso de que no brindemos un tiempo, este método nos devolverá la fecha actual devuelta por localtime().

Veamos un ejemplo:"""

import time

t = (2018, 30, 17, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))

"""Como puedes observar hemos hecho uso de ciertas directivas para mostrar la fecha. Estas te las 
describimos a continuación.

Directiva de strftime

Para realizar la impresión de la fecha con strftime tenemos mayor libertad de disposición de la forma 
de la impresión, para esto haremos uso de unos ciertos códigos que nos permiten pedirle a la máquina que
 tipo de datos le estamos pidiendo y cómo organizarlos.

Las directivas son las siguientes:

    %a: Día de la semana abreviado.
    %A: Día de la semana completo.
    %b: Nombre del mes abreviado.
    %B: Nombre del mes completo.
    %c: Representación del tiempo y fecha.
    %C: Número de siglo.
    %d: Día del mes. (dos dígitos: 01/31)
    %D: De la misma forma que mes/día/año.
    %e: Día del mes. (un dígito: 1/31)
    %g: Igual a %G, pero sin los siglos.
    %G: 4 dígitos del año correspondientes a la semana número ISO.
    %h: Igual a %b.
    %H: Hora usando reloj de 24 horas (00/23:59).
    %I: Hora usando reloj de 12 horas (01/11:59)
    %j: Día del año. (tres dígitos: 001/365)
    %m: Mes (01/12).
    %M: Minutos.
    %n: Nueva línea de caracteres.
    %p: AM o PM de acuerdo al valor obtenido.
    %r: Notación de tiempo en AM y PM.
    %R: Tiempo en notación de 24 horas.
    %S: Segundos.
    %t: Caracter de tabulación.
    %T: Hora actual (Equivalente a %H:%M:%S).
    %u: Día de la semana como número. (Lunes es el primer día)
    %U: Día de la semana como número. (Sábado es el primer día)
    %V: Semana ISO 8601. (01/53)
    %W: Número de semanas del año actual, iniciando con el primer lunes como primer día de semana.
    %w: Día de la semana como decimal (Sábado = 0).
    %x: Representación de la fecha sin hora.
    %X: Representación de la hora sin fecha.
    %y: Año sin siglos (00/99).
    %Y: año incluyendo los siglos.
    %Z: Tiempo de la zona horaria.
    %z: Abreviación del tiempo de la zona horaria.
    %%: Equivale a un porcentaje de porcentaje común.

time.strptime(str, fmt=’%a %b %d %H:%M:%S %Y’)

El método strptime() nos permite analizar una cadena de caracteres que representa una hora en un formato cualquiera.

El valor que nos devuelve es un struct_time como si estuviese devuelto por gmtime() o localtime().

En el caso de este método usaremos las mismas directivas usadas por strftime(), por lo cual es importante 
que las tengas a mano.

En el caso de que tengas un problema con el análisis de la cadena de caracteres o simplemente no pueda 
ser analizada tendrás un error del tipo ValueError."""

import time
struct_time = time.strptime("30 Nov 00", "%d %b %y")
print ("Tupla devuelta: %s " % struct_time)

#Y obtenemos algo parecido a lo siguiente:

#returned tuple: (2000, 11, 30, 0, 0, 0, 3, 335, -1)

#time.time

#Este método nos devuelve el tiempo como un número tipo float expresado en segundos desde la época en UTC.

#Veamos como funciona este método:

import time
print ("time.time(): %f " % time.time())
print (time.localtime( time.time() ))
print (time.asctime( time.localtime(time.time()) ))

#Y obtenemos un resultado del tipo:

#time.time(): 1522259409.699600
#time.struct_time(tm_year=2018, tm_mon=3, tm_mday=28, tm_hour=13, tm_min=20, tm_sec=9, tm_wday=2, tm_yday=87, tm_isdst=0)
#Wed Mar 28 13:20:09 2018

#time.tzset()

#Este método nos permite reiniciar las reglas de conversión usadas por la rutinas de la librería.

#Para usarlo debemos hacerlo con la siguiente sintaxis:

import time
import os

print('\n\n hooooooooolaaaaaaaaaa\n\n')
os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
time.tzset()
print (time.strftime('%X %x %Z'))
os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
time.tzset()
print (time.strftime('%X %x %Z'))

#Y obtenemos un resultado como el siguiente:

#13:00:40 02/17/09 EST
#05:00:40 02/18/09 AEDT

"""El Módulo de tiempo calendar

El módulo calendario nos brinda diversas funciones relacionadas con el calendario, incluyendo funciones 
que imprimen un calendario en formato textual para un mes o un año.

Por defecto, este módulo siempre tomará en cuenta el día lunes como el primer día de la semana y el
 sábado como el último. Esto es posible cambiarlo haciendo uso de la función calendar.setfirstweekday().

Esta es una lista con descripción de las funciones disponibles en Python relacionadas con el calendario.
 N°	Función con la descripción
1	

calendar.calendar(año,w=2,l=1,c=6)

Devuelve una cadena multilínea con un calendario por año con un formato de 3 columnas separadas 
por los espacios de c. w es el equivalente al ancho entre caracteres de cada fecha; cada línea 
tiene un ea extensión de 21*w+18+2*c. l es el número de líneas para cada semana.

2 calendar.firstweekday() 

Nos devuelve la configuración actual para el primero día de la semana. En el caso que se encuentre 
la configuración por defecto, obtendremos al lunes como el día 0 y al sábado como el 6.


3 calendar.isleap(año) 

Devuelve True si el año a evaluar es bisiesto, mientras que si es lo contrario devuelve False.


4 calendar.leapdays(año1,año2) 

Retorna el número total de días bisiestos entre los años del rango usado en (año1, año2).


5 calendar.monthcalendar(año,mes) 

Devuelve una cadena multilínea con un calendario para meses de años, una línea por semana junto
 con dos líneas cabeceras. w es el ancho en caracteres de cada fecha; cada línea tiene una extensión 
 de 7*w+6. l es el número de líneas por cada semana.


6 calendar.monthcalendar(año,mes)

Devuelve una lista de una lista de enteros, cada sublista nos muestra una semana. Los días fuera
 del mes del año están configurados como 0, mientras que los meses configurados dentro son del 1 en adelante.


7 calendar.monthrange(año,mes) 

Nos devuelve dos enteros. El primero se trata del código del día de la semana para el día del mes 
en el año, mientras que el segundo se trata del número de días en el mes. Los códigos para los días 
de la semana serán del 0 (Lunes) al 6 (Sábado), mientras que los meses son del 1 al 12.


8 calendar.prcal(año,w=2,l=1,c=6) 

Igual a imprimir calendar.calendar(año,wl,c).


9 calendar.prmonth(año,mes,w=2,l=1) 

Igual a imprimir calendar.month(año,mes,w,l).

10 calendar.setfirstweekday(día de la semana)

Permite configurar el primer día de la semana con un código. Por defecto los días de la semana serán
 codificados desde el día lunes como el 0 al día sábado como el 6.


11 calendar.timegm(tupletime) 

Es completamente inverso a time.gmtime. Toma una instancia del tiempo en forma de una tupla y devuelve 
la misma instancia como un número flotante en segundos desde la época.


12 calendar.weekday(año,mes,día) 

Retorna el código del día de la semana para la fecha que hemos otorgado. Los días de la semana por 
defecto serán del 0 (Lunes) al 6 (Sábado). Los meses, por otro lado irán del número 1 (Enero) al mes 12 (Diciembre)"""