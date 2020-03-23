"""                                                                     onstruyendo nuestro primer Blockchain

Bienvenido a esta primera parte de nuestro curso de Blockchain en Python. Sigue leyendo para que entiendas mejor, todos estos 
conceptos básicos.

Constantemente las personas tienden a usar el término “tecnología blockchain” para hablar de distintas cosas o conceptos, lo cual 
tiende a ser poco entendible, o incluso confuso. Muchas veces, hablan acerca de The Bitcoin Blockchain, otras veces están hablando 
de The Ethereum Blockchain, o incluso de otras monedas virtuales o tokens digitales,o quizás contratos inteligentes. Sin embargo, 
la mayoría de las veces, se están refiriendo a ledgers distribuidos. Los ledgers son una lista de transacciones replicadas en 
distintas computadoras, en vez de estar almacenadas en un servidor central.

La verdad, desde mi perspectiva, veo a la “tecnología blockchain” como una colección de tecnologías juntas, podemos verlo como una 
bolsa de Legos. Desde tu bolsa, tienes la posibilidad de sacar distintos ladrillos para juntar y crear distintas estructuras, a 
partir de ellos.


                    ¿Cómo podemos diferenciar una Blockchain de bloques de una base de datos normal?

Una Blockchain es una especie de paquete que contiene una base de datos normal, acompañado de algún software que va agregando 
nuevas filas, verifica que estas nuevas filas cumplan con ciertas reglas, y recibe y transmite nuevas filas a sus pares mediante 
una red; esto asegura que todos los pares contengan los mismos datos en su base de datos.


                                                        ¿Qué es una Blockchain?

La Blockchain, es posiblemente una de las tecnologías más significativas desde el inicio de la Internet. Es la tecnología central 
detrás del Bitcoin y otras monedas criptográficas.

Ten en cuenta que una Blockchain, es una cadena de registros inmutables y secuenciales, distribuidas en bloques. Pueden contener 
transacciones, archivos, o cualquier otro dato que necesites. Pero lo importante es que están encadenados usando hashes.

Hash: una función hash es algo que toma una entrada (que puede ser cualquier dato (números, archivos, etc.) y genera un hash. Un 
hash generalmente se muestra como un número hexadecimal.


                                                    ¿Quién puede hacer este curso?

Para todos aquellos que se sientan cómodos leyendo y escribiendo código en Python básico, y también para aquellos que buscan 
entender cómo funcionan las solicitudes HTTP, ya que la Blockchain que desarrollaremos aquí trabajará en conjunto con el protocolo 
HTTP.


                                                            ¿Qué necesitas?

Asegúrate de tener instalado Python 3.6 en conjunto con con pip. Igualmente, también necesitarás instalar Flask y la extraordinario
 biblioteca Request:

pip install Flask==0.12.2 requests==2.18.4

Y también necesitarás un cliente HTTP, como cURL o Postman. Sin embargo, cualquier cliente puede funcionar.
Construyendo tu primer Blockchain

Inicia tu editor de texto o IDE de preferencia, (te recomiendo el uso de PyCharm, ya que es mi favorito), y creas un nuevo archivo,
 titulado blockchain.py. Solo usaremos un solo archivo en este curso.

Luego vamos a crear una clase llamada Blockchain, cuyo constructor creará una lista vacía, con la que iniciaremos (aquí 
almacenaremos nuestra cadena de bloques) y haremos otra para almacenar transacciones. Aquí está el código para nuestra clase:"""

class Blockchain(object):
 def __init__(self):
   self.chain = []
   self.current_transactions = []
 def new_block(self):
   # Crea un nuevo bloque y lo añade a la cadena de paso
   pass
 def new_transaction(self):
   # Añade una nueva transacción a la lista de transacciones de paso
   pass 
 @staticmethod
 def hash(block):
   # Hashes de un bloque
   pass
 @property
 def last_block(self):
   #Devuelve el último bloque de la cadena
   pass

