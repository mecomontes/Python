# POLAR

#Importar pyplot
import matplotlib.pyplot as plt
#Importar numpy
import numpy as np

#Se crea el rango de valores angulares
theta = np.arange(0., 2., 0.005)*np.pi
#Se calcula el coseno del rango de valores angulares
r = 2*np.abs(np.cos(theta))
#Se crea la grafica en coordenadas polares pasando
#el angulo theta y los valores de r
plt.polar(theta, r)
#Se crea una grilla de los angulos 45,90 y 369
plt.thetagrids(range(45, 360, 90))
plt.rgrids(np.arange(0.2, 3.1, .7), angle=0);
#Se genera la grafica
plt.show()