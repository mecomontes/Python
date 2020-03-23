"""                     Ejemplo de aplicación de datos de vehículos – GUIs de visualización de datos con Dash y Python
cursodash-aprender-python
Objetivo del 5º tutorial de Curso de Dash en Python

-Cubriremos cómo realizar una aplicación de lectura del sensor de un vehículo.

-Te enseñamos la sintaxis completa y un ejemplo.

Bienvenido a la quinta parte de las aplicaciones de visualización de datos de la serie de tutoriales Python con Dash.
Aplicación de lectura de sensores de un vehículo con Dash

Ya que podría ser tedioso seguir el proceso si no tuvieras un lector OBD y un coche encendido, vamos a usar datos aleatorios.

Queremos que esta aplicación tenga un menú desplegable con opciones de datos que podríamos querer visualizar. Cuando elegimos algo,
 queremos añadirlo a la lista de cosas que estamos graficando. También nos gustaría tener la posibilidad de no visualizar algunas 
 gráficas y queremos que todos estos datos se grafiquen en vivo y tiempo real. Finalmente, nos gustaría tener los gráficos de un 
 tamaño intuitivo y dispuestos en la página web, aunque esto depende de cuántos gráficos estamos tratando de visualizar.

Para empezar, hagamos nuestras importaciones que necesitaremos:

    import dash
    import dash_core_components as dcc
    import dash_html_components as html
    from pandas_datareader.data import DataReader
    import time
    from collections import deque
    import plotly.graph_objs as go
    import random

A continuación, definiremos la aplicación, y luego especificaremos un diccionario para los puntos de datos que pretendemos cubrir:

    app = dash.Dash('Datos del Vehiculo a Tiempo Real')
    max_length = 50
    times = deque(maxlen=max_length)
    oil_temps = deque(maxlen=max_length)
    intake_temps = deque(maxlen=max_length)
    coolant_temps = deque(maxlen=max_length)
    rpms = deque(maxlen=max_length)
    speeds = deque(maxlen=max_length)
    throttle_pos = deque(maxlen=max_length)
    data_dict = {"Temperatura aceite":oil_temps,
    "Temperatura de Entrada": intake_temps,
    "Temperatura Refrigerante": coolant_temps,
    "RPM":rpms,
    "Velocidad":speeds,
    "Acelerador Posicion":throttle_pos}

Para esta aplicación, las opciones de datos que podemos graficar son estáticas, no hay razón para que cambien. Dicho esto, podemos
 usar eventos para actualizar esta lista y su menú desplegable, dependiendo de algún evento que esté cambiando. Necesitamos algunos
 datos de muestra con los que trabajar, así que:

    def update_obd_values(times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos):
    times.append(time.time())
     if len(times) == 1:
       #starting relevant values
       oil_temps.append(random.randrange(180,230))
       intake_temps.append(random.randrange(95,115))
       coolant_temps.append(random.randrange(170,220))
       rpms.append(random.randrange(1000,9500))
       speeds.append(random.randrange(30,140))
       throttle_pos.append(random.randrange(10,90))
     else:
       for data_of_interest in [oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos]:
         data_of_interest.append(data_of_interest[-1]+data_of_interest[-1]*random.uniform(-0.0001,0.0001))
     return times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos
    times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos = update_obd_values(times, oil_temps, intake_temps,
    coolant_temps, rpms, speeds, throttle_pos)

No quiero pasar mucho tiempo en este código, básicamente, sólo hace que los datos de muestra de estos valores que estamos midiendo
 sean un poco razonables. Si usted tiene una base de datos real o un sensor real para leer, le recomiendo encarecidamente que 
 reemplace mi código por algo que lea datos significativos!

Ahora podemos llegar a la estructura de esta aplicación, el diseño:

    app.layout = html.Div([
      html.Div([
        html.H2('Vehicle Data',
          style={'float': 'left',
                  }),
        ]),
     dcc.Dropdown(id='vehicle-data-name',
       options=[{'label': s, 'value': s}
         for s in data_dict.keys()],
       value=['Coolant Temperature','Oil Temperature','Intake Temperature'],
       multi=True
       ),
     html.Div(children=html.Div(id='graphs'), className='row'),
     dcc.Interval(
       id='graph-update',
       interval=100),
     ], className="container",style={'width':'98%','margin-left':10,'margin-right':10,'max-width':50000})

No debería sorprender, pero algo de esto podría requerir una explicación. Las opciones desplegables de dcc.Dropdown provienen de
 los valores de nuestro diccionario. Una vez más, este desplegable podría ser actualizado dinámicamente por eventos, ¡y no 
 necesita ser estático!. El Multi=True significa que podemos tener múltiples opciones seleccionadas.

Además de este menú desplegable, necesitamos el gráfico, pero, tenga en cuenta que tenemos un gráfico de identificación div dentro
 de un className de “fila”. El parámetro className es lo que reemplaza al parámetro class desde dentro de HTML. No podemos usar 
 class ya que esa palabra clave está ocupada en Python. Luego, aunque está al final, es parte del div principal y vemos que se 
 están aplicando algunos estilos. Me pareció que el Dash CSS por defecto tiene un ancho máximo por defecto para divs o algo así,
 así que puse un nuevo ancho máximo, y luego establecí el ancho de este div para que sea el 98% de la página. Noté que había mucho 
 espacio desperdiciado que simplemente no quería. Puedes sentirte libre de hacer los estilos que quieras!

Llegará más tarde, pero ten en cuenta que el className de la fila no viene del Dash CSS. En su lugar, viene de un marco de trabajo 
CSS externo (http://materializecss.com). Los estoy usando, porque estoy familiarizado con ese marco de trabajo, y es súper útil
 para hacer diseños de front-end de respuesta. No he encontrado nada para hacer inmersiones personalizadas/dinámicas basadas en el 
 contenido de los estilos predeterminados de Dash, así que por eso también tengo http://materializecss.com. Dicho esto, asegúrese 
 de comprobar todo lo que Dash tiene para ofrecer. Por ejemplo, echa un vistazo: los componentes principales. Cosas como subir 
 datos, tablas, deslizadores, desplegables (obviamente) y más …

Mientras estoy en el tema de los documentos, también le sugiero encarecidamente que eche un vistazo a la Documentación de Plotly, 
principalmente con cosas como diseños, conexión a bases de datos y generación de informes. Plotly te ofrece MUCHAS cosas que de 
otra manera esperarías que tuvieras que descubrir o construirte para ti mismo…

Bien, volvamos a nuestra aplicación, escribamos primero al decorador. Este es interesante, ya que, en realidad, vamos a tener 
Input, Output, y eventos!

    @app.callback(
     dash.dependencies.Output('graphs','children'),
     [dash.dependencies.Input('vehicle-data-name', 'value')],
     events=[dash.dependencies.Event('graph-update', 'interval')]
     )

Toda la salida en este caso va al div de graphs-IDed. Entonces, la entrada será el valor de nuestro desplegable con la 
identificación del nombre del vehículo. Finalmente, tenemos nuestro evento de intervalo, del que nos enteramos en nuestro 
tutorial anterior. Así que, aquí, tenemos un evento que está actualizando las cosas y la entrada del usuario.

Ahora para la función:

    @app.callback(
      dash.dependencies.Output('graphs','children'),
      [dash.dependencies.Input('vehicle-data-name', 'value')],
      events=[dash.dependencies.Event('graph-update', 'interval')]
      )
    def update_graph(data_names):
      graphs = []
      for data_name in data_names:
        data = go.Scatter(
          x=list(times),
          y=list(data_dict[data_name]),
          name='Scatter',
          fill="tozeroy",
          fillcolor="#6897bb"
          )
        graphs.append(html.Div(dcc.Graph(
          id=data_name,
          animate=True,
          figure={'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(times),max(times)]),
                  yaxis=dict(range=[min(data_dict[data_name]),max(data_dict[data_name])]),
                  margin={'l':50,'r':1,'t':45,'b':1},
                  title='{}'.format(data_name))}
          ), className=class_choice))
      return graphs

Esta función aún no está terminada, pero quería mantenerla simple y separar los datos y el código de Dash. Básicamente, esta
 función sólo construye la lista de gráficos, creando gráficos para cada uno de los elementos desde dentro en data_names, que 
 se pasa a esta función a través de nuestros valores del menú desplegable. Ahora realmente necesitamos los datos, y notarás que 
 necesitamos algo para elegir la opción class_choice.

    @app.callback(
      dash.dependencies.Output('graphs','children'),
      [dash.dependencies.Input('vehicle-data-name', 'value')],
      events=[dash.dependencies.Event('graph-update', 'interval')]
      )
    def update_graph(data_names):
      graphs = []
      update_obd_values(times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos)
      if len(data_names)&amp;gt;2:
        class_choice = 'col s12 m6 l4'
      elif len(data_names) == 2:
        class_choice = 'col s12 m6 l6'
      else:
        class_choice = 'col s12'
      for data_name in data_names:
        data = go.Scatter(
          x=list(times),
          y=list(data_dict[data_name]),
          name='Scatter',
          fill="tozeroy",
          fillcolor="#6897bb"
          )
        graphs.append(html.Div(dcc.Graph(
          id=data_name,
          animate=True,
          figure={'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(times),max(times)]),
                    yaxis=dict(range=[min(data_dict[data_name]),max(data_dict[data_name])]),
                    margin={'l':50,'r':1,'t':45,'b':1},
                    title='{}'.format(data_name))}
          ), className=class_choice))
      return graphs

La parte del if:

    if len(data_names)&amp;gt;2:
      class_choice = 'col s12 m6 l4'
    elif len(data_names) == 2:
      class_choice = 'col s12 m6 l6'
    else:
      class_choice = 'col s12'

A partir del estilo del framework Materializar CSS (todavía tenemos que introducirlo) es lo que dicta cuántos gráficos por “fila” 
permitiremos, dependiendo del tamaño de la pantalla. Los valores dictan cuántas “columnas”, de 12, ocupará un elemento. Por lo 
tanto, cuando hay sólo 1 gráfico, podríamos también tomar todas las columnas, sin importar el tamaño de la ventana. Si hay 
exactamente 2 elementos, entonces, en una pantalla pequeña, queremos que cada gráfico sea completamente ancho (por lo que no son 
súper comprimidos/delgados), pero luego ocupan sólo 6 columnas en las pantallas medianas y grandes, por lo que habría 2 cuadros 
por fila en este caso. Finalmente, si hay muchos gráficos para graficar, entonces, de nuevo, en una pantalla pequeña, un gráfico 
ocupa todas las columnas, en una pantalla mediana ocupamos 6, y, en una pantalla grande, cada gráfico ocupa 4 columnas, por lo 
que 3 gráficos podrían estar en cada fila.

Ahora, para que las cosas funcionen con el CSS de Materialize, necesitamos traerlo. Además, para usar Materialize en toda su 
extensión, necesitamos traer el Materialize JS también. Aunque es posible que no desee utilizar Materialize específicamente, es 
posible que a menudo se encuentre con que desea introducir CSS externos u otros scripts. Para hacer esto:

    external_css = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"]
    for css in external_css:
      app.css.append_css({"external_url": css})

Lo anterior para CSS, y esto para javascript:

    external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']
    for js in external_js:
      app.scripts.append_script({'external_url': js})

Finalmente corremos nuestra aplicación:

    if __name__ == '__main__':
    app.run_server(debug=True)

Código completo de la aplicación de lectura de sensores de un vehículo con Dash"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader.data import DataReader
import time
from collections import deque
import plotly.graph_objs as go
import random
app = dash.Dash('Datos del Vehiculo a Tiempo Real')
max_length = 50
times = deque(maxlen=max_length)
oil_temps = deque(maxlen=max_length)
intake_temps = deque(maxlen=max_length)
coolant_temps = deque(maxlen=max_length)
rpms = deque(maxlen=max_length)
speeds = deque(maxlen=max_length)
throttle_pos = deque(maxlen=max_length)
data_dict = {"Oil Temperature":oil_temps,
  "Intake Temperature": intake_temps,
  "Coolant Temperature": coolant_temps,
  "RPM":rpms,
  "Speed":speeds,
  "Throttle Position":throttle_pos}
def update_obd_values(times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos):
  times.append(time.time())
  if len(times) == 1:
    #starting relevant values
    oil_temps.append(random.randrange(180,230))
    intake_temps.append(random.randrange(95,115))
    coolant_temps.append(random.randrange(170,220))
    rpms.append(random.randrange(1000,9500))
    speeds.append(random.randrange(30,140))
    throttle_pos.append(random.randrange(10,90))
  else:
    for data_of_interest in [oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos]:
      data_of_interest.append(data_of_interest[-1]+data_of_interest[-1]*random.uniform(-0.0001,0.0001))
  return times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos
times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos = update_obd_values(times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos)
app.layout = html.Div([
  html.Div([
    html.H2('Datos del Vehiculo a Tiempo Real',
      style={'float': 'left',
            }),
    ]),
  dcc.Dropdown(id='vehicle-data-name',
               options=[{'label': s, 'value': s}
                  for s in data_dict.keys()],
               value=['Coolant Temperature','Oil Temperature','Intake Temperature'],
               multi=True
               ),
  html.Div(children=html.Div(id='graphs'), className='row'),
  dcc.Interval(
    id='graph-update',
    interval=100),
  ], className="container",style={'width':'98%','margin-left':10,'margin-right':10,'max-width':50000})
@app.callback(
  dash.dependencies.Output('graphs','children'),
  [dash.dependencies.Input('vehicle-data-name', 'value')],
  events=[dash.dependencies.Event('graph-update', 'interval')]
  )
def update_graph(data_names):
  graphs = []
  update_obd_values(times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos)
  if len(data_names)&amp;gt;2:
    class_choice = 'col s12 m6 l4'
  elif len(data_names) == 2:
    class_choice = 'col s12 m6 l6'
  else:
    class_choice = 'col s12'
  for data_name in data_names:
    data = go.Scatter(
      x=list(times),
      y=list(data_dict[data_name]),
      name='Scatter',
      fill="tozeroy",
      fillcolor="#6897bb"
      )
    graphs.append(html.Div(dcc.Graph(
      id=data_name,
      animate=True,
      figure={'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(times),max(times)]),
                yaxis=dict(range=[min(data_dict[data_name]),max(data_dict[data_name])]),
                margin={'l':50,'r':1,'t':45,'b':1},
                title='{}'.format(data_name))}
      ), className=class_choice))
  return graphs
external_css = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"]
for css in external_css:
  app.css.append_css({"external_url": css})
external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']
for js in external_css:
  app.scripts.append_script({'external_url': js})
if __name__ == '__main__':
  app.run_server(debug=True)