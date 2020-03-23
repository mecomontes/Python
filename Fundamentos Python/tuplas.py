### RECTAS

def punto_recta(p,r):
    x1,y1=p
    m,b=r
    
    if y1==m*x1+b:
        print('El punto SI está en la recta')
    else:
        print('El punto NO está en la recta')
    
m=float(input('ingrese la pendiente m = '))
b=float(input('ingrese la ordenada b = '))
recta=(m,b)
p=input('ingrese el punto a evaluar (x,y) = ')
punto=(float(p[1]),float(p[3]))

punto_recta(punto,recta)

### RECCTAS PARALELAS

m1=float(input('ingrese la pendiente m1 = '))
b1=float(input('ingrese la ordenada b1 = '))
m2=float(input('ingrese la pendiente m2 = '))
b2=float(input('ingrese la ordenada b2 = '))

if m1==m2:
    print('las rectas son paralelas')
elif m1*m2==-1:
    print('las rectas son perpendiculares')
else:
    print('las rectas son secantes')
    

#### RECTA ENTRE DOS PUNTOS
def recta_puntos(p1,p2):
    m=(p2[1]-p1[1])/(p2[0]-p1[0])
    b=p1[1]-m*p1[0]
    print(f'la recta que pasa por los puntos es (m,b) = ({m},{b})')

p1=(1,2)
p2=(5,7)
recta_puntos(p1,p2)