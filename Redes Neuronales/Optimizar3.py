#Tenemos que notar es que ahora tenemos que incluir el batch_size y las epocas

#{‘l1’: 32, ‘l2’: 16}

#Ese es el resultado que me dio a mi, por lo que salta otro error de la red, las capas
# van desde la mas densa, a la menos densa, que también lo hice con intención.

#Capas
def build_model(l1, l2):
  model = Sequential()
  model.add(Dense(l1, input_shape=(X_train.shape[1],), activation='relu'))
  model.add(Dropout(0.1))
  model.add(Dense(l2, activation='relu'))
  model.add(Dropout(0.1))
  model.add(Dense(1, activation='sigmoid'))
  model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['acc'])
  return model

parameters = parameters = {'l1':[16,32,64,128,256],
                           'l2':[16,23,64,128,256]}

estimator = KerasClassifier(build_fn=build_model, verbose=0, batch_size=16, epochs=100)
grid_search = GridSearchCV(estimator=estimator, param_grid=parameters, scoring='accuracy', cv=10)
grid_search.fit(X_train, y_train)