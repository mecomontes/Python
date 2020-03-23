### NÚMERO PAR

def par(n):
    if n%2==0:
        return 'true'
    else:
        return 'flase'

n=int(input('ingrese el valor a evaluar: '))
answer=par(n)
print(answer)

### NÚMERO PALÍNDROMO

def inver(n):
    invertido=n[::-1]
    return invertido

n=input('ingrese un número a evaluar: ')
n2=inver(n)

if n==n2:
    print('el número es palíndromo')
else:
    print('el número NO es palíndromo')
    
### PRIMOS
    
def divisible(num,den):
    if num%den==0:
        return 'true'
    else:
        return 'false'
    
def primo(n):
    prime=divisible(n,2)
    
    if prime=='true':
        print('el número es primo')
    else:
        print('el número no es primo')
        
### 