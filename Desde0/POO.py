"""¿Qué es la programación orientada a objetos?

La Programación Orientada a Objetos (POO u OOP según sus siglas en inglés) es un paradigma de programación
 que usa objetos y sus interacciones para diseñar aplicaciones y programas de computadora. Está basado en 
 varias técnicas, incluyendo herencia, modularidad, polimorfismo, y encapsulamiento. Su uso se popularizó
 a principios de la década de 1990. Actualmente son muchos los lenguajes de programación que soportan la 
 orientación a objetos.

La programación Orientada a objetos (POO) es una forma especial de programar, más cercana a como se expresan
 las cosas en la vida real que otros tipos de programación.

La POO es un paradigma de la programación de computadores; esto hace referencia al conjunto de teorías, 
estándares, modelos y métodos que permiten organizar el conocimiento, proporcionando un medio bien definido 
para visualizar el dominio del problema e implementar en un lenguaje de programación la solución a ese problema.

La POO se basa en el modelo objeto, donde el elemento principal es le objeto, el cual es una unidad que 
contiene todas sus características y comportamientos en sí misma, lo cual lo hace como un todo independiente,
 pero que se interrelaciona con objetos de su misma clase o de otras clase, como sucede en el mundo real.
 
Conceptos Fundamentales de la POO

La programación orientada a objetos es una forma de programar que trata de encontrar una solución a estos 
problemas. Introduce nuevos conceptos, que superan y amplían conceptos antiguos ya conocidos. Entre ellos 
destacan los siguientes:

                                                
                                                Clase:

Definiciones de las propiedades y comportamiento de un tipo de objeto concreto. La instanciación es la 
lectura de estas definiciones y la creación de un objeto a partir de ellas.

    
                                                Objeto:

Instancia de una clase. Entidad provista de un conjunto de propiedades o atributos (datos) y de comportamiento
 o funcionalidad (métodos), los mismos que consecuentemente reaccionan a eventos. Se corresponden con los objetos 
 reales del mundo que nos rodea, o con objetos internos del sistema (del programa). Es una instancia a una clase.

    
                                                 Método:

Algoritmo asociado a un objeto (o a una clase de objetos), cuya ejecución se desencadena tras la recepción de 
un “mensaje”. Desde el punto de vista del comportamiento, es lo que el objeto puede hacer. Un método puede producir 
un cambio en las propiedades del objeto, o la generación de un “evento” con un nuevo mensaje para otro objeto del
 sistema.

    
                                                 Mensaje:

Una comunicación dirigida a un objeto, que le ordena que ejecute uno de sus métodos con ciertos parámetros asociados
 al evento que lo generó

    
                                             Comportamiento:

Está definido por los métodos o mensajes a los que sabe responder dicho objeto, es decir, qué operaciones se pueden
 realizar con él.

    
                                                    Evento

Es un suceso en el sistema (tal como una interacción del usuario con la máquina, o un mensaje enviado por un objeto).
 El sistema maneja el evento enviando el mensaje adecuado al objeto pertinente. También se puede definir como evento 
 la reacción que puede desencadenar un objeto; es decir, la acción que genera.

   
                                                 Atributos:

Características que tiene la clase

    
                                            Propiedad o atributo:

Contenedor de un tipo de datos asociados a un objeto (o a una clase de objetos), que hace los datos visibles desde 
fuera del objeto y esto se define como sus características predeterminadas, y cuyo valor puede ser alterado por la 
ejecución de algún método.

    
                                                Estado interno:

Es una variable que se declara privada, que puede ser únicamente accedida y alterada por un método del objeto, y 
que se utiliza para indicar distintas situaciones posibles para el objeto (o clase de objetos). No es visible al 
programador que maneja una instancia de la clase.

    
                                            Componentes de un objeto:

Atributos, identidad, relaciones y métodos.

    
                                            Identificación de un objeto:

Un objeto se representa por medio de una tabla o entidad que esté compuesta por sus atributos y funciones 
correspondientes.


                                                POO en Python
                                

                                                Clases, Objetos y Métodos:

En python la POO se expresa de manera simple y fácil de escribir pero debes tener en cuenta que para programar 
debes entender cómo funciona la teoría de la POO y llevarla a código.

La teoría de la POO nos dice que todos los objetos deben pertenecer a una clase, ya que esta es la base para 
diferenciarse unos de otros teniendo atributos y comportamientos que los distingan de otros objetos que pertenezcan
 a otras clases, para crear clases en python lo hacemos de la siguiente manera:


                                                     class Coche():

Como puedes ver para crear una clase lo hacemos escribiendo la palabra class seguida del nombre de la clase y un par
de paréntesis, debes tener en cuenta que el nombre de la clase que hayas creado debe empezar por mayúsculas y si 
tiene más de una palabra debes usar la notación de camello.

Ya que tenemos una clase debemos definir sus atributos y comportamientos, para hacer esto debemos dejar la sangría 
correspondiente para indicarle que estamos escribiendo dentro de la clase, para definir un atributo simplemente 
creamos una variable con total normalidad y un valor que le quieras dar:   

class Coche():
    ruedas=4

Ahora que ya tenemos un atributo podemos agregarle un comportamiento que en python se conoce como métodos, 
para definir un método lo hacemos igual como lo hacemos con una función con la palabra por defecto def y el nombre 
de dicho método pero para diferenciar un método de una función lo hacemos escribiendo dentro de sus paréntesis el 
parámetro self:

def desplazamiento(self):
    pass

La palabra self hace referencia a los objetos que pertenezcan a la clase y la palabra pass que colocamos dentro
 del método le indica a el intérprete de python que todavía no le hemos definido ningún funcionamiento a ese método,
 ya que, si no escribimos la palabra pass cuando todavía no le asignemos nada al método al ejecutarlo nos dará un error.

Ya que explicamos esto terminaremos de definir el método desplazamiento y dentro esto solo colocaremos un print 
que nos dirá “El coche se esta desplazando sobre 4 ruedas”:

class Coche():
    ruedas=4
    def desplazamiento(self):
        print("El coche se esta desplazando sobre 4 ruedas")

Cuando tenemos nuestra clase lista ya podemos empezar a crear objetos que pertenezcan a esa clase, para crear
 objetos lo hacemos de la siguiente manera:

miVehiculo=Coche()

Después del “=” le estamos especificando a que clase pertenece el objeto que acabamos de crear.

Para poder mostrar todo los atributos y comportamientos que tiene un objeto a la hora de ejecutar un programa 
de POO en python, hacemos lo siguiente:

Para mostrar atributos:

miObjeto.atributo

Para mostrar métodos:

miObjeto.metodo()

Siguiendo con el ejemplo, para mostrar en pantalla el atributo y el comportamiento de la clase que le dimos a 
nuestro objeto “miVehiculo” lo hacemos de la siguiente manera:

print("Mi coche tiene ", miVehiculo.ruedas, " ruedas")
miVehiculo.desplazamiento()

Si has seguido este ejemplo ya tendrías el ejemplo completo de esta manera:   """

