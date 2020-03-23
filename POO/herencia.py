class Animal:
    @property
    def terrestre(self):
        return True
    
class Mascota:
    nombre = 'Todas las mascotas necesitan un nombre'
    
    def mostrar_nombre(self):
        print(self.nombre)

class Felino(Animal):# HEredad los métodos de Animal
    @property
    def garras_retractiles(self):
        return True
    
    def cazar(self):
        print('El felino está cazando')
        
class Jaguar(Felino):# Hereda los métodos de felino
    pass

class Gato(Felino, Mascota):# Hereda los métodos de felino y Mascota - Herencia Múltiple
    def gato_cazador(self):
        self.cazar()
        
gato = Gato()
gato.nombre = 'Gato con nombre'
gato.mostrar_nombre()
jaguar = Jaguar()

print(gato.garras_retractiles)
print(jaguar.garras_retractiles)        
    