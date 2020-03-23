import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# X es la 10x10 matrix de Hilbert
X = 1. / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
y = np.ones(10)
n_alphas = 200
alphas = np.logspace(-10, -2, n_alphas)
coefs = []

for a in alphas:
    ridge = linear_model.Ridge(alpha=a, fit_intercept=False)
    ridge.fit(X, y)
    coefs.append(ridge.coef_)
    
    # mostramos resultados
    ax = plt.gca()
    ax.plot(alphas, coefs)
    ax.set_xscale('log')
    ax.set_xlim(ax.get_xlim()[::-1]) # reverse axis
    plt.xlabel('alpha')
    plt.ylabel('weights')
    plt.title('Coeficientes de cresta en función de la regularización')
    plt.axis('tight')
    plt.show()