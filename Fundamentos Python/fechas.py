### DÍA SIGUIENTE

dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

año=int(input('ingrese el año: '))
mes=int(input('ingrese el mes: '))
dia=int(input('ingrese el día: '))
fecha=(año,mes,dia)

if dia<dias_mes[mes-1]:
    dia_siguiente=(año,mes,dia+1)
elif mes==12 and dia==31:
    dia_siguiente=(año+1,1,1)
elif dia==dias_mes[mes-1]:
    dia_siguiente=(año,mes+1,1)
else:
    print('error en los datos')
    
print(f'el dia siguiente es {dia_siguiente}')

### DIAS ENTRE

f1=input('ingrese la primer fecha: ')
f2=input('ingrese la segunda fecha: ')

