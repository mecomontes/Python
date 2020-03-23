import numpy as np
import datetime
import matplotlib.pyplot as plt
import pylab as pl

def scrapping(cant):
    import pandas_datareader as pdr
    
    ecopetrol=pdr.get_data_yahoo('EC',start=datetime.datetime(2015,10,1))
    #print(ecopetrol)
    #print(ecopetrol.head())
    #print(ecopetrol.tail())
    #print(ecopetrol.loc['2009'].head())
    #print(ecopetrol.loc['2007'].tail())
    #print(ecopetrol['Adj Close'])
    #print(ecopetrol['close'][-30:])
    
    column=ecopetrol['Close'][-cant:]
    print(ecopetrol['Close'][-cant:])
    
    column.plot(grid=True)
    plt.show()
    return column

def media(t,cond_ini,mu_estimada):
    return cond_ini*np.exp(mu_estimada*t)

def varianza(t,cond_ini,mu_estimada,sigma_estimada):
    return (cond_ini**2)*np.exp(2*mu_estimada*t)*(np.exp(t*sigma_estimada**2)-1)

def mediaYdt(t,cond_ini,mu_estimada,sigma_estimada):
    dt=2*(varianza(t,cond_ini,mu_estimada,sigma_estimada))**0.5
    me=media(t,cond_ini,mu_estimada)
    return me-dt,me+dt

def mu(t,column,drift,D):
    valor_actual=column[t-1]
    return valor_actual+valor_actual*drift*D

def sigma(t,column,volatility,D):
    valor_actual=column[t-1]
    return valor_actual*volatility*D**0.5

def estimacion_modelo1(column,D):
    n=len(column)
    rg=range(1,n)
    cte=1/(n*D)
    quo=[(column.iloc[t]/column.iloc[t-1])-1 for t in rg]
    mu=cte*np.sum(quo)
    sigma=(cte*np.sum((quo-mu*D**2)))**0.5
    return mu,sigma

def estimacion_modelo2(column,D):
    rg=range(1,len(column)-1)
    const=1/D
    denom=np.sum(column)
    h=np.array([column.iloc[i+1]-column.iloc[i] for i in rg])
    num=np.sum(h)
    drift=num/denom
    b=np.array(column**2)
    denom=np.sum(b)
    j=np.array([(column.iloc[i+1]-column.iloc[i])**2 for i in rg])
    num=np.sum(j)
    volatility=(num/denom)**0.5
    return drift,volatility

def errores(column,mu_estimada):
    primero=column[0]
    n=len(column)
    m=np.array([media(t,primero,mu_estimada) for t in range(n)])
    ecm=np.linalg.norm(m-column)/(n**0.5)
    mape=100*np.sum(np.abs((m-column)/column))/n
    return ecm,mape

def fechas_dia():
    dia=datetime.datetime.today().weekday()
    
    if dia==0:
        des=[0,1,2,3,4]
    elif dia==1:
        des=[0,1,2,3,6]
    elif dia==2:
        des=[0,1,2,5,6]
    elif dia==1:
        des=[0,1,4,5,6]
    elif dia==1:
        des=[0,3,4,5,6]
    
    ant=[7-des[i] for i in range(5)]
    
    return ant,des

def fechas():
    ant,des=fechas_dia(0)
    ahora=datetime.datetime.now()
    ia=ahora.strftime("%H:%M, %d/%m/%y")
    antes5=[(ahora-datetime.timedelta(days=i)).strftime("%d/%m/%y") for i in ant]
    despues5=[(ahora-datetime.timedelta(days=i)).strftime("%d/%m/%y") for i in ant]
    hoy=ahora.strftime("%d/%m/%y")
    return ia,hoy,antes5,despues5

