#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# Estos modulos habilitan la comunicacion con el CGI
import cgi, cgitb; cgitb.enable()
# HTTP Header. Es conveniente ponerlo inmediatamente despues del import
print("Content-type: text/html; charset=utf-8\n\n")

# Para usar el Dicctionario de sustitucion
from string import Template

# Para generar un numero aleatorio
import random

class AnswerGenerator():
    answers = ["Ask Again later"
        , "Can Not Predict Now","Without a Doubt"
        , "Is Decidely So","Concentrate and Ask Again","My Sources Say No"
        , "Yes, Definitely","Don't Count On It","Signs Point to Yes"
        , "Better Not Tell You Now","Outlook Not So Good","Most Likely"
        , "Very Doubtful","As I See It, Yes","My Reply is No","It Is Certain"
        , "Yes","You May Rely On It","Outlook Good","Reply Hazy Try Again"]

    def get_random_answer(self):
        return self.answers[random.randrange(0, len(self.answers))]

if __name__ == "__main__":

    # Crea una instancia de .FieldStorage() donde se
    form = cgi.FieldStorage()

    # Obtiene datos de los campos
    question = form.getvalue('Question')

    with open("eight_ball.py.html") as template:
        html_template = template.read()

    subst_dict = dict (
        title = "Python WITHOUT Frameworks",
        header = "Ask the 8 Ball",
        footer = "Ing. Linux says hi!",
        question = "",
        answer = ""
    )

    if (question != None):
        generator = AnswerGenerator()

        subst_dict["question"] = question
        subst_dict["answer"] = generator.get_random_answer()

    # Imprime el template sustituyendo las palabras en el diccionario
    print(Template(html_template).safe_substitute(subst_dict))