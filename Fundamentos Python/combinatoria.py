# PUNTO 14

### funcion factorial
def factorial(f):
    
    factor=1
    for x in range(1,f+1):
        factor=factor*(x)
    return factor

def Combinatoria(A,B,C):
    Comb=A/(B*C)
    return Comb

flag=1
    
while flag==1:
    m=int(input('Ingrese el valor de m: '))
    n=int(input('Ingrese el valor de n: '))
    
    if m>=n:
        A=factorial(m)
        B=factorial(n)
        C=factorial(m-n)
        Comb=Combinatoria(A,B,C)
        print(f'La combinatoria de m con n es C(m,n) = {Comb}')
        flag=0
        
    else:
        print('ERROR: m debe ser mayor que n \n Intentalo nuevamente \n\n\n')