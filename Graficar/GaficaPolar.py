import numpy as np
import matplotlib.pyplot as pl

pl.figure(1)

L=10
h=10

x=np.linspace(0,L)
y=np.linspace(-h/2,h/2)

X,Y=np.meshgrid(x,y)

Sxx = 12*X*Y/h**3

pl.imshow(Sxx)
pl.colorbar()
pl.show()

pl.figure(2)
pl.contourf(X, Y, Sxx,alpha=0.8)

pl.figure(3)
pl.contour(X, Y, Sxx,colors='red',linewidths=1.5)


fig=pl.figure(4)
pl.subplot(111, polar=True)
pl.contourf(X, Y, Sxx)
pl.contour(X, Y, Sxx)
pl.show()