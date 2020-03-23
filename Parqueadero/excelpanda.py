## verificar as hojas y datos del archivo

import pandas as pd
import datetime

datos=pd.read_csv('parqueadero.csv',header=0)
df=pd.DataFrame(datos)
print(df)
print(datos.info())
print(datos.head())
#print(datos.iloc[:])