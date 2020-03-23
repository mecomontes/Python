import matplotlib.pyplot as plt

Lista2=[10, 34, 46, 53, 56, 62, 68, 78]

#ordenar de menor a mayor (Ascendente)

#Ordenamiento burbuja
Lista1=[39, 91, 25, 32, 31, 32]
posulti=Lista1[-1]
contult=0

for i in range(len(Lista1)):
  for j in range(i+1,len(Lista1)):
    if Lista1[j]<Lista1[i]:
      if Lista1[i]==posulti or Lista1[j]==posulti:
        contult+=1
      aux=Lista1[i]
      Lista1[i]=Lista1[j]
      Lista1[j]=aux
print(Lista1,contult)

#ordenamiento seleccion
Lista1=[39, 91, 25, 32, 31, 32]
cont0=0
pos0=Lista1[0]

for i in range(len(Lista1)-1,0,-1):
  posmayor=0
  for j in range(1,i+1):
    if Lista1[j]>Lista1[posmayor]:
      posmayor=j
      if Lista1[i]==pos0 or Lista1[posmayor]==pos0:
        cont0+=1      
    aux=Lista1[i]
    Lista1[i]=Lista1[posmayor]
    Lista1[posmayor]=aux

print(Lista1,cont0)

#ordenamiento por insercion
Lista1=[39, 91, 25, 32, 31, 32]
contMed=0
medio=int((len(Lista1))/2)
posMed=Lista1[medio]

for i in range(1,len(Lista1)):
  actual=Lista1[i]
  posicion=i
  while posicion>0 and Lista1[posicion-1]>actual:
    Lista1[posicion]=Lista1[posicion-1]
    posicion=posicion-1
    if Lista1[posicion]==posMed or Lista1[posicion-1]==posMed:
      contMed+=1

  Lista1[posicion]=actual
print(Lista1,contMed)

contDesc=0
for i in range(len(Lista1)):
  for j in range(i+1,len(Lista1)):
    if Lista1[j]>Lista1[i]:
      contDesc+=1
      aux=Lista1[i]
      Lista1[i]=Lista1[j]
      Lista1[j]=aux

print(Lista1,contDesc)

plt.plot(Lista1)