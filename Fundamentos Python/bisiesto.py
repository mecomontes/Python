def comprobar(año):

    if año%400==0:
        print('el año ', año, ' es bisiesto')
        mes=400
    elif año%4==0 and año%100!=0:
        print(f'el año {año} es bisiesto')
        mes=4
    else:
        print(f'el año {año} NO es bisiesto')
        mes=0
    return año, mes
    
    
    
x=int(input('ingrese un año: '))
a,m=comprobar(x)
