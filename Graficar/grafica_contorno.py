##### ejemplo tarea

import numpy as np                  # Cargamos numpy como el alias np
import matplotlib.pyplot as plt     # Crgagamos matplotlib.pyplot como el alias plt

# Creamos una figura
# Crear una figura de 8x6 puntos de tamaño, 80 puntos por pulgada
plt.figure(dpi=80)

# Creamos los arrays dimensionales
L=10
h=5
x = np.linspace(0, L, 256, endpoint=True)#crear el vector de valores en x
y = np.linspace(-h/2, h/2, 256, endpoint=True)#crear el vector de valores en x

# Obtenemos las corrdenadas resultantes de esos arrays
X, Y = np.meshgrid(x, y)

# Definimos la grÃ¡fica sen (x^2 + y^2)
Sxx = 12*X*Y/h**3

# Establecer límites del eje x
plt.xlim(0, L)

# Ticks en x
#plt.xticks(np.linspace(0, L, 11, endpoint=True))

# Establecer límites del eje y
plt.ylim(-h, h)

# Ticks en y
#plt.yticks(np.linspace(-h, h, 11, endpoint=True))

# Representamos
plt.imshow(Sxx);

# AÃ±adimos una colorbar
plt.colorbar();

# Mostramos en pantalla
plt.show()

plt.contourf(X, Y, Sxx)
plt.contour(X, Y, Sxx, colors='black')