def grafico(column,est_medias,est_ic_2_5,est_ic_97_5,titulo_grafico,nombre_imagen):
    ejex=np.array(range(35))
    pl.plot(ejex[:30],column,'-bo',label='Cotizacion Real')
    pl.plot(ejex,est_medias,'g',label='Medias')
    pl.plot(ejex,est_ic_2_5,'r',label='IC 2.5%')
    pl.plot(ejex,est_ic_97_5,'r',label='IC 97.5%')
    pl.plot(ejex[30:],est_medias[30:],'-yo',label='Prevision')
    pl.axvline(29,color='k')
    pl.title(titulo_grafico)
    pl.xlabel('Tiempo [Dias]')
    pl.ylabel('Cotizacion')
    pl.legend(loc='upper left')
    pl.xlim(0,36)
    mx=np.max(est_ic_97_5)
    mn=np.min(est_ic_2_5)
    pl.ylim(0.7*mn,1.3*mx)
    pl.savefig(nombre_imagen)
    pl.close()
    return True

def grafico_comparativo(reales,historico_media,historico_ic275,historico_ic975,titulo_grafico,nombre_imagen):
    ejex=np.array(range(10))
    pl.plot(ejex,reales,'-bo',label='Cotizacion Real')
    pl.plot(ejex,historico_media,'g',label='Medias')
    pl.plot(ejex,historico_ic275,'r',label='IC 2.5%')
    pl.plot(ejex,historico_ic975,'r',label='IC 97.5%')
    pl.title(titulo_grafico)
    pl.xlabel('Tiempo [Dias]')
    pl.ylabel('Cotizacion')
    pl.legend(loc='upper left')
    pl.xlim(0,9)
    mx=np.max(historico_ic975)
    mn=np.min(historico_ic275)
    pl.ylim(0.7*mn,1.3*mx)
    pl.savefig(nombre_imagen)
    pl.close()
    return True


D=1
NOM='Ecopetrol'
CODE='EC'

column=scrapping(30)

n=len(column)
rg30=range(n)
rg35=range(n+5)

ia,hoy,antes5,despues5=fechas()

#       MEtodo 1

est_mu,est_sigma=estimacion_modelo1(column,D)
ecm,mape=errores(column,est_mu)
est_medias=np.array([media(t,column[0],est_mu) for t in rg35])
aux=np.array([mediaYdt(t,column[0],est_mu,est_sigma) for t in rg35])
est_ic_2_5=aux[:,0]
est_ic_97_5=aux[:,1]
grafico(column,est_medias,est_ic_2_5,est_ic_97_5,'METODO 1','Metodo1.png')

media_hist=np.zeros(10)
ic_2_5_hist=np.zeros(10)
ic_97_5_hist=np.zeros(10)
share=scrapping(40)

for i in range(10):
    datos=share[i:30+i]
    est_mu,est_sigma=estimacion_modelo1(datos,D)
    media_hist[i]=media(30+i+1,datos[0],est_mu)
    aux=mediaYdt(30+i+1,datos[0],est_mu,est_sigma)
    ic_2_5_hist[i]=aux[0]
    ic_97_5_hist[i]=aux[1]

grafico_comparativo(column[20:30],media_hist,ic_2_5_hist,ic_97_5_hist,'METODO 1','MetodoComparativo1.png')


#       Metodo 2

est_mu2,est_sigma2=estimacion_modelo2(column,D)
ecm2,mape2=errores(column,est_mu2)
est_medias2=np.array([media(t,column[0],est_mu2) for t in rg35])
aux=np.array([mediaYdt(t,column[0],est_mu2,est_sigma2) for t in rg35])
est_ic_2_52=aux[:,0]
est_ic_97_52=aux[:,1]
grafico(column,est_medias2,est_ic_2_52,est_ic_97_52,'METODO 2','Metodo2.png')

media_hist2=np.zeros(10)
ic_2_5_hist2=np.zeros(10)
ic_97_5_hist2=np.zeros(10)

for i in range(10):
    datos=share[i:30+i]
    est_mu2,est_sigma2=estimacion_modelo2(datos,D)
    media_hist2[i]=media(30+i+1,datos[0],est_mu2)
    aux=mediaYdt(30+i+1,datos[0],est_mu2,est_sigma2)
    ic_2_5_hist2[i]=aux[0]
    ic_97_5_hist2[i]=aux[1]

grafico_comparativo(column[20:30],media_hist2,ic_2_5_hist2,ic_97_5_hist2,'METODO 2','MetodoComparativo2.png')    