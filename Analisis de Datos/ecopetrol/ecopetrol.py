import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt
    
ecopetrol=pdr.get_data_yahoo('EC',start=datetime.datetime(2015,10,1))
#print(ecopetrol)
#print(ecopetrol.head())
#print(ecopetrol.tail())
#print(ecopetrol.loc['2009'].head())
#print(ecopetrol.loc['2007'].tail())
#print(ecopetrol['Adj Close'])
#print(ecopetrol['close'][-30:])

column=ecopetrol['Close'][-30:]
print(ecopetrol['Close'][-30:])

column.plot(grid=True)
plt.show()