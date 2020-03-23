import matplotlib.pyplot as plt

b=float(input('b='))
h=float(input('h='))
d=float(input('d='))
dp=float(input("d'="))
#Rec=float(input('Recubrimiento='))
#cuantia=float(input('cuantia='))
fpc=float(input("f'c="))
fy=float(input('fy='))
#phi=float(input('Phi='))
Pui=float(input('Pu='))
Mui=float(input('Mu='))

cuantia=[0.01,0.015,0.02,0.025,0.03,0.035,0.04]

for cuant in cuantia:
    As=cuant*b*h/2
    Aps=cuant*b*h/2

    beta=0.85-0.05*(fpc-28)/7
    if beta<0.65:
        beta=0.65
    elif  beta>0.85:
        beta=0.85

    Pumin=0.1*b*h*fpc*10**2
    Put=[]
    Mut=[]

    for Pu in range(0,int(Pumin),5):
        phi=0.65+0.25*(Pumin-Pu)/Pumin
        if phi<0.65:
            phi=0.65
        elif phi>0.9:
            phi=0.9

        aCmin=0.85*fpc*beta*b
        bCmin=-(Pu*10**-2/phi+fy*As-600*Aps)
        cCmin=-600*Aps*dp

        x1=(-bCmin+(bCmin**2-4*aCmin*cCmin)**0.5)/(2*aCmin)

        if x1>0:
            Cmin=x1
        else:
            Cmin=(-bCmin-(bCmin**2-4*aCmin*cCmin)**0.5)/(2*aCmin)

        Mu=phi*(0.85*fpc*beta*Cmin*b*(h/2-(beta*Cmin)/2)+600*(Cmin-dp)*Aps/Cmin*((d-dp)/2)+fy*As*((d-dp)/2))*10**2
        Put.append(Pu)
        Mut.append(Mu)
    
    ad=Pumin-int(Pumin)

    phi=0.65
    Cb=(600*d)/(fy+600)
    fps=600*(Cb-dp)/(Cb)
    if fps>420:
        fps=420

    Pub=phi*(0.85*fpc*beta*600*d*b/(fy+600)+600*(Cb-dp)*Aps/Cb-fy*As)*10**2
    Mub=phi*(0.85*fpc*beta*600*d*b/(fy+600)*(h/2-(beta*600*d)/(2*(fy+600)))+600*(Cb-dp)*Aps/Cb*((d-dp)/2)+fy*As*((d-dp)/2))*10**2

    for Pu in range(int(Pumin),int(Pub),5):

        aCmin=0.85*fpc*beta*b
        bCmin=-(Pu*10**-2/phi+fy*As-600*Aps)
        cCmin=-600*Aps*dp

        x1=(-bCmin+(bCmin**2-4*aCmin*cCmin)**0.5)/(2*aCmin)

        if x1>0:
            Cmin=x1
        else:
            Cmin=(-bCmin-(bCmin**2-4*aCmin*cCmin)**0.5)/(2*aCmin)

        Mu=phi*(0.85*fpc*beta*Cmin*b*(h/2-(beta*Cmin)/2)+600*(Cmin-dp)*Aps/Cmin*((d-dp)/2)+fy*As*((d-dp)/2))*10**2
        Put.append(Pu+ad)
        Mut.append(Mu)

    Pumax=0.75*phi*(0.85*fpc*(b*h-As)+(fy*As))*10**2 #"Error aca" 
    ad=Pub-int(Pub)
    
    for Pu in range(int(Pub),int(Pumax),5):

        aCmax=0.85*fpc*beta*b
        bCmax=-(Pu*10**-2/phi+fy*As-600*Aps)
        cCmax=-600*Aps*dp

        x1=(-bCmax+(bCmax**2-4*aCmax*cCmax)**0.5)/(2*aCmax)

        if x1>0:
            Cmax=x1
        else:
            Cmax=(-bCmax-(bCmax**2-4*aCmax*cCmax)**0.5)/(2*aCmax)

        Mu=phi*(0.85*fpc*beta*Cmax*b*(h/2-(beta*Cmax)/2)+600*(Cmax-dp)*Aps/Cmax*((d-dp)/2)+fy*As*((d-dp)/2))*10**2
        Put.append(Pu+ad)
        Mut.append(Mu)
        
    aCmax=0.85*fpc*beta*b
    bCmax=-(Pumax*10**-2/phi+fy*As-600*Aps)
    cCmax=-600*Aps*dp

    x1=(-bCmax+(bCmax**2-4*aCmax*cCmax)**0.5)/(2*aCmax)

    if x1>0:
        Cmax=x1
    else:
        Cmax=(-bCmax-(bCmax**2-4*aCmax*cCmax)**0.5)/(2*aCmax)

    Mumax=phi*(0.85*fpc*beta*Cmax*b*(h/2-(beta*Cmax)/2)+600*(Cmax-dp)*Aps/Cmax*((d-dp)/2)+fy*As*((d-dp)/2))*10**2
    Put.append(Pumax)
    Mut.append(Mumax)

    plt.plot(Mut,Put)
    plt.xlabel('Mu Ton-m')
    plt.ylabel('Pu Ton')
    plt.grid()
plt.axvline(Mui)
plt.axhline(Pui)
plt.show()

"""


"""