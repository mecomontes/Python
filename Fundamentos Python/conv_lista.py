# Importa módulo pickle
import pickle

# Declara lista
lista = ['Perl', 'Python', 'Ruby']

# Abre archivo binario para escribir   
archivo = open('lenguajes.dat', 'wb')

# Escribe lista en archivo
pickle.dump(lista, archivo)

# Cierra archivo
archivo.close