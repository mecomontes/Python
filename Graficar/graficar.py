#### gráfica simple

import pylab as pl
import numpy as np

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)#crear el vector de valores en x

C, S = np.cos(X), np.sin(X)#crear los vectores C (coseno) y S (seno)

pl.plot(X, C)
pl.plot(X, S)

pl.show()


###################################################################3

# Crear una figura de 8x6 puntos de tamaño, 80 puntos por pulgada
pl.figure(figsize=(8, 4), dpi=80)

# Crear una nueva subgráfica en una rejilla de 1x1
pl.subplot(111)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# Graficar la función coseno con una línea continua azul de 1 pixel de grosor
pl.plot(X, C, color="blue", linewidth=1.0, linestyle=":", label='Coeseno')

# Graficar la función coseno con una línea continua verde de 1 pixel de grosor
pl.plot(X, S, color="green", linewidth=1.0, linestyle="--", label='Seno')

# Establecer límites del eje x
pl.xlim(-4.0, 4.0)

# Ticks en x
pl.xticks(np.linspace(-4, 4, 9, endpoint=True))

# Establecer límites del eje y
pl.ylim(-1.0, 1.0)

# Ticks en y
pl.yticks(np.linspace(-1, 1, 5, endpoint=True))

# Leyenda
pl.legend(loc='upper left')

# Guardar la figura usando 72 puntos por pulgada
# savefig("exercice_2.png", dpi=72)

# Mostrar resultado en pantalla
pl.show()







def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 -y ** 2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

pl.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='jet')
C = pl.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)