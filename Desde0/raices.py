def raiz(i):  # Función que calcula la raíz cuadrada de un número
    return i**(1/2)
def raizCuadratico(a,b,c):  # Función que calcula las raíces de un polinomio cuadrático
    return ((-b+raiz(b**2-(4*a*c)))/(2*a)),((-b-raiz(b**2-(4*a*c)))/(2*a))
