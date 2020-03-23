"""                                             Interfaz de Usuario Interactiva con Dash
curso-Dash-aprender-python
Objetivo del 2º tutorial de Curso de Dash en Python

-Aprenderemos a realizar importaciones de entrada y salida.

-Ver un código para crear una función de ejemplo.

Bienvenido a la segunda parte de la serie de tutoriales Dash en python para crear interfaces de usuario interactivas de 
visualización de datos. En este tutorial, vamos a cubrir la interactividad de la interfaz de usuario con un ejemplo de entrada 
de texto. Este ejemplo es muy parecido al que puede encontrar en la guía del usuario de Dash.
Crear interfaces de usuario interactivas con Dash

Para empezar, hagamos algunas importaciones:

    import dash
    from dash.dependencies import Input, Output
    import dash_core_components as dcc
    import dash_html_components as html

Lo nuevo aquí son las importaciones de Input (entrada) y Output (salida), que usaremos envolviendo una función que se encargará de 
la entrada y salida. Dash usará React en segundo plano para que podamos trabajar con estas entradas y salidas en directo.

Nuestro diseño será simple: tener un campo de entrada y luego un campo de salida. Por ahora, tomemos la entrada y repitámosla como
 salida.

    app = dash.Dash()
    app.layout = html.Div([
      dcc.Input(id='input', value='Escribe algo aqui!', type='text'),
      html.Div(id='output')
    ])

A continuación, crearemos la función que produce lo que queramos basándonos en la entrada. En este caso, sólo será un texto simple,
 pero también podríamos tener una salida de datos gráficos basados en alguna entrada…etc. Vamos a usar el siguiente decorador para 
 envolver esta función y determinar a qué corresponden las entradas y salidas:

    
    @app.callback(
      Output(component_id='output', component_property='children'),
      [Input(component_id='input', component_property='value')]
    )

Para continuar vamos a crear la función:

    @app.callback(
      Output(component_id='output', component_property='children'),
      [Input(component_id='input', component_property='value')]
    )
    def update_value(input_data):
      return 'Input: "{}"'.format(input_data)

Simple por ahora, pero podrías imaginarte cómo podríamos hacer esto más interesante y bastante rápido. Por ejemplo, podríamos estar 
usando Quandl, esperando un símbolo válido (evaluando la validez ya sea por expresiones regulares o intentando tirar hasta que algo
 es realmente devuelto) para algún conjunto de datos, una vez válido, devolver el marco de datos, tal vez en forma de tabla, o 
incluso un gráfico.
Código completo de la interface de usuario interactivas con Dash"""

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
app = dash.Dash()
app.layout = html.Div([
  dcc.Input(id='input', value='Escribe algo aqui!', type='text'),
  html.Div(id='output')
])
@app.callback(
  Output(component_id='output', component_property='children'),
  [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
  return 'Input: "{}"'.format(input_data)
if __name__ == '__main__':
  app.run_server(debug=True)

"""Ahora ejecutando todo el código deberíamos ver:

curso-Dash-aprender-python

¿Recuerdas lo que dije antes sobre usar Dash para graficar dinámicamente algo basado en un símbolo? Pues lo hacemos en el próximo 
tutorial."""
