cadena1 = 'tengo una yama que Yama se llama'  # declara variable
lista1 = ['pera', 'manzana', 'naranja', 'uva']  # declara lista
longitud = len(cadena1)  # 32, devuelve longitud de la cadena
elem = len(lista1)  # 4, devuelve nº elementos de la lista 
cuenta = cadena1.count('yama')  # 1, cuenta apariciones de 'yama'
print(cadena1.find('yama'))  # 10, devuelve posición de búsqueda 
cadena2 = cadena1.join('***')  # inserta cadena1 entre caracteres  
lista1 = cadena1.split(' ')  # divide cadena por separador → lista
tupla1 = cadena1.partition(' ')  # divide cadena por separador → tupla 
cadena2 = cadena1.replace('yama','cabra',1) # busca/sustituye términos 
numero = 3.14  # asigna número con decimales
cadena3 = str(numero)  # convierte número a cadena
#cadena1.startswith('tengo'):  # evalúa si comienza por “tengo”: True
#cadena1.endswith("llama"):  # evalúa si termina por “llama”: True
#cadena1.find("llama") != -1:  # evalúa si contiene “llama”: True
cadena4 = 'Python'  # asigna una cadena a una variable
print(cadena4[0:4])  # muestra desde la posición 0 a 4: "Pyth"
print(cadena4[1])  # muestra la posición 1: "y"
print(cadena4[:3] + '-' + cadena4[3:])  # muestra "Pyt-hon"
print(cadena4[:-3])  # muestra todo menos las tres últimas: "Pyt"

# declara variable con cadena alfanumérica
cadena5 = "  abc;123  "

# suprime caracteres en blanco (y \t\n\r) por la derecha
print(cadena5.rstrip())  # "  abc;123"

# suprime caracteres en blanco (y \t\n\r) por la izquierda
print(cadena5.lstrip())  # "abc;123  "

# suprime caracteres en blanco (y \t\n\r) por derecha e izquierda 
print(cadena5.strip())  # "abc;123"

# suprime caracteres del argumento por la derecha e izquierda
print(cadena5.strip("123456790; "))  # "abc"

cadena6 = "Mar"   # declara una variable
print(cadena5.upper())   # convierte a mayúsculas: "MAR"
print(cadena5.lower())   # convierte a minúsculas: "mar" 


lista1 = ['uno', 2, True]  # declara una lista heterogénea
lista2 = [1, 2, 3, 4, 5]  # declara lista numérica (homogénea)
lista3 = ['nombre', ['ap1', 'ap2']]  # declara lista dentro de otra
lista4 = [54,45,44,22,0,2,99]  # declara una lista numérica
print(lista1)  # ['uno', 2, True], muestra toda la lista
print(lista1[0])  # uno, muestra el primer elemento de la lista
print(lista2[-1])  # 5, muestra el último elemento de la lista
print(lista3[1][0])  # calle, primer elemento de la lista anidada
print(lista2[0:3:1])  # [1,2,3], responde al patrón inicio:fin:paso
print(lista2[::-1])  # devuelve la lista ordenada al revés
lista1[2] = False  # cambia el valor de un elemento de la lista
lista2[-2] = lista2[-2] + 1  # 4+1 → 5 – cambia valor de elemento
lista2.pop(0)  # borra elemento indicado o último si no indica
lista1.remove('uno')  # borra el primer elemento que coincida
del lista2[1]  # borra el segundo elemento (por índice)  
lista2 = lista2 + [6]  # añade elemento al final de la lista
lista2.append(7)  # añade un elemento al final con append()
lista2.extend([8, 9])  # extiende lista con otra por el final
lista1.insert(1, 'dos')  # inserta nuevo elemento en posición
del lista2[0:3]  # borra los elementos desde:hasta
lista2[:] = []  # borra todos los elementos de la lista 
print(lista1.count(2))  # cuenta el nº de veces que aparece 2
print(lista1.index("dos"))  # busca posición que ocupa elemento
#lista3.sort()  # ordena la lista
#lista3.sort(reverse=True)  # ordena la lista en orden inverso
lista5 = sorted(lista4)  # ordena lista destino 
tupla1 = (1, 2, 3)  # declara tupla (se usan paréntesis)...
tupla2 = 1, 2, 3  # ...aunque pueden declararse sin paréntesis
tupla3 = (100,)  # con un elemento hay terminar con “,”
tupla4 = tupla1, 4, 5, 6  # anida tuplas
tupla5 = ()  # declara una tupla vacía
tupla2[0:3]  # (1, 2, 3), accede a los valores desde:hasta