# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 08:42:03 2018

@author: andre
"""

import sympy as sym
from sympy.abc import x
from sympy import sqrt
I=sym.integrate(3*x**3,(x,0,1))
print(I)