"""La clase Blockchain, que hemos creado, es la encargada de administrar nuestra cadena. Esta almacenará transacciones, y también 
contiene algunos métodos de ayuda para añadir nuevos bloques a la cadena. Sigamos desarrollando algunos métodos.


                                                    ¿Cómo debería verse un bloque?

Cada uno de los bloques posee un índice, una marca de tiempo (en tiempo Unix), algunas transacciones, una prueba (que lo veremos 
mas adelante), y el hash perteneciente al bloque anterior.

He aquí un ejemplo de cómo se ve un bloque individual:"""

block = {
'index': 1,
'timestamp': 1506057125.900785,
'transactions': [
{
'sender': "8527147fe1f5426f9dd545de4b27ee00",
'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
'amount': 5,
}
],
'proof': 324984774000,
'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}

"""Cada bloque nuevo, contiene en su interior el hash del bloque anterior. Esto es realmente importante, ya que le otorga 
inquinabilidad a la Blockchain, imagina esto: si alguien corrompiera un bloque anterior en la cadena, todos los bloques siguientes 
llevarán hashes incorrectos.
Agregando las transacciones a un bloque

Vamos a necesitar una manera de añadir transacciones a un bloque. El método que crearemos: new_transaction(), será responsable 
de esto. Y aunque no lo creas, es bastante directo."""

class Blockchain(object):
  ...
  def new_transaction(self, sender, recipient, amount):
    """
    Crea una nueva transacción para ir al siguiente Bloque minado
    :param sender: <str> Dirección del remitente
    :param recipient: <str> Dirección del destinatario
    :param amount: <int> Cantidad
    :return: <int> El índice del Bloque que llevará a cabo esta transacción
    """
    self.current_transactions.append({
     'sender': sender,
     'recipient': recipient,
     'amount': amount,
    })
    return self.last_block['index'] + 1

"""Luego de que new_transaction() agrega una nueva transacción a la lista, devuelve el índice del bloque donde se añadirá la 
transacción, y el siguiente será extraído. Esto será muy útil para el usuario que emite la transacción.


                                                Creando tus nuevos bloques

Cuando nuestra Blockchain es instanciada necesitaremos sembrarla con un bloque de génesis, un bloque sin predecesores. También 
tendremos que añadir una “prueba” a nuestro bloque de génesis que es el resultado de la minería (o prueba de trabajo). Hablaremos 
más sobre la minería más adelante.

Además de realizar nuestro bloque génesis en el constructor que tenemos, también tendremos que desarrolla métodos para new_block(),
new_transaction(), y hash():"""

import hashlib
import json
from time import time
class Blockchain(object):
  def __init__(self):
   self.current_transactions = []
   self.chain = []
   # Crea el bloque génesis
   self.new_block(previous_hash=1, proof=100)
  def new_block(self, proof, previous_hash=None):
   """
   Crear un nuevo Bloque en el Cadena de Bloques
   :param proof: <int> La prueba dada por el algoritmo de Prueba de Trabajo
   :param previous_hash: (Opcional) <str> Hash del Bloque anterior
   :return: <dict> Nuevo Bloque
   """
   block = {
     'index': len(self.chain) + 1,
     'timestamp': time(),
     'transactions': self.current_transactions,
     'proof': proof,
     'previous_hash': previous_hash or self.hash(self.chain[-1]),
   }
   # Anular la lista actual de transacciones
   self.current_transactions = []
   self.chain.append(block)
   return block
  def new_transaction(self, sender, recipient, amount):
   """
   Crea una nueva transacción para ir al siguiente Bloque minado
   :param sender: <str> Dirección del remitente
   :param recipient: <str> Dirección del destinatario
   :param amount: <int> Cantidad
   :return: <int> El índice del Bloque que llevará a cabo esta transacción
   """
   self.current_transactions.append({
    'sender': sender,
    'recipient': recipient,
    'amount': amount,
   })
   return self.last_block['index'] + 1
  @property
  def last_block(self):
   return self.chain[-1]
  @staticmethod
  def hash(block):
   """
   Crea un hash de bloque SHA-256
   :param block: <dict> bloque
   :return: <str>
   """
   # Debemos asegurarnos de que el Diccionario esté Ordenado, o tendremos hashes inconsistentes
   block_string = json.dumps(block, sort_keys=True).encode()
   return hashlib.sha256(block_string).hexdigest()

"""Técnicamente ya estamos terminando de representar nuestra Blockchain. Sin embargo, en este punto debes preguntarte cómo se 
crean, forjan, o extraen los bloques recién hechos.


                                                    ¿Cómo comprender la prueba del trabajo?

Un algoritmo de Prueba de Trabajo (PoW), se utiliza para comprender, cómo es que se crean o extraen nuevos bloques en la Blockchain.
 El objetivo del PoW es descubrir un número que resuelva un problema. El número debe ser difícil de encontrar, pero fácil de 
 verificar (computacionalmente) por cualquier persona en la red. Esta es la idea central detrás del algoritmo de Prueba de trabajo.


Ahora veamos un ejemplo muy simple para ayudar a comprender esto.

Digamos que el hash de un número entero x multiplicado por otro y debe en 0. Por lo tanto, hash(x * y) = ac23dc…0. Para este 
ejemplo arreglemos x = 5. Implementando lo siguiente en Python:"""

from hashlib import sha256
x = 5
y = 0 # Aún no sabemos lo que debería ser...
while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
   y += 1
print(f'La solución es = {y}')

"""La solución aquí es y = 21. Como, el hash producido termina en 0:

hash(5 * 21) = 1253e9373e...5e3600155e860

Si tomamos el ejemplo de Bitcoin, el algoritmo de prueba de trabajo se llama Hashcash. Y no se diferencia mucho del ejemplo que 
acabo de mostrarte. Es el algoritmo por el cual, los mineros compiten por resolver para crear un bloque nuevo. Por lo general lo 
difícil está determinado por la cantidad de caracteres buscados en una cadena. Cada minero es recompensado por su solución, al 
recibir una moneda por transacción.

Sin embargo, la red puede verificar fácilmente su solución.
Implementando la Prueba de trabajo básica

Implementemos un algoritmo similar para nuestra cadena de bloques. Nuestra regla será similar al ejemplo anterior:

Busca un número p que al hacer hash con la solución del bloque anterior se produzca un hash con 4 0s a la izquierda."""

import hashlib
import json
from time import time
from uuid import uuid4
class Blockchain(object):
    ...
    def proof_of_work(self, last_proof):
     """
     Algoritmo Simple de Prueba de Trabajo:
     Buscar un número p' tal que hash(pp') contenga 4 ceros a la izquierda, donde p es la anterior p''.
     p es la prueba anterior, y p' es la nueva prueba
     :param last_proof: <int>
     :return: <int>
     """
     proof = 0
     while self.valid_proof(last_proof, proof) is False:
      proof += 1
     return proof
    @staticmethod
    def valid_proof(last_proof, proof):
      """
      Valida la prueba: ¿Contiene el hash(last_proof, proof) 4 ceros a la izquierda?
      :param last_proof: <int> Prueba Previa
      :param proof: <int> Prueba de corriente
      :return: <bool> True si es correcto, False si no lo es.
      """
      guess = f'{last_proof}{proof}'.encode()
      guess_hash = hashlib.sha256(guess).hexdigest()
      return guess_hash[:4] == "0000"

"""Para ajustar la dificultad del algoritmo, podríamos modificar el número de ceros a la izquierda. Pero 4 es suficiente. 
Descubriras que la adición de un cero inicial único marca una gran diferencia con el tiempo requerido para encontrar una solución.


Nuestra clase está casi completa y estamos listos para comenzar a interactuar con ella mediante solicitudes HTTP."""