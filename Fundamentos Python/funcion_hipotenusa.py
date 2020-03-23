#
import math as sqrt

print("\t Calcudora de hipotenusas \n")

def hipotenusa(Cateto1, Cateto2):
  Cateto1_Cuadrado= Cateto1*Cateto1
  Cateto2_Cuadrado= Cateto2*Cateto2
  Catetos=Cateto1_Cuadrado+Cateto2_Cuadrado
  Hipotenusa=sqrt(Catetos)
  print("\nLa hipotenusa del triangulo rectangulo de lados %.1f y %.1f es: %.3f" % (Cateto1, Cateto2, Hipotenusa))

Cateto1= float(input("Ingrese la longitud de un cateto para calcular la hipotenusa: "))
Cateto2=float(input("\nIngrese la longitud del otro cateto para calcular la hipotenusa: "))

hipotenusa(Cateto1, Cateto2)

