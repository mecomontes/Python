class Animal:
    @property
    def terrestre(self):
        return True
    
class Mascota:
    nombre = 'Todas las mascotas necesitan un nombre'
    
    def __init__(self,nombre):
        self.nombre = nombre
        
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
    def __init__(self,nombre):
        Mascota.__init__(self, nombre)
        self.nombre_gato = nombre
    
    def gato_cazador(self):
        self.cazar()
    
    def mostrar_nombre(self):
        Mascota.mostrar_nombre(self) #toma el método mostrar_nombre de la clase Mascota
        print('El nombre del gato es: {}'.format(self.nombre)) #Realmente el usa el este método que es propio de la clase
        
gato = Gato('Patricio')
gato.nombre = 'Gato con nombre'
gato.mostrar_nombre()
jaguar = Jaguar()

print(gato.garras_retractiles)
print(jaguar.garras_retractiles)        
    