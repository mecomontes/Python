# Función para generar la aproximación a Pi

def Funcion_Pi(Nsumas):
    Suma = 3.0
    SoR = 0  #Suma o resta
    for x in range(0,Nsumas):
        if(x == 0):
            print("Suma numero",x+1,"Valor pi",Suma)
        else:

            if(SoR == 0):
                Suma = float(Suma + (4.0/((x*2)*((x*2)+1)*((x*2)+2))))
                SoR = 1
                print("Suma numero",x+1,"Valor pi",Suma)
            else:
                Suma = float(Suma - (4.0/((x*2)*((x*2)+1)*((x*2)+2))))
                SoR = 0
                print("Suma numero",x+1,"Valor pi",Suma)

# Llamado a la función
Nsumas = int(input("Cuantas Sumas:"))
Funcion_Pi(Nsumas)
