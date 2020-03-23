###parqueadero

import csv

csvarchivo = open('parqueadero.csv')  # Abrir archivo csv
entrada = csv.reader(csvarchivo)  # Leer todos los registros
reg = next(entrada)  # Leer registro (lista)
print(reg)  # Mostrar registro
reg = next(entrada)  # Leer registro (lista)
placa=next(entrada)
print(reg)  # Mostrar registro
placa = next(entrada)  # Leer campos
print(placa)