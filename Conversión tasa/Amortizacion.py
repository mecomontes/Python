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
    DF={1:'Pago Intereses Periódico y Capital al Final',2:'Pago único al Final de Intereses y Capital',
       3:'Cuotas Iguales',4:'Abonos Constantes a Capital',5:'Gradiente Aritmético',6:'Gradiente Geométrico'}
    D={"A":12,"S":6,"T":3,"B":2,"M":1}
    
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Amortization.xlsx')
    worksheet = workbook.add_worksheet('Hoja 1')

    money_format = workbook.add_format({'num_format': '$#,##0'})
    money_format.set_align('center')
    money_format.set_align('vcenter')
    money_format.set_border(style=2)
                                 
    head_format = workbook.add_format()
    head_format.set_align('center')
    head_format.set_align('vcenter')
    head_format.set_bold()
    head_format.set_border(style=2)
    head_format.set_pattern(1)  # This is optional when using a solid fill.
    head_format.set_bg_color('#00AAFF')
    worksheet.set_column('A:F', 20)
    
    worksheet.set_column('I:I', 35)
    worksheet.set_column('H:H', 20)
    
    cell_format = workbook.add_format()
    cell_format.set_align('center')
    cell_format.set_align('vcenter')
    cell_format.set_border(style=2)
    

    per=D[Pago]
    N=int(Plazo*12/per)
    Head=['n','FECHA','INTERESES','ABONO CAPITAL','CUOTA','SALDO']
    Legend=['FECHA','FORMATO','MONTO','PLAZO','PERIODOS','TASA CONVERT']
    Datos=[str(Dia)+'/'+str(Mes)+'/'+str(Año),DF[FP],Monto,str(Plazo)+' Años',N,str(round(tasa,4))+'%  '+str(Pago)+'V']
    worksheet.write(1,2,0,cell_format)
    worksheet.write(1,3,0,cell_format)
    worksheet.write(1,4,0,cell_format)
    worksheet.write(1,5,Monto,money_format)
    
    for i in range(6):
        worksheet.write(0,i,Head[i],head_format)
        worksheet.write(3+i,7,Legend[i],head_format)
        worksheet.write(3+i,8,Datos[i],cell_format)
    
    
    worksheet.write(5,8,Datos[2],money_format)
    Total_Interes=0
    Total_Abono=0
    Total_Cuota=0
    
    if FP==1:
        Cuota=Monto*tasa/100
        Abono=0
    elif FP==3:
        Cuota=Monto*tasa*((1+tasa/100)**N/((1+tasa/100)**N-1))/100
    elif FP==4:
        Abono=Monto/N
    elif FP==5:
        Cuota=(Monto-GA*100*((1-(1+tasa/100)**-N)/(tasa/100)-N/(1+tasa/100)**N)/tasa)/((1-(1+tasa/100)**-N)/(tasa/100))
        Abono=Cuota-Monto*tasa/100
    elif FP==6 and tasa!=GG:
        Cuota=Monto*(tasa/100-GG/100)/(1-((1+GG/100)/(1+tasa/100))**N)
        Abono=Cuota-Monto*tasa/100
    elif FP==6 and tasa==GG:
        Cuota=Monto*(1+tasa/100)/N
        Abono=Cuota-Monto*tasa/100
        
    for i in range(N+1):
        worksheet.write(i+1,0,i,cell_format)
        Mes+=per
        if Mes>12:
            Mes-=12
            Año+=1
        
        Interes=Monto*tasa/100
        
        if FP==1 and i==N-1:
            Cuota=Interes+Monto
            Abono=Monto
        elif FP==2 and i<N-1:
            Cuota=0
            Abono=-Interes
        elif FP==2 and i==N-1: 
            Abono=Monto
            Cuota=Monto+Interes
        elif FP==3 and i<N:
            Abono=Cuota-Interes
        elif FP==4 and i<N:
            Cuota=Abono+Interes
        elif FP==5 and 0<i<N:
            Cuota+=GA
            Abono=Cuota-Interes
        elif FP==6 and 0<i<N:
            Cuota*=(1+GG/100)
            Abono=Cuota-Interes
            
        Monto-=Abono
            
        worksheet.write(i+1,1,str(Dia)+'/'+str(Mes)+'/'+str(Año),cell_format)
        if i<N:
            worksheet.write(i+2,2,Interes,money_format)
            worksheet.write(i+2,3,Abono,money_format)
            worksheet.write(i+2,4,Cuota,money_format)
            worksheet.write(i+2,5,Monto,money_format)
            Total_Interes+=Interes
            Total_Abono+=Abono
            Total_Cuota+=Cuota
        
    worksheet.write(i+2,0,'TOTAL',head_format)
    worksheet.write(i+2,2,Total_Interes,money_format)
    worksheet.write(i+2,3,Total_Abono,money_format)
    worksheet.write(i+2,4,Total_Cuota,money_format)
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
Plazo=1
tasa=2
nomi='N'
peri='B'
VoAi='V'
Pago='B'
GA=200000
GG=2

tasa=CambioTasa(nomi,peri,VoAi,tasa,'N',Pago,'V')

print('\n\n             Seleccione la Forma de Pago:')
print('     1. Pago Intereses Periódico y Capital al Final')
print('     2. Pago único al Final de Intereses y Capital')
print('     3. Cuotas Iguales')
print('     4. Abonos Constantes a Capital ')
print('     5. Gradiente Aritmético')
print('     6. Gradiente Geométrico\n\n')

FP=int(input(' Elija una opción: '))

Archivo(Dia,Mes,Año,Monto,tasa,Plazo,FP,Pago)