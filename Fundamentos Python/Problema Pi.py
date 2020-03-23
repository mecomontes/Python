#  Aproximaciones de Pi

Numero_Aproximaciones = int(input("Ingrese el numero de aproximaciones: "))

Sumatoria = 0
x = 0

for i in range(Numero_Aproximaciones):
    if i == 0:
        Valor_Expresion = 3
    else:
        Valor_Expresion = 4/(x*(x+1)*(x+2))
        Residuo = i % 2
        if Residuo == 0:
            Valor_Expresion = Valor_Expresion*(-1)
    Sumatoria += Valor_Expresion
    x += 2
    print(Valor_Expresion)

print("\n Sumatoria: %f de %d aproximaciones" % (Sumatoria, Numero_Aproximaciones))
