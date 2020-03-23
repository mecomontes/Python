"""                                             Gráficos en vivo – GUIs de visualización de datos con Dash y Python
quandl-dash-python
Objetivo del 4º tutorial de Curso de Dash en Python

-Indicaremos paso a paso las importaciones, la sintaxis y las acciones básicas para realizar un gráfico a tiempo real.

-Te mostramos la sintaxis completa de un gráfico a tiempo real.

Bienvenido a la cuarta parte de la serie de tutoriales de visualización de datos en web con Dash. En este tutorial, vamos a crear 
gráficos de actualización en vivo con Dash y Python. Las gráficas en vivo pueden ser útiles para una variedad de tareas, pero
 planeo usar gráficas en vivo para mostrar datos de sensores que están constantemente recolectando información.
Gráficos a tiempo real con Dash en Python

Para empezar, hagamos algunas importaciones:

    import dash
    from dash.dependencies import Output, Event
    import dash_core_components as dcc
    import dash_html_components as html
    import plotly
    import random
    import plotly.graph_objs as go
    from collections import deque

 

La mayoría de estas importaciones deberían tener sentido para usted, excepto tal vez las dos últimas importaciones. Vamos a 
importar plotly.graph_objs ya que es la manera que he encontrado para establecer límites de ejes para las tablas. Probablemente 
hay una manera de hacerlo sin esa importación. A continuación, estamos importando deque, que es un ingenioso contenedor que viene 
con la capacidad de establecer un límite de tamaño (maxlen). Una vez que el contenedor deque está lleno, cualquier apéndice 
subsiguiente mostrará el primer elemento(s) para cumplir con la restricción.

A continuación, comencemos con los datos de muestra. Sólo vamos a crear algunos datos aleatorios para dar un ejemplo:

    X = deque(maxlen=20)
    X.append(1)
    Y = deque(maxlen=20)
    Y.append(1)

Desde aquí, añadiremos movimientos aleatorios para simular algunos datos. A continuación, vamos a configurar la propia aplicación:

    app = dash.Dash(__name__)
    app.layout = html.Div(
      [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
          id='graph-update',
          interval=1*1000
        ),
      ]
    )

 

Un gráfico está aquí como de costumbre, sólo, esta vez, sólo con un ID, y animate a true. Debajo de esto, tenemos un dcc.Interval 
que especificará con qué frecuencia se actualizará este div. Ahora, todo lo que necesitamos es algún tipo de función que actualice 
el elemento con el id de live-graph. Hemos hecho esto antes con la entrada/salida del campo de texto. En este caso, sin embargo,
 no necesitamos ninguna entrada, sólo salida. Sin embargo, el hecho de que no tengamos ninguna entrada no significa que no 
 necesitemos algún tipo de disparador para que esta función funcione. Este disparador se llama event. En nuestro caso, el event 
 es en realidad sólo el intervalo que hemos establecido para ejecutarse con el id de graph-update. Por lo tanto, necesitamos hacer
 una función que salga a live-graph, y que sea activada por un event con el id de graph-update. Nuestro decorador/envoltura será 
 así:

    @app.callback(Output('live-graph', 'figure'),
      events=[Event('graph-update', 'interval')])

Continuando con esto, agreguemos algunos datos aleatorios. Tal vez uses una base de datos, o tal vez algún archivo.csv o.txt. 
Quién sabe.

    @app.callback(Output('live-graph', 'figure'),
        events=[Event('graph-update', 'interval')])
    def update_graph_scatter():
        X.append(X[-1]+1)
        Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))

Ahora que hemos añadido algunos datos nuevos cada vez que se ejecuta esta función, también queremos seguir adelante y graficarla. 
Este será el típico gráfico de trazado:

    data = plotly.graph_objs.Scatter(
      x=list(X),
      y=list(Y),
      name='Scatter',
      mode= 'lines+markers'
      )

 

Nótese que necesitamos pasar una lista para x e y, no podemos conservar el objeto deque.

Finalmente, todo lo que necesitamos hacer es devolver algo que complete un elemento “graph” en el guión. Recordemos el ejemplo de 
la parte 1:

     dcc.Graph(
       id='example',
       figure={
         'data': [
           {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 2, 1, 7], 'type': 'line', 'name': 'Bicicletas'},
           {'x': [1, 2, 3, 4, 5], 'y': [4, 6, 4, 7, 5], 'type': 'bar', 'name': 'Bicicletas electricas'},
         ],
         'layout': {
           'title': 'Ejemplo básico Dash'
     }
     }
     )

 

Ya tenemos el dcc.Graph, que ya tiene un id, así que realmente sólo necesitamos esa parte de la figura. Así:

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
      yaxis=dict(range=[min(Y),max(Y)]),)}

Entonces la función entera es:

    @app.callback(Output('live-graph', 'figure'),
        events=[Event('graph-update', 'interval')])
    def update_graph_scatter():
        X.append(X[-1]+1)
        Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))
        data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )
        return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
             yaxis=dict(range=[min(Y),max(Y)]),)}

Código completo de un Gráfico a tiempo real con Dash en Python"""

import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)
app = dash.Dash(__name__)
app.layout = html.Div(
  [
    dcc.Graph(id='live-graph', animate=True),
    dcc.Interval(
      id='graph-update',
      interval=1*1000
    ),
  ]
)
@app.callback(Output('live-graph', 'figure'),
    events=[Event('graph-update', 'interval')])
def update_graph_scatter():
  X.append(X[-1]+1)
  Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))
  data = plotly.graph_objs.Scatter(
    x=list(X),
    y=list(Y),
    name='Scatter',
    mode= 'lines+markers'
    )
  return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
      yaxis=dict(range=[min(Y),max(Y)]),)}
if __name__ == '__main__':
  app.run_server(debug=True)