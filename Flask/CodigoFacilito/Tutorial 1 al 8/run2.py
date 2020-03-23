from flask import Flask   # Importar al mÃ³dulo de Flask
from flask import request # Permite trabajar con parámetros

app = Flask(__name__)     # Crear un aplicaciÃ³n. Nueva instancia con parámetro name

@app.route("/")           # Se define una ruta bÃ¡sica. wrap o decorador
def index():               # FunciÃ³n correspondiente para manejar la solicitud                                                               
    return "Hola Mundo"     # Lo Ãºnico que se muestra en nuestra web

#params/Robinson/Skills
@app.route("/params/")     # sin parámetro
@app.route("/params/<name>/")   # Llevar parámetro name
@app.route("/params/<name>/<last_name>/")   # Llevar parámetro name
@app.route("/params/<name>/<last_name>/<int:edad>/")   # Llevar parámetro name

def params(name = 'este es un valor por default', last_name = 'nada', edad = 'no nacido'): # Por defecto, los parámetros son de tipo string                                                               
    return 'El parametro es:  {} {}, Edad {} Años'.format(name,last_name,edad)    # Lo Ãºnico que se muestra en nuestra web
    
if __name__ == "__main__":#Revis si el archivo ejecutado es el programa principal
    app.run(debug = True, port = 8000)   # Ejecutar la aplicaciÃ³n. correr el servidor
