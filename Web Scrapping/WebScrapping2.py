"""                                                     Web scraping con Beautiful Soup II
W

eb scraping con Beautiful Soup4
Objetivo del 3° tutorial de Curso de Web Scraping con Python

Explorar los diferentes usos de web scraping

Analizar los datos extraídos con nuestra técnica de web scraping
Introducción

Muchos análisis de datos, big data y proyectos de machine learning requieren técnicas de web scraping para que recojan los datos 
con los que usted trabajará. El lenguaje de programación Python es ampliamente utilizado en la comunidad científica de datos, y 
por lo tanto tiene un ecosistema de módulos y herramientas que usted puede utilizar en sus propios proyectos. En este tutorial 
nos enfocaremos en el módulo Beautiful Soup con un enfoque mas complejo que el ejemplo de Web scraping con Beautiful Soup I.

En este tutorial, vamos a recopilar y analizar una página web con el fin de obtener datos textuales y escribir la información que 
hemos recopilado en un archivo CSV.


                                                                Condiciones previas

Antes de trabajar en este tutorial, debe tener un entorno de programación Python.

Usted debe tener instalados los módulos Beautiful Soup, csv y urllib3 . Por lo que sería útil tener un conocimiento práctico de 
estos módulos.

Además, dado que trabajaremos con datos extraídos de una web, usted debe estar cómodo con la estructura HTML y el etiquetado.
Entendiendo los datos

En este tutorial trabajaremos con datos del sitio web oficial https://www.icfo.eu/  el Instituto de Ciencias Fotónicas. ICFO es
 un centro de investigación especializado en fotónica, la ciencia que estudia la luz. Fue creado en Barcelona en marzo de 2002 
 por el Departamento de Universidades, Investigación y Sociedad de la Información de la Generalitat de Cataluña y por la 
 Universidad Politécnica de Catalunya. ICFO se trasladó en 2005 en el Parque Mediterráneo de la Tecnología, a Castelldefels, 
 en el área metropolitana de Barcelona, en un edificio de 9.000 metros cuadrados. A fecha de 2018 cuenta con unos 80 laboratorios 
 y más de 750 trabajadores.


                                                        ¿Y esto que aplicaciones tiene?

Por ejemplo ahora vamos a imaginar que queremos hacer una base datos con todos los expertos de fotónica del mundo porque queremos 
hacer un evento de fotónica. Para que el evento tenga éxito necesitamos recopilar todos los expertos que trabajan en ICFO y 
organizaciones como esta, una vez tengamos la base datos podemos mandarles un email a cada uno e invitarlos a nuestro evento.

Esto es tan solo un ejemplo (no real) para que veamos las posibles aplicaciones del web scrapping, te animamos a que uses la 
creatividad para hacer proyectos que resulten funcionales en tu empresa o entorno laboral.


                                                    Empezamos el Web scraping con Beautiful Soup

Si nos vamos a la parte de los profesionales que trabajan en ICFO podemos ver sus perfiles y sus datos como, nombre, teléfono, 
especialidad … información muy valiosa. Por ejemplo -> https://www.icfo.eu/people/people_details?people_id=296


                                                            Web scraping con Beautiful Soup

A continuación y como siempre antes de scrapear veremos el código en HTML para ver la estructura de la web como las clases y 
etiquetas. Si queremos ir directamente a los campos que queremos recopilar también podemos seleccionar el campo y con el botón 
derecho del ratón le damos a inspeccionar elemento (esto se puede hacer con cualquier navegador):

Aquí podemos ver que el nombre y la especialidad de este perfil, los cuales están en un h4, información util para nuestro código 
en python. Aparte del nombre y la especialidad también vamos a scrapear la posición de la persona.


                                                            Web scraping con Beautiful Soup4

La posición de este perfil se encuentra en una class_=’position’ como se puede ver en la imagen.

 
Empezamos con el código en python"""

from bs4 import BeautifulSoup
import urllib3
http = urllib3.PoolManager()
i_list=range(1, 1944, 1)
web = http.request('GET', 'https://www.icfo.eu/people/people_details?people_id=296')
soup = BeautifulSoup(web.data, "lxml")
nameyesp = soup.find_all('h4')
print(nameyesp[0].get_text())
pos=soup.find_all(class_='position')
print(pos[0].get_text())

"""si ejecutamos este código podemos en el terminar el nombre, especialidad y posición de este perfil:

Juan Manuel Fernández López, Mechanics
 Engineering

Para encontrar el nombre y la especilidad hemos usado nameyesp = soup.find_all(‘h4′), posteriormente extraemos el texto con el 
comando nameyesp[0].get_text() . A continuación hacemos algo muy parecido con la posición, usamos primero el comando  
pos=soup.find_all(class_=’position’) y luego extraemos el texto pos[0].get_text().

 
Analizando la url y exportando los datos en csv

Para extraer todos los perfiles tenemos que analizar la url, por ejemplo la del anterior perfil es:

https://www.icfo.eu/people/people_details?people_id=296

Examinado la url podemos ver que los perfiles siguen el patrón

https://www.icfo.eu/people/people_details?people_id=297

https://www.icfo.eu/people/people_details?people_id=298

https://www.icfo.eu/people/people_details?people_id=299

...

Aunque no todas las url tienen perfiles, no es ningun problema. Ya que la idea es implemntar un for que recorra todas las url 
que queramos scrapear.

Para exportar los datos en un formato mas cómodo como csv podemos implemntar algo parecido al post anterior de Beautiful Soup. 
Utilizando:

import csv

csv.writer

writernow

De esta manera nuestro código final sería de la forma:"""

from bs4 import BeautifulSoup
import csv
import urllib3
f = csv.writer(open("datos2.csv", "w"))
f.writerow(["Names" , "Position" ])
http = urllib3.PoolManager()
i_list=range(1, 1500, 1)
for i in i_list:
  web = http.request('GET', 'https://www.icfo.eu/people/people_details?people_id=' + str(i))
  soup = BeautifulSoup(web.data, "lxml")
  nameyesp = soup.find_all('h4')
  print(str(i)+'***************')
  if len(nameyesp) >0:
      nameyesp = soup.find_all('h4')
      namef = nameyesp[0].get_text()
      pos=soup.find_all(class_='position')
      posf = pos[0].get_text()
      f.writerow([namef, posf])
  else:
       print('url vacia')

"""Hemos añadido un condicional if para solventar el caso de cuando la longitud de nameyesp sea 0, ya que nos devolvería un error 
al extraer un texto que no hay.

Con este código python recorre 1500 url y scrapea todo el contenido que le hemos dicho (se puede scrapear mucho mas como emails, 
telefonos, laboratorios…). En caso de que quieras hacer esto de forma manual tardarías horas sin embargo con python y beautiful 
soup podemos hacerlo de forma automática y obtener todos estos datos en un bonito archivo cvs listo para analizar.

 
Siempre ten en cuenta ser considerado

    Al scrapear páginas web, es importante tener en cuenta los servidores de los que se está obteniendo información.
    Compruebe si un sitio web tiene términos de uso que se refieren scrapeo web. Además, comprueba si un sitio tiene una API que 
    le permita capturar datos antes de scrapearlos usted mismo.
    Asegúrese de no acceder continuamente a los servidores para recopilar datos. Una vez que haya recopilado lo que necesita de 
    un sitio, ejecute scripts que repasarán los datos localmente en lugar de sobrecargar los servidores de otra persona."""
