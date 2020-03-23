K='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ,;.:" ÁÉÍÓÚÜ'
Clave=list(K)
Valor=list(range(10,10+len(Clave)))
D=dict(zip(Clave,Valor))
Original=input('ingrese el mensaje a codificar: ').upper()
ListaOriginal=list(Original)
Codificado=[]

for i in range(len(ListaOriginal)):
    Codificado.append(D[ListaOriginal[i]])
    
print(Original)
print(Codificado)

Dinv=dict(zip(Valor,Clave))

Reverso=''

for i in range(len(Codificado)):
    Reverso+=Dinv[Codificado[i]]
    print(Codificado[i],end='')
    
print(Reverso)