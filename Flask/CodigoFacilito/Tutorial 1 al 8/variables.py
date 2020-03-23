from flask import Flask   
from flask import render_template

app = Flask(__name__)    

@app.route("/user/<name>/")          
def user(name = 'Meco'):                
    age = 34
    lista = [1,2,3,4,6]
    return render_template('user.html', nombre = name, Edad = age, Lista = lista)   

if __name__ == "__main__":
    app.run(debug = True, port = 8000)  