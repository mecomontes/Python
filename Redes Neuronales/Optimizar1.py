##  https://medium.com/@jcrispis56/una-introducci%C3%B3n-completa-a-redes-neuronales-con-python-y-tensorflow-2-0-b7f20bcfebc5?fbclid=IwAR1VJ9JrW6Mpe6mb5ufUsxhsg-BLTFdYZ9WbMmHkleil3obLv-y-ButcmlA


##Primero antes de empezar necesitamos darnos mejor a la idea de cuanto es nuestro error, 
#para eso vamos a realizar un proceso llamado cross_validation, lo que hace este proceso, es
#entrenar una cantidad de veces que tu definas y devuelve la métrica que le indiques para 
#todos los pasos, esto es mas que nada porque en cada época la perdida suele variar, entonces 
#esto nos permitirá hacernos a la idea de en este caso la precisión calculando la media de 
#todas estas precisiones, para implementarlo haremos lo siguiente

#Primero importaremos lo que necesitemos, en este caso nuestro algoritmo de cross validator, 
#y un wrapper que permitira usar modelos de keras con scikit learn, asique hagamoslo:"""

from tensorflow.keras.layers import Dropout

def build_model():
  model = Sequential()
  model.add(Dense(32, input_shape=(X_train.shape[1],), activation='relu'))
  model.add(Dropout(0.2))
  model.add(Dense(16, activation='relu'))
  model.add(Dropout(0.3))
  model.add(Dense(1, activation='sigmoid'))
  model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['acc'])
  return model

estimator = KerasClassifier(build_fn=build_model, verbose=0, batch_size=16, epochs=100)
accuracies = cross_val_score(estimator, X_train, y_train, cv=10, n_jobs=-1)
mean_acc = accuracies.mean()
variance_acc = accuracies.std()
print('Precision media: ', mean_acc)