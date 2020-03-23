from flask import Flask   
from flask import render_template

app = Flask(__name__)    

@app.route("/")          
def index():           
    name = 'Meco'     
    return render_template('extends.html', nombre = name)   

@app.route("/client/")          
def client():           
    list_name = [ 'Meco' , 'Katthy' , 'Candy' ]     
    return render_template('client.html', lista = list_name)   

if __name__ == "__main__":
    app.run(debug = True, port = 8000) 
