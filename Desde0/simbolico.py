from sympy import *
import math

x,y,t=symbols('x y t',real=True)
f=x**2-3*x*y-6*y**3
fx=diff(f,x)
fy=diff(f,y)
fx3=fx.evalf(subs={x:3,y:5})
g=f.subs([(x,3-5*t),(y,2+2*t)])
p=solve(g,t)

