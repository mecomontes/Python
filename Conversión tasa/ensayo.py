D={"A":12,"S":6,"T":3,"B":2,"M":1}

Dia=int(input('Día: '))
Mes=int(input('Mes: '))
Año=int(input('Año: '))
Monto=int(input('Monto: '))
Plazo=int(input('Plazo: '))

Tasa=input('Tasa: ').upper()
tasa=float(Tasa.split(' ')[0])
tipo=list(Tasa.split(' ')[1])
nomi=tipo[0]
peri=tipo[1]
VoAi=tipo[2]

Pago=input('Periodo de Pago: ').upper()[0]


