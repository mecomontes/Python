from flask import Flask   
from flask import render_template

import forms

app = Flask(__name__)    

@app.route('/')          
def index():     
    comment_form = forms.CommentForm()    
    title = 'Curso Flask'                                          
    return render_template('index.html' , title = title, form = comment_form)   

if __name__ == "__main__":
    app.run(debug = True, port = 8000)   


## MAcro del tutorial 10
    
"""{% macro show_list_h(value) %}

    <h1> {{ value }} </h1>
    <h2> {{ value }} </h2>
    <h3> {{ value }} </h3>
    <h4> {{ value }} </h4>
    <h5> {{ value }} </h5>


{% endmacro %}"""