class Coche():
    ruedas=4
    def desplazamiento(self):
        print("El coche se esta desplazando sobre 4 ruedas")
miVehiculo=Coche()
print("Mi coche tiene ", miVehiculo.ruedas, " ruedas")
miVehiculo.desplazamiento()

###Y al ejecutarlo nos mostrara lo siguiente:

#Mi coche tiene 4 ruedas
#El coche se esta desplazando sobre 4 ruedas

"""#Puedes observar que hemos creado un objeto que pertenece a una clase y cuya clase tiene atributos y 
#comportamientos únicos de que lo diferencia de otros objetos. El ejemplo habla de que nuestros objetos 
#son vehículos y sus diferentes tipos que en la POO serían clases, tales como: motos, aviones, trenes, etc. 
#En la POO podemos agregar todas las clases que queramos o necesitemos. Ahora agregaremos la clase moto con 
#sus propios atributos y comportamientos:

class Moto():
    ruedas=2
    def desplazamiento(self):
        print("La moto se esta desplazando sobre 2 ruedas")

Ahora tenemos dos clases que nos permitirán creas más objetos que tengan diferentes atributos y comportamientos,
 tal y como se muestra en el siguiente ejemplo:"""

class Coche(): #      Clase
    ruedas=4   #      Atributo
    def desplazamiento(self):#      Método
        print("El coche se esta desplazando sobre 4 ruedas")
        
class Moto():
    ruedas=2
    def desplazamiento(self):
        print("La moto se esta desplazando sobre 2 ruedas")

print("---------------Primer objeto---------------")       
miVehiculo=Coche()    #     Objeto
print("Mi coche tiene ", miVehiculo.ruedas, " ruedas")
miVehiculo.desplazamiento()

print("---------------Segundo objeto---------------")
miVehiculo=Moto()    #      Objeto
print("Mi moto tiene ", miVehiculo.ruedas, " ruedas")
miVehiculo.desplazamiento()

#Si ejecutamos el ejemplo nos mostrara lo siguiente:

#Mi coche tiene 4 ruedas
#El coche se esta desplazando sobre 4 ruedas 
#---------------Segundo objeto---------------
#Mi moto tiene 2 ruedas
#La moto se esta desplazando sobre 2 ruedas

