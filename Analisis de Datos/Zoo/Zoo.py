import pandas as pd
import numpy as np

df=pd.read_csv('zoo.csv',delimiter=',',names=['Animal','ID','Water'])
df.head()
df.tail()
df.sample(5)
print(df['Animal'])
print(df[['Animal','Water']])
print(df.ID)

s=pd.Series([1,2,3,4,5,6,7])
print(s)

#  https://www.tutorialspoint.com/python_pandas/python_pandas_series.htm