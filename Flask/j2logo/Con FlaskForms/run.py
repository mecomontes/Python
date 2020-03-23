from flask import Flask
from flask import render_template
from flask import request

import forms

app = Flask(__name__)

# Renderizar los templates con Jinja2
@app.route("/")
def index():
    page = request.args.get('page', 1)
    list = request.args.get('list', 20)
    return render_template("index.html")

@app.route("/p/<string:slug>/")
def show_post(slug = "Meco"):
    return render_template("post_view.html", slug_title=slug)

# Dos diferentes URL para el administrador y modificaciones
@app.route("/admin/")
@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return "post_form {}".format(post_id)

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    return render_template("signup_form.html")

# http://localhost:5000/signup/

if __name__ == "__main__":
    app.run(debug = True, port = 8000) 