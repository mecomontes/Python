import numpy as np
import math as m

A=float(input('Altura del agua A: '))
B=float(input('Altura del estrato uno B: '))
C=float(input('Altura del estrato dos C: '))
D=float(input('Distancia del agua D: '))
E=float(input('Distancia de Presa E: '))
F=float(input('Distancia de Suelo F: '))

b1=float(input('b1: '))
b2=float(input('b2: '))
b3=float(input('b3: '))
b4=float(input('b4: '))
b5=float(input('b5: '))
L1=float(input('L1: '))
L2=float(input('L2: '))
L3=float(input('L3: '))

Dx=float(input('Delta X Dx: '))
Dx=float(input('Delta X Dx: '))
k1=float(input('Permeabilidad del estrato 1: '))
e1=float(input('Relacion de vacío del estrato 1: '))
w1=float(input('Contenido de Humedad del estrato 1: '))
v1=float(input('Módulo de Poison del estrato 1: '))
E1=float(input('M´0dulo de Young del estrato 1: '))

k2=float(input('Permeabilidad del estrato 2: '))
e2=float(input('Relacion de vacío del estrato 2: '))
w2=float(input('Contenido de Humedad del estrato 2: '))
v2=float(input('Módulo de Poison del estrato 2: '))
E2=float(input('M´0dulo de Young del estrato 2: '))

Gc=float(input('Gamma del concreto Gc: '))
Gw=float(input('Gamma del agua Gc: '))
Gs=float(input('Gamma s: '))

Punto=float(input('Coordenada del punto: '))

"""
A=3 
B=2 
C=2 
D=2 
E=2 
F=2

Gc=24
Gw=10
Gs=2.6

b1=0.4 
b2=0.2 
b4=0.2 
b5=1 
L1=1 
L2=1 
L3=5

k1=0.01 
e1=0.8 
w1=0.4 
v1=0.25 
E1=15

k2=0.02
e2=1 
w2=0.35 
v2=0.2 
E2=16

Dz=1
Dx=1
"""
Nx=int((D+E+F)/Dx)
Nz=int((B+C)/Dz)

Punto=[1.5,1]
b3=E-b1-b2-b4

K=np.zeros((Nz,Nx+1))
H=np.zeros((Nz,Nx))
N=Nx*(Nz-1)
h=[]
As=np.zeros((N,N))
b=np.zeros((N,1))

px1=int(D/Dx)
px2=int((D+b1)/Dx)
px3=int((D+b1+b2)/Dx)
px4=int((D+b1+b2+b3)/Dx)
px5=int((D+E)/Dx)

pzc=int(B/Dz)
pz1=int((L1+L2)/Dz)
pz1=int(L2/Dz)

for i in range(Nx):
    if i*Dx<px1:
        h.append(A+B+C)
    elif px1<i*Dx<px5:
        h.append(0)
    else:
        h.append(B+C)
        
