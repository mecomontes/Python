""" Activar en google el envío de correo desde aplicaciones externas
    https://myaccount.google.com/lesssecureapps?pli=1
"""

#importar librería de correos 
import smtplib

#Credenciales de Gmail
gmail_user = 'mecomontes@gmail.com' #mi correo de Gmail
gmail_password = 'mecomontes0116' #password del correo

#datos del correo a enviar
from_email = gmail_user

#lista de email donde se envía el correo
to = ['mecomontes@gmail.com']
subject = 'prueba desde python'
body = 'contenido del correo'

#añadir headers del correo
mail ="""\
From: {}
To: {}
Subject: {}
""".format(from_email,", ".join(to), subject, body)

#usar la librería para enviarlo
try:
    #conexión con el servidor smtp de google
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #Nos identificamos con el servidor
    server.ehlo()
    #accedemos a nuestra cuenta
    server.login(gmail_user, gmail_password)
    #enviamos el email
    server.sendmail(from_email, to, mail)
    #cerramos conexión
    server.close()
    
    print('Correo enviado')
except Exception as e:
    print('Error al enviar el correo: ', e)
    