"""La POO tiene tres tipos de propiedades que permiten facilitar esta forma de programar y en este tutorial te explicaremos
 cada una ellas que son: la encapsulación, herencia y polimorfismo.
 
 
                                             Polimorfismo

La palabra polimorfismo viene del griego poli que significa muchas y morfismo que significa formas, es decir, 
muchas formas. El polimorfismo en python es la capacidad que tienen los objetos de diferentes clases para usar 
un comportamiento o atributo del mismo nombre pero con diferente valor.

En el ejemplo anterior de clases, objetos y métodos como pueden observar todos los vehículos tienen la capacidad 
de desplazarse pero no se desplazan de la misma manera, dado que una moto se desplaza sobre dos ruedas y un coche 
se desplaza sobre cuatro, eso es el polimorfismo.

class Coche():
    ruedas=4
    def desplazamiento(self):
        print("El coche se esta desplazando sobre 4 ruedas")
class Moto():
    ruedas=2
    def desplazamiento(self):
        print("La moto se esta desplazando sobre 2 ruedas")

                                            
        
                                            Encapsulación

La encapsulación es una forma de darle uso exclusivo a los comportamientos o atributos que posee una clase, 
es decir, protege esos atributos y comportamientos para que no sean usados de manera externa.

En python para hacer que un atributo o comportamiento sea privado tenemos que colocar un par de guiones bajos 
antes del nombre del atributo o comportamiento “__nombre”.

Para empezar nuestro ejemplo de encapsulación vamos a crear una clase que llamaremos “Ejemplo” y dentro de 
ella declaramos un método al que llamaremos “publico” que contendrá un return que solo mostrara una cadena
}de texto que dirá “Soy un método público a la vista de todo”:

    class Ejemplo():
        def publico(self):
            return "Soy un método público, a la vista de todo"

Ahora declaramos un método que se llame “privado” pero antes de su nombre pondremos un par de guiones bajos “__” 
y dentro del método una cadena de texto como en el método anterior:

    class Ejemplo():
        def publico(self):
            return "Soy un método público, a la vista de todo"
        def __privado(self):
            return "Soy un metodo privado, para ti no existo"

Ya con todo esto creamos un objeto perteneciente a la clase ejemplo y procedemos a imprimir los dos métodos 
hemos creado:

    class Ejemplo():
        def publico(self):
            return "Soy un método público, a la vista de todo"
        def __privado(self):
            return "Soy un metodo privado, para ti no existo"
    objeto = Ejemplo()
    print(objeto.publico())
    print(objeto.__privado())

Si ejecutamos el ejemplo nos mostrara algo parecido:

Soy un método público, a la vista de todo
Traceback (most recent can last):
 File “encapsulación.py”, line 12, in (module)
print(objeto.__private())
AttributeError: ‘Ejemplo’ object has no attribute ‘__privado’

Como puedes ver al ejecutarlo si nos muestra el contenido del método publico pero a la hora de mostrar el método 
privado nos dice que tal método no existe pero en realidad si solo que por ser privado no puede ser mostrado 
externamente.

Python posee varias formas de mostrar contenido privado y una de ella en el name mangling, para aplicar el name 
mangling debemos hacerlos de esta manera:

    print(objeto._Ejemplo__privado())"""
    
    
class Ejemplo():
    def publico(self):
        return "Soy un método público, a la vista de todo"
    def __privado(self):
        return "Soy un metodo privado, para ti no existo"
        
objeto = Ejemplo()
print(objeto.publico())
print(objeto._Ejemplo__privado())


"""Al poner el nombre del objeto seguido de un punto “.”, un guion bajo “_”, el nombre de la clase y luego el nombre
del método privado le estamos diciendo a python que tiene derecho a mostrar este método privado y si ejecutas el
programa cambiando esa línea de código de esta manera te mostrara lo siguiente:      """

#Soy un método público, a la vista de todo
#Soy un metodo privado, para ti no existo



"""                                        Métod set() y get()

Con esto ya podemos acceder a los métodos privados que queramos pero como mencionamos anteriormente hay varias 
maneras de mostrar atributos o comportamientos que sean privados y para esto existen dos métodos especiales que 
sirven para acceder a los valores privados, estos dos métodos son el get (obtener, conseguir) y el 
set (establecer, colocar).

Para empezar declaramos un constructor que le de estado inicial a un atributo al cual vamos a hacer que sea 
privado y eso los hacemos de la siguiente manera:

    class Ejemplo():
        def __init__(self):
            self.__oculto="Me encuentro oculto en la clase"
        def publico(self):
            return "Soy un método público, a la vista de todo"
        def __privado(self):
            return "Soy un metodo privado, para ti no existo"

Ahora que tenemos un atributo privado, creamos un método get que sería algo como decir “obtener oculto” y dentro 
del método get le vamos a decir que nos retorne el atributo que está oculto:

    class Ejemplo():
        def __init__(self):
            self.__oculto="Me encuentro oculto en la clase"
        def publico(self):
            return "Soy un método público, a la vista de todo"
        def __privado(self):
            return "Soy un metodo privado, para ti no existo"
        def get_oculto(self):
            return self.__oculto  

Y ahora solo hacemos un llamado a este método y ejecutamos el programa:"""

