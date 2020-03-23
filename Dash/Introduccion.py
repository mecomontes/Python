"""                         Introducción a Dash, una potente GUIs con visualizadores dinámicos
curso-Dash-aprender-python
Objetivo del 1º tutorial de Curso de Dash en Python

-Conocer un poco acerca de Dash

-Aprender a instalar Dash.

-Realizar un ejemplo practico.

Hola y bienvenidos a una serie de tutoriales Python sobre visualización de datos con Dash. Para graficar datos personalmente 
siempre he usado Matplotlib, la cual es una librería de gráficos normal, y es el backend de muchos otros paquetes como el de 
Pandas. Aunque he sido capaz de hacer cualquier gráfico que necesite en Matplotlib, hay algunos problemas que siempre he 
experimentado:

    Interactividad – Los gráficos de Matplotlib no son interactivos.
    Incrustación – Mientras que podemos incrustar gráficos de matplotlib en otras aplicaciones, esto puede ser un proceso muy 
    tedioso y toma mucho tiempo de desarrollo.
    Estética – Aunque es algo trivial, sí importa. Cuando las gráficas son sólo para mí, no importa mucho cómo se vean. Si estás 
    intentando vender algo basado en gráficos, o vender una aplicación con tablas incrustadas. Matplotlib es probablemente 
    inaceptable porque la representación no es atractiva.

Dash es un framework de Python para la creación de aplicaciones web analíticas

Para gráficos rápidos para probar, prototipos…etc, lo mas recomendable es usar Matplotlib, principalmente debido a la muy buena 
integración con la librería Pandas.
Características de Dash:

    Ligero

Las aplicaciones Dash requieren muy poco tiempo para empezar y son extremadamente ligeras en de Python puro.

    Control directo

Dash proporciona una interfaz sencilla para vincular controles de interfaz de usuario, como controles deslizantes, desplegables y 
gráficos, con el código de análisis de datos de Python.

    Completamente personalizable

Cada elemento estético de una aplicación Dash es personalizable. Las aplicaciones Dash se crean y se publican en la Web, por lo 
que está disponible toda la potencia de CSS.


Instalación de Dash

Para usar Dash, necesitamos los siguientes paquetes: dash, dash-renderer, dash-html-components, dash-core-components, y plotly. 
Estos paquetes también tienen varias dependencias. Puede instalarlos en Linux con:

sudo pip install dash dash-renderer dash-html-components dash-core-components plotly

o, en Windows, abra cmd.exe como administrador y haga lo siguiente:

pip install dash dash-renderer dash-html-components dash-core-components plotly

Ejemplo con Dash

Ahora vamos a mostrar un ejemplo rápido y básico de Dash en acción.

Para empezar, hagamos algunas importaciones:"""

import dash
import dash_core_components as dcc
import dash_html_components as html

 

"""Aquí, sólo estamos importando cosas como la librería dash, varios componentes (cosas como componentes de gráficos), y luego 
componentes HTML (cosas como etiquetas div…etc). A continuación, comenzamos nuestra aplicación:"""

app = dash.Dash()

"""Dado que Dash está construido alrededor del framework de Flask, muchos de estos ajustes y configuraciones de aplicaciones 
deberían resultarle familiares si está familiarizado con Flask. A continuación, creamos un diseño:"""

app.layout = html.Div('Tutoriales Dash en AprenderPython.com')

"""En el caso anterior, esto haría que una aplicación web simplemente dijera “Tutoriales Dash en AprenderPython.com” en la 
carga de la página. Nada asombroso, pero bueno es muy simple! Ahora hagamos esto:"""

if __name__ == '__main__':
    app.run_server(debug=True)

"jecute esto, y debería ver lo siguiente en su consola:"
"""curso-Dash-aprender-python

Esto debería ser bastante fácil de entender ahora mismo, pero rápidamente empezaremos a añadir atributos e incrustar etiquetas 
HTML hijas dentro de aquí. El contenido real de una etiqueta se encuentra bajo un parámetro llamado children, que tendrá el 
siguiente aspecto:"""

app.layout = html.Div(children='Tutoriales Dash en AprenderPython.com')

#Restarting with stat

#Ahora, puedes escribir en tu navegador 127.0.0.1:8050 y deberías ver algo como:

