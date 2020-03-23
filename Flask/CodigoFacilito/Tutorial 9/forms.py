from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
    
class CommentForm(Form):
    username = StringField('username')
    email = EmailField('Correo electrónico')
    comments = TextField('Comentario')
