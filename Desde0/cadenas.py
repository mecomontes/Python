"""ste método se utiliza para eliminar todos los espacios en blanco iniciales y finales de una cadena. 
También tiene en cuenta los tabuladores y saltos de línea. """

hola = ' \t\t\n\tHola \n '
print(hola)

    ### >>>Hola
	
	 
hola_limpio = hola.strip()
print(hola_limpio)
#>>>Hola

###     replace()

cadena = 'aaaaaa'
nueva = cadena.replace('a', 'b', 3)
print('mayuscula: ',cadena.upper())
print('minuscula: ',cadena.lower())

###    >>> 'bbbaaa'


"""la forma de comprobar como un auténtico pythonista 🐍 si una estructura de datos está vacía 
es la siguiente:"""

if list:
      print('No vacía')
else:
      print('Vacía')
if dict:
      print('No vacía')
else:
      print('vacía')

"""Por tanto, si una estructura de datos está vacía, devuelve «False» cuando es usada 
en un contexto booleano. Por el contrario, si contiene elementos, devuelve «True» 
al tratarla en un contexto booleano.

Veámoslo con un ejemplo:

Vamos a definir una función para comprobar si una estructura de datos está vacía:"""

def is_empty(data_structure):
    if data_structure:
        print("No está vacía")
        return False
    else:
        print("Está vacía")
        return True
"""
>>>d = {}
>>>t = ()
>>>l = []
>>>str = ''
>>>s = set()
"""

