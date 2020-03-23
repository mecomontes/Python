"""                                         Web Scraping en Paginas Amarillas con Selenium, Bonus



paginas-amarillas-web-scraping-aprender-python
Objetivo de la 5º lección del Curso de Web Scraping con Python

Aprender a realizar web scraping usando Selenium y Python

Realizar web scraping en una web de páginas amarillas

Hola! hoy os traigo un interesante script en el que podéis realizar web scraping. Mirando algunas de las grandes webs que hay en 
castellano me he topado con paginasamarillas.es, donde se puede encontrar casi de todo.

Lo primero que nos encontramos en esta web son 2 huecos y un botón:

¿Qué estamos buscando?
¿Dónde?
Botón (para buscar…)

paginas-amarillas-web-scraping-aprender-python

Los primero que debemos hacer es analizar estos 2 huecos y el botón. Si nos fijamos en la siguientes imágenes, podemos hacer un 
inspeccionar elemento y ver la información de ellos.

Inspeccionamos elementos del 1º hueco

paginas-amarillas-web-scraping-aprender-python

 

Inspeccionamos elementos del 2º hueco

paginas-amarillas-web-scraping-aprender-python

 

Inspeccionamos elementos del botón

paginas-amarillas-web-scraping-aprender-python

 

Una vez escribimos lo que queremos buscar y dónde, pulsamos el botón y la web nos dará una lista. Esta es la lista objetivo la 
cual escrapearemos para guardar la información. Yo he escrito, bares en Barcelona 🍻

Para escrapear esta lista nos hemos fijado tan sólo en dos clases : “listado-item” y “box“.

En la siguiente imagen puedes ver “listado-item“.

paginas-amarillas-web-scraping-aprender-python

En la siguiente imagen puedes ver “box”:

paginas-amarillas-web-scraping-aprender-python

 

Una vez hemos explicado la metodología que hemos usado os dejamos aqui todo el código!
Código para web scraping con Selenium:"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def ir_paginas_amarillas_web(cadena, city):
  driver = webdriver.Firefox(executable_path=r'C:\Users...añade tu ruta del... \geckodriver.exe')
  #Página a la que queremos acceder   driver.get("https://www.paginasamarillas.es/")
  lista_datos = []
  try:
    #Verificamos si el elemento con ID="whatInput" ya está cargado, este elemento es la caja de texto donde se hacen las busquedas
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "whatInput")))
    #Obtenemos la caja de texto de busquedas
    input_nombre = driver.find_element_by_id("whatInput")
    #Enviamos la cadena que estamos buscando
    input_nombre.send_keys(cadena)
    #Verificamos si el elemento con ID="whereInput" ya está cargado, este elemento es la caja de lugar donde se hacen las busquedas
    input2_nombre = driver.find_element_by_id("whereInput")
    #Enviamos la ciudad que estamos buscando
    input2_nombre.send_keys(city)
    #Obtenemos el botón que ejecuta la búsqueda
    boton = driver.find_element_by_id("submitBtn")
    #Damos click al botón
    boton.click()
  except:
    #Mostramos este mensaje en caso de que se presente algún problema
    print ("El elemento no está presente")
  try:
    #Si se encuentran resultados la página los muestra en elementos de nombre "listado-item"
    #Para ello esperamos que estos elementos se carguen para proceder a consultarlos
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "listado-item")))
  except:
    print ('Elementos no encontrados')
    #Obtenemos en una lista los elementos encontrados
  resultados = driver.find_elements_by_class_name("listado-item")
  for resultado in resultados:
    #En cada uno de los elementos encontrados buscamos un elemento interno que tiene por nombre box
    try:
      datos = resultado.find_element_by_class_name("box")
      print ('datos=', datos.text)
    except:
      datos='-'
      print('datos=0')
    print ("==============================\n")
  driver.close()
  return lista_datos
def main():
  print (ir_paginas_amarillas_web('talleres de coches','Barcelona'))
main()

"""El código se compone con una función “ir_paginas_amarillas_web” donde se introducen los 2 campos de entrada. Luego podemos
 encontrar que tiene varios try y except para evitar un crash de python.  También es importante comentar que tenemos un for el 
 cual recorre todo el listado-item.
No olvides:

Cambiar la línea 7 ya que el driver lo puedes guardar donde gustes
Te recomendamos que juegues con el código, lo cambies y modifiques
El código lo tenemos comentado, lee el código tranquilamente

Ahora con este código podemos hacer búsquedas automáticas para escrapear o lo que se te ocurra. Las aplicaciones ya dependen de tu
 imaginación!"""