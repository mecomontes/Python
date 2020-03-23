"""    ### Público
class Usuario:
    def __init__(self, username, password, email): #Metodo init con sus atributos username, password, email
        self.username = username  #Atributo
        self.password = self.generar_password(password)  #Atributo
        self.email = email        #Atributo
        
    def generar_password(self, password):
        return password.upper()
Meco =Usuario('Robison', '1234', 'mecomontes@gmail.com') #Objeto Meco al cual se le pasan los atributos de la plantilla Usuario
print(Meco.username)
Meco.password = 'Aquí se cambia el password
print(Meco.password)
print(Meco.email)
"""

"""
### Privado

class Usuario:
    def __init__(self, username, password, email): #Metodo init con sus atributos username, password, email
        self.username = username  #Atributo Púbico
        self.__password = self.__generar_password(password)  #Atributo Privado
        self.email = email        #Atributo Público
        
    def __generar_password(self, password):
        return password.upper()
    
    def get_password(self):
        return self.__password
    
Meco =Usuario('Robison', 'hola1234', 'mecomontes@gmail.com') #Objeto Meco al cual se le pasan los atributos de la plantilla Usuario
print(Meco.username)
print(Meco.email)
print(Meco.get_password())
"""

class Usuario:
    def __init__(self, username, password, email): #Metodo init con sus atributos username, password, email
        self.username = username  #Atributo Púbico
        self.__password = self.__generar_password(password)  #Atributo Privado
        self.email = email        #Atributo Público
        
    def __generar_password(self, password):
        return password.upper()
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, valor):
        self.__password = self.__generar_password(valor)
    
Meco =Usuario('Robison', 'hola1234', 'mecomontes@gmail.com') #Objeto Meco al cual se le pasan los atributos de la plantilla Usuario
print(Meco.username)
Meco.password = 'Nuevo Password'
print(Meco.email)
print(Meco.get_password())