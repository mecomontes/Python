"""                                                     Gráficos dinámicos con Dash

quandl-dash-python2
Objetivo del 3º tutorial de Curso de Dash en Python

-Aprender a realizar un gráfico de ejemplo

-Veremos la sintaxis completa para realizar el gráfico dinámico.

Bienvenido a la tercera parte de la serie de tutoriales de visualización de datos basada en web con Dash. Hasta este punto, hemos 
aprendido cómo hacer un gráfico simple y cómo actualizar dinámicamente elementos HTML a tiempo real sin necesidad de actualizar la 
página.


                                                Gráficos dinámicos con Dash de bitcoin
nos registramos en quandl.com

Vamos la web quandl.com, y tomaremos alguna información de los valores de las criptomonedas que ahora estan muy de moda. Para 
seguir este tutorial exacto necesitarás la librería quandl. Si aún no lo tienes, ejecuta esta línea como administrador en tu 
cmd.exe:

pip install quandl

Ahora nos vamos a la web quandl.com y nos registramos para poder usar su API para leer los valores que vamos a plotear con Dash. 
En el buscador he puesto bitfinex y vemos que es gratis, ver la siguiente imagen:

quandl-dash-python

Yo he seleccionado el BTC/EUR, por lo que ahora me parece una grafica del valor del bitcoin en euros. A continuación en la parte 
derecha podemos ver la forma de exportar estos datos entre los que podemos encontrar python, ver la siguiente imagen:

quandl-dash-python2

Si pulsamos en python nos dira el código y su API, en mi caso me sale:

quandl.get(“BITFINEX/BTCEUR”, authtoken=”4YdrsrrLrRHyJFSFGzwk”)

Ahora ya podemos hacer una prueba simple para ver si tenemos los datos:

    import quandl
    mydata=quandl.get("BITFINEX/BTCEUR", authtoken="4YdrsrrLrRHyJFSFGzwk", start_date="2017-5-5", end_date="2018-3-3")
    print(mydata.High)

Ahora por consola me sale el precio high del bitcoin en euros. Es posible que recibas una advertencia sobre la falta de 
fiabilidad o que la web ya no tenga estos valores. Si es sólo una advertencia, ignóralo, de lo contrario revisa otra cosa a 
plotear en Quandl, y siéntete libre de enviarme un correo electrónico, puedo actualizar este código usando alguna otra fuente.

Seguimos adelante para extraer todos los datos y hacer un plot dinámico con Dash. Escribe una fecha de inicio, una fecha de 
finalización, y ya está todo listo. El retorno es un marco de datos con Dash.

Ya hemos visto cómo hacer un gráfico básico en python con Dash.
Código completo de Gráficos dinámicos de bitcoin con Dash

Todo lo que necesitamos hacer es básicamente reemplazar los valores x e y con lo que queramos esta vez. Bastante fácil, partiendo 
del código básico del gráfico anterior:"""

import quandl
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
app = dash.Dash()
app.layout = html.Div(children=[
  html.Div(children='''
  BTC/Eur:
  '''),
  dcc.Input(id='input', value='', type='text'),
  html.Div(id='output-graph'),
])
@app.callback(
  Output(component_id='output-graph', component_property='children'),
  [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
  mydata =quandl.get("BITFINEX/BTCEUR", authtoken="KkuxY-z7FbHxc5uMx-xz", start_date="2017-5-5", end_date="2018-3-3")
  return dcc.Graph(
    id='example-graph',
    figure={
      'data': [
        {'x': mydata.index, 'y': mydata.High, 'type': 'line', 'name': input_data},
      ],
      'layout': {
        'title': input_data
      }
    }
  )
if __name__ == '__main__':
  app.run_server(debug=True)

#Resultado final de un Gráfico dinámico del bitcoin con Dash

#Ahora si vamos a la dirección: http://127.0.0.1:8050/ vemos nuestra gráfica perfectamente definida: