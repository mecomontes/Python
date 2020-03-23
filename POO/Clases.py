""" Estos Métodos son usados para modificar las clases"""

class Usuario:
    def __new__(self):#método mágico
        print('Primero en ejecutar')
        return super().__new__(cls)
        
    def __init__(self):#Método Mágico
        print('Segundo en ejecutar')
    
    def __str__(self):#método mágico
        print('Cuando se intenta mostrar el objeto')
        
    def __getattr__(self, nombre):#método mágico
        print('Aquí no se encontró el atributo')
    
    def mostrar_password(self):
        print(self.__password)

usuario = Usuario()
usuario.nombre = 'Meco'    # Se crea el atributo dentro del método
usuario.__password = 'No Secreto'
print(usuario.nombre)
print(usuario.__dict__)
usuario.mostrar_password