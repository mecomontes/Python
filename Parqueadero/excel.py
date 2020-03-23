#### documento excel

import pandas as pd

datos=pd.ExcelFile('parqueadero.xlsx')
print(datos.sheet_names)
dataframe=datos.parse('Hoja1')
print(dataframe)
print(dataframe.loc[:,'ingreso'])
n=len(dataframe)

contE=0
contS=0

for i in range(n):
    if dataframe.loc[i,'ingreso']=='E':
        contE+=contE
    else:
        contS+=contS
print(contE)