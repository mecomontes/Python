# Calculador Peso Molecular Aminoacidos
# Constantes Peso Atomico
PO = 15.9994
PC = 12.011
PN = 14.00674
PS = 32.066
PH = 1.00794

# Entrada

nombre_aminoacido = str(input("Ingrese el nombre del aminoacido a calcular: "))
O = int(input("Ingrese la cantidad de Oxigeno que contiene el aminoacido: "))
C = int(input("Ingrese la cantidad de Carbono que contiene el aminoacido: "))
N = int(input("Ingrese la cantidad de Nitrogeno que contiene el aminoacido: "))
S = int(input("Ingrese la cantidad de Asufre que contiene el aminoacido: "))
H = int(input("Ingrese la cantidad de Hidrogeno que contiene el aminoacido: "))

#Proceso

PM = PO*O+PC*C+PN*N+PS*S+PH*H

#Salida

print('El peso atómico de ' + nombre_aminoacido + ' es {PM} g/mol')

