from tabulate import tabulate

# Imprime tabla a partir de los datos de 
# una lista de listas:

rios1 = [['Almanzora', 105],
         ['Guadiaro', 79],
         ['Guadalhorce', 154],
         ['Guadalmedina', 51.5]]
        
print(tabulate(rios1))