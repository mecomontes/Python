caracter=input('ingrese el caracter a evaluar: ')

if caracter in '0123456789':
    print('el caracter ingresado es el numero ' + caracter)

elif caracter in 'abcdefghijklmnopqrstuvwxyz':
    print('el caracter es la letra '+ caracter + ' en minuscula')

elif caracter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print("EL CARACTER ES LA LETRA " + caracter + " en MAYUSCULA")
else:
    print("no es ni numero ni letra, es el simbolo " + caracter)