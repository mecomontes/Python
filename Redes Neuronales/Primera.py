import numpy as np

def nonlin(x,deriv=False):### """función de perdida como una derivación de la función Sigmoide"""
    if deriv==True:
        return x*(1-x)
    return 1/(1+np.exp(-x))

X=np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]]) ## """Dataset para entrenar la red"""
Y=np.array([[0],[1],[1],[0]])

np.random.seed(1) ###"""definimos una seed e inicializamos de forma aleatoria nuestros pesos"""

syn0 = 2*np.random.random((3,4)) - 1  ###"""Primera capa con 3 entradas y 4 Salidas"""
syn1 = 2*np.random.random((4,1)) - 1  #"""Segunda capa con 4 entradas y 1 Salida"""

for j in range(60000): #"""producto punto de nuestros datos nuestros pesos (Suma Ponderada) y 
                           # lo pasamos por nuestra función de activación."""
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))
    l2 = nonlin(np.dot(l1,syn1))

    l2_error = Y - l2  #"""Calcular el error entre los datos obtenidos y os reales"""
    
        

    l2_delta = l2_error*nonlin(l2,deriv=True)  #"""Descenso de Gradiente: La pendiente se calcula 
   # multiplicando nuestra perdida actual (l2_error) con la derivada de nuestras predicciones actuales, 
   # de esta manera vamos a saber para que dirección ajustar los pesos."""

    l1_error = l2_delta.dot(syn1.T)
    

    l1_delta = l1_error * nonlin(l1,deriv=True)  # """Multiplicarla por la transpuesta de los pesos de 
    #la capa s{iguiente, de este modo propagaremos el error hacia atrás, es decir, clacular la dirección
    #hacia donde moveré los pesos de la ultima capa, y de esta manera el error de la capa anterior sera
    #mas el cambio formaran parte activa para que la capa siguiente calcule la dirección hacia donde 
    #debe mover los pesos."""

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)  #"""Finalmente ajustamos el valor de nuestros pesos, multiplicando la 
    #transpuesta de la capa por sus respectivas optimizaciones, o direcciones hacia donde actualizar los 
    #pesos, y esto se suma a nuestros pesos actuales, actualizando las dos capas a la vez."""
    
print(l2)