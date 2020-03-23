#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 15:27:53 2019

@author: meco
"""

"""Para simular con el módulo secrets el ejemplo visto en el apartado anterior, 
basta ejecutar el siguiente código:"""

import secrets
secrets.token_hex(20)
##>>>'ccaf5c9a22e854856d0c5b1b96c81e851bafb288'

"""En ciertas ocasiones, puede que queramos que el secreto forma parte de una URL, 
por ejemplo, para resetear un password. En ese caso es más apropiado usar la función 
token_urlsafedel mismo modo. Esta nos garantiza que los caracteres generados son 
seguros de usar en una URL:"""

secrets.token_urlsafe(20)
##>>>'dxM4-BL1CPeHYIMmXNQevdlsvhI'

"""Hay que tener en cuenta que el número que se pasa entre paréntesis no es la longitud 
del número de caractéres, si no de bytes. En el caso de la función token_hex, 1 byte se 
corresponden con 2 dígitos hexadecimales. En cuanto a la función token_urlsafe, la cadena 
devuelta está codificada en Base 64, lo que viene a ser 1,3 caractéres por cada byte (aunque 
no siempre es así).

Si no se indica el número de bytes a utilizar, el módulo secrets usará uno razonable por 
defecto (que puede cambiar en cualquier momento en futuras actualizaciones)."""