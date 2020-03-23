import xlsxwriter

"""from datetime import date
from datetime import datetime
from datetime import time
Today=date.today()
Date = str(Today.day) + '/' + str(Today.month) + '/' + str(Today.year)
print(Date)"""

def CambioTasa(nomi,peri,VoAi,tasa,nomf,perf,VoAf):
   
    D={"A":12,"S":6,"T":3,"B":2,"M":1,"Q":1/2,"D":1/30,"N":0}
    
    def quitar_nominal (tasa,peri,nomi):
        tasa=tasa*D[peri]/D[nomi]
        print("La tasa sin nominal es: ",tasa,"% ",peri ," ",VoAi)
        return tasa
    
    def quitar_anticipado (tasa):
        tasa=((tasa/100)/(1-tasa/100))*100
        print("La tasa vencida (efectiva) es: ",tasa,"% ",peri ," Vencida")
        return tasa
    
    def cambiar_periodo (tasa,perf,peri):
        tasa=((1+tasa/100)**(D[perf]/D[peri])-1)*100
        print ( "La tasa vencida es: ", tasa, "% ", perf , " Vencida")
        return tasa
    
    
    if (nomi,peri,VoAi)==(nomf,perf,VoAf):
        print("La tasa ingresada es la misma buscada ",nomi," ",peri," ",VoAi)
    
    else:
        if nomi != 'N':
            tasa = quitar_nominal ( tasa, peri, nomi )
            
        if (peri,VoAi) != (perf,VoAf):
            if VoAi == 'A':
                tasa = quitar_anticipado (tasa)
            if peri != perf:
                tasa = cambiar_periodo (tasa,perf,peri)
    
    return tasa


def Archivo(Dia,Mes,Año,Monto,tasa,Plazo,FP,Pago):
    DF={1:'Pago Intereses Periódico y Capital al Final',2:'Pago único al Final de Intereses y Cpaital',
       3:'Cuotas Iguales',4:'Abonos Constantes a Capital',5:'Gradiente Aritmético',6:'Gradiente Geométrico'}
    D={"A":12,"S":6,"T":3,"B":2,"M":1}
    
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Amortization.xlsx')
    worksheet = workbook.add_worksheet(DF[FP])

    money = workbook.add_format({'num_format': '$#,##0'})
    money.set_align('center')
    money.set_align('vcenter')
    money.set_bold()
    money.set_border(style=2)
                                 
    head_format = workbook.add_format()
    head_format.set_align('center')
    head_format.set_align('vcenter')
    head_format.set_bold()
    head_format.set_border(style=2)
    worksheet.set_column('A:Z', 15)
    
    cell_format = workbook.add_format()
    cell_format.set_align('center')
    cell_format.set_align('vcenter')
    cell_format.set_border(style=2)

    per=D[Pago]
    N=int(Plazo*12/per)
    Head=['n','FECHA','INTERESES','ABONO CAPITAL','CUOTA','SALDO']
    Legend=['FECHA','FORMATO','MONTO','PLAZO','PERIODOS','TASA CONVERT']
    Datos=[str(Dia)+'/'+str(Mes)+'/'+str(Año),DF[FP],Monto,str(Plazo)+' Años',N,str(round(tasa,4))+'%  '+str(Pago)+'V']
    
    for i in range(6):
        worksheet.write(0,i,Head[i],head_format)
        worksheet.write(3+i,7,Legend[i],head_format)
        worksheet.write(3+i,8,Datos[i],cell_format)
    
    
    worksheet.write(5,8,Datos[2],money)
    
    for i in range(N):
        worksheet.write(i+1,0,i,cell_format)
        Mes+=per
        if Mes>12:
            Mes-=12
            Año+=1

        worksheet.write(i+1,1,str(Dia)+'/'+str(Mes)+'/'+str(Año),cell_format)
        
    workbook.close()
    
    


"""Fecha=input('Fecha: ')

Dia=int(Fecha.split('/')[0])
Mes=int(Fecha.split('/')[1])
Año=int(Fecha.split('/')[2])

Monto=int(input('Monto: '))
Plazo=int(input('Plazo: '))

Tasa=input('Tasa: ').upper()
tasa=float(Tasa.split(' ')[0])
tipo=list(Tasa.split(' ')[1])
nomi=tipo[0]
peri=tipo[1]
VoAi=tipo[2]

Pago=input('Periodo de Pago: ').upper()[0]"""

Dia=22
Mes=11
Año=2019
Monto=25000000
Plazo=15
tasa=24
nomi='T'
peri='M'
VoAi='A'
Pago='B'

tasa=CambioTasa(nomi,peri,VoAi,tasa,'N',Pago,'V')

print('\n\n             Seleccione la Forma de Pago:')
print('     1. Pago Intereses Periódico y Capital al Final')
print('     2. Pago único al Final de Intereses y Cpaital')
print('     3. Cuotas Iguales')
print('     4. Abonos Constantes a Capital ')
print('     5. Gradiente Aritmético')
print('     6. Gradiente Geométrico\n\n')

FP=int(input(' Elija una opción: '))

Archivo(Dia,Mes,Año,Monto,tasa,Plazo,FP,Pago)