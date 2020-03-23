from datetime 
import datetime

from datetime 
import time



tarifa = 2000



hora_entrada = datetime.now()

print(hora_entrada)



placa = input("Ingrese la placa sin espacios: ")

ultimo = placa[5]



lunes =["0","1","2","3"]

martes = ["4","5","6","7"]



dia = input("Ingrese el dia de la semana: ")

if dia == 
"lunes": 

for i in lunes:

if ultimo == i:

print("Tiene pico y placa")



hora_salida = datetime.now()

print(hora_salida)



dif = hora_salida - hora_entrada

print(dif)



valor = dif * tarifa

print(valor)


