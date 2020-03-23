#from flask import Flask   # Importar al m贸dulo de Flask
from flask import Flask, render_template # Importar el renderizador
app = Flask(__name__)     # Crear un aplicaci贸n. Nueva instancia con par醡etro name

@app.route("/")           # Se define una ruta b谩sica. wrap o decorador
def main():               # Funci贸n correspondiente para manejar la solicitud                                                               
 #   return "Welcome!"     # Lo 煤nico que se muestra en nuestra web
    return render_template('index.html') #Devuelve el archivo plantilla renderizado



if __name__ == "__main__":#Revis si el archivo ejecutado es el programa principal
    app.run(debug=True)   # Ejecutar la aplicaci贸n. correr el servidor

# http://localhost:5000/
    
