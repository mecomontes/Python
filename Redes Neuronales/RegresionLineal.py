import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Carga el conjunto de datos de diabetes
diabetes = datasets.load_diabetes()

# Use una característica
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Divide los datos en conjuntos de formación/pruebas
diabetes_X_train = diabetes_X[:-50]
diabetes_X_test = diabetes_X[-50:]

# Dividir los objetivos en conjuntos de formación/pruebas
diabetes_y_train = diabetes.target[:-50]
diabetes_y_test = diabetes.target[-50:]

# Crear objeto de regresión lineal
regr = linear_model.LinearRegression()

# Entrene el modelo utilizando los juegos de entrenamiento
regr.fit(diabetes_X_train, diabetes_y_train)

# Realice predicciones utilizando el conjunto de pruebas
diabetes_y_pred = regr.predict(diabetes_X_test)

# los coeficients
print('Coefficients: \n', regr.coef_)

# El error al cuadrado medio
print("Mean squared error: %.2f"% mean_squared_error(diabetes_y_test, diabetes_y_pred))

# Puntuación de varianza explicada: 1 es una predicción perfecta
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot salidas
plt.scatter(diabetes_X_test, diabetes_y_test, color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()