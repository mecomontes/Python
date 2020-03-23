from flask import Flask   # Importar al mÃ³dulo de Flask
from flask import request # Permite trabajar con parámetros
app = Flask(__name__)     # Crear un aplicaciÃ³n. Nueva instancia con parámetro name

@app.route("/")           # Se define una ruta bÃ¡sica. wrap o decorador
def index():               # FunciÃ³n correspondiente para manejar la solicitud                                                               
    return "Hola Mundo"     # Lo Ãºnico que se muestra en nuestra web

@app.route("/saluda")           # Se define una ruta bÃ¡sica. wrap o decorador
def saluda():               # FunciÃ³n correspondiente para manejar la solicitud                                                               
    return "Hola, Cómo estas?"     # Lo Ãºnico que se muestra en nuestra web

@app.route("/params")           # Se define una ruta bÃ¡sica. wrap o decorador
def params():               # FunciÃ³n correspondiente para manejar la solicitud                                                               
    param1 = request.args.get('params1','no contiene este parametro')
    param2 = request.args.get('params2','no contiene este parametro') 
    return 'El parametro es:  {} , {}'.format(param1,param2)    # Lo Ãºnico que se muestra en nuestra web
    #http://localhost:8000/params
    #http://localhost:8000/params?params1=Robinson%20Montes
    #http://localhost:8000/params?params1=Robinson%20Montes&params2=Meco
    
if __name__ == "__main__":#Revis si el archivo ejecutado es el programa principal
    app.run(debug = True, port = 8000)   # Ejecutar la aplicaciÃ³n. correr el servidor

# http://localhost:8000/