class Ejemplo():
    def __init__(self):
        self.__oculto="Me encuentro oculto en la clase"
    def publico(self):
        return "Soy un método público, a la vista de todo"
    def __privado(self):
        return "Soy un metodo privado, para ti no existo"
    def get_oculto(self):
        return self.__oculto
    
objeto = Ejemplo()
print(objeto.publico())
print(objeto._Ejemplo__privado())
print(objeto.get_oculto())


#Y al ejecutarlo nos mostrara lo siguiente:

#Soy un método público, a la vista de todo
#Soy un metodo privado, para ti no existo
#Me encuentro oculto en la clase

"""Como puedes ver hemos accedido al atributo privado por medio de un método get, ahora vemos a utilizar 
un método set, este método sirve para cambiarle los valores a todo lo que este encapsulado y eso lo hacemos 
de la siguiente manera:"""

class Ejemplo():
    def __init__(self):
        self.__oculto="Me encuentro oculto en la clase"
    def publico(self):
        return "Soy un método público, a la vista de todo"
    def __privado(self):
        print ("Soy un metodo privado, para ti no existo")
    def get_oculto(self):
        return self.__oculto
    def set_oculto(self):
        self.__oculto = self.__privado()
        
objeto = Ejemplo()
print(objeto.publico())
print(objeto._Ejemplo__privado())
print(objeto.get_oculto())
objeto.set_oculto()


"""En este ejemplo le hemos cambiando al método “__privado” el return por un print y le asignamos su valor al 
atributo oculto por medio del método set para que nos imprima lo siguiente:"""

#Soy un método público, a la vista de todo
#Soy un metodo privado, para ti no existo
#None
#Me encuentro oculto en la clase
#Soy un metodo privado, para ti no existo

"""Con esto hemos explicado un poco como aplicar la encapsulación en python, ahora solo falta explicar el concepto 
de herencia en python que es uno de los más importantes en la programación orientada a objetos.


                                            Herencia

La Herencia explica que puede crearse un objeto a partir de otro objeto ya existente. El nuevo objeto hereda 
todas las cualidades del objeto del que deriva y además puede añadir nuevas funcionalidades o modificar las 
ya existentes.

Para aplicar la herencia en python debemos crear una súper clase o clase padre la cual tendrá los atributos 
y comportamientos principales que tendrán todas las clases derivadas de la clase padre, en este tutorial 
basaremos nuestros ejemplo de herencia con un caso de padres e hijos y para empezar declaramos la clase 
padre a la cual llamaremos “Padre” y le daremos los siguientes atributos y un comportamiento de la siguiente forma:

    class Padre():
      
        caballo="negro"
        ojos="azules"
        def conducir_coche(self):
            print ("La persona sabe conducir coches")

Ahora que tenemos la clase padre podemos declarar una clase que herede todos los atributos y comportamientos que 
tiene la clase padre, esta clase que derivada de la clase padre la vamos a llama “Hijo” y para indicar en python 
que una clase que está heredando de otra hay que escribir el nombre de la clase de la cual está heredando dentro 
de los paréntesis que están después del nombre de la clase que lo hereda:

    class Hijo(Padre):

Haciendo esto automáticamente la clase hijo ya tiene todo los atributos y comportamiento que tiene la clase padre 
sin necesidad de haberlos declarado dentro de la clase hijo.

La herencia también permite que las clases derivada de una clase padre también tengan atributos y comportamientos 
propios que no están en la clase padre:

    class Hijo(Padre):
      
        def conducir_moto(self):
            print ("La persona sabe conducir moto")

Con esto si creamos un objeto perteneciente a la clase hijo y le decimos que imprima todos los atributos y 
comportamientos que tiene la clase padre lo hará con total normalidad como si los hubieras declarado en la 
clase hijo tal y como se muestra el en siguiente ejemplo:"""

class Padre():
  
    cabello="negro"
    ojos="azules"
    def conducir_coche(self):
        print ("La persona sabe conducir coches")
class Hijo(Padre):
  
    def conducir_moto(self):
        print ("La persona sabe conducir moto")

persona=Hijo()
print(persona.cabello)
print(persona.ojos)
persona.conducir_coche()
persona.conducir_moto() 

#Si ejecutamos este ejemplo nos mostrara lo siguiente:

#Negro
#azules
#La persona sabe conducir coches
#La persona sabe conducir moto
