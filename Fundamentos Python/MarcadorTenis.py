##### set de tenis

marcadores=int(input('ingrese la cantidad de marcadores a verificar: '))
cont=1

while cont<=marcadores:
    cont=cont+1
    m=int(input('ingrese numero de juegos ganados por A:' ))
    n=int(input('ingrese numero de juegos ganados por B:' ))
    
    if m>7 or n>7:
        print('marcador invalido')
    elif m<6 and n<6:
        print('el juego aun notermina')
    elif m==7 and (n==5 or n==6):
        print('el ganador del set es el jugador A')
    elif n==7 and (m==5 or m==6):
        print('el ganador del set es el jugador B')
    elif n==6 and m<5:
        print('el ganador del set es el jugador B')
    elif m==6 and n<5:
        print('el ganador del set es el jugador A')
    else:
         print('marcador invalido')