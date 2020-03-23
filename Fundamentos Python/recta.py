def punto_recta(x,y,recta):
    
    if y==recta[0]*x+recta[1]:
        print('el punto está en la recta')
    else:
        print('el punto no está en la recta')
        
recta=(3,4)
x,y=(2,10)
punto_recta(x,y,recta)