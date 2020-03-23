D={"A":12,"S":6,"T":3,"B":2,"M":1,"Q":1/2,"D":1/30,"N":0}

tasa=float(input("Ingrese tasa sin %: "))
nomi=input("Ingrese nominal de la tasa: ")
peri=input("Ingrese periodo de la tasa: ")
VoAi=input("La tasa es Vencida o Anticipada: ")
nomf=input("Ingresar nominal de la tasa buscada: ")
perf=input("Ingresar periodo de la tasa buscada: ")
VoAf=input("La tasa buscada es Vencida o Anticipada: ")

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

def agregar_anticipado (tasa):
    tasa=((tasa/100)/(1+tasa/100))*100
    print ( "La tasa vencida es: ", tasa, "% ", perf, " Anticipada")
    return tasa

def agregar_nominal (tasa,perf,nomf):
    tasa = tasa*D[nomf]/D[perf]
    print("La tasa con nominal es: ",tasa,"% ",nomf," ",perf," ",VoAf)
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
        if VoAf == 'A':
            tasa = agregar_anticipado (tasa)
            
    if nomf != 'N':
        tasa = agregar_nominal (tasa,perf,nomf)


