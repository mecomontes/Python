##Entonces haremos la primera mejora, que sera agregar una cantidad de Dropout, que basicamente 
#lo que hace es apagar neuronas al azar con el fin de que las neuronas no se vuelvan tan dependientes 
#de los datos, es decir que se entrenen mejor para evitar el overfitting, para ello importaremos 
#nuestra capa de dropout.

#La capa dropout recibe como parámetro un numero entre 0 y 1 que representa el porcentaje de neuronas
# que va a desactivar en esa capa, yo le pondré 0.1 porque me ocupare de ello luego.

#Ahora comenzaremos el proceso de Fine Tunning, donde buscaremos posibles errores, y combinaciones de 
#parámetros que puedan mejorar nuestro modelo.

#Este proceso ocupa mucha ram (hasta 16 gb) por lo que te recomiendo hacerlo en esta pagina:

#Google Colab

#dropouts, el plan de optimizacion que tengo es el siguiente:

#    Compilación
#    Densidad de las capas de neuronas
#    Dropout

#así que vamos a importar las librerías que necesito.

from sklearn.model_selection import GridSearchCV
from tensorflow.keras.layers import Dropout

def build_model(optimizer):
  model = Sequential()
  model.add(Dense(32, input_shape=(X_train.shape[1],), activation='relu'))
  model.add(Dropout(0.1))
  model.add(Dense(64, activation='relu'))
  model.add(Dropout(0.1))
  model.add(Dense(1, activation='sigmoid'))
  model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['acc'])
  return model

parameters = parameters = {'batch_size': [16,32],
             'epochs':[100,500],
             'optimizer': ['adadelta', 'rmsprop']}

estimator = KerasClassifier(build_fn=build_model, verbose=0)
grid_search = GridSearchCV(estimator=estimator, param_grid=parameters, scoring='accuracy', cv=10)
grid_search.fit(X_train, y_train)
grid_search.best_params_

#Y queda en evidencia un error fatal de nuestro modelo, y es que a propósito, puse un optimizador 
#que no sirve para este tipo de problemas, por lo que nos dará una precisión muy baja.