if L1+L2<B+C and L3>A and b5<E and b3>0:
    for i in range(Nz):
        for j in range(1,Nx):               
            if (px2 < j*Dx < px3 and i*Dz < pz1) or (px4 < j*Dx < px5 and i*Dz < pz2):
                K[i][j]=0            
            elif i*Dz < pzc:
                K[i][j]=k1
                ei=e1
                vi=v1
            else:
                K[i][j]=k2
                ei=e2
                vi=v2

    for i in range(1,Nz):
        for j in range(1,Nx+1):
            K1=K[i-1][j-1]
            K2=K[i-1][j]
            K3=K[i][j]
            K4=K[i][j-1]

            Ca=K1+K2
            Cb=K3+K4
            Cd=K2+K3
            Ci=K1+K4
            Cc=2*(K1+K2+K3+K4)
            
            if i==1:
                if j==1:
                    As[j-1][Nx*(i-1)+j-1]=Cc
                    As[j-1][Nx*(i)+j-1]=-Cb
                    As[j-1][Nx*(i-1)+j]=-Cd
                    b[j-1]=Ca*h[j-1]
                elif j==Nx:
                    As[j-1][Nx*(i-1)+j-1]=Cc
                    As[j-1][Nx*(i)+j-1]=-Cb
                    As[j-1][Nx*(i-1)+j-2]=-Ci
                    b[j-1]=Ca*h[j-1]
                else:
                    As[j-1][Nx*(i-1)+j-1]=Cc
                    As[j-1][Nx*(i)+j-1]=-Cb
                    As[j-1][Nx*(i-1)+j]=-Cd
                    As[j-1][Nx*(i-1)+j-2]=-Ci
                    b[j-1]=Ca*h[j-1]
                    
            elif i==Nz-1:
                if j==1:
                    As[Nx*(i-1)+j-1][Nx*(i-1)+j-1]=Cc
                    As[Nx*(i-1)+j-1][Nx*(i-2)+j-1]=-Ca
                    As[Nx*(i-1)+j-1][Nx*(i-1)+j]=-Cd
                elif j==Nx:
                    As[Nx*(i-1)+j-1][Nx*(i-1)+j-1]=Cc
                    As[Nx*(i-1)+j-1][Nx*(i-2)+j-1]=-Ca
                    As[Nx*(i-1)+j-1][Nx*(i-1)+j-2]=-Ci
                else:
                    As[Nx*(i-1)+j-1][Nx*(i-1)+j-1]=Cc
                    As[Nx*(i-1)+j-1][Nx*(i-2)+j-1]=-Ca
                    As[Nx*(i-1)+j-1][Nx*(i-1)+j]=-Cd
                    As[Nx*(i-1)+j-1][Nx*(i-1)+j-2]=-Ci
                
            else:
                As[Nx*(i-1)+j-1][Nx*(i-1)+j-1]=Cc
                As[Nx*(i-1)+j-1][Nx*(i)+j-1]=-Cb
                As[Nx*(i-1)+j-1][Nx*(i-1)+j]=-Cd
                As[Nx*(i-1)+j-1][Nx*(i-1)+j-2]=-Ci
                As[Nx*(i-1)+j-1][Nx*(i-2)+j-1]=-Ca
                 
    X=np.linalg.inv(As)@b
    for i in range(len(X)):
        h.append(X[i][0])
    
    for i in range(Nz):
        for j in range(Nx):
            H[i][j]=h[Nx*i+j]
    
    
    for i in range(Nz):
        for j in range(Nx):
            H[i][j]=h[Nx*i+j]

    
    if Punto[0]<D+E+F and Punto[1]<B+C:
        x=int(Punto[0]/Dx)
        z=int(Punto[1]/Dz)
        P=10*(H[z][x]-Punto[1])
        print('\n\nEl valor de la presión de poros en el punto es ',P,'kN/m3')
    
    den=B+C-z
    
    if x<D:#zona 1
        beta=m.atan((D-x)/den)
        teta=m.atan((x)/den)
        alfa=teta+beta
        Szw=Gw*A*(alfa+m.sin(alfa)*m.cos(alfa+2*beta))/m.pi
        Sxw=Gw*A*(alfa-m.sin(alfa)*m.cos(alfa+2*beta))/m.pi
        Txzw=Gw*A*(m.sin(alfa)*m.sin(alfa+2*beta))/m.pi
        
        teta=m.atan((D-x)/den)
        beta=m.atan((D+b5-x)/den)
        alfa=beta-teta
        Szr=Gc*L3*(alfa+m.sin(alfa)*m.cos(alfa+2*beta))/m.pi
        Sxr=Gc*L3*(alfa-m.sin(alfa)*m.cos(alfa+2*beta))/m.pi
        Txzr=Gc*L3*(m.sin(alfa)*m.sin(alfa+2*beta))/m.pi
        
        teta=m.atan((D+E-x)/den)
        beta=m.atan((D+b5-x)/den)
        alfa=teta-beta
        R1=((D+E-x)**2+(den)**2)**0.5
        R2=((D+b5-x)**2+(den)**2)**0.5
        Szt=Gc*L3*(x*alfa/(E-b5)-m.sin(2*beta))/(2*m.pi)
        Sxt=Szt=Gc*L3*(x/(E-b5)-z*m.log(R1**2/R2**2)/(E-b5)+m.sin(2*beta))/(2*m.pi)
        Txzt=Gc*L3*(1-2*x/(E-b5)+m.cos(2*beta))/(2*m.pi)
        
        # pantalla 1
        R1=((D+b1-x)**2+(den-(L2+L1))**2)**0.5
        R2=((D+b1-x)**2+(den)**2)**0.5
        M=(1-vi)/vi
        Szp1=Gc*L2*(((M+1)/2*M)*((((z-L1+L2)**3)/R1**4)+((z+L1+L2)*((((z+L1+L2)**2)+2*L1+L2*z)/R2**4)-(8*L1+L2*z*(L1+L2+z)*x**2/R2**6)))+((M-1)/4*M)*(((z-L1+L2)/R1**2)+((3*z+L1+L2)/R2**2)-((4*z*x**2)/R2**4)))/(m.pi)
        Sxp1=Gc*L2*((((M+1)/2*M)*(((((z-L1+L2)*x**2)/R1**4)+((z+L1+L2)*(x**2+2*L1+L2**2)-(2*L1+L2*x**2))/R2**4)-(8*L1+L2*z*(L1+L2+z)*x**2/R2**6)))+((M-1)/4*M)*((-(z-L1+L2)/R1**2)+((z+3*L1+L2)/R2**2)+((4*z*x**2)/R2**4)))/(m.pi)
        Txzp1=Gc*L2*x*(((M+1)/2*M)*(((((z-L1+L2)**2)/R1**4)+((z**2-2*L1+L2*z-(L1+L2)**2)/R2**4)-(8*L1+L2*z*(L1+L2+z)**2/R2**6)))+((M-1)/4*M)*((1/R1**2)-(1/R2**2)+((4*z*(L1+L2+z))/R2**4)))/(m.pi)
        
        # pantalla 2
        R1=((D+E-b4-x)**2+(den-L2)**2)**0.5
        R2=((D+E-b4-x)**2+(den)**2)**0.5
        M=(1-vi)/vi
        Szp2=Gc*L2*(((M+1)/2*M)*((((z-L2)**3)/R1**4)+((z+L2)*((((z+L2)**2)+2*L2*z)/R2**4)-(8*L2*z*(L2+z)*x**2/R2**6)))+((M-1)/4*M)*(((z-L2)/R1**2)+((3*z+L2)/R2**2)-((4*z*x**2)/R2**4)))/(m.pi)
        Sxp2=Gc*L2*(((((M+1)/2*M)*(((((z-L2)*x**2)/R1**4)+((z+L2)*((x**2)+2*L2**2)-(2*L2*x**2))/R2**4)-(8*L2*z*(L2+z)*x**2)/R2**6)))+((M-1)/4*M)*((-(z-L2)/R1**2)+((z+3*L2)/R2**2)+((4*z*x**2)/R2**4)))/(m.pi)
        Txzp2=Gc*L2*x*(((M+1)/2*M)*(((((z-L2)**2)/R1**4)+((z**2-2*L2*z-L2**2)/R2**4)-(8*L2*z*(L2+z)**2/R2**6)))+((M-1)/4*M)*((1/R1**2)-(1/R2**2)+((4*z*(L2+z))/R2**4)))/(m.pi)
        

        Gsat=Gw*(ei+Gs)/(1+ei)
        Szs=Gsat*z
        
        SzT=Szw+Szr+Szt+Szs+Szp1+Szp2
        SxT=Sxw+Sxr+Sxt+Sxp1+Sxp2
        TxzT=Txzw+Txzr+Txzt+Txzp1+Txzp2
        
        
        Ms=np.zeros((2,2))
        Ms[0][0]=Sxt-P
        Ms[0][1]=Txzt
        Ms[1][0]=Txzt
        Ms[1][1]=Szt-P
        
        Centro=(Ms[0][0]+Ms[1][1])/2
        Radio=(((Ms[0][0]-Ms[1][1])/2)**2+Ms[1][0]**2)**0.5
        
        Sep=np.zeros((2,2))
        Sep[0][0]=Centro+Radio
        Sep[0][1]=0
        Sep[1][0]=0
        Sep[1][1]=Centro-Radio
        
        print('\n\nMatriz de Esfuerzos Efectivos \n\n',Ms)
        print('\n\nMatriz de Esfuerzos Efectivos Pricipales  \n\n',Sep)
        
    elif D<x<D+b5:#zona 3
        beta=m.atan((x-D)/den)
        teta=m.atan((x)/den)
        alfa=teta-beta
        Szw=Gw*A*(alfa+m.sin(alfa)*m.cos(alfa+2*beta))/m.pi
        Sxw=Gw*A*(alfa-m.sin(alfa)*m.cos(alfa+2*beta))/m.pi
        Txzw=Gw*A*(m.sin(alfa)*m.sin(alfa+2*beta))/m.pi
        
        teta=m.atan((x-D)/den)
        beta=m.atan((D+b5-x)/den)
        alfa=beta+teta
        Szr=Gc*L3*(alfa+m.sin(alfa)*m.cos(alfa+2*beta))/m.pi
        Sxr=Gc*L3*(alfa-m.sin(alfa)*m.cos(alfa+2*beta))/m.pi
        Txzr=Gc*L3*(m.sin(alfa)*m.sin(alfa+2*beta))/m.pi
        
        teta=m.atan((D+E-x)/den)
        beta=m.atan((D+b5-x)/den)
        alfa=teta-beta
        R1=((D+E-x)**2+(den)**2)**0.5
        R2=((D+b5-x)**2+(den)**2)**0.5
        Szt=Gc*L3*(x*alfa/(E-b5)-m.sin(2*beta))/(2*m.pi)
        Sxt=Szt=Gc*L3*(x/(E-b5)-z*m.log(R1**2/R2**2)/(E-b5)+m.sin(2*beta))/(2*m.pi)
        Txzt=Gc*L3*(1-2*x/(E-b5)+m.cos(2*beta))/(2*m.pi)
        
        # pantalla 1
        R1=((D+b1-x)**2+(den-(L2+L1))**2)**0.5
        R2=((D+b1-x)**2+(den)**2)**0.5
        M=(1-vi)/vi
        Szp1=Gc*L2*(((M+1)/2*M)*((((z-L1+L2)**3)/R1**4)+((z+L1+L2)*((((z+L1+L2)**2)+2*L1+L2*z)/R2**4)-(8*L1+L2*z*(L1+L2+z)*x**2/R2**6)))+((M-1)/4*M)*(((z-L1+L2)/R1**2)+((3*z+L1+L2)/R2**2)-((4*z*x**2)/R2**4)))/(m.pi)
        Sxp1=Gc*L2*((((M+1)/2*M)*(((((z-L1+L2)*x**2)/R1**4)+((z+L1+L2)*(x**2+2*L1+L2**2)-(2*L1+L2*x**2))/R2**4)-(8*L1+L2*z*(L1+L2+z)*x**2/R2**6)))+((M-1)/4*M)*((-(z-L1+L2)/R1**2)+((z+3*L1+L2)/R2**2)+((4*z*x**2)/R2**4)))/(m.pi)
        Txzp1=Gc*L2*x*(((M+1)/2*M)*(((((z-L1+L2)**2)/R1**4)+((z**2-2*L1+L2*z-(L1+L2)**2)/R2**4)-(8*L1+L2*z*(L1+L2+z)**2/R2**6)))+((M-1)/4*M)*((1/R1**2)-(1/R2**2)+((4*z*(L1+L2+z))/R2**4)))/(m.pi)
        
        # pantalla 2
        R1=((D+E-b4-x)**2+(den-L2)**2)**0.5
        R2=((D+E-b4-x)**2+(den)**2)**0.5
        M=(1-vi)/vi
        Szp1=Gc*L2*(((M+1)/2*M)*((((z-L2)**3)/R1**4)+((z+L2)*((((z+L2)**2)+2*L2*z)/R2**4)-(8*L2*z*(L2+z)*x**2/R2**6)))+((M-1)/4*M)*(((z-L2)/R1**2)+((3*z+L2)/R2**2)-((4*z*x**2)/R2**4)))/(m.pi)
        Sxp1=Gc*L2*(((((M+1)/2*M)*(((((z-L2)*x**2)/R1**4)+((z+L2)*((x**2)+2*L2**2)-(2*L2*x**2))/R2**4)-(8*L2*z*(L2+z)*x**2)/R2**6)))+((M-1)/4*M)*((-(z-L2)/R1**2)+((z+3*L2)/R2**2)+((4*z*x**2)/R2**4)))/(m.pi)
        Txzp1=Gc*L2*x*(((M+1)/2*M)*(((((z-L2)**2)/R1**4)+((z**2-2*L2*z-L2**2)/R2**4)-(8*L2*z*(L2+z)**2/R2**6)))+((M-1)/4*M)*((1/R1**2)-(1/R2**2)+((4*z*(L2+z))/R2**4)))/(m.pi)
        

        Gsat=Gw*(ei+Gs)/(1+ei)
        Szs=Gsat*z
        
        SzT=Szw+Szr+Szt+Szs+Szp1+Szp2
        SxT=Sxw+Sxr+Sxt+Sxp1+Sxp2
        TxzT=Txzw+Txzr+Txzt+Txzp1+Txzp2
        
        Ms=np.zeros((2,2))
        Ms[0][0]=Sxt-P
        Ms[0][1]=Txzt
        Ms[1][0]=Txzt
        Ms[1][1]=Szt-P
        
        Centro=(Ms[0][0]+Ms[1][1])/2
        Radio=(((Ms[0][0]-Ms[1][1])/2)**2+Ms[1][0]**2)**0.5
        
        Sep=np.zeros((2,2))
        Sep[0][0]=Centro+Radio
        Sep[0][1]=0
        Sep[1][0]=0
        Sep[1][1]=Centro-Radio
        
        print('\n\nMatriz de Esfuerzos Efectivos \n\n',Ms)
        print('\n\nMatriz de Esfuerzos Efectivos Pricipales  \n\n',Sep)
        
    elif D+b5<x<D+E: #zona 4
        beta=m.atan((x-D)/den)
        teta=m.atan((x)/den)
        alfa=teta-beta
        Szw=Gw*A*(alfa+m.sin(alfa)*m.cos(alfa+2*beta))/m.pi
        Sxw=Gw*A*(alfa-m.sin(alfa)*m.cos(alfa+2*beta))/m.pi
        Txzw=Gw*A*(m.sin(alfa)*m.sin(alfa+2*beta))/m.pi
        
        teta=m.atan((x-D)/den)
        beta=m.atan((x-D-b5)/den)
        alfa=teta-beta
        Szr=Gc*L3*(alfa+m.sin(alfa)*m.cos(alfa+2*beta))/m.pi
        Sxr=Gc*L3*(alfa-m.sin(alfa)*m.cos(alfa+2*beta))/m.pi
        Txzr=Gc*L3*(m.sin(alfa)*m.sin(alfa+2*beta))/m.pi
        
        teta=m.atan((D+E-x)/den)
        beta=m.atan((D+b5-x)/den)
        alfa=teta-beta
        R1=((D+E-x)**2+(den)**2)**0.5
        R2=((D+b5-x)**2+(den)**2)**0.5
        Szt=Gc*L3*(x*alfa/(E-b5)-m.sin(2*beta))/(2*m.pi)
        Sxt=Szt=Gc*L3*(x/(E-b5)-z*m.log(R1**2/R2**2)/(E-b5)+m.sin(2*beta))/(2*m.pi)
        Txzt=Gc*L3*(1-2*x/(E-b5)+m.cos(2*beta))/(2*m.pi)
        
        # pantalla 1
        R1=((D+b1-x)**2+(den-(L2+L1))**2)**0.5
        R2=((D+b1-x)**2+(den)**2)**0.5
        M=(1-vi)/vi
        Szp1=Gc*L2*(((M+1)/2*M)*((((z-L1+L2)**3)/R1**4)+((z+L1+L2)*((((z+L1+L2)**2)+2*L1+L2*z)/R2**4)-(8*L1+L2*z*(L1+L2+z)*x**2/R2**6)))+((M-1)/4*M)*(((z-L1+L2)/R1**2)+((3*z+L1+L2)/R2**2)-((4*z*x**2)/R2**4)))/(m.pi)
        Sxp1=Gc*L2*((((M+1)/2*M)*(((((z-L1+L2)*x**2)/R1**4)+((z+L1+L2)*(x**2+2*L1+L2**2)-(2*L1+L2*x**2))/R2**4)-(8*L1+L2*z*(L1+L2+z)*x**2/R2**6)))+((M-1)/4*M)*((-(z-L1+L2)/R1**2)+((z+3*L1+L2)/R2**2)+((4*z*x**2)/R2**4)))/(m.pi)
        Txzp1=Gc*L2*x*(((M+1)/2*M)*(((((z-L1+L2)**2)/R1**4)+((z**2-2*L1+L2*z-(L1+L2)**2)/R2**4)-(8*L1+L2*z*(L1+L2+z)**2/R2**6)))+((M-1)/4*M)*((1/R1**2)-(1/R2**2)+((4*z*(L1+L2+z))/R2**4)))/(m.pi)
        
        # pantalla 2
        R1=((D+E-b4-x)**2+(den-L2)**2)**0.5
        R2=((D+E-b4-x)**2+(den)**2)**0.5
        M=(1-vi)/vi
        Szp1=Gc*L2*(((M+1)/2*M)*((((z-L2)**3)/R1**4)+((z+L2)*((((z+L2)**2)+2*L2*z)/R2**4)-(8*L2*z*(L2+z)*x**2/R2**6)))+((M-1)/4*M)*(((z-L2)/R1**2)+((3*z+L2)/R2**2)-((4*z*x**2)/R2**4)))/(m.pi)
        Sxp1=Gc*L2*(((((M+1)/2*M)*(((((z-L2)*x**2)/R1**4)+((z+L2)*((x**2)+2*L2**2)-(2*L2*x**2))/R2**4)-(8*L2*z*(L2+z)*x**2)/R2**6)))+((M-1)/4*M)*((-(z-L2)/R1**2)+((z+3*L2)/R2**2)+((4*z*x**2)/R2**4)))/(m.pi)
        Txzp1=Gc*L2*x*(((M+1)/2*M)*(((((z-L2)**2)/R1**4)+((z**2-2*L2*z-L2**2)/R2**4)-(8*L2*z*(L2+z)**2/R2**6)))+((M-1)/4*M)*((1/R1**2)-(1/R2**2)+((4*z*(L2+z))/R2**4)))/(m.pi)
        
        
        Gsat=Gw*(ei+Gs)/(1+ei)
        Szs=Gsat*z
        
        SzT=Szw+Szr+Szt+Szs+Szp1+Szp2
        SxT=Sxw+Sxr+Sxt+Sxp1+Sxp2
        TxzT=Txzw+Txzr+Txzt+Txzp1+Txzp2
        
        Ms=np.zeros((2,2))
        Ms[0][0]=Sxt-P
        Ms[0][1]=Txzt
        Ms[1][0]=Txzt
        Ms[1][1]=Szt-P
        
        Centro=(Ms[0][0]+Ms[1][1])/2
        Radio=(((Ms[0][0]-Ms[1][1])/2)**2+Ms[1][0]**2)**0.5
        
        Sep=np.zeros((2,2))
        Sep[0][0]=Centro+Radio
        Sep[0][1]=0
        Sep[1][0]=0
        Sep[1][1]=Centro-Radio
        
        print('\n\nMatriz de Esfuerzos Efectivos \n\n',Ms)
        print('\n\nMatriz de Esfuerzos Efectivos Pricipales  \n\n',Sep)
        
    elif D+E<x<D+E+F:#zona 2
        beta=m.atan((x-D)/den)
        teta=m.atan((x)/den)
        alfa=teta-beta
        Szw=Gw*A*(alfa+m.sin(alfa)*m.cos(alfa+2*beta))/m.pi
        Sxw=Gw*A*(alfa-m.sin(alfa)*m.cos(alfa+2*beta))/m.pi
        Txzw=Gw*A*(m.sin(alfa)*m.sin(alfa+2*beta))/m.pi
        
        teta=m.atan((x-D)/den)
        beta=m.atan((x-D-b5)/den)
        alfa=teta-beta
        Szr=Gc*L3*(alfa+m.sin(alfa)*m.cos(alfa+2*beta))/m.pi
        Sxr=Gc*L3*(alfa-m.sin(alfa)*m.cos(alfa+2*beta))/m.pi
        Txzr=Gc*L3*(m.sin(alfa)*m.sin(alfa+2*beta))/m.pi
        
        teta=m.atan((x-D-E)/den)
        beta=m.atan((x-D-b5)/den)
        alfa=beta-teta
        R1=((D+E-x)**2+(den)**2)**0.5
        R2=((D+b5-x)**2+(den)**2)**0.5
        Szt=Gc*L3*(x*alfa/(E-b5)-m.sin(2*beta))/(2*m.pi)
        Sxt=Szt=Gc*L3*(x/(E-b5)-z*m.log(R1**2/R2**2)/(E-b5)+m.sin(2*beta))/(2*m.pi)
        Txzt=Gc*L3*(1-2*x/(E-b5)+m.cos(2*beta))/(2*m.pi)
        
        # pantalla 1
        R1=((D+b1-x)**2+(den-(L2+L1))**2)**0.5
        R2=((D+b1-x)**2+(den)**2)**0.5
        M=(1-vi)/vi
        Szp1=Gc*L2*(((M+1)/2*M)*((((z-L1+L2)**3)/R1**4)+((z+L1+L2)*((((z+L1+L2)**2)+2*L1+L2*z)/R2**4)-(8*L1+L2*z*(L1+L2+z)*x**2/R2**6)))+((M-1)/4*M)*(((z-L1+L2)/R1**2)+((3*z+L1+L2)/R2**2)-((4*z*x**2)/R2**4)))/(m.pi)
        Sxp1=Gc*L2*((((M+1)/2*M)*(((((z-L1+L2)*x**2)/R1**4)+((z+L1+L2)*(x**2+2*L1+L2**2)-(2*L1+L2*x**2))/R2**4)-(8*L1+L2*z*(L1+L2+z)*x**2/R2**6)))+((M-1)/4*M)*((-(z-L1+L2)/R1**2)+((z+3*L1+L2)/R2**2)+((4*z*x**2)/R2**4)))/(m.pi)
        Txzp1=Gc*L2*x*(((M+1)/2*M)*(((((z-L1+L2)**2)/R1**4)+((z**2-2*L1+L2*z-(L1+L2)**2)/R2**4)-(8*L1+L2*z*(L1+L2+z)**2/R2**6)))+((M-1)/4*M)*((1/R1**2)-(1/R2**2)+((4*z*(L1+L2+z))/R2**4)))/(m.pi)
        
        # pantalla 2
        R1=((D+E-b4-x)**2+(den-L2)**2)**0.5
        R2=((D+E-b4-x)**2+(den)**2)**0.5
        M=(1-vi)/vi
        Szp1=Gc*L2*(((M+1)/2*M)*((((z-L2)**3)/R1**4)+((z+L2)*((((z+L2)**2)+2*L2*z)/R2**4)-(8*L2*z*(L2+z)*x**2/R2**6)))+((M-1)/4*M)*(((z-L2)/R1**2)+((3*z+L2)/R2**2)-((4*z*x**2)/R2**4)))/(m.pi)
        Sxp1=Gc*L2*(((((M+1)/2*M)*(((((z-L2)*x**2)/R1**4)+((z+L2)*((x**2)+2*L2**2)-(2*L2*x**2))/R2**4)-(8*L2*z*(L2+z)*x**2)/R2**6)))+((M-1)/4*M)*((-(z-L2)/R1**2)+((z+3*L2)/R2**2)+((4*z*x**2)/R2**4)))/(m.pi)
        Txzp1=Gc*L2*x*(((M+1)/2*M)*(((((z-L2)**2)/R1**4)+((z**2-2*L2*z-L2**2)/R2**4)-(8*L2*z*(L2+z)**2/R2**6)))+((M-1)/4*M)*((1/R1**2)-(1/R2**2)+((4*z*(L2+z))/R2**4)))/(m.pi)
        
        Gsat=Gw*(ei+Gs)/(1+ei)
        Szs=Gsat*z
        
        SzT=Szw+Szr+Szt+Szs+Szp1+Szp2
        SxT=Sxw+Sxr+Sxt+Sxp1+Sxp2
        TxzT=Txzw+Txzr+Txzt+Txzp1+Txzp2
        
        Ms=np.zeros((2,2))
        Ms[0][0]=Sxt-P
        Ms[0][1]=Txzt
        Ms[1][0]=Txzt
        Ms[1][1]=Szt-P
        
        Centro=(Ms[0][0]+Ms[1][1])/2
        Radio=(((Ms[0][0]-Ms[1][1])/2)**2+Ms[1][0]**2)**0.5
        
        Sep=np.zeros((2,2))
        Sep[0][0]=Centro+Radio
        Sep[0][1]=0
        Sep[1][0]=0
        Sep[1][1]=Centro-Radio
        
        print('\n\nMatriz de Esfuerzos Efectivos \n\n',Ms)
        print('\n\nMatriz de Esfuerzos Efectivos Pricipales  \n\n',Sep)