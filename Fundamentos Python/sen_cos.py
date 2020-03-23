def factorial(n):
    factor=1
    for i in range(n):
        factor=factor*(i+1)
    return factor

def cosx(m,x):
    sumac=0
    for i in range(m):
        sumac=sumac+(-1)**i*(x)**(2*i)/factorial(2*i)
    return sumac

def senx(m,x):
    sumas=0
    for i in range(m):
        sumas=sumas+(-1)**i*(x)**(2*i+1)/factorial(2*i+1)
    return sumas
        
m=int(input('ingrese el grado de la aproximación m: '))
x=float(input('ingrese el vallor a calcular x: '))

print('el valor de la aproximación para el seno es ',senx(m,x))
print('el valor de la aproximación para el seno es ',cosx(m,x))