"""Si no tienes etiquetas incrustadas, o atributos como style o id o className (el equivalente en Dash de la clase de HTML), puede
 que no veas la necesidad de nombrar explícitamente a los children, pero te sugiero que lo hagas para cualquier aplicación que 
 esté configurada para crecer.

Los children también pueden ser una lista de artículos, no sólo uno. Añadamos un gráfico y hagamos este 1º tutorial de Dash en 
python un poco mas interesante:"""

import dash
import dash_core_components as dcc
import dash_html_components as html
app = dash.Dash()
app.layout = html.Div(children=[
  html.H1(children='Tutoriales Dash en AprenderPython.com'),
  dcc.Graph()])
if __name__ == '__main__':
  app.run_server(debug=True)

"""Aquí, puedes ver que nuestro diseño consiste en un div gigante, que contiene los siguientes children: una etiqueta h1 de 
“Tutoriales Dash en AprenderPython.com” y un dcc.Graph. Esto no se ejecutará todavía, necesitamos especificar los elementos del 
gráfico, así que ahora vamos a construirlo. He aquí un ejemplo de gráfico rápido:"""

app.layout = html.Div(children=[
  html.H1(children='Tutoriales Dash en AprenderPython.com'),
  dcc.Graph(id='ejemplo',
    figure={
      'data': [
        {'x': [1, 2, 3, 4], 'y': [1, 8, 3, 7], 'type': 'line', 'name': 'Bicicletas'},
        {'x': [1, 2, 3, 4], 'y': [5, 2, 8, 8], 'type': 'bar', 'name': 'Bicicletas electricas'},
        ],
      'layout': {
      'title': 'Ejemplo básico en Dash'
        }
      })
  ])
if __name__ == '__main__':
  app.run_server(debug=True)
  
"""El ID es obligatorio, y podemos utilizarlo más tarde para manipular el gráfico. Luego tenemos el elemento de la figure, que
 contiene los datos y el diseño del gráfico. Aquí es donde pasamos todos los datos y qué tipo de gráfico queremos, junto con otros
 bits de información. Dentro de la maquetación, podemos añadir cosas como el título que hemos añadido aquí.

Ahora al ejecutar nos da:

curso-Dash-aprender-pythonAhora notará que puedes cambiar las cosas en tiempo real mientras su servidor se está ejecutando. Cada 
vez que guarde su script, el servidor debería actualizarse. A veces esto no funciona, o se produce un error, y entonces las cosas
 pueden ponerse feas. Cuando todo lo demás falla, puedes eliminar los procesos en ejecución de Python para reiniciar las cosas
 (puedes ir al administrador de tareas y eliminar los procesos que se no quieren actualizarse)

Ahora que podemos ver cómo crear gráficos, nos vamos a centrar de nuevo en la interactividad. Dash nos da el poder de la librería 
javascript React, con la que podemos interactuar en tiempo real con nuestra aplicación,"""