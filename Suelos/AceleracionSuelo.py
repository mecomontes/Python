import numpy as np
import matplotlib.pyplot as plt



file = open("acel3.txt", "r")
mat = file.readlines()
mat1 = [] 
for i in range(0,len(mat)):   
    if i == 3: #Si voy en la linea 3(puedo sacar el dt)
        ldt = mat[i].split("DT=") #Creo una lista donde la primera posicion es el texto antes del dt y la segunda posicion dps del dt
        ldt = ldt[1].split(" ") #toma la segunda posicion de ldt 
        dt = float(ldt[3])
    if i >= 4:
        lis = mat[i].split(" ")
        lis2 = [] #Va a contener los valores como tal de cada linea de datos (solo numeros)
        for j in range(len(lis)):   #Recorro a lis el cual cntiene una lista que contiene los valores de cada linea de datos del archivo (la cual contiene posiciones vacias por los espacios en blanco)
            if len(lis[j]) != 0:   #Si el valor es numerico, lo que no sea numerico lo ignora        
                lis2.append(float(lis[j]))  # Añado el dato
        mat1.append(lis2) #Añado la lista que contiene los datos de la linea en la que va a la matriz mat1 (la cual finalmente tendrá todos los datos, en cada fila la matriz contiene los datos de una fila del archivo) 
        
listac = []
g=9.81

for i in range(len(mat1)):
    for j in range(5):
        listac.append(mat1[i][j]*g) #### aceleración en m/s^2

listac.pop(-1)
listac.pop(-2)   

N=len(listac)

lis_time = []

for i in range(N):
    lis_time.append(i*dt)  

lis_vel =  []

for i in range(N):
    lis_vel.append(listac[i]*dt)
    
#lis_vel1 = [0]

#for i in range(N-1):
    #m=(listac[i+1]-listac[i])/dt
    #lis_vel1.append(m*(lis_time[i+1]**2+lis_time[i]**2)/2-m*lis_time[i+1]*lis_time[i]+listac[i+1]*dt)
    
lis_dist = []

for i in range(N):
    lis_dist.append(lis_vel[i]*dt)
    
#lis_dist1 = [0]

#for i in range(N-1):
    #m=(lis_vel1[i+1]-lis_vel1[i])/dt
    #lis_dist1.append(m*(lis_time[i+1]**2+lis_time[i]**2)/2-m*lis_time[i+1]*lis_time[i]+lis_vel1[i+1]*dt)
        
plt.plot(lis_time,listac,color="red")
plt.xlabel("Tiempo")
plt.ylabel("Aceleración")
plt.show()

plt.plot(lis_time,lis_vel,color="blue")
plt.xlabel("Tiempo")
plt.ylabel("Velocidad")
plt.show()

plt.plot(lis_time,lis_dist,color="green")
plt.xlabel("Tiempo")
plt.ylabel("Desplazamiento")
plt.show()

fourier = np.fft.fft(listac)
#freq = np.fft.fftfreq(N, d=dt)

freq=[]
freq025_20=[]
for i in range(N):
    freq.append((i+1)/(N*dt))
    if freq[i]>=0.25 and freq[i]<=20:
	freq025_20.append(freq[i])

plt.plot(freq,np.abs(fourier),color="purple")
plt.xlabel("Frecuencia")
plt.ylabel("Magnitud")
plt.show()

T=[]
for i in range(N):
    T.append(1/freq[i])

#acel horiz. maxima
amax=np.max(np.absolute(listac))

#vel horiz. maxima
vmax=np.max(np.absolute(lis_vel))

#dist horiz. maxima
dmax=np.max(np.absolute(lis_dist))

#periodo predominante
Mmax=np.argmax(fourier)
Tp=1/freq[Mmax]

#arias intensity
Ia=[]
Iacum=0

for i in range(N):
    Iacum+=np.pi*(np.absolute(listac[i])**2)*dt/(2*g)
    Ia.append(Iacum)
    
Iamax=Ia[-1]
Ia95=0.95*Iamax
Ia5=0.05*Iamax
menor95=Iamax
menor5=Iamax

for i in range(N):
    
    dif=np.absolute(Ia95-Ia[i])
    if menor95>dif:
        menor95=dif
        pos95=i
        
    dif=np.absolute(Ia5-Ia[i])
    if menor5>dif:
        menor5=dif
        pos5=i
        
t95=lis_time[pos95]
t5=lis_time[pos5]

t5_95=t95-t5

texto='t5-95 = ' + str(round(t5_95,4)) +'seg'
plt.plot(lis_time,Ia,color="green")
plt.text(200,1.5e-10,texto)
plt.xlabel("tiempo (s)")
plt.ylabel("Arias intensity (m/s)")
plt.plot(t95,Ia95,'ko')
plt.plot(t5,Ia5,'ko')
plt.axvline(t5, color='r', ls="dotted")
plt.axvline(t95,color='r', ls="dotted")
plt.show()

#CAV
CAV=[]
CAVcum=0

for i in range(N):
    if np.absolute(listac[i])*100>=5:
        CAVcum+=(np.absolute(listac[i]*100))*dt
        CAV.append(CAVcum)

plt.plot(lis_time,CAV,color="red")
plt.xlabel("tiempo (s)")
plt.ylabel("Cumulative absolute velocity (cm/s)")
plt.show()



#Tm: periodo medio 
freq

Ugd=np.absolute(fourier)**2
Ugn=(np.absolute(fourier)**2)*1/freq



