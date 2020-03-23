def graficar(num1,num2,num3):   
    if num1 > 0 and num1 < 20 or num2 > 0 and num2 < 20 or num3 > 0 and num1 < 20:
        
        for x in range(num1):
            print ("*",end='  ')
        print('\n')
        
        for x in range(num2):
            print ("*",end='  ')
        print('\n')
        
        for x in range(num3):
            print ("*",end='  ')
        print('\n')


x = int(input("Ingrese el primer numero:"))
y = int(input("Ingrese el segundo numero:"))
z = int(input("Ingrese el tercer numero:"))
print('\n')

graficar(x,y,z)