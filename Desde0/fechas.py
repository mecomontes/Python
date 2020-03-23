#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 15:32:46 2019

@author: meco
"""

import datetime
datetime.timedelta(days=1)

###   Restar días a una fecha

"""Para restar días a una fecha simplemente pasamos los días al objeto timedelta y 
se los restamos a la fecha base. Por ejemplo, si queremos representar la fecha de 
«ayer», haremos lo siguiente:"""

ahora = datetime.datetime.utcnow()
print(ahora)
   ###>>> 2019-03-21 11:01:04.192582

ayer = ahora - datetime.timedelta(days=1)
print(ayer)
#>>>2019-03-20 11:01:04.192582

#Restar horas a una fecha

#En el siguiente ejemplo veremos cómo obtener la hora anterior a la actual:

hace_una_hora = ahora - datetime.timedelta(hours=1)
print(hace_una_hora)
#>>>2019-03-21 10:01:04.192582

#Sumar días a una fecha

##Para sumar días a una fecha solamente tenemos que pasar los días al objeto timedelta
# y se los sumamos a la fecha base. El ejemplo que sigue obtiene la fecha de mañana:

tomorrow = ahora + datetime.timedelta(days=1)
print(tomorrow)
#>>>2019-03-22 11:01:04.192582

ahora=datetime.datetime.now()
print('la hora es: ',ahora)