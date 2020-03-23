
#Dropouts
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from tensorflow.keras.layers import Dropout
from sklearn.model_selection import GridSearchCV

def build_model(d1, d2):
    model = Sequential()
    model.add(Dense(32, input_shape=(X_train.shape[1],), activation='relu'))
    model.add(Dropout(d1))
    model.add(Dense(16, activation='relu'))
    model.add(Dropout(d2))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['acc'])
    return model

parameters = parameters = {'d1':[0.1,0.2,0.3],
                            'd2':[0.1,0.2,0.3]}

estimator = KerasClassifier(build_fn=build_model, verbose=0, batch_size=16, epochs=100)
grid_search = GridSearchCV(estimator=estimator, param_grid=parameters, scoring='accuracy', cv=10)
grid_search.fit(X_train, y_train)